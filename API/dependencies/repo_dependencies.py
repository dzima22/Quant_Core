from API.terminal_repo.repository import Repository
from API.dependencies.data_dependencies import get_data_service


def get_repository() -> Repository:
    return Repository(
        data_service=get_data_service()
    )