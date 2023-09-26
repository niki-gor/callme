import aiosql
from fastapi import FastAPI
import pkg_resources

from callme.config import Config
from callme.repos.connections import get_connections_pool


config = Config()

connections_pool = get_connections_pool(config)

queries_path = pkg_resources.resource_filename(__name__, "repos/queries")
queries = aiosql.from_path(queries_path, "asyncpg")

teams = TeamRepo(connections_pool, queries)
users = UserRepo(connections_pool, queries)
duties = DutyRepo(connections_pool, queries)

team_router = TeamRouter(teams)
user_router = UserRouter(users)
duty_router = DutyRouter(duties)

app = FastAPI()
app.include_router(team_router)
app.include_router(user_router)
app.include_router(duty_router)
