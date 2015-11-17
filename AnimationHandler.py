"""Class for handling loading multiple images and storing animations"""

import pygame
import gametools.ImageLoader as ImageLoader

class AnimationHandler(object):
    """Handles the loading of frames of an animation.
    
    Not sure if this should be a part of the ImageLoader class or if
    I will end up creating more methods for this to use.
    """

    def __init__(self):
        """Sets up the image_loader to load main sprite sheet"""

        self.image_loader = ImageLoader.ImageLoader()
        self.time_between_frames = 0.05
        self.delay = 0
        self.delay_reload = 0

    def load_animation(self, filename, rel_w, rel_h, rel_x, rel_y, num_frames):
        """Loads and returns the frames of an animation.
        
        Arguments:
            filename - name of the sprite sheet without the ending or the res/
            rel_w - width of a single frame in the animation
            rel_h - height of a single frame in the animation
            rel_x - relative x position on the sprite sheet of the first frame
            rel_y - relative y position on the sprite sheet of the first frame
            num_frames - number of frames in the animation
            
        Returns:
            Python list containing the frames of the animation
            
        Explaination of rel_x and rel_y:
            Based on the relative width and height of a single frame. if the
            relative size of a sprite is 32 x 64, and the location on the
            sprite sheet is (64, 0), the rel_x and rel_y would be (2, 0).

            Basically:
                rel_x = actual_x / rel_w
                rel_y = actual_y / rel_h
        """

        sprite_sheet = self.image_loader.load_image(filename)
        frame_list = []

        for i in range(num_frames):
            sub_image = sprite_sheet.subsurface((int(rel_x * rel_w + i * rel_w),
                                                 int(rel_y * rel_h),
                                                 rel_w,
                                                 rel_h))

            frame_list.append(sub_image)

        return frame_list

    def update(self, Entity, tick):
        """Updates the given entity's animation
        
        Arguments:
            Entity - the entity that will be updated
            tick - time since the last frame in seconds
            
        """
        
        #As long as the entity has an animation
        if Entity.selected_animation is not None:
            Entity.ani_timer += tick

            #if it is time to switch frames
            if Entity.ani_timer >= self.time_between_frames:
                Entity.ani_timer -= self.time_between_frames
                num_frames = len(Entity.animations[Entity.selected_animation])
                Entity.ani_frame = (Entity.ani_frame + 1) % num_frames

