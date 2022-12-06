def main():
    with open('input.txt', 'r') as f:
        data = [line.strip('\n') for line in f]

    s = [[ln[4 * x + 1] for ln in data if len(ln) == len(data[0])
          and ln[4 * x + 1].isalpha()] for x in range(len(data[0][1::4]))]
    moves = [ln.split(' ') for ln in data if ln.split(' ')[0] == 'move']

    for m in moves:
        s[int(m[5])-1] = s[int(m[3])-1][0:int(m[1])] + s[int(m[5])-1]
        s[int(m[3])-1] = s[int(m[3])-1][int(m[1])::]

    print(''.join([i[0] for i in s]))


main()
