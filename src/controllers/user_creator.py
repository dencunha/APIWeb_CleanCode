from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UsarCreator:
    def __init__(self, users_repository: UsersRepositoryInterface): # Inversão da dependência - D SOLID
        self.__users_repo = users_repository
    