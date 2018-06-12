"Module for creating andela test user"

from api.models.push_id import PushID


class User:
    def __init__(self, email, first_name, last_name):
        self.id = PushID().next_id()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.name = '{0} {1}'.format(first_name, last_name)
        self.picture = 'http://i.pravatar.cc/300'
        self.roles = {
            "Andelan": "-KiihfZoseQeqC6bWTau",
            "Fellow": "-KXGy1EB1oimjQgFim6C"
        }

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'picture': self.picture,
            'roles': self.roles
        }


user_one = User('test_user@andela.com', 'test', 'user')
