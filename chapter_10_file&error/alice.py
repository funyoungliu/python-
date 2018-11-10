filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError as e:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件中有多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
