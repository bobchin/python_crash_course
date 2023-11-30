
def describe_pet(animal_type, pet_name):
    """ペットについての情報を出力する"""
    print(f"\n私は{animal_type}を飼っています。")
    print(f"{animal_type}の名前は{pet_name.title()}です。")

describe_pet('フェレット', 'せぶん')
describe_pet('イヌ', 'ウィリー')

describe_pet(animal_type='フェレット', pet_name='せぶん')
describe_pet(pet_name='せぶん', animal_type='フェレット')

print("/////////////////////////////////////////////////")

def describe_pet(pet_name, animal_type='イヌ'):
    """ペットについての情報を出力する"""
    print(f"\n私は{animal_type}を飼っています。")
    print(f"{animal_type}の名前は{pet_name.title()}です。")

describe_pet(pet_name='ウィリー')
describe_pet('ウィリー')

describe_pet('せぶん', 'フェレット')
describe_pet(pet_name='せぶん', animal_type='フェレット')
describe_pet(animal_type='フェレット', pet_name='せぶん')
