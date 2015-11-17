"""Class for loading images quickly"""

import pygame


class ImageLoader(object):
    """Class for loading a single image or multiple images quickly.

    Class for loading images quickly and cleanly.
    """

    def __init__(self):
        """Does nothing"""

        pass

    def load_image(self, image_name, colorkey=(255, 0, 255)):
        """Loads a single image from the image name.

        Arguments:
            image_name - the filename of the image (without res or extension)
            colorkey - the color used to colorkey the image

        Surrounds image_name in "res/" and ".png" and loads it.

        Automatically colorkey's.

        Returns the loaded image.
        """

        filename = "res/" + image_name + ".png"
        return_image = pygame.image.load(filename).convert()
        return_image.set_colorkey(colorkey)

        return return_image

    def load_images(self, image_names, colorkey=(255, 0, 255)):
        """Loads and returns multiple images in a list.

        Arguments:
            image_names - list of filenames of images
            colorkey - the color used to colorkey images

        uses the load_image function multiple times and returns list of images
        """

        return_images = []
        for name in image_names:
            return_images.append(self.load_image(name, colorkey))

        return return_images

    def load_frame(self, image, rel_w, rel_h, rel_x, rel_y):
        """Loads a section of an image, useful for spritesheets
        
        Arguments:
            image - Image that the section will be from
            rel_w - How wide the section (not total image) is.
            rel_h - How tall the section (not total image) is.
            rel_x - Based on rel_w and rel_h, the x value of the section.
            rel_y - Based on rel_w and rel_h, the y value of the section.
            
        Explaination of rel_x and rel_y:
            If the total size of the image is 64x64 and you want an 4x8 section
            from (16, 16), the arguments would look like the following:
                rel_w = 4
                rel_h = 8
                rel_x = 4
                rel_h = 2
                
        Returns section as a pygame.Surface()
        """

        return image.subsurface(rel_x * rel_w,
                                rel_y * rel_h,
                                rel_w,
                                rel_h)
