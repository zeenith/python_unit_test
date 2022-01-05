import unittest


class MotDePasseValide:
    def __init__(self, password):

        self.password = password


    def checkPasswordLength(self):
        return bool(10 <= len(self.password) <= 25)


    def checkSpecialChar(self):

        sc_list = list('[@_!#$%^&*()<>?/\|}{~:]')
        for char in self.password:
            if char in sc_list:
                return True
        return False

    def checkCase(self):
        low = False
        up = False
        for char in self.password:
            if char.isupper():
                up = True
            if char.islower():
                low = True
        return low and up

    def checkObvious(self):
        obvious_tuple = ('azertyuiop', 'azerty', 'qwertyuiop', 'password', 'password01', 'Azertyuiop01*')
        for obvious in obvious_tuple:
            if self.password == obvious:
                return False
        return True

    def checkSpace(self):
        for char in self.password:
            if char.isspace():
                return False
        return True

    def checkNum(self):
        num = False
        for char in self.password:
            if char.isnumeric():
                num = True
        return num

    def isValid(self):
        return self.checkPasswordLength() and self.checkCase() and self.checkObvious() and \
               self.checkSpecialChar() and self.checkSpace() and self.checkNum()


class MyTestCase(unittest.TestCase):

    def test_password_valid_length(self):
        password = MotDePasseValide("azerf2222222345")
        self.assertEqual(password.checkPasswordLength(), True)

    def test_password_valid_SC(self):
        password = MotDePasseValide("aaaaaaa*aa")
        self.assertEqual(password.checkSpecialChar(), True)

    def test_password_valid_case(self):
        password = MotDePasseValide("aAa")
        self.assertEqual(password.checkCase(), True)

    def test_password_valid_obvious(self):
        password = MotDePasseValide("azerf2222222345")
        self.assertEqual(password.checkObvious(), True)

    def test_password_valid_space(self):
        password = MotDePasseValide("azerf2222222345")
        self.assertEqual(password.checkSpace(), True)

    def test_password_valid_num(self):
        password = MotDePasseValide("azerf2222222345")
        self.assertEqual(password.checkNum(), True)

    def test_password_valid_isValid(self):
        password = MotDePasseValide("0123456789*Aa")
        self.assertEqual(password.isValid(), True)


if __name__ == '__main__':
    unittest.main()
