import asyncio
import uuid
import httpx
from callme.models import Teams


async def create_teams(client: httpx.AsyncClient, teams: Teams):
    coroutines = []
    for team in teams:
        coroutines.append(client.post("/teams", data=team.model_dump_json(exclude="users")))
    result = await asyncio.gather(*coroutines)
    for response in result:
        print(response.status_code)
        print(response.headers)


async def create_team_rosters(client: httpx.AsyncClient, teams: Teams):
    coroutines = []
    for team in teams:
        roster_name = str(uuid.uuid4())
        coroutines.append(client.post(f"/teams/{team.name}/rosters/{roster_name}"))
    result = await asyncio.gather(*coroutines)
    print(result)


def login(host: str, username: str, password: str) -> httpx.AsyncClient:
    content = f"username={username}&password={password}"
    response = httpx.post(f"{host}/login", content=content)
    cookies = {"oncall-auth": response.cookies["oncall-auth"]}
    headers = {"X-Csrf-Token": response.json()["csrf_token"]}
    return httpx.AsyncClient(base_url=f'{host}/api/v0', headers=headers, cookies=cookies)


async def set_teams_schedule(host: str, username: str, password: str, teams: Teams):
    client = login(host, username, password)
    client.base_url = f"{host}/api/v0"
    async with login(host, username, password) as client:
        await create_teams(client, teams)
        await create_team_rosters(client, teams)
        # await create_team_users(client, teams)
        # await create_shifts(client, teams)
