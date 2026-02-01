from src.models.repositories.users_repository import UsersRepository
from src.models.connection.db_connection_handler import DbConnectionHandler
from src.controllers.user_finder import UserFinder
from src.views.user_finder_views import UserFinderView

def user_finder_composer():
    conn = DbConnectionHandler()
    model = UsersRepository(conn)
    controller = UserFinder(model)
    view = UserFinderView(controller)
    return view
