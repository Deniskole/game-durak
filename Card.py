class Card:
    def __init__(self, suit, rank, trump):
        suits = ['♦', '♥', '♠', '♣']
        ranks = ['J', 'Q', 'K', 'A']
        # suits = ['D', 'H', 'S', 'C']
        # Jack , Queen, King, Ace

        self.points = rank

        # Инициализация масти карты
        self.suit = suits[suit]

        # Инициализация ранга карты
        if rank < 11:
            self.rank = rank
        else:
            self.rank = ranks[rank - 11]

        if suit == trump:
            self.trump = 'Козырная карта'
        else:
            self.trump = ' '

    # Показать карту
    def show_card(self):
        length = len(str(self.rank))
        # Корректное отображение для более чем 1 символ
        if length >= 2:
            print('|' + str(self.suit) + ' ¯¯|')
            print('| ' + str(self.rank) + ' |  ' + str(self.trump))
            print('|__ ' + str(self.suit) + '|')
        # Корректное отображение для менее 1 символа
        else:
            print('|' + str(self.suit) + '¯¯|')
            print('| ' + str(self.rank) + ' |  ' + str(self.trump))
            print('|__' + str(self.suit) + '|')

        print(' ')
        return ' '

    # Получить кол-во очков карты
    def get_points(self):
        # Если карта козырная тогда +10 очков
        if self.trump == 'Козырная карта':
            self.points += 10
        return self.points
