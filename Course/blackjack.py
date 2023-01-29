from game_mechanic import Game


def main():
    while True:
        newgame = Game()
        newgame.start()
        replay = input("Бажаєш зіграти ще раз? 'Так' чи 'ні'?").lower()
        if replay == "y" or replay == "так":
            continue
        else:
            print("Дякую за чудову гру! До наступного разу!")
            break


if __name__ == "__main__":
    main()
