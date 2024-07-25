# Maximilian Richter
# Sina Steinmüller
# Stand: 2024-07-17
""" 
This program uses Pygame to detect keyboard input and control the drone based on the user's choice.
"""
import pygame
import sys
 
# Initialisiere Pygame
pygame.init()

# Bildschirmgröße und Farben
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialisiere das Fenster
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Control")


# Initialisiere die Zustandsvariable für die Tasten
keys_pressed = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

# Hauptfunktion zur Tastatureingabe und Richtungsaktualisierung
def run_keyboard_control(direction_callback):
    direction = "none"
    direction_changed = False  # Flag, um zu prüfen, ob die Richtung geändert wurde
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    keys_pressed["up"] = True
                elif event.key == pygame.K_s:
                    keys_pressed["down"] = True
                elif event.key == pygame.K_a:
                    keys_pressed["left"] = True
                elif event.key == pygame.K_d:
                    keys_pressed["right"] = True
                elif event.key == pygame.K_t:  # Hinzufügen der Erkennung für "T"
                    keys_pressed["takeoff"] = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys_pressed["up"] = False
                elif event.key == pygame.K_s:
                    keys_pressed["down"] = False
                elif event.key == pygame.K_a:
                    keys_pressed["left"] = False
                elif event.key == pygame.K_d:
                    keys_pressed["right"] = False
                elif event.type == pygame.KEYUP and event.key == pygame.K_t:  # Hinzufügen der Erkennung für das Loslassen von "T"
                    keys_pressed["takeoff"] = False
                
        # Initialisieren Sie das Flag außerhalb der Event-Schleife
        takeoff_triggered = False

        # Innerhalb der Event-Schleife
        

        # Überprüfe den Zustand der Tasten und führe Befehle aus
        try:
            if keys_pressed["up"]:
                direction_callback("up")
            if keys_pressed["down"]:
                direction_callback("down")
            if keys_pressed["left"]:
                direction_callback("left")
            if keys_pressed["right"]:
                direction_callback("right")
            if keys_pressed.get("takeoff") and not takeoff_triggered:  # Überprüfung auf "takeoff" und ob es bereits ausgelöst wurde
                direction_callback("takeoff")
                takeoff_triggered = True  # Setzen Sie das Flag, nachdem "takeoff" ausgelöst wurde
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")

        # Überprüfe den Zustand der Tasten und führe Befehle aus
        if keys_pressed["up"]:
            direction_callback("up")
        if keys_pressed["down"]:
            direction_callback("down")
        if keys_pressed["left"]:
            direction_callback("left")
        if keys_pressed["right"]:
            direction_callback("right")

        # Zeichne den Bildschirm (optional)
        screen.fill(WHITE)
        pygame.display.flip()

        clock.tick(60)  # Begrenze die Schleife auf 60 FPS


if __name__ == "__main__":
    # Beispiel für die Verwendung von run_keyboard_control
    def direction_callback(direction):
        print(f"keyboardcontrol.py sagt {direction}")

    run_keyboard_control(direction_callback)
