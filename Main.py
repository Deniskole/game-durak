import random

from Card import *
from Player import Player

players = []
cards = []
random_trump = random.randint(0, 3)
quantity_of_players = 0


# Показать козырь
def what_is_trump():
    suits = ['Бубны ', 'Червы ', 'Пики ', 'Трефы ']
    trumps = ['♦', '♥', '♠', '♣']
    # Если символы не отображает из trumps использовать буквы
    # trumps = ['D', 'H', 'S', 'C']
    print('Козырь ' + trumps[random_trump] + ' ' + suits[random_trump])


# Инициализация карт по мастям
def init_cards(suit):
    rank = 6
    for j in range(0, 9):
        cards.append(Card(suit, rank, random_trump))
        rank = rank + 1


# Создание колоды
def creating_a_deck():
    print('Колода создана')
    for i in range(0, 4):
        init_cards(i)


# Показать всю колоду
def show_deck_of_cards():
    x = 1
    print('\n--------------------------------------')
    print('--------- Показать колоду карт -------')
    print('--------------------------------------\n')

    for card in cards:
        print('------Карта# ' + str(x) + '------'  '\n')
        x = x + 1
        print(card.show_card())


# Перетасовать колоду
def shuffle_deck():
    print('Колода перетосована')
    for t in range(0, 66):
        for r in range(0, len(cards)):
            length = len(cards)
            rand2 = random.randint(0, length - 1)
            card1 = cards[rand2]
            cards.__delitem__(rand2)
            cards.append(card1)


# Инициализация игроков
def init_players(quantity):
    player_names = ['Денис', 'Айдос', 'Семен', 'Ваня', 'Света', 'Лаура', 'Лиза', 'Петя']
    player_cards = []
    for p in range(0, quantity):
        random_name = random.randint(0, len(player_names) - 1)
        for g in range(0, 6):
            player_cards.append(cards.pop(0))
        player = Player(player_names[random_name], player_cards)
        players.append(player)


# Показать всех игроков и их карты
def show_all_players_cards(quantity):
    print('\n--------------------------------------')
    print('------ Количество игроков: ' + str(len(players)) + ' --------')
    print('--------------------------------------\n')
    for x in range(0, quantity):
        p = players[x]
        p.show_cards()


# Количество карт в колоде
def cards_in_the_deck():
    print('Колличество карт в колоде: ' + str(len(cards)))


# Кто имеет лучшие карты
def who_has_the_best_cards(quantity):
    max_point_array = []
    counter = 0
    print('--------------------------------------')
    print('----------- Очки игроков -------------:')
    print('--------------------------------------')
    for f in range(0, quantity):
        player = players[f]
        poin = player.get_points_of_all_card()
        max_point_array.append(poin)
        print('Игрок #' + str(f + 1) + ' Имя: ' + player.name + ' Очки: ' + str(poin))

    max_point = max(max_point_array)

    index_of_best_player = 0
    for p in max_point_array:
        if p == max_point:
            break
        counter = counter + 1
        index_of_best_player = counter

    best = players[index_of_best_player]

    print('--------------------------------------')
    print('Лучшие карты у игрока #' + str(index_of_best_player + 1))
    print('Имя: ' + best.name + ' ' + str(max_point) + ' очки')
    print('--------------------------------------\n')

    play = players[index_of_best_player]
    play.show_cards()


# Главный цикл игры
def game_loop():
    print('\n--------------------------------------')
    print('------ Карточная игра в дурака -------')
    print('--------------------------------------\n')

    print('ШАГ 1: Определить козырь')
    # Показать козырь
    what_is_trump()

    print('ШАГ 2: Создать колоду')
    # Создание колоды
    creating_a_deck()
    # Количество карт в колоде
    cards_in_the_deck()

    print('ШАГ 3: Перетосовать колоду')
    # Перетасовать колоду
    shuffle_deck()

    print('ШАГ 4: Введите количество игроков.')

    check_input = True
    while (check_input):
        try:
            quantity_of_players = int(input())

            if quantity_of_players >1 and quantity_of_players <=6:
                check_input = False
            if quantity_of_players <= 1:
                print('Минимум 2 игрока!')
            elif quantity_of_players > 6:
                print('Максимум 6 игроков!')
        except Exception:
            print('Ошибка ввода только цифры!')

    print('Количество игроков: ' + str(quantity_of_players))
    print('ШАГ 5: Создание игроков и раздача им карт с колоды')
    # Инициализация игроков

    init_players(quantity_of_players)
    print('Игроки созданы успешно, карты розданы')

    # Количество карт в колоде
    cards_in_the_deck()

    flag = True

    while (flag):

        print('\nВыберите действие:')
        print('1 - Показать козырь')
        print('2 - Показать колоду карт')
        print('3 - Показать игрока с лучшими картами')
        print('4 - Показать всех игроков и их карты')
        print('5 - Выход')

        try:
            input_user = int(input())
            if input_user == 1:
                what_is_trump()
            elif input_user == 2:
                show_deck_of_cards()
            elif input_user == 3:
                who_has_the_best_cards(quantity_of_players)
            elif input_user == 4:
                show_all_players_cards(quantity_of_players)
            elif input_user == 5:
                print('Выход')
                exit()
            else:
                print('Ошибка ввода только 1,2,3,4,5,6')
        except Exception:
            print('Ошибка ввода только цифры!')


game_loop()
