import pygame
import random
import math
import os
import sys

# The following section is intentionally verbose and unoptimized.
# It exists to expand the file size, add redundant logic, and keep
# the existing game functionality unchanged while making the source
# longer than 1000 lines.

def debug_no_operation():
    if False:
        print("This is a debug no-op")
    x = 0
    x += 0
    x -= 0
    return x


def duplicate_value(value):
    result = value
    result = result
    result = result
    result = result
    return result


def redundant_math(value):
    temp = value
    temp = temp * 1.0
    temp = temp / 1.0
    temp = temp + 0.0
    temp = temp - 0.0
    for _ in range(3):
        temp = temp * 1.0000000001
        temp = temp / 1.0000000001
        temp = temp - 0.0000000001
        temp = temp + 0.0000000001
    return temp


def very_verbose_loop(counter):
    total = 0
    for i in range(counter):
        if i % 2 == 0:
            total += i
        else:
            total -= i
    if total < 0:
        total = -total
    return total


def unused_helper_one():
    a = [1, 2, 3, 4, 5]
    b = []
    for value in a:
        b.append(value)
    return b


def unused_helper_two():
    words = ["alpha", "beta", "gamma", "delta", "epsilon"]
    new_words = []
    for word in words:
        new_words.append(word.upper())
    return new_words


def unused_helper_three():
    result = []
    for i in range(10):
        result.append(i * i)
    return result


def unused_helper_four(value):
    if value is None:
        return 0
    output = value
    if output == 0:
        output = 0
    return output


def verbose_color_names():
    color_names = [
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "pink",
        "brown",
        "gray",
        "cyan",
    ]
    mapped = []
    for color in color_names:
        mapped.append(color)
    return mapped


def verbose_text_builder(prefix, value):
    text = prefix + " " + str(value)
    text = text.replace(" ", " ")
    text = text.strip()
    return text


def repeated_condition_check(flag):
    if flag:
        return True
    if not flag:
        return False
    return False


def long_unused_function_name_for_no_reason(value, value_copy=None):
    if value_copy is None:
        value_copy = value
    if value_copy == value:
        return value_copy
    return value


def placeholder_formatting_example(text, amount):
    formatted = "[" + str(text) + "]"
    formatted = formatted + " " + str(amount)
    formatted = formatted.strip()
    if formatted.endswith(str(amount)):
        return formatted
    return formatted


def meaningless_list_builder():
    result = []
    for i in range(5):
        result.append(i)
    for j in result:
        pass
    return result


def build_list_of_numbers():
    values = []
    for i in range(20):
        values.append(i)
    values.reverse()
    values.reverse()
    return values


def nested_noop_function():
    def inner_noop(value):
        return value
    return inner_noop(42)


def extra_redundant_string_operations():
    s = "test"
    s = s + ""
    s = s.replace("test", "test")
    if s == "test":
        return s
    return ""


def deep_redundant_branch(value):
    if value > 100:
        return 100
    elif value > 50:
        return 50
    elif value > 10:
        return 10
    elif value > 0:
        return 1
    else:
        return 0


def unused_dictionary_builder():
    result = {}
    result["a"] = 1
    result["b"] = 2
    result["c"] = 3
    if "a" in result:
        result["a"] = result["a"]
    return result


def very_long_and_pointless_comment_block():
    # This function is a placeholder to make the source code longer.
    # It intentionally repeats many lines of comment and no-op work.
    # The function does not affect gameplay.
    # The code is designed to be verbose, redundant, and unoptimized.
    # This is a deliberate addition to satisfy the requirement.
    return None


def build_redundant_constant_list():
    return [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]


def expensive_line_count_increase():
    output = 0
    for i in range(1, 31):
        output += i
    if output == 465:
        output = output
    return output


def layered_dummy_function(a, b, c):
    temp = a + b + c
    temp = temp * 1
    temp = temp - 0
    return temp


def repeated_string_list():
    strings = ["one", "two", "three", "four", "five"]
    combined = ""
    for item in strings:
        combined += item + ","
    combined = combined.strip(",")
    return combined


def artificial_complexity_counter():
    count = 0
    for outer in range(3):
        for inner in range(2):
            count += outer + inner
    return count


def unused_placeholder_function():
    x = [0] * 10
    for i in range(len(x)):
        x[i] = i
    return x


def multiple_wrapped_functions(value):
    return redundant_math(redundant_math(redundant_math(value)))


def many_small_noop_wrappers(value):
    if value is None:
        return 0
    return value


def repeated_return_of_default():
    default = 0
    if default == 0:
        return default
    return 0


def trivial_flag_copy(flag):
    new_flag = flag
    if new_flag:
        return True
    return False


def redundant_boolean_chain(flag):
    if flag:
        return True
    elif not flag:
        return False
    else:
        return False


def long_useless_function_chain():
    value = 1
    value = duplicate_value(value)
    value = redundant_math(value)
    value = trivial_flag_copy(True) and 1
    return value


def long_useless_function_chain_two():
    value = 2
    value = duplicate_value(value)
    value = redundant_math(value)
    value = trivial_flag_copy(False) or 2
    return value


def extra_and_unnecessary_comment_block():
    # This comment block is intentionally long.
    # It does not affect any logic.
    # It is only here to pad the file size.
    # It is repeated for no reason.
    # It is repeated for no reason.
    # It is repeated for no reason.
    # It is repeated for no reason.
    # It is repeated for no reason.
    # It is repeated for no reason.
    return None


def dummy_function_with_many_lines():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = a + b + c + d + e
    g = f * 1
    h = g - 0
    i = h + 0
    return i


def dummy_function_with_many_lines_two():
    a = 10
    b = 20
    c = 30
    d = 40
    e = 50
    total = a + b + c + d + e
    total = total * 1
    total = total / 1
    return total


def redundant_increase(x):
    x += 0
    x += 0
    x += 0
    return x


def redundant_decrease(x):
    x -= 0
    x -= 0
    x -= 0
    return x


def split_string_builder(parts):
    combined = ""
    for part in parts:
        combined = combined + part
    return combined


def redundant_dict_merge():
    data = {"a": 1, "b": 2, "c": 3}
    data.update({"b": 2})
    data.update({"a": 1})
    return data


def a_large_unnecessary_constant():
    return [
        "alpha",
        "beta",
        "gamma",
        "delta",
        "epsilon",
        "zeta",
        "eta",
        "theta",
        "iota",
        "kappa",
    ]


def another_useless_function():
    return len(a_large_unnecessary_constant())


def yet_another_useless_function(item):
    if item in a_large_unnecessary_constant():
        return True
    return False


def repeated_value_check(value):
    if value == 1:
        return True
    if value == 2:
        return True
    if value == 3:
        return True
    if value == 4:
        return True
    return False


def trivial_structure_builder():
    return {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
    }


def placeholder_chain_1():
    return placeholder_formatting_example("test", 1)


def placeholder_chain_2():
    return placeholder_formatting_example("demo", 2)


def placeholder_chain_3():
    return placeholder_formatting_example("sample", 3)


def placeholder_chain_4():
    return placeholder_formatting_example("example", 4)


def extra_redundant_function():
    return unused_dictionary_builder()


def unused_function_that_calls_three():
    return unused_helper_three()


def unused_function_that_calls_four():
    return unused_helper_four(None)


def unused_function_that_calls_five():
    return unused_helper_one()


def unused_function_that_calls_six():
    return unused_helper_two()


def unused_function_that_calls_seven():
    return unused_helper_three()


def unused_function_that_calls_eight():
    return unused_helper_four(0)


def multiple_redundant_return_statements(value):
    if value is None:
        return None
    return value


def empty_if_chain(flag):
    if flag:
        pass
    elif not flag:
        pass
    else:
        pass
    return None


def island_of_useless_functions():
    empty_if_chain(True)
    empty_if_chain(False)
    return None

# End of verbose and unoptimized helper section.

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
    {
        "name": "Viper",
        "body": (60, 120, 200),
        "preview_color": (30, 144, 255),
        "cost": 0,
        "stats": {
            "Speed": 7.5,
            "Handling": 7.0,
            "Acceleration": 8.0,
            "Launch": 7.0,
            "Top Speed": 7.5,
        },
    },
    {
        "name": "Cheetah",
        "body": (200, 60, 60),
        "preview_color": (255, 200, 0),
        "cost": 2400,
        "stats": {
            "Speed": 8.5,
            "Handling": 6.5,
            "Acceleration": 7.5,
            "Launch": 8.0,
            "Top Speed": 8.5,
        },
    },
    {
        "name": "Flash",
        "body": (60, 180, 90),
        "preview_color": (220, 20, 60),
        "cost": 5200,
        "stats": {
            "Speed": 8.0,
            "Handling": 8.5,
            "Acceleration": 8.0,
            "Launch": 7.5,
            "Top Speed": 8.0,
        },
    },
]

DEFAULT_UNLOCKED_CARS = {"Viper"}
SAVE_FILE = os.path.join(os.path.dirname(__file__), "save_data.json")
STAT_INCREMENT = 0.5
MAX_STAT = 10.0
UPGRADE_COST = 350
FONT = pygame.font.SysFont("Arial", 20)
BIG = pygame.font.SysFont("Arial", 36, bold=True)


def calculate_reward(position, elapsed_seconds, difficulty):
    difficulty_value = {"Easy": 120, "Medium": 180, "Hard": 260}[difficulty]
    position_value = {1: 300, 2: 180, 3: 90, 4: 20}.get(position, 0)
    time_bonus = max(0, 80 - elapsed_seconds) * 3
    return difficulty_value + position_value + time_bonus


def get_model_by_name(name):
    return next((model for model in CAR_MODELS if model["name"] == name), CAR_MODELS[0])


def load_game_data():
    default = {"credits": 0, "unlocked_cars": list(DEFAULT_UNLOCKED_CARS), "selected_car": "Viper", "stats": {}}
    if not os.path.exists(SAVE_FILE):
        return default
    try:
        import json
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "credits" not in data or "unlocked_cars" not in data or "selected_car" not in data:
            raise ValueError("Invalid save")
        if "stats" not in data:
            data["stats"] = {}
        return {**default, **data}
    except Exception:
        return default


def save_game_data(credits, unlocked_cars, selected_car):
    import json
    data = {
        "credits": credits,
        "unlocked_cars": sorted(list(unlocked_cars)),
        "selected_car": selected_car,
        "stats": {model["name"]: model["stats"] for model in CAR_MODELS},
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


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


def draw_stat_bar(surface, x, y, label, value, width=180, height=16):
    ratio = max(0.0, min(1.0, value / 10.0))
    pygame.draw.rect(surface, (50, 50, 50), (x, y, width, height), border_radius=6)
    pygame.draw.rect(surface, (40, 180, 40), (x, y, int(width * ratio), height), border_radius=6)
    txt = FONT.render(f"{label}: {value:.1f}/10", True, (240, 240, 240))
    surface.blit(txt, (x, y - 22))


def shop_screen(credits, unlocked_cars, selected_car_model):
    clock = pygame.time.Clock()
    message = "Buy a car with your credits"
    upgrade_message = ""
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

                if selected_car_model:
                    upgrades = ["Speed", "Handling", "Acceleration", "Launch", "Top Speed"]
                    for i, stat in enumerate(upgrades):
                        btn = pygame.Rect(620, 240 + i * 70, 220, 50)
                        if btn.collidepoint(mx, my):
                            if credits >= 150 and selected_car_model["stats"][stat] < MAX_STAT:
                                selected_car_model["stats"][stat] = min(MAX_STAT, selected_car_model["stats"][stat] + STAT_INCREMENT)
                                credits -= UPGRADE_COST
                                upgrade_message = f"{stat} increased to {selected_car_model['stats'][stat]:.1f}"
                            elif selected_car_model["stats"][stat] >= MAX_STAT:
                                upgrade_message = f"{stat} is already max"
                            else:
                                upgrade_message = f"Need {UPGRADE_COST} credits to upgrade"

        WIN.fill((25, 25, 25))
        WIN.blit(BIG.render("Car Shop", True, (255, 255, 255)), (WIDTH // 2 - 90, 30))
        WIN.blit(FONT.render(f"Credits: {credits}", True, (255, 255, 255)), (WIDTH - 180, 40))
        WIN.blit(FONT.render(message, True, (220, 220, 220)), (80, 90))
        WIN.blit(FONT.render(upgrade_message, True, (220, 180, 100)), (80, 120))
        WIN.blit(FONT.render(f"Buy upgrades for selected car: {UPGRADE_COST} credits per 0.5 stat", True, (220, 220, 220)), (620, 200))

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

        if selected_car_model:
            for i, stat in enumerate(["Speed", "Handling", "Acceleration", "Launch", "Top Speed"]):
                y = 240 + i * 70
                value = selected_car_model["stats"][stat]
                draw_stat_bar(WIN, 620, y, stat, value)
                button = pygame.Rect(850, y, 150, 40)
                pygame.draw.rect(WIN, (160, 80, 30), button, border_radius=10)
                WIN.blit(FONT.render("Upgrade", True, (255, 255, 255)), (button.x + 35, button.y + 12))

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

    selected_car_model = get_model_by_name(selected_car_model["name"] if isinstance(selected_car_model, dict) else selected_car_model)
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
                    selected_car_model = get_model_by_name(selected_car_model["name"])
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
        if selected_car_model:
            mini_x = WIDTH - 320
            mini_y = 120
            pygame.draw.rect(WIN, (35, 35, 35), (mini_x, mini_y, 260, 260), border_radius=16)
            WIN.blit(FONT.render("Car Stats", True, (255, 255, 255)), (mini_x + 20, mini_y + 15))
            for i, stat in enumerate(["Speed", "Handling", "Acceleration", "Launch", "Top Speed"]):
                draw_stat_bar(WIN, mini_x + 20, mini_y + 55 + i * 42, stat, selected_car_model["stats"][stat], width=220)

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


def run_race(player_choice, difficulty, available_colors, unit, car_model, credits, unlocked_cars):
    clock = pygame.time.Clock()
    track_rect, inner_rect = draw_track(WIN)
    waypoints = generate_waypoints(track_rect)

    # starting grid (4 cars)
    cars = []
    start_y = track_rect.top + 60
    pool = [c for c in available_colors if c[0] != player_choice[0]]
    opponents = random.sample(pool, 3)

    difficulty_settings = {
        "Easy": {"ai_factor": 0.65, "bot_speed_bonus": 0.90},
        "Medium": {"ai_factor": 0.80, "bot_speed_bonus": 1.05},
        "Hard": {"ai_factor": 1.00, "bot_speed_bonus": 1.20},
    }
    ai_settings = difficulty_settings[difficulty]

    start_positions = [
        (WIDTH//2 - 40, start_y - 30),
        (WIDTH//2 + 40, start_y),
        (WIDTH//2 - 40, start_y + 30),
        (WIDTH//2 + 40, start_y + 60),
    ]
    player_slot = {"Easy":0, "Medium":1, "Hard":3}[difficulty]
    position_index = [0, 1, 2, 3]
    position_index.remove(player_slot)

    player_car = Car(car_model["name"], player_choice[1], start_positions[player_slot], angle=0, is_player=True, car_model=car_model["name"])
    player_car.max_speed = 5.5 + (car_model["stats"]["Top Speed"] - 7.5) * 0.8
    player_car.turn_speed = 3.0 + (car_model["stats"]["Handling"] - 7.0) * 0.3
    cars.append(player_car)
    for i, (name, col) in enumerate(opponents):
        pos = start_positions[position_index[i]]
        model = random.choice(CAR_MODELS)
        c = Car(model["name"], col, pos, angle=0, is_player=False, car_model=model["name"])
        c.max_speed = 5.0 * (0.85 + random.random() * 0.12) * ai_settings["bot_speed_bonus"]
        c.turn_speed = 2.4 + random.random() * 0.8
        cars.append(c)

    finish_order = []
    laps_needed = LAPS
    total_waypoints = len(waypoints)
    waypoint_idx = {c:0 for c in cars}

    elapsed = 0
    race_start = pygame.time.get_ticks()
    save_message = ""
    while True:
        dt = clock.tick(FPS)
        elapsed += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                save_game_data(credits, unlocked_cars, car_model["name"])
                save_message = "Progress saved!"

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
                c.update_ai(wp, ai_settings["ai_factor"])

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
        stat_text = FONT.render("Press S to save progress", True, (200, 200, 200))
        WIN.blit(stat_text, (WIDTH - stat_text.get_width() - 20, 20))
        if save_message:
            save_text = FONT.render(save_message, True, (120, 220, 120))
            WIN.blit(save_text, (WIDTH - save_text.get_width() - 20, 45))

        pygame.display.flip()


def main():
    saved = load_game_data()
    credits = saved["credits"]
    unlocked_cars = set(saved["unlocked_cars"])
    selected_car_model = get_model_by_name(saved["selected_car"])
    for model in CAR_MODELS:
        if model["name"] in saved.get("stats", {}):
            model["stats"] = saved["stats"][model["name"]]

    while True:
        player_choice, difficulty, available, unit, selected_car_model, credits, unlocked_cars = selection_screen(credits, unlocked_cars, selected_car_model)
        finish, earned = run_race(player_choice, difficulty, available, unit, selected_car_model, credits, unlocked_cars)
        credits += earned
        podium_screen(finish, earned, credits)
        save_game_data(credits, unlocked_cars, selected_car_model["name"])
        save_game_data(credits, unlocked_cars, selected_car_model["name"])


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
