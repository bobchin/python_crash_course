
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}の好きなプログラミング言語は{language.title()}です")

print("///////////////////////////////////////////////////////////")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

print("///////////////////////////////////////////////////////////")

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}、あなたの好きなプログラミング言語は{language}ですね！")

print("///////////////////////////////////////////////////////////")

if 'erin' not in favorite_languages:
    print("Erin、投票してください！")

print("///////////////////////////////////////////////////////////")

for name in sorted(favorite_languages):
    print(f"{name.title()}、投票ありがとう。")

print("///////////////////////////////////////////////////////////")

for language in favorite_languages.values():
    print(language.title())

print("///////////////////////////////////////////////////////////")

for language in set(favorite_languages.values()):
    print(language.title())

# 集合
languages = {'python', 'ruby', 'python', 'c'}
print(languages)