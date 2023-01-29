from game_items import Deck, Dealer, Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()

    def start(self):
        print("Нумо грати в Блекджек!")
        self.deck.shuffle()
        print(">>> Раунд перший!<<<")
        self.player.take_card(self.deck.get_top_card())
        self.dealer.take_card(self.deck.get_top_card())
        print(self.player)
        print()
        print(self.dealer)

        while self.player.active or self.dealer.active:
            print(">>> Наступний раунд <<<")
            if self.player.active and self.player.ask_card():
                self.player.take_card(self.deck.get_top_card())
                print(f"Гравець отримує {self.player.cards[-1]}")
                if self.player.points > 21:
                    break
            if self.dealer.active and self.dealer.ask_card():
                self.dealer.take_card(self.deck.get_top_card())
                print(f"Дилер отримує {self.dealer.cards[-1]}")
                if self.dealer.points > 21:
                    break
            print(self.player)
            print()
            print(self.dealer)

        print(">>> Остаточний результат <<<")
        print(self.player)
        print()
        print(self.dealer)
        print("~~~~~~~~~~~~~~~")
        if (self.player.points > 21) or (self.player.points < self.dealer.points <= 21):
            print("Шкода, дилер виграв.")
        elif (self.dealer.points > 21) or (self.player.points > self.dealer.points):
            print("Вітання! Ти переміг!")
        else:
            print("Це нічия.")
        print("~~~~~~~~~~~~~~~")
