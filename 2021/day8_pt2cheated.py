def get_mapping(patterns):
    pattern_of_1 = pattern_of_4 = None
    mapping = {}
 
    for pattern in patterns:
        n = len(pattern)
        sorted_pattern_str = ''.join(sorted(pattern))
        pattern = set(pattern)
 
        if n == 2:
            pattern_of_1 = pattern
            mapping[sorted_pattern_str] = 1
        elif n == 3:
            mapping[sorted_pattern_str] = 7
        elif n == 4:
            pattern_of_4 = pattern
            mapping[sorted_pattern_str] = 4
        elif n == 7:
            mapping[sorted_pattern_str] = 8
 
    for pattern in patterns:
        if pattern in mapping:
            continue
 
        n = len(pattern)
        sorted_pattern_str = ''.join(sorted(pattern))
        pattern = set(pattern)
 
        if n == 6:
            if len(pattern & pattern_of_1) == 2:
                if len(pattern & pattern_of_4) == 3:
                    mapping[sorted_pattern_str] = 0
                else:
                    mapping[sorted_pattern_str] = 9
            else:
                mapping[sorted_pattern_str] = 6
        elif n == 5:
            if len(pattern & pattern_of_1) == 1:
                if len(pattern & pattern_of_4) == 2:
                    mapping[sorted_pattern_str] = 2
                else:
                    mapping[sorted_pattern_str] = 5
            else:
                mapping[sorted_pattern_str] = 3            
 
    return mapping
 
def get_decoded_output(outputs, mapping):
    res = []
 
    for output in outputs:
        res.append(str(mapping[''.join(sorted(output))]))
 
    return ''.join(res)
 
def solve_part_2(patterns_group, outputs_group):
    res = 0
 
    for patterns, outputs in zip(patterns_group, outputs_group):
        mapping = get_mapping(patterns)
        res += int(get_decoded_output(outputs, mapping))
 
    return res

if __name__ == '__main__':
    with open('input8.txt') as f:
        patterns_group = []
        outputs_group = []
 
        for line in f.readlines():
            line = line.strip().split(' | ')
 
            patterns_group.append(line[0].strip().split(' '))
            outputs_group.append(line[1].strip().split(' '))
 
        print(solve_part_2(patterns_group, outputs_group))