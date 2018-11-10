filename = 'pi_digits.txt'
#读取行
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
