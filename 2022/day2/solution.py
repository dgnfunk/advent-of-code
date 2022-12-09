# 1. Rock paper scissors tornaments
#     1.1 2 Players
#     1.2 3 Options
#         1.1 Rock3 > scissors2
#         1.2 scissors2 > paper1
#         1.3 paper1 > Rock3
#     1.3 Game can be end in draw
# 2. Input a strategy guide
#     First Column
#         A: Rock = 1
#         B: paper = 2
#         C: scissors = 3
#     Second Column
#         X: Rock/lose
#         Y: paper/draw
#         Z: scissors/win
#     Win = 6
#     Draw = 3
#     Lose = 0
options_values = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

results_values = {
    'win': 6,
    'draw': 3,
    'lose': 0
}

options_posibilities = {
    'rock': ['scissors', 'rock', 'paper'],
    'paper': ['rock', 'paper', 'scissors'],
    'scissors': ['paper', 'scissors', 'rock']
}


def get_option_type(val):
    if val == 'A':
        return 'rock'
    if val == 'X':
        return 'lose'
    if val == 'B':
        return 'paper'
    if val == 'Y':
        return 'draw'
    if val == 'C':
        return 'scissors'
    if val == 'Z':
        return 'win'


def day2_solution():
    rounds = []
    results = []

    with open('input.txt', 'r') as f:
        for line in f:
            round = []
            for col in line:
                if col.isspace() is False:
                    round.append(get_option_type(col))
            rounds.append(round)
            

        for round in rounds:
            answer = None
            possible_answers = options_posibilities[round[0]]
            score = 0

            if round[1] == 'win':
                answer = possible_answers[2]
                score += options_values[answer] + results_values['win']
            elif round[1] == 'draw':
                answer = possible_answers[1]
                score += options_values[answer] + results_values['draw']
            elif round[1] == 'lose':
                answer = possible_answers[0]
                score += options_values[answer] + results_values['lose']

            print('Score for', round, answer, score)
            results.append(score)
        
        print('Total:', sum(results))



if __name__ == '__main__':
    day2_solution()