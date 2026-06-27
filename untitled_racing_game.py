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

    def rect(self):
        return pygame.Rect(self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)

    def draw(self, surf):
        # Draw rotated rectangle as car
        rect = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        rect.fill(self.color)
        rotated = pygame.transform.rotate(rect, -self.angle)
        r = rotated.get_rect(center=(self.x, self.y))
        surf.blit(rotated, r.topleft)

    def update_player(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed = min(self.max_speed, self.speed + 0.15)
        else:
            self.speed = max(0, self.speed - 0.08)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle += self.turn_speed * (self.speed / self.max_speed)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle -= self.turn_speed * (self.speed / self.max_speed)
        rad = math.radians(self.angle)
        self.x += math.sin(rad) * self.speed
        self.y -= math.cos(rad) * self.speed

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
    pygame.draw.rect(surface, (50, 50, 50), track_rect)
    inner = track_rect.inflate(-160, -120)
    pygame.draw.rect(surface, (22, 120, 84), inner)
    # start/finish line
    start_x = WIDTH // 2
    pygame.draw.line(surface, (255,255,255), (start_x, track_rect.top), (start_x, track_rect.top+40), 6)
    return track_rect


def generate_waypoints(track_rect):
    # around the center of the track rectangle
    left = track_rect.left + 20
    right = track_rect.right - 20
    top = track_rect.top + 20
    bottom = track_rect.bottom - 20
    return [
        (WIDTH//2, top + 10),
        (right - 10, HEIGHT//2 - 80),
        (right - 10, bottom - 10),
        (WIDTH//2, bottom - 10),
        (left + 10, bottom - 10),
        (left + 10, HEIGHT//2 - 80),
        (left + 10, top + 10),
    ]


def selection_screen():
    clock = pygame.time.Clock()
    chosen_colors = random.sample(COLOR_POOL, 4)
    player_choice = None
    difficulty = "Medium"
    difficulties = ["Easy", "Medium", "Hard"]

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
                    bx = 150 + i * 180
                    by = 260
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
                # start
                start_rect = pygame.Rect(WIDTH//2 - 80, 460, 160, 50)
                if start_rect.collidepoint(mx, my) and player_choice:
                    return player_choice, difficulty, chosen_colors

        WIN.fill((30, 30, 30))
        WIN.blit(BIG.render("Choose Your Car Color", True, (255,255,255)), (WIDTH//2 - 170, 30))
        WIN.blit(FONT.render("Available colors (pick one):", True, (200,200,200)), (80, 210))
        for i, (name, col) in enumerate(chosen_colors):
            bx = 150 + i * 180
            by = 260
            pygame.draw.circle(WIN, col, (bx, by), 40)
            txt = FONT.render(name.capitalize(), True, (255,255,255))
            WIN.blit(txt, (bx - txt.get_width()//2, by + 50))
            if player_choice and player_choice[0] == name:
                pygame.draw.circle(WIN, (255,255,255), (bx, by), 46, 3)

        WIN.blit(FONT.render("Select Difficulty:", True, (200,200,200)), (80, 350))
        for i, d in enumerate(difficulties):
            bx = 150 + i * 180
            by = 380
            r = pygame.Rect(bx - 60, by - 20, 120, 40)
            color = (100,100,100) if d != difficulty else (200,100,50)
            pygame.draw.rect(WIN, color, r)
            WIN.blit(FONT.render(d, True, (255,255,255)), (bx - 20, by - 10))

        start_rect = pygame.Rect(WIDTH//2 - 80, 460, 160, 50)
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

        info = FONT.render("Press Enter to go back to selection", True, (200,200,200))
        WIN.blit(info, (WIDTH//2 - info.get_width()//2, HEIGHT - 60))
        pygame.display.flip()


def run_race(player_choice, difficulty, available_colors):
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
    ai_factor = {"Easy":0.85, "Medium":1.0, "Hard":1.15}[difficulty]

    # create car objects: player first
    player_car = Car(player_choice[0], player_choice[1], (start_x, start_y), angle=0, is_player=True)
    cars.append(player_car)
    for i, (name, col) in enumerate(opponents):
        c = Car(name, col, (start_x + (i+1)*60, start_y), angle=0, is_player=False)
        # give slight variations to max speed
        c.max_speed = c.max_speed * (0.95 + random.random()*0.15)
        cars.append(c)

    finish_order = []
    laps_needed = LAPS
    total_waypoints = len(waypoints)
    waypoint_idx = {c:0 for c in cars}

    elapsed = 0
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
                # check proximity to waypoint
                if math.hypot(c.x - wp[0], c.y - wp[1]) < 30:
                    waypoint_idx[c] = (idx + 1) % total_waypoints
                    # crossing start line checks when wrapping to waypoint 0
                    if waypoint_idx[c] == 0:
                        c.lap += 1
                        if c.lap >= laps_needed and not c.finished:
                            c.finished = True
                            finish_order.append(c)
            # player lap detection: check crossing near start (y less than track_rect.top+50 and x near center)
            if c.is_player and not c.finished:
                if c.y < track_rect.top + 60 and abs(c.x - WIDTH//2) < 80:
                    # Assume crossing forward (simple debounce)
                    if getattr(c, '_crossed', False) is False:
                        c._crossed = True
                else:
                    c._crossed = False
                # increment lap if crossed finish area and moving downwards (approx)
                if c._crossed and c.y > track_rect.top + 80:
                    c.lap += 1
                    c._crossed = False
                    if c.lap >= laps_needed and not c.finished:
                        c.finished = True
                        finish_order.append(c)

        # check if race finished (3 finishers)
        if len(finish_order) >= 3:
            return finish_order

        # draw
        draw_track(WIN)
        for c in cars:
            c.draw(WIN)

        # HUD
        hud = FONT.render(f"Lap: {player_car.lap}/{laps_needed}  Difficulty: {difficulty}", True, (255,255,255))
        WIN.blit(hud, (20, 20))

        pygame.display.flip()


def main():
    while True:
        player_choice, difficulty, available = selection_screen()
        finish = run_race(player_choice, difficulty, available)
        podium_screen(finish)


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
