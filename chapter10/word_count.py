from os import path

def count_words(filename):
    """ファイルに含まれるだいたいの単語の数を数える。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except:
        #print(f"ごめんなさい。{filename} は見当たりません。")
        pass
    else:
        # ファイル内のだいたいの単語の数を数える
        words = contents.split()
        num_words = len(words)
        print(f"ファイル {filename} には約{num_words}の単語が含まれます。")


filename = path.join(path.dirname(__file__), "alice.txt")
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    filename = path.join(path.dirname(__file__), filename)
    count_words(filename)