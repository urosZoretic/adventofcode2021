from functools import cache

print("Dirac Dice")

def getMoves(lastRolledNumber):
    sum = 0
    for i in range(3):
        lastRolledNumber += 1
        sum += lastRolledNumber
        if lastRolledNumber == 100:
            lastRolledNumber = 0

    return sum, lastRolledNumber

## From input
player1Position = 2 # 4 #example
player1Score = 0

# from input
player2Position = 8 # 8 #example
player2Score = 0

nbRolls = 0
boardSize = 10

deterministicDiceRoll = 0
deterministicDiceSize = 100

nbRounds = 0
while player1Score < 1000 and player2Score < 1000:
    movePosition, deterministicDiceRoll = getMoves(deterministicDiceRoll)

    if nbRounds % 2 == 0:
        player1Position = (player1Position + movePosition) % boardSize
        if player1Position == 0:
            player1Position = boardSize
        player1Score += player1Position
    else:
        player2Position = (player2Position + movePosition) % boardSize
        if player2Position == 0:
            player2Position = boardSize
        player2Score += player2Position

    nbRolls += 3
    nbRounds += 1

minScorer = min(player1Score, player2Score)
print("part1 Score: ", nbRolls * minScorer)

##################### part2
@cache
def play_dice(
        p1_position,
        p2_position,
        dice_roll_n=0,
        dice_sum=0,
        p1_score=0,
        p2_score=0,
        next_player=1,
        winning_score=21,
        board_size=10,
):
    p1_wins = 0
    p2_wins = 0
    if next_player == 1:
        if dice_roll_n < 3:
            for i in range(1, 4):
                next_dice_sum = dice_sum + i
                next_dice_roll_n = dice_roll_n + 1
                wins = play_dice(
                    p1_position,
                    p2_position,
                    next_dice_roll_n,
                    next_dice_sum,
                    p1_score,
                    p2_score,
                    next_player,
                )
                p1_wins += wins[0]
                p2_wins += wins[1]
        else:
            dice_roll_n = 0
            next_p1_position = p1_position + dice_sum
            if next_p1_position > board_size:
                next_p1_position %= board_size
                if next_p1_position == 0:
                    next_p1_position = board_size
            next_p1_score = p1_score + next_p1_position
            if next_p1_score >= winning_score:
                p1_wins += 1
            else:
                wins = play_dice(
                    next_p1_position,
                    p2_position,
                    dice_roll_n,
                    dice_sum=0,
                    p1_score=next_p1_score,
                    p2_score=p2_score,
                    next_player=2,
                )
                p1_wins += wins[0]
                p2_wins += wins[1]

    if next_player == 2:
        if dice_roll_n < 3:
            for i in range(1, 4):
                next_dice_sum = dice_sum + i
                next_dice_roll_n = dice_roll_n + 1
                wins = play_dice(
                    p1_position,
                    p2_position,
                    next_dice_roll_n,
                    next_dice_sum,
                    p1_score,
                    p2_score,
                    next_player,
                )
                p1_wins += wins[0]
                p2_wins += wins[1]
        else:
            dice_roll_n = 0
            next_p2_position = p2_position + dice_sum
            if next_p2_position > board_size:
                next_p2_position %= board_size
                if next_p2_position == 0:
                    next_p2_position = board_size
            next_p2_score = p2_score + next_p2_position
            if next_p2_score >= winning_score:
                p2_wins += 1
            else:
                wins = play_dice(
                    p1_position,
                    next_p2_position,
                    dice_roll_n,
                    dice_sum=0,
                    p1_score=p1_score,
                    p2_score=next_p2_score,
                    next_player=1,
                )
                p1_wins += wins[0]
                p2_wins += wins[1]

    return p1_wins, p2_wins


player1Position = 2 # 4 #example
# from input
player2Position = 8 # 8 #example
p1_wins, p2_wins = play_dice(player1Position, player2Position)
print("part2.",  max(p1_wins, p2_wins))


