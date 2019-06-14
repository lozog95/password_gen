import string
from app import Generator


class TestGenerator():
    def test_generate_only_lowercase(self):
        pwd = Generator(10, False, False, False).generate()
        print(pwd)
        only_lowercase = True
        for letter in pwd:
            if letter not in string.ascii_lowercase:
                only_lowercase = False
        assert only_lowercase == True

    def test_generate_uppercase(self):
        pwd = Generator(10, False, True, False).generate()
        print(pwd)
        uppercase = True
        for letter in pwd:
            if letter not in string.ascii_lowercase + string.ascii_uppercase:
                uppercase = False
        assert uppercase == True

    def test_generate_digits(self):
        pwd = Generator(10, False, False, True).generate()
        print(pwd)
        digits = True
        for letter in pwd:
            if letter not in string.ascii_lowercase + string.digits:
                digits = False
        assert digits == True

    def test_generate_special(self):
        pwd = Generator(10, True, False, False).generate()
        print(pwd)
        special = True
        for letter in pwd:
            if letter not in string.ascii_lowercase + string.punctuation:
                special = False
        assert special == True

    def test_generate_combined(self):
        pwd = Generator(10, True, True, True).generate()
        print(pwd)
        combined = True
        for letter in pwd:
            if letter not in string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase:
                combined = False
        assert combined == True

    def test_generate_len(self):
        pwd_short = Generator(8, False, False, False).generate()
        pwd_med = Generator(12, False, False, False).generate()
        pwd_long = Generator(16, False, False, False).generate()
        assert len(pwd_short) == 8
        assert len(pwd_med) == 12
        assert len(pwd_long) == 16
