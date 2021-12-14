from time import perf_counter as pfc
from collections import Counter, defaultdict


def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()

    template = lines.split("\n\n")[0]
    rules = lines.split("\n\n")[1].split("\n")
    rules = [tuple(rule.split(" -> ")) for rule in rules]

    rules_dct = dict()
    for rule in rules:
        rules_dct[rule[0]] = rule[1]

    return template, rules_dct

def insertBetweenPairs(polymer, rules) -> str:
    # Initialize result polymer
    polymer_copy = ""

    # Create pairs
    for a, b in zip(polymer, polymer[1:]):

        # Add the first letter of the pair to the polymer
        polymer_copy += a

        # If the pair is in the rules, add the correct value to the polymer
        if rules.get(a + b, "not_found") != "not_found":
            polymer_copy += rules.get(a+b)

    # Add the last letter to the polymer
    polymer_copy += polymer[-1]

    return polymer_copy

def solvePuzzle(puzzleInput) -> int:
    polymer, rules = readInput(puzzleInput)

    steps = 10
    for _ in range(steps):
        polymer = insertBetweenPairs(polymer, rules)
    
    # Count the occurrences of the letters
    occurrences = Counter(polymer)
    values = occurrences.values()

    # Get the one with most occurrences and the one with least occurrences
    count_most_common = max(values)
    count_least_common = min(values)


    return count_most_common - count_least_common


def insertBetweenPairs2(template, rules, steps=40) -> str:
    letter_count = Counter(template)

    # Create polymer string from the pairs
    polymer_pair_count = Counter(["".join(x) for x in zip(template, template[1:])])

    # Do as many times as steps
    for _ in range(steps):

        # Initialize integer default dict
        current_count = defaultdict(int)
        
        # Iterate through the pairs in the polymer
        for pair in polymer_pair_count.keys():

            # Increase the count of the pair (pair's first letter and rules insertion letter) by the amount stored in polymer_pair_count
            current_count[pair[0] + rules[pair]] += polymer_pair_count[pair]

            # Increase the count of the pair (rules insertion letter and pair's second letter) by the amount stored in polymer_pair_count
            current_count[rules[pair] + pair[1]] += polymer_pair_count[pair]

            # Increase the letter count's insertion letters value by the count of the pairs in the polymer_pair_count
            letter_count[rules[pair]] += polymer_pair_count[pair]
        
        # Update the polymer_pair_count
        polymer_pair_count = current_count

    # Return the letter counter
    return letter_count


def solvePuzzle2(puzzleInput) -> int:
    template, rules = readInput(puzzleInput)
    
    letter_count = insertBetweenPairs2(template, rules, 40)
    
    # Get the one with most occurrences and the one with least occurrences
    return letter_count.most_common()[0][1] - letter_count.most_common()[-1][1]


if __name__ == '__main__':
    start_time = pfc()
    print(solvePuzzle('input14.txt'))
    print(pfc() - start_time)

    start_time = pfc()
    print(solvePuzzle2('input14.txt'))
    print(pfc() - start_time)