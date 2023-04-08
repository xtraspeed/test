def get_binary_combinations(length):
    combinations = []
    for i in range(2**length):
        binary = "{0:b}".format(i).zfill(length)
        combinations.append(binary)
    #print (len(combinations))
    filtered_combinations = [c for c in combinations if '0000' not in c]
    #print (len(filtered_combinations))
    return len(filtered_combinations)

def get_invalid_binary_strings(n):
    invalid_strings = []
    for i in range(2**n):
        b = format(i, f'0{n}b')
        if '0000' in b or b[-1] == '0':
            invalid_strings.append(b)
    return len(invalid_strings)
    
def main():
    n = 5
    ans = get_binary_combinations(n)
    ans2 = get_invalid_binary_strings(n)/2**n
    ans2 = int(round(ans2*100, 2))
    final_answer = (f"{ans2}"+"/"+f"{ans}")
    print (final_answer)
    
if __name__ == '__main__':
    main()

#Approach: Consider attending as 1 and not attending as 0 and accordingly generate binary strings.
