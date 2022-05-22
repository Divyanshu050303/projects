import random
import time

rock=1
paper=2
scissor=3

name={rock:"Rock", paper:"Paper", scissor:"Scissor"}
rules={rock:scissor, paper:rock, scissor:paper}
player_score=0
computer_score=0


def start():
    print("Let's play a game of  Rock, Paper, Scissors.")
    while game():
        pass
    scores()


def game():
    player=move()
    computer=random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print("Rock=1\nPaper=2\nScissor=3\nMake a move: ")
        player=int(input())
        try:
            if(player in (1, 2, 3,)):
                return player
        except ValueError:
            pass
        print("I didn't understand that.Please enter 1, 2 or 3")


def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer threw {0}".format(name[computer]))
    global  player_score, computer_score
    if player==computer:
        print("Tie game")
    else:
        if rules[player]==computer:
            print("Your victory has been assured.")
            player_score+=1
        else:
            print("The computer laugh as you realise you have been defeated.")
            computer_score+=1


def play_again():
    print("Would you like to play again? y/n")
    answer=input()
    if answer =="y":
        return answer
    else:
        print("Thank you very much for playing out game.See you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("player:", player_score)
    print("Computer:", computer_score)


if __name__ =='__main__':
    start()