if __name__ == '__main__':

    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_highest_points = sorted(set(points for _,points in records))[1]

    for failure in sorted([name for name, points in records if points == second_highest_points]):
        print(failure)
    