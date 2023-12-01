from os import path

filename = path.join(path.dirname(__file__), "pi_digits.txt")

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


filename = path.join(path.dirname(__file__), "pi_million_digits.txt")
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("誕生日をmmddyyフォーマットで入力してください: ")
if birthday in pi_string:
    print("円周率の最初の100万桁にあなたの誕生日がみつかりました！")
else:
    print("円周率の最初の100万桁にあなたの誕生日はみつからないようです。")


