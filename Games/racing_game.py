import pygame
import random
import math
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

FONT = pygame.font.SysFont("Arial", 20)
BIG = pygame.font.SysFont("Arial", 36, bold=True)

LAPS = 3
CHECKPOINT_RADIUS = 90
CHECKPOINT_DRAW_RADIUS = 18


class Car:
    def __init__(self, name, color, pos, angle=0, is_player=False):
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

    def rect(self):
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def draw(self, surf):
        # Draw a non-rotating car body to avoid visual glitches
        rect = pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        pygame.draw.rect(surf, self.color, rect)
        if self.wall_hit > 0:
            pygame.draw.rect(surf, (255, 255, 255), rect, 3)

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

    def is_on_road(self, track_rect):
        inner = track_rect.inflate(-160, -120)
        return track_rect.collidepoint(self.x, self.y) and not inner.collidepoint(self.x, self.y)

    def apply_surface_effect(self, track_rect):
        inner = track_rect.inflate(-160, -120)
        if self.is_on_road(track_rect):
            return

        if not track_rect.collidepoint(self.x, self.y):
            if self.x < track_rect.left:
                self.x = track_rect.left
                self.angle = (180 - self.angle) % 360
            elif self.x > track_rect.right:
                self.x = track_rect.right
                self.angle = (180 - self.angle) % 360
            if self.y < track_rect.top:
                self.y = track_rect.top
                self.angle = (-self.angle) % 360
            elif self.y > track_rect.bottom:
                self.y = track_rect.bottom
                self.angle = (-self.angle) % 360
        elif inner.collidepoint(self.x, self.y):
            left_gap = abs(self.x - inner.left)
            right_gap = abs(self.x - inner.right)
            top_gap = abs(self.y - inner.top)
            bottom_gap = abs(self.y - inner.bottom)
            min_gap = min(left_gap, right_gap, top_gap, bottom_gap)
            if min_gap == left_gap:
                self.x = inner.left
                self.angle = (180 - self.angle) % 360
            elif min_gap == right_gap:
                self.x = inner.right
                self.angle = (180 - self.angle) % 360
            elif min_gap == top_gap:
                self.y = inner.top
                self.angle = (-self.angle) % 360
            else:
                self.y = inner.bottom
                self.angle = (-self.angle) % 360

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
    # draw asphalt rectangle track
    track_rect = pygame.Rect(80, 80, WIDTH - 160, HEIGHT - 240)
    border = 18
    outer = track_rect.inflate(border * 2, border * 2)
    # draw red/white checkered barrier around the outside of the track
    block = 24
    for x in range(outer.left, outer.right, block):
        color = (255, 0, 0) if ((x // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (x, track_rect.top - border, block, border))
        pygame.draw.rect(surface, color, (x, track_rect.bottom, block, border))
    for y in range(outer.top, outer.bottom, block):
        color = (255, 0, 0) if ((y // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (track_rect.left - border, y, border, block))
        pygame.draw.rect(surface, color, (track_rect.right, y, border, block))
    pygame.draw.rect(surface, (50, 50, 50), track_rect)
    inner = track_rect.inflate(-160, -120)
    pygame.draw.rect(surface, (22, 120, 84), inner)
    # draw inner checkered barrier around the grass area
    inner_border = 16
    for x in range(inner.left, inner.right, block):
        color = (255, 0, 0) if ((x // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (x, inner.top - inner_border, block, inner_border))
        pygame.draw.rect(surface, color, (x, inner.bottom, block, inner_border))
    for y in range(inner.top, inner.bottom, block):
        color = (255, 0, 0) if ((y // block) % 2 == 0) else (255, 255, 255)
        pygame.draw.rect(surface, color, (inner.left - inner_border, y, inner_border, block))
        pygame.draw.rect(surface, color, (inner.right, y, inner_border, block))
    # draw grandstands and fans
    stand_height = 50
    stand_color = (130, 130, 130)
    left_stand = pygame.Rect(track_rect.left + 40, track_rect.top - border - stand_height - 20, 240, stand_height)
    right_stand = pygame.Rect(track_rect.right - 280, track_rect.top - border - stand_height - 20, 240, stand_height)
    pygame.draw.rect(surface, stand_color, left_stand)
    pygame.draw.rect(surface, stand_color, right_stand)
    for i in range(6):
        for row in range(3):
            fan_x = left_stand.left + 20 + i * 36
            fan_y = left_stand.top + 10 + row * 12
            pygame.draw.circle(surface, (255, 220, 180), (fan_x, fan_y), 5)
            fan_x = right_stand.left + 20 + i * 36
            pygame.draw.circle(surface, (255, 220, 180), (fan_x, fan_y), 5)
    # draw cheering flags
    for i in range(3):
        fx = left_stand.left + 40 + i * 70
        pygame.draw.polygon(surface, (255, 0, 0), [(fx, left_stand.top), (fx + 12, left_stand.top + 8), (fx, left_stand.top + 16)])
        fx = right_stand.left + 40 + i * 70
        pygame.draw.polygon(surface, (0, 0, 255), [(fx, right_stand.top), (fx + 12, right_stand.top + 8), (fx, right_stand.top + 16)])
    # draw trees and bushes behind stands
    for i, tx in enumerate(range(track_rect.left + 20, track_rect.right, 120)):
        pygame.draw.rect(surface, (101, 67, 33), (tx, track_rect.top - border - stand_height - 60, 10, 20))
        pygame.draw.circle(surface, (20, 120, 20), (tx + 5, track_rect.top - border - stand_height - 70), 18)
        pygame.draw.circle(surface, (16, 100, 16), (tx - 18, track_rect.top - border - stand_height - 50), 12)
        pygame.draw.circle(surface, (16, 100, 16), (tx + 18, track_rect.top - border - stand_height - 50), 12)
    # start/finish line
    start_x = WIDTH // 2
    pygame.draw.line(surface, (255,255,255), (start_x, track_rect.top), (start_x, track_rect.top+40), 6)
    return track_rect


def generate_waypoints(track_rect):
    left = track_rect.left + 40
    right = track_rect.right - 40
    top = track_rect.top + 40
    bottom = track_rect.bottom - 40
    return [
        (right, top),
        (right, bottom),
        (left, bottom),
        (left, top),
    ]


def selection_screen():
    clock = pygame.time.Clock()
    chosen_colors = list(COLOR_POOL)
    player_choice = None
    difficulty = "Medium"
    unit = "km/h"
    difficulties = ["Easy", "Medium", "Hard"]
    units = ["km/h", "mph"]

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()
                # color buttons
                for i, (name, col) in enumerate(chosen_colors):
                    bx = 120 + (i % 5) * 160
                    by = 240 + (i // 5) * 120
                    br = pygame.Rect(bx - 40, by - 40, 80, 80)
                    if br.collidepoint(mx, my):
                        player_choice = (name, col)
                # difficulty buttons
                for i, d in enumerate(difficulties):
                    bx = 150 + i * 180
                    by = 380
                    br = pygame.Rect(bx - 60, by - 20, 120, 40)
                    if br.collidepoint(mx, my):
                        difficulty = d
                # unit buttons
                for i, u in enumerate(units):
                    bx = 150 + i * 180
                    by = 450
                    br = pygame.Rect(bx - 60, by - 20, 120, 40)
                    if br.collidepoint(mx, my):
                        unit = u
                # start
                start_rect = pygame.Rect(WIDTH//2 - 80, 520, 160, 50)
                if start_rect.collidepoint(mx, my) and player_choice:
                    return player_choice, difficulty, chosen_colors, unit

        WIN.fill((30, 30, 30))
        WIN.blit(BIG.render("Choose Your Car Color", True, (255,255,255)), (WIDTH//2 - 170, 30))
        WIN.blit(FONT.render("Available colors (pick one):", True, (200,200,200)), (80, 210))
        for i, (name, col) in enumerate(chosen_colors):
            bx = 120 + (i % 5) * 160
            by = 240 + (i // 5) * 120
            pygame.draw.circle(WIN, col, (bx, by), 30)
            txt = FONT.render(name.capitalize(), True, (255,255,255))
            WIN.blit(txt, (bx - txt.get_width()//2, by + 40))
            if player_choice and player_choice[0] == name:
                pygame.draw.circle(WIN, (255,255,255), (bx, by), 36, 3)

        WIN.blit(FONT.render("Select Difficulty:", True, (200,200,200)), (80, 350))
        for i, d in enumerate(difficulties):
            bx = 150 + i * 180
            by = 380
            r = pygame.Rect(bx - 60, by - 20, 120, 40)
            color = (100,100,100) if d != difficulty else (200,100,50)
            pygame.draw.rect(WIN, color, r)
            WIN.blit(FONT.render(d, True, (255,255,255)), (bx - 20, by - 10))

        WIN.blit(FONT.render("Speed unit:", True, (200,200,200)), (80, 450))
        for i, u in enumerate(units):
            bx = 150 + i * 180
            by = 450
            r = pygame.Rect(bx - 60, by - 20, 120, 40)
            color = (100,100,100) if u != unit else (200,100,50)
            pygame.draw.rect(WIN, color, r)
            WIN.blit(FONT.render(u, True, (255,255,255)), (bx - 20, by - 10))

        start_rect = pygame.Rect(WIDTH//2 - 80, 520, 160, 50)
        pygame.draw.rect(WIN, (30, 160, 30) if player_choice else (80,80,80), start_rect)
        WIN.blit(FONT.render("Start Race", True, (255,255,255)), (start_rect.x + 28, start_rect.y + 12))

        pygame.display.flip()


def podium_screen(finish_order):
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
            # draw car as circle
            pygame.draw.circle(WIN, car.color, (px, py - 30), 30)
            txt = BIG.render(f"{label}: {car.name}", True, car.color)
            WIN.blit(txt, (px - txt.get_width()//2, py + 10))
            if car.finish_time is not None:
                minutes = car.finish_time // 60000
                seconds = (car.finish_time // 1000) % 60
                centis = (car.finish_time % 1000) // 10
                time_txt = FONT.render(f"{minutes}:{seconds:02}.{centis:02}", True, (255,255,255))
                WIN.blit(time_txt, (px - time_txt.get_width()//2, py + 40))

        info = FONT.render("Press Enter to go back to selection", True, (200,200,200))
        WIN.blit(info, (WIDTH//2 - info.get_width()//2, HEIGHT - 60))
        pygame.display.flip()


def run_race(player_choice, difficulty, available_colors, unit):
    clock = pygame.time.Clock()
    track_rect = draw_track(WIN)
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

    player_car = Car(player_choice[0], player_choice[1], start_positions[player_slot], angle=0, is_player=True)
    player_car.max_speed = 5.5
    cars.append(player_car)
    for i, (name, col) in enumerate(opponents):
        pos = start_positions[position_index[i]]
        c = Car(name, col, pos, angle=0, is_player=False)
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
            c.apply_surface_effect(track_rect)

        # check if race finished (3 finishers)
        if len(finish_order) >= 3:
            return finish_order

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
    while True:
        player_choice, difficulty, available, unit = selection_screen()
        finish = run_race(player_choice, difficulty, available, unit)
        podium_screen(finish)


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
