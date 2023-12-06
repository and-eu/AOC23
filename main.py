import re

def day1_part1(file_name: str)->int:
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
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

def day1_part2(file_name: str):  # not working
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
    list_with_numbers = []
    numbers_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    iter = 1
    for line in lines:
        numbers_on_line = {}
        for item in numbers_map.keys():
            index = line.find(item)
            if index != -1:
                numbers_on_line[index] = numbers_map[item]
        for i in range(len(line)):
            if line[i].isdigit():
                numbers_on_line[i] = int(line[i])
        print(f"Linia {iter} are dictionarul: {dict(sorted(numbers_on_line.items()))}")
        a = numbers_on_line[min(numbers_on_line.keys())]
        b = numbers_on_line[max(numbers_on_line.keys())]
        print(f"Numerele pt linia {iter} sunt: {a}, {b}")
        list_with_numbers.append(int(str(a)+str(b)))
        iter += 1
    print(list_with_numbers)
    return sum(list_with_numbers)

def day1_part2_take2(file_name: str):
    with open(file_name, 'r') as fin:
        lines = fin.readlines()
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


    return list_with_numbers

def day1_part2_take3(file_name: str):
    with open(file_name, 'r') as fin:
        mtext = fin.read()
    list_with_numbers = []
    numbers_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for key, val in numbers_map.items():
        regex = f"((?={key}))"
        mtext = re.subn(regex, str(val), mtext)[0]
    text_lista = mtext.split()
    for line in text_lista:
        temp_list = [character for character in line if character.isdigit()]
        list_with_numbers.append(int(temp_list[0]+temp_list[-1]))

    return list_with_numbers



if __name__ == '__main__':
    #print(day1_part1("input1.txt"))
    list1 = day1_part2_take2("input1.txt")
    list2 = day1_part2_take3("input1.txt")

    print(f"Sum de lista1 = {sum(list1)}")
    print(f"Sum de lista2 = {sum(list2)}")

    if len(list1)==len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                print(f"Pozitia {i} nu este identica: {list1[i]}, {list2[i]}")
