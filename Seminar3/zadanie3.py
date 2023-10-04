# Задание 3.  (необязательное)
#Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов. 
#Для этого, вам потребуется расширить класс User новым свойством, указывающим, обладает ли пользователь админскими правами. 
#Протестируйте данную функцию.

class User:
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin

    def __str__(self):
        return f"User(username={self.username}, is_admin={self.is_admin})"


class UserRepository:
    def __init__(self):
        self.logged_in_users = []

    def login(self, user):
        self.logged_in_users.append(user)

    def logout_all_except_admins(self):
        self.logged_in_users = [user for user in self.logged_in_users if user.is_admin]

    def __str__(self):
        return f"UserRepository(logged_in_users={self.logged_in_users})"


# Тесты
import unittest

class TestUserRepository(unittest.TestCase):

    def test_logout_all_except_admins(self):
        user1 = User("user1")
        user2 = User("user2")
        admin1 = User("admin1", is_admin=True)

        repository = UserRepository()
        repository.login(user1)
        repository.login(user2)
        repository.login(admin1)

        repository.logout_all_except_admins()

        self.assertEqual(len(repository.logged_in_users), 1)
        self.assertTrue(admin1 in repository.logged_in_users)
        self.assertFalse(user1 in repository.logged_in_users)
        self.assertFalse(user2 in repository.logged_in_users)

if __name__ == '__main__':
    unittest.main()
