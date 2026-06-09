import unittest

from toolkit import check_password_strength


class PasswordStrengthTests(unittest.TestCase):
    def test_weak_password(self) -> None:
        result = check_password_strength("abc")
        self.assertEqual(result["level"], "Weak")
        self.assertEqual(result["score"], 1)

    def test_moderate_password(self) -> None:
        result = check_password_strength("Password1")
        self.assertEqual(result["level"], "Moderate")
        self.assertEqual(result["score"], 4)

    def test_strong_password(self) -> None:
        result = check_password_strength("Str0ng!Pass")
        self.assertEqual(result["level"], "Strong")
        self.assertEqual(result["score"], 5)


if __name__ == "__main__":
    unittest.main()
