import os


def get_host() -> str:
    return os.getenv("PGHOST")


def get_port() -> int:
    return os.getenv("PGPORT")


def get_user() -> str:
    return os.getenv("PGUSER")


def get_password() -> str:
    return os.getenv("PGPASSWORD")


def get_database() -> str:
    return os.getenv("PGDATABASE")


def get_database_url() -> str:
    return f"postgresql://{get_user()}:{get_password()}@{get_host()}:{get_port()}/{get_database()}"
