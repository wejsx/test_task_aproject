import httpx

from dataclasses import dataclass, field
from typing import Optional

from infra.exceptions import HTTPError


@dataclass(eq=False, order=False, unsafe_hash=False)
class HTTPClient:
    HEADERS: dict = field(default_factory=lambda: {}, init=False)

    async def post(self, url: str, json: Optional[dict] = None, headers: Optional[dict] = None) -> dict:
        if headers:
            self.HEADERS = headers

        try:
            async with httpx.AsyncClient(headers=self.HEADERS) as client:
                r = await client.post(url=url, json=json)
                r.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPError from e
        else:
            return r.json()

    async def get(self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None) -> dict:
        try:
            async with httpx.AsyncClient(params=params) as client:
                r = await client.get(url=url)
                r.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPError from e
        else:
            return r.json()