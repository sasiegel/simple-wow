import classes
import random

def main():
    both_living = True
    p1 = classes.Mage('player1', 5)
    p2 = classes.Paladin('player2', 4)
    while both_living:
        p1_action = random.choice(p1.abilities)
        p1_action(p2)
        if p2.hp <= 0:
            print('Player 1 wins!')
            both_living = False
            continue
        p2_action = random.choice(p2.abilities)
        p2_action(p1)
        if p1.hp <= 0:
            print('Player 2 wins!')
            both_living = False
            continue


if __name__ == "__main__":
    main()