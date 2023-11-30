
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    if 1 < len(languages):
        print(f"\n{name.title()}の好きな言語")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        language = languages[0]
        print(f"\n{name.title()}の好きな言語は{language.title()}です。")