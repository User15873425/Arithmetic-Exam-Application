from random import choice, randint

score, msg = [], ['Enter a number:', 'simple operations with numbers 2-9', 'integral squares of 11-29']
while (lvl := input(f'Which level do you want? {msg[0]}\n1 - {msg[1]}\n2 - {msg[2]}\n')) not in ('1', '2'):
    print('Incorrect format.')
for _ in range(5):
    print(*[[a := randint(2, 9), op := choice('+-*'), b := randint(2, 9)], [x := randint(11, 29)]][int(lvl)-1])
    answer = str
    while not isinstance(answer, int):
        try:
            answer = int(input())
        except ValueError:
            print('Incorrect format.')
    score.append(answer == ({'+': a + b, '-': a - b, '*': a * b}.get(op), x * x)[int(lvl)-1])
    print(('Wrong!', 'Right!')[score[-1]])
save = input(f'Your score is {sum(score)}/5. Would you like to save the result? Enter yes or no.\n')
if save in ('yes', 'YES', 'y', 'Yes'):
    with open('results.txt', 'a+') as f:
        name = input('What is your name?\n')
        print(f'{name}: {sum(score)}/5 in level {lvl} {msg[int(lvl)]}.', file=f)
    print('The results are saved in "results.txt".')
