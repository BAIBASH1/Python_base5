import random
from faker import Faker
import file_operations

skills = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]
runic_alphabet = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
runic_skills = [
    'С͒т͒͒р̋̋͠͠е͠͠м͒͠ит͒͒е͠͠л̋͠ь̋н͒'
    'ы̋̋͠͠й͒͠ п̋͠р̋̋͠͠ы̋̋͠͠ж͒о̋к̋̋',
    'Э͒͠͠л̋̋͠͠е͠͠͠к̋̋̋̋т͒͒р̋̋͠͠ич̋͠е͠͠͠с͒͒к̋̋̋̋ий'
    '͒͠ в͒͠ы̋͠с͒͒т͒͒р̋̋͠͠е͠͠͠л̋̋͠͠',
    'Л̋͠е͠д̋̋я̋н͒о̋й͒͠ у͒͠д̋̋а͠р̋͠',
    'С͒т͒͒р̋̋͠͠е͠͠м͒͠ит͒͒е͠͠л̋͠ь̋н͒ы̋͠й͒͠ у͒͠д̋а͠р̋̋͠͠',
    'К̋̋ис͒л̋̋͠͠о̋т͒н͒ы̋͠й͒͠ в͒͠з̋̋͠г͒͠л̋̋͠͠я̋д̋',
    'Т͒а͠й͒͒͠͠н͒ы̋͠й͒͒͠͠ п̋͠о̋б̋е͠г͒͠',
    'Л̋͠е͠͠д̋я̋н͒о̋й͒͠ в͒͠ы̋͠с͒т͒р̋͠е͠͠л̋͠'
]


def convert_and_add_scills(skill):
    for word in skill:
        skill = skill.replace(word, runic_alphabet[word])
    runic_skills.append(skill)
    return runic_skills


def main():
    fake = Faker('ru_RU')
    for n in range(1, 11):
        random_skills = random.sample(runic_skills, 3)
        content = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'job': fake.job(),
            'town': fake.city(),
            'strength': random.randint(3, 18),
            'agility': random.randint(3, 18),
            'endurance': random.randint(3, 18),
            'intelligence': random.randint(3, 18),
            'luck': random.randint(3, 18),
            'skill_1': random_skills[0],
            'skill_2': random_skills[1],
            'skill_3': random_skills[2]
        }
        file_operations.render_template(
            'charsheet.svg',
            f"карточки игроков/card{n}.svg",
            content
        )


if __name__ == '__main__':
    main()
