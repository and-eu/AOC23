import re

def read_lines(file_name: str):
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
    return lines

def day1_part1(file_name: str)->int:
    lines = read_lines(file_name)
    list_with_numbers = []
    for line in lines:
        temp_list = []
        for c in line:
            if c.isdigit():
                temp_list.append(c)
        list_with_numbers.append(int(temp_list[0]+temp_list[-1]))
    total = 0
    for i in list_with_numbers:
        total = total+i
    return total

def day1_part2_take2(file_name: str):
    lines = read_lines(file_name)
    list_with_numbers = []
    regex = r"((?=one))|((?=two))|((?=three))|((?=four))|((?=five))|((?=six))|((?=seven))|((?=eight))|((?=nine))"
    for line in lines:
        numbers_on_line = {}
        match_iter = re.finditer(regex, line)
        for item in match_iter:
            for i in range(1,10):
                match = item.group(i)
                if match is not None:
                    numbers_on_line[item.start()] = i

        for j in range(len(line)):
            if line[j].isdigit():
                numbers_on_line[j] = int(line[j])

        a = numbers_on_line[min(numbers_on_line.keys())]
        b = numbers_on_line[max(numbers_on_line.keys())]
        list_with_numbers.append(int(str(a)+str(b)))

    return sum(list_with_numbers)

def day2_part1_take1(file_name: str):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    lines = read_lines(file_name)



if __name__ == '__main__':
    #print(day1_part1("input1.txt"))
    #print(day1_part2_take2("input1.txt"))
    print(day2_part1_take1("input2.txt"))

