import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler
from .users_repository import UsersRepository

@pytest.mark.skip(reason="Insert in DB")
def test_users_repository():
    db_con = DbConnectionHandler()
    users_repo = UsersRepository(db_con)


    person_name = "Nome meu"
    age = 456
    height = 7.34

    users_repo.insert_user(person_name, age, height)
    users = users_repo.select_user(person_name)

    assert isinstance(users, list)
    assert len(users) == 1
    assert users[0].person_name == person_name
    assert users[0].age == age
    assert users[0].height == height
