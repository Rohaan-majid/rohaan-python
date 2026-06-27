import pygame
import random
import math
import os
import sys

# Simple top-down racing game with color selection, difficulty, and podium

pygame.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Racer")
FPS = 60

# Define 10 colors with names
COLOR_POOL = [
    ("red", (220, 20, 60)),
    ("blue", (30, 144, 255)),
    ("green", (34, 139, 34)),
    ("yellow", (255, 215, 0)),
    ("orange", (255, 140, 0)),
    ("purple", (147, 112, 219)),
    ("pink", (255, 105, 180)),
    ("brown", (160, 82, 45)),
    ("gray", (128, 128, 128)),
    ("cyan", (0, 206, 209)),
]

CAR_MODELS = [
    {"name": "Viper", "body": (60, 120, 200), "preview_color": (30, 144, 255), "cost": 0},
    {"name": "Cheetah", "body": (200, 60, 60), "preview_color": (255, 200, 0), "cost": 600},
    {"name": "Flash", "body": (60, 180, 90), "preview_color": (220, 20, 60), "cost": 1000},
]

DEFAULT_UNLOCKED_CARS = {"Viper"}

FONT = pygame.font.SysFont("Arial", 20)
BIG = pygame.font.SysFont("Arial", 36, bold=True)


def calculate_reward(position, elapsed_seconds, difficulty):
    difficulty_value = {"Easy": 120, "Medium": 180, "Hard": 260}[difficulty]
    position_value = {1: 300, 2: 180, 3: 90, 4: 20}.get(position, 0)
    time_bonus = max(0, 80 - elapsed_seconds) * 3
    return difficulty_value + position_value + time_bonus


def draw_car_preview(surface, x, y, color, model_name):
    body_surface = pygame.Surface((70, 110), pygame.SRCALPHA)
    body_surface.fill((0, 0, 0, 0))

    if model_name == "Cheetah":
        body_points = [
            (14, 34), (20, 18), (34, 10), (46, 18), (54, 34), (50, 48), (50, 74), (54, 88),
            (44, 100), (34, 96), (24, 100), (14, 88), (18, 74), (18, 48),
        ]
    elif model_name == "Flash":
        body_points = [
            (14, 34), (24, 16), (34, 10), (44, 16), (54, 34), (50, 48), (50, 74), (54, 88),
            (44, 100), (34, 96), (24, 100), (14, 88), (18, 74), (18, 48),
        ]
    else:
        body_points = [
            (14, 34), (24, 16), (34, 10), (44, 16), (54, 34), (50, 48), (50, 74), (54, 88),
            (44, 100), (34, 96), (24, 100), (14, 88), (18, 74), (18, 48),
        ]

    pygame.draw.polygon(body_surface, color, body_points)
    pygame.draw.rect(body_surface, (220, 220, 220), (20, 26, 28, 12), border_radius=4)
    pygame.draw.rect(body_surface, (30, 30, 30), (22, 44, 24, 18), border_radius=4)
    pygame.draw.rect(body_surface, (250, 250, 250), (24, 48, 20, 10), border_radius=3)
    pygame.draw.rect(body_surface, (40, 40, 40), (20, 70, 28, 10), border_radius=3)
    pygame.draw.rect(body_surface, (30, 30, 30), (16, 34, 8, 8), border_radius=2)
    pygame.draw.rect(body_surface, (30, 30, 30), (46, 34, 8, 8), border_radius=2)
    rotated = pygame.transform.rotate(body_surface, -90)
    rect = rotated.get_rect(center=(x, y))
    surface.blit(rotated, rect.topleft)


LAPS = 3
CHECKPOINT_RADIUS = 90
CHECKPOINT_DRAW_RADIUS = 18
TRACK_INSET_X = 260
TRACK_INSET_Y = 220


class Car:
    def __init__(self, name, color, pos, angle=0, is_player=False, car_model="Standard"):
        self.name = name
        self.color = color
        self.x, self.y = pos
        self.angle = angle
        self.speed = 0.0
        self.max_speed = 4.0
        self.turn_speed = 3.0
        self.width = 24
        self.height = 40
        self.lap = 0
        self.finished = False
        self.finish_time = None
        self.is_player = is_player
        self.wall_hit = 0
        self.car_model = car_model

    def rect(self):
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def draw(self, surf):
        body_surface = pygame.Surface((70, 110), pygame.SRCALPHA)
        body_surface.fill((0, 0, 0, 0))

        body_points = [
            (14, 34),
            (24, 16),
            (34, 10),
            (44, 16),
            (54, 34),
            (50, 48),
            (50, 74),
            (54, 88),
            (44, 100),
            (34, 96),
            (24, 100),
            (14, 88),
            (18, 74),
            (18, 48),
        ]
        pygame.draw.polygon(body_surface, self.color, body_points)
        pygame.draw.rect(body_surface, (220, 220, 220), (20, 26, 28, 12), border_radius=4)
        pygame.draw.rect(body_surface, (30, 30, 30), (22, 44, 24, 18), border_radius=4)
        pygame.draw.rect(body_surface, (250, 250, 250), (24, 48, 20, 10), border_radius=3)
        pygame.draw.rect(body_surface, (40, 40, 40), (20, 70, 28, 10), border_radius=3)
        pygame.draw.rect(body_surface, (20, 20, 20), (24, 82, 8, 12), border_radius=3)
        pygame.draw.rect(body_surface, (20, 20, 20), (38, 82, 8, 12), border_radius=3)
        pygame.draw.rect(body_surface, (255, 255, 255), (18, 18, 10, 6), border_radius=2)
        pygame.draw.rect(body_surface, (255, 255, 255), (42, 18, 10, 6), border_radius=2)
        pygame.draw.rect(body_surface, (30, 30, 30), (16, 34, 8, 8), border_radius=2)
        pygame.draw.rect(body_surface, (30, 30, 30), (46, 34, 8, 8), border_radius=2)
        pygame.draw.polygon(body_surface, (255, 255, 255), [(14, 24), (26, 16), (34, 20), (24, 28)])
        pygame.draw.polygon(body_surface, (255, 255, 255), [(54, 24), (44, 16), (34, 20), (46, 28)])
        if self.car_model == "Sprint":
            pygame.draw.rect(body_surface, (220, 220, 220), (22, 64, 26, 8), border_radius=3)
        elif self.car_model == "Touring":
            pygame.draw.rect(body_surface, (200, 200, 200), (18, 64, 34, 8), border_radius=3)

        rotated = pygame.transform.rotate(body_surface, -self.angle)
        r = rotated.get_rect(center=(self.x, self.y))
        surf.blit(rotated, r.topleft)

        if self.wall_hit > 0:
            pygame.draw.rect(surf, (255, 255, 255), r, 2)

    def update_player(self, keys):
        forward = keys[pygame.K_w]
        reverse = keys[pygame.K_s]
        left = keys[pygame.K_a]
        right = keys[pygame.K_d]

        if forward:
            self.speed = min(self.max_speed, self.speed + 0.15)
        elif reverse:
            if self.speed > 0:
                self.speed = max(0, self.speed - 0.3)
            else:
                self.speed = max(-self.max_speed * 0.6, self.speed - 0.1)
        else:
            if self.speed > 0:
                self.speed = max(0, self.speed - 0.08)
            elif self.speed < 0:
                self.speed = min(0, self.speed + 0.08)

        speed_factor = max(0.3, min(1.0, abs(self.speed) / self.max_speed))
        turn_rate = self.turn_speed * (0.8 + 0.7 * speed_factor)

        if left:
            self.angle -= turn_rate
        if right:
            self.angle += turn_rate

        rad = math.radians(self.angle)
        self.x += math.sin(rad) * self.speed
        self.y -= math.cos(rad) * self.speed

        if self.wall_hit > 0:
            self.wall_hit -= 1

    def is_on_road(self, outer_rect, inner_rect):
        return outer_rect.collidepoint(self.x, self.y) and not inner_rect.collidepoint(self.x, self.y)

    def apply_surface_effect(self, outer_rect, inner_rect):
        if self.is_on_road(outer_rect, inner_rect):
            return

        if not outer_rect.collidepoint(self.x, self.y):
            if self.x < outer_rect.left:
                self.x = outer_rect.left
            elif self.x > outer_rect.right:
                self.x = outer_rect.right
            if self.y < outer_rect.top:
                self.y = outer_rect.top
            elif self.y > outer_rect.bottom:
                self.y = outer_rect.bottom
        elif inner_rect.collidepoint(self.x, self.y):
            left_gap = abs(self.x - inner_rect.left)
            right_gap = abs(self.x - inner_rect.right)
            top_gap = abs(self.y - inner_rect.top)
            bottom_gap = abs(self.y - inner_rect.bottom)
            min_gap = min(left_gap, right_gap, top_gap, bottom_gap)
            if min_gap == left_gap:
                self.x = inner_rect.left
            elif min_gap == right_gap:
                self.x = inner_rect.right
            elif min_gap == top_gap:
                self.y = inner_rect.top
            else:
                self.y = inner_rect.bottom

        self.speed = -self.speed * 0.85
        self.wall_hit = 10

    def update_ai(self, waypoint, ai_speed_factor):
        # simple steering toward waypoint
        if self.finished:
            return
        dx = waypoint[0] - self.x
        dy = waypoint[1] - self.y
        target_angle = math.degrees(math.atan2(dx, -dy))
        # normalize
        diff = (target_angle - self.angle + 180) % 360 - 180
        self.angle += max(-3, min(3, diff))
        target_speed = self.max_speed * ai_speed_factor
        # small random fluctuation
        self.speed += (target_speed - self.speed) * 0.05
        rad = math.radians(self.angle)
        self.x += math.sin(rad) * self.speed
        self.y -= math.cos(rad) * self.speed


def draw_track(surface):
    surface.fill((22, 120, 84))
    track_rect = pygame.Rect(90, 100, WIDTH - 180, HEIGHT - 240)
    inner_rect = track_rect.inflate(-TRACK_INSET_X, -TRACK_INSET_Y)
    border = 18
    outer = track_rect.inflate(border * 2, border * 2)

    block = 24
    for x in range(outer.left, outer.right, block):
        color = (255, 0, 0) if ((x // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (x, track_rect.top - border, block, border), border_radius=6)
        pygame.draw.rect(surface, color, (x, track_rect.bottom, block, border), border_radius=6)
    for y in range(outer.top, outer.bottom, block):
        color = (255, 0, 0) if ((y // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (track_rect.left - border, y, border, block), border_radius=6)
        pygame.draw.rect(surface, color, (track_rect.right, y, border, block), border_radius=6)

    pygame.draw.rect(surface, (50, 50, 50), track_rect, border_radius=50)
    pygame.draw.rect(surface, (22, 120, 84), inner_rect, border_radius=40)

    inner_border = 16
    for x in range(inner_rect.left, inner_rect.right, block):
        color = (255, 0, 0) if ((x // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (x, inner_rect.top - inner_border, block, inner_border), border_radius=4)
        pygame.draw.rect(surface, color, (x, inner_rect.bottom, block, inner_border), border_radius=4)
    for y in range(inner_rect.top, inner_rect.bottom, block):
        color = (255, 0, 0) if ((y // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (inner_rect.left - inner_border, y, inner_border, block), border_radius=4)
        pygame.draw.rect(surface, color, (inner_rect.right, y, inner_border, block), border_radius=4)

    stand_height = 50
    stand_color = (130, 130, 130)
    left_stand = pygame.Rect(track_rect.left + 40, track_rect.top - border - stand_height - 20, 240, stand_height)
    right_stand = pygame.Rect(track_rect.right - 280, track_rect.top - border - stand_height - 20, 240, stand_height)
    pygame.draw.rect(surface, stand_color, left_stand, border_radius=8)
    pygame.draw.rect(surface, stand_color, right_stand, border_radius=8)
    for i in range(6):
        for row in range(3):
            fan_x = left_stand.left + 20 + i * 36
            fan_y = left_stand.top + 10 + row * 12
            pygame.draw.circle(surface, (255, 220, 180), (fan_x, fan_y), 5)
            fan_x = right_stand.left + 20 + i * 36
            pygame.draw.circle(surface, (255, 220, 180), (fan_x, fan_y), 5)
    for i in range(3):
        fx = left_stand.left + 40 + i * 70
        pygame.draw.polygon(surface, (255, 0, 0), [(fx, left_stand.top), (fx + 12, left_stand.top + 8), (fx, left_stand.top + 16)])
        fx = right_stand.left + 40 + i * 70
        pygame.draw.polygon(surface, (0, 0, 255), [(fx, right_stand.top), (fx + 12, right_stand.top + 8), (fx, right_stand.top + 16)])
    for i, tx in enumerate(range(track_rect.left + 20, track_rect.right, 120)):
        pygame.draw.rect(surface, (101, 67, 33), (tx, track_rect.top - border - stand_height - 60, 10, 20))
        pygame.draw.circle(surface, (20, 120, 20), (tx + 5, track_rect.top - border - stand_height - 70), 18)
        pygame.draw.circle(surface, (16, 100, 16), (tx - 18, track_rect.top - border - stand_height - 50), 12)
        pygame.draw.circle(surface, (16, 100, 16), (tx + 18, track_rect.top - border - stand_height - 50), 12)
    for tx in range(track_rect.left + 90, track_rect.right, 160):
        pygame.draw.rect(surface, (120, 80, 40), (tx, track_rect.bottom + 16, 24, 70))
        pygame.draw.rect(surface, (80, 140, 80), (tx - 8, track_rect.bottom + 8, 40, 18))

    start_x = WIDTH // 2
    pygame.draw.line(surface, (255,255,255), (start_x, track_rect.top), (start_x, track_rect.top + 40), 6)
    return track_rect, inner_rect


def generate_waypoints(track_rect):
    left = track_rect.left + 70
    right = track_rect.right - 70
    top = track_rect.top + 70
    bottom = track_rect.bottom - 70
    return [
        (WIDTH // 2, track_rect.top + 20),
        (right, top),
        (right, bottom),
        (left, bottom),
        (left, top),
    ]


def shop_screen(credits, unlocked_cars, selected_car_model):
    clock = pygame.time.Clock()
    message = "Buy a car with your credits"
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                back_rect = pygame.Rect(80, 580, 140, 45)
                if back_rect.collidepoint(mx, my):
                    return credits, unlocked_cars, selected_car_model

                for model in CAR_MODELS:
                    card_rect = pygame.Rect(100 + CAR_MODELS.index(model) * 250, 220, 200, 260)
                    if card_rect.collidepoint(mx, my):
                        if model["name"] in unlocked_cars:
                            selected_car_model = model
                            message = f"{model['name']} selected"
                        elif credits >= model["cost"]:
                            credits -= model["cost"]
                            unlocked_cars.add(model["name"])
                            selected_car_model = model
                            message = f"Unlocked {model['name']} for {model['cost']} credits"
                        else:
                            message = f"Need {model['cost'] - credits} more credits"

        WIN.fill((25, 25, 25))
        WIN.blit(BIG.render("Car Shop", True, (255, 255, 255)), (WIDTH // 2 - 90, 30))
        WIN.blit(FONT.render(f"Credits: {credits}", True, (255, 255, 255)), (WIDTH - 180, 40))
        WIN.blit(FONT.render(message, True, (220, 220, 220)), (80, 90))

        for i, model in enumerate(CAR_MODELS):
            card_rect = pygame.Rect(100 + i * 250, 220, 200, 260)
            card_color = (70, 70, 70)
            if model["name"] == selected_car_model["name"]:
                card_color = (200, 120, 50)
            elif model["name"] in unlocked_cars:
                card_color = (60, 120, 60)
            pygame.draw.rect(WIN, card_color, card_rect, border_radius=16)
            draw_car_preview(WIN, card_rect.centerx, card_rect.top + 90, model["preview_color"], model["name"])
            WIN.blit(FONT.render(model["name"], True, (255, 255, 255)), (card_rect.x + 20, card_rect.top + 140))
            status = "Selected" if model["name"] == selected_car_model["name"] else ("Unlocked" if model["name"] in unlocked_cars else f"Buy {model['cost']}")
            WIN.blit(FONT.render(status, True, (255, 255, 255)), (card_rect.x + 20, card_rect.top + 170))
            WIN.blit(FONT.render("Click to buy/select", True, (220, 220, 220)), (card_rect.x + 20, card_rect.top + 200))

        pygame.draw.rect(WIN, (40, 140, 40), (80, 580, 140, 45), border_radius=8)
        WIN.blit(FONT.render("Back", True, (255, 255, 255)), (125, 592))
        pygame.display.flip()


def selection_screen(credits, unlocked_cars, selected_car_model):
    clock = pygame.time.Clock()
    chosen_colors = list(COLOR_POOL)
    player_choice = None
    difficulty = "Medium"
    unit = "km/h"
    difficulties = ["Easy", "Medium", "Hard"]
    units = ["km/h", "mph"]
    message = "Choose a color and start the race"

    if selected_car_model["name"] not in unlocked_cars:
        selected_car_model = next((model for model in CAR_MODELS if model["name"] in unlocked_cars), CAR_MODELS[0])

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                for i, (name, col) in enumerate(chosen_colors):
                    bx = 120 + (i % 5) * 160
                    by = 240 + (i // 5) * 120
                    br = pygame.Rect(bx - 40, by - 40, 80, 80)
                    if br.collidepoint(mx, my):
                        player_choice = (name, col)
                for i, d in enumerate(difficulties):
                    bx = 150 + i * 180
                    by = 380
                    br = pygame.Rect(bx - 60, by - 20, 120, 40)
                    if br.collidepoint(mx, my):
                        difficulty = d
                for i, u in enumerate(units):
                    bx = 150 + i * 180
                    by = 450
                    br = pygame.Rect(bx - 60, by - 20, 120, 40)
                    if br.collidepoint(mx, my):
                        unit = u
                shop_rect = pygame.Rect(WIDTH // 2 - 90, 520, 180, 50)
                if shop_rect.collidepoint(mx, my):
                    credits, unlocked_cars, selected_car_model = shop_screen(credits, unlocked_cars, selected_car_model)
                    message = f"Current car: {selected_car_model['name']}"
                start_rect = pygame.Rect(WIDTH // 2 - 80, 585, 160, 50)
                if start_rect.collidepoint(mx, my) and player_choice:
                    return player_choice, difficulty, chosen_colors, unit, selected_car_model, credits, unlocked_cars

        WIN.fill((30, 30, 30))
        WIN.blit(BIG.render("Choose Your Race Setup", True, (255, 255, 255)), (WIDTH // 2 - 190, 30))
        WIN.blit(FONT.render("Available colors (pick one):", True, (200, 200, 200)), (80, 210))
        for i, (name, col) in enumerate(chosen_colors):
            bx = 120 + (i % 5) * 160
            by = 240 + (i // 5) * 120
            pygame.draw.circle(WIN, col, (bx, by), 30)
            txt = FONT.render(name.capitalize(), True, (255, 255, 255))
            WIN.blit(txt, (bx - txt.get_width() // 2, by + 40))
            if player_choice and player_choice[0] == name:
                pygame.draw.circle(WIN, (255, 255, 255), (bx, by), 36, 3)

        WIN.blit(FONT.render("Current car:", True, (200, 200, 200)), (80, 320))
        WIN.blit(FONT.render(selected_car_model["name"], True, (255, 255, 255)), (180, 320))
        draw_car_preview(WIN, 300, 340, selected_car_model["preview_color"], selected_car_model["name"])

        WIN.blit(FONT.render("Select Difficulty:", True, (200, 200, 200)), (80, 370))
        for i, d in enumerate(difficulties):
            bx = 150 + i * 180
            by = 400
            r = pygame.Rect(bx - 60, by - 20, 120, 40)
            color = (100, 100, 100) if d != difficulty else (200, 100, 50)
            pygame.draw.rect(WIN, color, r)
            WIN.blit(FONT.render(d, True, (255, 255, 255)), (bx - 20, by - 10))

        WIN.blit(FONT.render("Speed unit:", True, (200, 200, 200)), (80, 470))
        for i, u in enumerate(units):
            bx = 150 + i * 180
            by = 500
            r = pygame.Rect(bx - 60, by - 20, 120, 40)
            color = (100, 100, 100) if u != unit else (200, 100, 50)
            pygame.draw.rect(WIN, color, r)
            WIN.blit(FONT.render(u, True, (255, 255, 255)), (bx - 20, by - 10))

        WIN.blit(FONT.render(f"Credits: {credits}", True, (255, 255, 255)), (WIDTH - 180, 25))
        shop_rect = pygame.Rect(WIDTH // 2 - 90, 520, 180, 50)
        pygame.draw.rect(WIN, (180, 120, 40), shop_rect)
        WIN.blit(FONT.render("Open Shop", True, (255, 255, 255)), (shop_rect.x + 35, shop_rect.y + 12))
        start_rect = pygame.Rect(WIDTH // 2 - 80, 585, 160, 50)
        pygame.draw.rect(WIN, (30, 160, 30) if player_choice else (80, 80, 80), start_rect)
        WIN.blit(FONT.render("Start Race", True, (255, 255, 255)), (start_rect.x + 28, start_rect.y + 12))
        WIN.blit(FONT.render(message, True, (220, 220, 220)), (80, 650))

        pygame.display.flip()


def podium_screen(finish_order, earned_credits, credits):
    # finish_order: list of (Car)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        WIN.fill((30,30,30))
        WIN.blit(BIG.render("Race Results", True, (255,255,255)), (WIDTH//2 - 120, 30))

        # Podium positions
        podium_x = WIDTH//2
        podium_y = HEIGHT//2 + 80
        # heights
        heights = {"1st":120, "2nd":80, "3rd":60}
        positions = {"1st":(podium_x, podium_y - heights["1st"]),
                     "2nd":(podium_x + 140, podium_y - heights["2nd"]),
                     "3rd":(podium_x - 140, podium_y - heights["3rd"]) }

        # draw podium blocks
        for label, (px, py) in positions.items():
            h = heights[label]
            w = 120
            r = pygame.Rect(px - w//2, podium_y - h, w, h)
            pygame.draw.rect(WIN, (200,200,200), r)
            WIN.blit(FONT.render(label, True, (0,0,0)), (r.centerx - 16, r.top - 24))

        # draw top-3 cars on podium
        for i in range(min(3, len(finish_order))):
            car = finish_order[i]
            label = "1st" if i == 0 else ("2nd" if i == 1 else "3rd")
            px, py = positions[label]
            body_surface = pygame.Surface((70, 110), pygame.SRCALPHA)
            body_surface.fill((0, 0, 0, 0))
            body_points = [
                (14, 34), (24, 16), (34, 10), (44, 16), (54, 34), (50, 48), (50, 74), (54, 88), (44, 100), (34, 96), (24, 100), (14, 88), (18, 74), (18, 48)
            ]
            pygame.draw.polygon(body_surface, car.color, body_points)
            pygame.draw.rect(body_surface, (220, 220, 220), (20, 26, 28, 12), border_radius=4)
            pygame.draw.rect(body_surface, (30, 30, 30), (22, 44, 24, 18), border_radius=4)
            pygame.draw.rect(body_surface, (250, 250, 250), (24, 48, 20, 10), border_radius=3)
            pygame.draw.rect(body_surface, (40, 40, 40), (20, 70, 28, 10), border_radius=3)
            pygame.draw.rect(body_surface, (30, 30, 30), (16, 34, 8, 8), border_radius=2)
            pygame.draw.rect(body_surface, (30, 30, 30), (46, 34, 8, 8), border_radius=2)
            rotated = pygame.transform.rotate(body_surface, -90)
            r = rotated.get_rect(center=(px, py - 30))
            WIN.blit(rotated, r.topleft)
            txt = BIG.render(f"{label}: {car.name}", True, car.color)
            WIN.blit(txt, (px - txt.get_width()//2, py + 10))
            if car.finish_time is not None:
                minutes = car.finish_time // 60000
                seconds = (car.finish_time // 1000) % 60
                centis = (car.finish_time % 1000) // 10
                time_txt = FONT.render(f"{minutes}:{seconds:02}.{centis:02}", True, (255,255,255))
                WIN.blit(time_txt, (px - time_txt.get_width()//2, py + 40))

        WIN.blit(FONT.render(f"Credits earned: +{earned_credits}", True, (120, 220, 120)), (WIDTH//2 - 120, HEIGHT - 95))
        WIN.blit(FONT.render(f"Total credits: {credits}", True, (255,255,255)), (WIDTH//2 - 95, HEIGHT - 70))
        info = FONT.render("Press Enter to go back to selection", True, (200,200,200))
        WIN.blit(info, (WIDTH//2 - info.get_width()//2, HEIGHT - 40))
        pygame.display.flip()


def run_race(player_choice, difficulty, available_colors, unit, car_model):
    clock = pygame.time.Clock()
    track_rect, inner_rect = draw_track(WIN)
    waypoints = generate_waypoints(track_rect)

    # starting grid (4 cars)
    cars = []
    start_x = WIDTH//2 - 120
    start_y = track_rect.top + 60
    # choose other 3 colors from available_colors excluding player's choice
    pool = [c for c in available_colors if c[0] != player_choice[0]]
    opponents = random.sample(pool, 3)

    # map difficulties to ai speed factor
    ai_factor = {"Easy":0.60, "Medium":0.75, "Hard":0.95}[difficulty]

    # create car objects: player first
    slots = [WIDTH//2 - 90, WIDTH//2 - 30, WIDTH//2 + 30, WIDTH//2 + 90]
    player_slot = {"Easy":0, "Medium":1, "Hard":3}[difficulty]
    grid_slots = [0, 1, 2, 3]
    grid_slots.remove(player_slot)

    start_positions = [
        (WIDTH//2 - 40, start_y - 30),
        (WIDTH//2 + 40, start_y),
        (WIDTH//2 - 40, start_y + 30),
        (WIDTH//2 + 40, start_y + 60),
    ]
    position_index = [0, 1, 2, 3]
    player_slot = {"Easy":0, "Medium":1, "Hard":3}[difficulty]
    position_index.remove(player_slot)

    player_car = Car(car_model["name"], player_choice[1], start_positions[player_slot], angle=0, is_player=True, car_model=car_model["name"])
    player_car.max_speed = 5.5
    cars.append(player_car)
    for i, (name, col) in enumerate(opponents):
        pos = start_positions[position_index[i]]
        model = random.choice(CAR_MODELS)
        c = Car(model["name"], col, pos, angle=0, is_player=False, car_model=model["name"])
        # give slight variations to max speed
        c.max_speed = c.max_speed * (0.85 + random.random() * 0.15)
        cars.append(c)

    finish_order = []
    laps_needed = LAPS
    total_waypoints = len(waypoints)
    waypoint_idx = {c:0 for c in cars}

    elapsed = 0
    race_start = pygame.time.get_ticks()
    while True:
        dt = clock.tick(FPS)
        elapsed += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # update
        for c in cars:
            if c.finished:
                continue
            if c.is_player:
                c.update_player(keys)
            else:
                idx = waypoint_idx[c]
                wp = waypoints[idx]
                c.update_ai(wp, ai_factor)

            idx = waypoint_idx[c]
            wp = waypoints[idx]
            dist = math.hypot(c.x - wp[0], c.y - wp[1])
            if dist < CHECKPOINT_RADIUS:
                if not getattr(c, '_hit_waypoint', False):
                    c._hit_waypoint = True
                    waypoint_idx[c] = (idx + 1) % total_waypoints
                    if waypoint_idx[c] == 0:
                        c.lap += 1
                        if c.lap >= laps_needed and not c.finished:
                            c.finished = True
                            c.finish_time = pygame.time.get_ticks() - race_start
                            finish_order.append(c)
            else:
                c._hit_waypoint = False

        # apply surface effects after movement
        for c in cars:
            c.apply_surface_effect(track_rect, inner_rect)

        # check if race finished (all cars)
        if len(finish_order) >= len(cars):
            player_position = finish_order.index(player_car) + 1 if player_car in finish_order else len(cars)
            earned = calculate_reward(player_position, int((pygame.time.get_ticks() - race_start) / 1000), difficulty)
            return finish_order, earned

        # draw
        draw_track(WIN)
        # draw visible starting grid slots
        start_slots = [WIDTH//2 - 90, WIDTH//2 - 30, WIDTH//2 + 30, WIDTH//2 + 90]
        for i, slot_x in enumerate(start_slots):
            pygame.draw.rect(WIN, (180, 180, 180), (slot_x - 20, start_y - 50, 40, 50), 2)
            label = FONT.render(str(i + 1), True, (255, 255, 255))
            WIN.blit(label, (slot_x - label.get_width()//2, start_y - 48))
        # draw checkpoints at each turn
        for idx, wp in enumerate(waypoints):
            color = (255, 255, 0) if idx == waypoint_idx[player_car] else (200, 200, 200)
            pygame.draw.circle(WIN, color, (int(wp[0]), int(wp[1])), CHECKPOINT_DRAW_RADIUS)
            pygame.draw.circle(WIN, (0, 0, 0), (int(wp[0]), int(wp[1])), CHECKPOINT_DRAW_RADIUS + 4, 3)

        for c in cars:
            c.draw(WIN)

        # HUD
        elapsed_time = pygame.time.get_ticks() - race_start
        minutes = elapsed_time // 60000
        seconds = (elapsed_time // 1000) % 60
        centis = (elapsed_time % 1000) // 10
        timer_text = f"Time: {minutes}:{seconds:02}.{centis:02}"
        speed_mph = abs(player_car.speed) * 20
        if unit == "km/h":
            speed_value = int(speed_mph * 1.609344)
        else:
            speed_value = int(speed_mph)
        speed_text = f"Speed: {speed_value} {unit}"
        hud1 = FONT.render(f"Lap: {player_car.lap}/{laps_needed}  Difficulty: {difficulty}", True, (255,255,255))
        hud2 = FONT.render(timer_text + "   " + speed_text, True, (255,255,255))
        WIN.blit(hud1, (20, 20))
        WIN.blit(hud2, (20, 45))

        pygame.display.flip()


def main():
    credits = 0
    unlocked_cars = set(DEFAULT_UNLOCKED_CARS)
    selected_car_model = CAR_MODELS[0]
    while True:
        player_choice, difficulty, available, unit, selected_car_model, credits, unlocked_cars = selection_screen(credits, unlocked_cars, selected_car_model)
        finish, earned = run_race(player_choice, difficulty, available, unit, selected_car_model)
        credits += earned
        podium_screen(finish, earned, credits)


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
