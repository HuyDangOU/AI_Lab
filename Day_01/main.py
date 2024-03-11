



def print_my_name(name):
    print(name)

def print_odd_number_in_range(begin, end):
    print("Print odd from %d to %d" % (begin, end))
    for i in range(begin, end + 1):
        if i % 2 == 0:
            print(i)

def sum_odd_number_in_range(begin, end):
    result = 0
    for i in range(begin, end + 1):
        if i % 2 == 0:
            result += i
    return result

def sum_all_number_in_range(begin, end):
    result = 0
    for i in range(begin, end + 1):
        result += i
    return result

def print_key_in_my_dict(my_dict):
    for key in my_dict.keys():
        print(key)

def print_value_in_my_dict(my_dict):
    for value in my_dict.values():
        print(value)

def print_key_value_in_my_dict(my_dict):
    for key in my_dict.keys():
        print("Key: %s - Value: %d" % (key, my_dict[key]))

def make_tuple(courses, names):
    result = []
    for course in courses:
        for name in names:
            result.append(tuple([name, course]))
    return result

def count_consonant_way1(input_string):
    not_consonant = ["e", "y", "u", "i", "o", "a"]
    result = 0
    for char in input_string:
        if char not in not_consonant:
            result +=1
    return result

def count_consonant_way2(input_string):
    not_consonant = ["e", "y", "u", "i", "o", "a"]
    result = 0
    for char in input_string:
        if char in not_consonant:
            continue
        else:
            result +=1
    return result

def divine_to_num_in_range(begin, end, dividend):
    for num in range(begin, end + 1):
        try:
            print("%d / %d = %.1f" % (dividend, num, (dividend / num)))
        except ZeroDivisionError:
            print("Can't divide by zero")

def sort_tuple(names, ages):
    data_tuples = []
    for index in range(0, len(names)):
        data_tuples.append(tuple([names[index], ages[index]]))
    data_tuples.sort(key=lambda tup: tup[1])
    return data_tuples

def read_file(path):
    lines = None
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        print(line)

def sum_of_two_number(a,b):
    return a + b

def rank_of_matrix(matrix):
    return len(matrix)

if __name__ == "__main__":
    my_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }

    courses = [131, 141, 142, 212]
    names = ["Maths", "Physics", "Chem", "Bio"]

    ages = [23, 10, 80]
    people_names = ["Hoa", "Lam", "Nam"]

    print_my_name("Dang Dinh Huy")
    print_odd_number_in_range(1, 10)
    print("Sum: %d" % sum_odd_number_in_range(1, 10))
    print(("Sum all: %d" % sum_all_number_in_range(1,10)))
    print_key_in_my_dict(my_dict)
    print_value_in_my_dict(my_dict)
    print_key_value_in_my_dict(my_dict)
    print(make_tuple(courses, names))
    print(count_consonant_way1("jabbawocky"))
    print(count_consonant_way2("jabbawocky"))
    divine_to_num_in_range(-2, 3, 10)
    print(sort_tuple(people_names, ages))
    read_file("firstname.txt")
    print(sum_of_two_number(3, 4))

    m = [[1,2,3], [4,5,6], [7,8,9]]
    v = [[1,2,3]]
    print(rank_of_matrix(m))
    print(rank_of_matrix(v))
