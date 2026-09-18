import os,sys

input_file = os.path.join(os.path.dirname(__file__), "input.txt")
if os.path.exists(input_file):
    sys.stdin = open(input_file, "r")

def rotate(pattern):
    return ["".join(row) for row in zip(*pattern[::-1])]

def get_canonical(pattern):
    candidates = []
    curr = pattern

    for _ in range(2):
        for _ in range(4):
            candidates.append(tuple(curr))
            curr = rotate(curr)
        curr = [row[::-1] for row in curr]
    return min(candidates)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    index = 1
    unique_patterns = set()

    for i in range(N):
        H = int(input_data[index])
        W = int(input_data[index + 1])
        index += 2

        pattern = []
        for _ in range(H):
            pattern.append(input_data[index])
            index += 1

        canonical = get_canonical(pattern)
        unique_patterns.add(canonical)

    print(len(unique_patterns))


if __name__ == '__main__':
    main()