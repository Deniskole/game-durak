class Player():
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    # Показать все карты игрока
    def show_cards(self):
        print('')
        print('        Карты игрока имя: ' + self.name)
        print()
        for t in range(0, 6):
            card = self.cards[t]
            card.show_card()

    # Получение суммы всех очков карт игрока
    def get_points_of_all_card(self):
        length = len(self.cards)
        total_points = 0
        for x in range(0, length):
            card = self.cards[x]
            total_points += card.get_points()
        return total_points
