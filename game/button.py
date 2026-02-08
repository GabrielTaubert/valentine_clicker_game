import pygame

class Button:

    def __init__(self, image, position):
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect(center=position)

        self.is_pressed = False
        self.press_timer = 0
        self.press_duration = 0.1

        self.font = pygame.font.Font("assets/font/Minecraft.ttf", 60)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.shrink()
                return True
        return False

    def shrink(self):
        self.is_pressed = True
        #self.press_timer = 0

        scale = 0.85  # 85% Größe
        w = int(self.original_image.get_width() * scale)
        h = int(self.original_image.get_height() * scale)

        self.image = pygame.transform.scale(self.original_image, (w, h))
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        text = self.font.render("Quit", True, (148, 27, 45))

        text_rect = text.get_rect(center=self.rect.center)
        text_rect.y += 8

        screen.blit(text, text_rect)