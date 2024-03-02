import pygame
import random
import sys

# вводим пигаме
pygame.init()

# разрешение экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test Your Knowledge")

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# шрифты
font = pygame.font.SysFont("Arial", 25)
big_font = pygame.font.SysFont("Arial", 48)

# вопросы
questions = [
    {"question": "How many continents are there?", "answer": 10},
    {"question": "Answer of 3/3(3*3)*3/3+3 ?", "answer": 12},
    {"question": "When did the second world war start?", "answer": 1939},
    {"question": "How high is the eiffel tower?", "answer": 300},
    {"question": "How many countries in europe", "answer": 50},
    {"question": "How many bones are there in the adult human body?", "answer": 206},
    {"question": "What is the atomic number of oxygen?", "answer": 8},
    {"question": "How many countries does the equator pass through?", "answer": 11},
    {"question": "How many time zones are there in Russia?", "answer": 11},
    {"question": "How many planets are in our solar system? (count Pluto)", "answer": 8},


]

# переменные
in_menu = True
game_running = False
question_index = 0
user_answer = ""
score = 0

# графика
try:
    background_image = pygame.image.load("background.png")
except Exception:
    background_image = pygame.Surface((screen_width, screen_height))
    background_image.fill(WHITE)

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)


# функции
# функция рисования
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


# функция отрисовки меню
def draw_menu():
    screen.blit(background_image, (0, 0))
    draw_text("TEST YOUR KNOWLEDGE", big_font, BLACK, screen, 180, 50)
    draw_text("Start Game", font, BLUE, screen, 320, 250)
    draw_text("Exit", font, BLACK, screen, 360, 300)


# функция отрисовки игры
def draw_game():
    global user_answer
    screen.blit(background_image, (0, 0))
    question = questions[question_index]["question"]
    draw_text(question, font, BLACK, screen, 100, 200)
    input_box = pygame.Rect(100, 250, 140, 32)
    pygame.draw.rect(screen, BLACK, input_box, 2)
    draw_text(user_answer, font, BLACK, screen, 105, 255)


# функция запуска игры
def start_game():
    global in_menu, game_running
    in_menu = False
    game_running = True


# функция выхода
def exit_game():
    pygame.quit()
    sys.exit()


# функция перехода к следующему вопросу
def next_question():
    global question_index, user_answer, score
    # переменная для хранения правильного ответа
    correct_answer = questions[question_index]["answer"]
    # проверка правильности ответа
    try:

        user_input = int(user_answer)
        # вычисление разницы между правильным ответом и введенным пользователем
        difference = abs(correct_answer - user_input)
        ## увеличиваем баллы за правильные ответы
        score += max(0, 100 - difference * 10)
    except ValueError:
        # если пользователь ничего не ввел
        pass

    # обнуляем переменные
    question_index += 1
    if question_index >= len(questions):
        # если вопросы закончились
        show_results()
    else:
        # если еще есть вопросы
        user_answer = ""


# функция показа результата
def show_results():
    global game_running
    game_running = False
    final_score = (score / len(questions))
    screen.blit(background_image, (0, 0))
    draw_text(f"Your Score: {final_score}%", big_font, BLACK, screen, 200, 250)


# цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if in_menu:
                if event.key == pygame.K_RETURN:
                    start_game()
            elif game_running:
                if event.key == pygame.K_RETURN:
                    next_question()
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    if event.unicode.isdigit():
                        user_answer += event.unicode

    screen.fill(WHITE)
    if in_menu:
        draw_menu()
    elif game_running:
        draw_game()
    else:
        show_results()

    pygame.display.update()

pygame.quit()
