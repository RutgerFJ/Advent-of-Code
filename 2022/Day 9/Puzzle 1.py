def track_trace(h_pos, t_pos):
    difference = (h_pos[0] - t_pos[0], h_pos[1] - t_pos[1])
    if difference == (2, 0):
        t_pos[0] += 1
    elif difference == (-2, 0):
        t_pos[0] -= 1
    elif difference == (0, 2):
        t_pos[1] += 1
    elif difference == (0, -2):
        t_pos[1] -= 1
    elif sum(difference) == 3:
        t_pos[0] += 1
        t_pos[1] += 1
    elif sum(difference) == -3:
        t_pos[0] -= 1
        t_pos[1] -= 1
    elif difference in [(-1, 2), (-2, 1)]:
        t_pos[0] -= 1
        t_pos[1] += 1
    elif difference in [(1, -2), (2, -1)]:
        t_pos[0] += 1
        t_pos[1] -= 1
    return t_pos


def main():
    with open('input.txt', 'r') as f:
        content = [line.strip().split() for line in f]

    move_dict = {'U': [0, 1],
                 'R': [1, 0],
                 'D': [0, -1],
                 'L': [-1, 0]}
    head_pos = [0, 0]
    tail_pos = [0, 0]

    visited = []
    for i in content:
        for x in range(int(i[1])):
            visited.append(tuple(tail_pos))
            head_pos[0] += move_dict[i[0]][0]
            head_pos[1] += move_dict[i[0]][1]
            tail_pos = track_trace(head_pos, tail_pos)

    print(len(set(visited)))


main()
