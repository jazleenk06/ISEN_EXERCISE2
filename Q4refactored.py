import random

def create_beasts():
    player_one_health = 50
    player_two_health = 50

    player_one_beast = input("Player 1, choose your beast: ")
    player_two_beast = input("Player 2, choose your beast: ")

    print("Player 1's beast is a " + player_one_beast)
    print("Player 2's beast is a " + player_two_beast)

    return player_one_health, player_two_health, player_one_beast, player_two_beast


def attack(dice_type, dice_number):
    total = 0
    for _ in range(dice_number):
        total += random.randint(1, dice_type)
    return total


def print_attack_message(player_one_beast, player_one_attack, player_two_beast, player_two_attack):
    print(f"{player_one_beast} attacks {player_two_beast} for {player_one_attack} damage")
    print(f"{player_two_beast} attacks {player_one_beast} for {player_two_attack} damage")


def play_game(player_one_health, player_two_health, player_one_beast, player_two_beast):
    while player_one_health > 0 and player_two_health > 0:
        print(f"{player_one_beast}'s health: {player_one_health}")
        print(f"{player_two_beast}'s health: {player_two_health}")

        player_one_defend = input("Player 1, do you want to defend? (y/n): ")
        player_two_defend = input("Player 2, do you want to defend? (y/n): ")

        if player_one_defend == "y":
            player_one_attack = attack(6, 2)
        else:
            player_one_attack = attack(6, 2)

        if player_two_defend == "y":
            player_two_attack = attack(6, 2)
        else:
            player_two_attack = attack(6, 2)

        player_one_health -= player_two_attack
        player_two_health -= player_one_attack

        print_attack_message(player_one_beast, player_one_attack, player_two_beast, player_two_attack)

    return player_one_health, player_two_health, player_one_beast, player_two_beast


def print_winner(player_one_health, player_two_beast):
    if player_one_health <= 0:
        print(f"{player_two_beast} wins!")
    else:
        print(f"Player 1's beast wins!")


if __name__ == "__main__":
    player_one_health, player_two_health, player_one_beast, player_two_beast = create_beasts()
    player_one_health, player_two_health, player_one_beast, player_two_beast = play_game(player_one_health, player_two_health, player_one_beast, player_two_beast)
    print_winner(player_one_health, player_one_beast)

