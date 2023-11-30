import os
from dotenv import load_dotenv
from requests import Session

def get_requests_session() -> Session:
    session = Session()
    session.headers.update({"User-Agent": "https://github.com/jmerle/advent-of-code-2023 by jaspervmerle@gmail.com"})

    load_dotenv()
    session.cookies.set("session", os.environ["SESSION_COOKIE"])

    return session
