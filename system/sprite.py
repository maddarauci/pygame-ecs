import system.system
import system.components


class spriteSystem(system.system.System):
    def main(self, deltaTime, events):
        for component in self.all_components:
            component.screen.blit(component.sprite, component.rect)
