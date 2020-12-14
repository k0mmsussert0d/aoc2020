import re


def parse_passport(text: str) -> dict:
    return {k: v for k, v in [x.split(':') for x in re.split(r'\n|\s', text)]}


def validate_passport(passport: dict) -> bool:
    required = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    if not set(required).issubset(set(passport.keys())):
        return False

    hgt_regexp = re.search(r'^(\d+)(\w+)$', passport.get('hgt'))
    hgt_check = False
    if hgt_regexp is not None:
        if hgt_regexp.group(2) == 'cm':
            hgt_check = hgt_regexp.group(1).isdigit() and 150 <= int(hgt_regexp.group(1)) <= 193
        elif hgt_regexp.group(2) == 'in':
            hgt_check = hgt_regexp.group(1).isdigit() and 59 <= int(hgt_regexp.group(1)) <= 76

    hcl_check = re.match(r'^#[0-9a-f]{6}$', passport.get('hcl')) is not None

    return (passport['byr'].isdigit() and 1920 <= int(passport['byr']) <= 2002 and
            passport['iyr'].isdigit() and 2010 <= int(passport['iyr']) <= 2020 and
            passport['eyr'].isdigit() and 2020 <= int(passport['eyr']) <= 2030 and
            hgt_check and hcl_check and
            passport.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
            passport['pid'].isdigit() and len(passport['pid']) == 9)


if __name__ == '__main__':
    with open('input1') as file:
        data = file.read()

    passports = [parse_passport(x) for x in data.split('\n\n')]
    print(sum([validate_passport(x) for x in passports]))
