import argparse
import asyncio
from callme import api_requests
from callme.parser import parse_teams_schedule_file
from callme.config import Config


if __name__ == "__main__":
    config = Config()

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default="schedule.yml")
    args = parser.parse_args()

    teams = parse_teams_schedule_file(args.filename)
    asyncio.run(
        api_requests.set_teams_schedule(
            host=config.host,
            username=config.username,
            password=config.password,
            teams=teams.teams,
        )
    )
