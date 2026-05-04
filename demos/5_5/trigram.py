with open('ling471/demos/5_5/trigrams.txt') as f:
    lines = f.readlines()
    n_to_the = 0
    n_to_the_other = 0
    n_to_the_wrong = 0
    n_tokens = len(lines)
    for line in lines:
        # replace the following line with your code
        break
    
    print(f'to the: {n_to_the}')
    print(f'to the other: {n_to_the_other}')
    print(f'to the wrong: {n_to_the_wrong}')
    print(f'total: {n_tokens}')
    print(f'p(other | to the): {n_to_the_other / n_to_the * 100}')
    print(f'p(wrong | to the): {n_to_the_wrong / n_to_the * 100}')
    print(n_to_the_wrong / n_to_the)
