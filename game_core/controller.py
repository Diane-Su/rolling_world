import pygame


class EventController():
    def __init__(self):
        self.running = True
        pass

    def get_keyboard_command(self):
        command = ["None"]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            command.append("MOVE_LEFT")
        if keys[pygame.K_RIGHT]:
            command.append("MOVE_RIGHT")
        if keys[pygame.K_UP]:
            command.append("MOVE_UP")
        if keys[pygame.K_DOWN]:
            command.append("MOVE_DOWN")

        return {"Address": "GameMode",
                "Type": type(command),
                "Data": command}

    def is_running(self):
        """ Handle the event from window , mouse or button.

        :return: Bool,False means game closed
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.running = False

        return self.running

    def update(self):
        pass

