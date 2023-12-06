import re
from pprint import pprint

def read_lines(file_name: str):
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
    return lines

def read_file(file_name: str):
    with open(file_name, 'r') as fin:
        text = fin.read()
    return text

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
    text = read_file(file_name)
    regex_lines = r"(Game \d+:)((((,?\s?(\d+\s\w+))+);?\s?)+)$"
    line_matches = re.finditer(regex_lines, text, re.MULTILINE)
    master_dict = {}
    for item in line_matches:
        master_dict[item.group(1)[0:-1]] = item.group(2)[1:]

    regex_values = r"(\d+\s\w+),?\s?(\d+\s\w+)?,?\s?(\d+\s\w+)?"
    for key, value in master_dict.items():
        value_matches = re.finditer(regex_values, value)
        value_list = []

        for match in value_matches:
            asd_dic = {}
            if match.group(1) is not None:
                split_group1 = match.group(1).split()
                asd_dic[split_group1[1]] = split_group1[0]
            if match.group(2) is not None:
                split_group2 = match.group(2).split()
                asd_dic[split_group2[1]] = split_group2[0]
            if match.group(3) is not None:
                split_group3 = match.group(3).split()
                asd_dic[split_group3[1]] = split_group3[0]
            value_list.append(asd_dic)
        master_dict[key] = value_list
    id_list = []
    for key, value in master_dict.items():
        i = 0
        for dic in value:
            if 'red' in dic:
                if int(dic['red']) > 12:
                    i += 1
            if 'green' in dic:
                if int(dic['green']) > 13:
                    i += 1
            if 'blue' in dic:
                if int(dic['blue']) > 14:
                    i += 1
        if i == 0:
            id_list.append(int(key[5:]))
    return sum(id_list)

if __name__ == '__main__':
    #print(day1_part1("input1.txt"))
    #print(day1_part2_take2("input1.txt"))
    print(day2_part1_take1("input2.txt"))

