for test in range(int(input())):
    n = int(input())
    students = {}
    hours = {}
    dates = set()
    no_of_students = 0
    for i in range(n):
        name, time, date, status, roll_no = input().split()
        time = int(time)
        if roll_no not in students:
            no_of_students += 1
            students[roll_no] = {date: [time]}
            dates.add(date)

        elif date not in students[roll_no]:
            students[roll_no] = {date: [time]}
            dates.add(date)
            no_of_students += 1

        else:
            #print('else')
            students[roll_no][date].append(time)
    for j in students:
        for i in students[j]:

            if i not in hours.keys():
                hours[j] = abs(students[j][i][1] - students[j][i][0])
            else:
                hours[j] += abs(students[j][i][1] - students[j][i][0])
    print(max(hours.values()), no_of_students//len(dates), hours)

# 1
# 6
# dhruv 320 26/03/2021 Entry 087
# uttam 130 26/03/2021 Exit 056
# uttam 16 26/03/2021 Entry 056
# johar 460 28/04/2021 Entry 074
# dhruv 520 26/03/2021 Exit 087
# johar 720 28/04/2021 Exit 074
