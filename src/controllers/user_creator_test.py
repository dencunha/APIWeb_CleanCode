import pytest
from .user_creator import UsarCreator

#Classe Mock
class UserRepositoryMock:
    def __init__(self):
        self.select_user_att = {}
        self.insert_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return []

    def insert_user(self, person_name: str, age: int, height: float) -> None:
        self.insert_user_att["person_name"] = person_name
        self.insert_user_att["age"] = age
        self.insert_user_att["height"] = height

class UserRepositoryMockWithError:
    def __init__(self):
        self.select_user_att = {}

    def select_user(self, person_name: str) -> list:
        self.select_user_att["person_name"] = person_name
        return[1, 2, 3]

def test_insert_new_user():
    user_repository = UserRepositoryMock()
    user_creator = UsarCreator(user_repository)

    person_name = "my_peroaijsoiajs"
    age= 54
    height = 1.69

    response = user_creator.insert_new_user(person_name, age, height)

    # print(response)
    # print(user_repository.select_user_att)
    assert user_repository.select_user_att["person_name"] == person_name
    assert user_repository.insert_user_att["age"] == age

    assert isinstance(response, dict)
    assert "Type" in response
    assert response["count"] == 1
    assert response["message"] == "Usuário cadastrado com sucesso!"

def test_insert_new_user_with_error():
    user_repository = UserRepositoryMockWithError()
    user_creator = UsarCreator(user_repository)

    with pytest.raises(Exception) as exc_info:
        user_creator.insert_new_user("something", 32, 1.88)

    # print(exc_info.value)
    assert str(exc_info.value) == "Usuário já cadastrado!"