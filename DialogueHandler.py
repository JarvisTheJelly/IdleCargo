"""This class handles nearly every aspect of dialogue. See docstring. """

import pygame


class DialogueHandler(object):
    """The class that handles dialogue.

    This class can store fonts, render text, determine proper spacing
    for text, and in the future possibly determine where to split
    up long text inputs into multiple boxes and scroll text.
    """

    def __init__(self):
        """Initializes the handler, sets up basic variables.

        The fonts are stored in a dictionary so they can be called
        by a user-given name.
        """

        self.fonts = {"default": pygame.font.Font(None, 30),
                      "speaker": pygame.font.Font(None, 30),
                      "details": pygame.font.Font(None, 15)}
        self.fonts["speaker"].set_italic(True)
        self.fonts["details"].set_italic(True)
        self.padding = 20

    def add_font(self, font_name, font):
        """Adds a font to the font dictionary.

        Arguments:
            font_name - the key used to reference the font.
            font - a pygame.font.Font instance.
        """

        self.fonts[font_name] = font

    def render_text(self, font_name, text, color=(0, 0, 0), quotes=True):
        """Renders and returns given text.

        Arguments:
            font_name - the key for the wanted font
            text - the text to be rendered
            color - a tuple of length 3 containing the color wanted
            quotes - bool to determine whether to surround the text in quotes

        Returns:
            A pygame.Surface of the rendered text
        """

        #TODO: Make this format the text then render it

        if quotes:
            text = "\"" + text + "\""
        return self.fonts[font_name].render(text, True, color)

    def create_text_box(self, rendered_text, speaker, base_size):
        """Creates and returns a text box.

        Argumnts:
            rendered_text - pre-rendered text the will be what is spoken
            speaker - a string containing who / what said the text
            base_size - the size of the surface you are planning to blit to

        Returns:
            A pygame.Surface that contains the text box image
        """

        #Get information on the size of the text box based on given dimensions
        width = base_size[0] - self.padding * 2
        height = base_size[1] * 0.30 - self.padding

        #Create the text box
        text_box = pygame.Surface((width, height))

        #Color the text box
        text_box.fill((255, 255, 255))
        pygame.draw.rect(text_box, (0, 0, 0), (0, 0, width, height), 5)

        #set up where to blit the rendered text to the text box
        rendered_text_rect = rendered_text.get_rect()
        rendered_text_rect.center = (width // 2, height // 2)

        #Check to see if there is a speaker, if so blit their name
        if speaker != "":
            speaker_text = self.render_text("speaker",
                    speaker + ":",
                    quotes=False)

            text_box.blit(speaker_text, (20, 20))

        detail_render = self.render_text("details",
                "PRESS SPACE TO CONTINUE",
                quotes=False)

        text_box.blit(detail_render, (20, height - 20))

        #blit the rendered text to the text box
        text_box.blit(rendered_text, rendered_text_rect)

        #All done!
        return text_box

    def render_box(self, text_box, surface):
        """Renders a text box to a given surface

        Arguments:
            text_box - The text box that will be blit to the surface
            surface - The surface to which you would like to blit the box

        Returns:
            None
        """

        #Get pos information based on the surface.
        pos = (self.padding, surface.get_height() * 0.70)

        #Blit the text box to the surface.
        surface.blit(text_box, pos)
