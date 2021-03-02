import json
from ..base import BaseSearch, ReturnType, SearchItem


class Search(BaseSearch):
    name = "GoogleCustomJsonApi"
    search_url = "https://www.googleapis.com/customsearch/v1?"
    summary = "Search with Google Custom API\nNeed a API Key a Context Search (CX)\n" \
              "see: https://developers.google.com/custom-search/v1/using_rest"
    key = None
    cx = None

    def __init__(self, api_key, search_cx):
        self.key = api_key
        self.cx = search_cx

    def get_params(self, query=None, page=None, offset=None, **kwargs):
        params = {}
        params["key"] = self.key  # kwargs.get('key')
        params["cx"] = self.cx  # kwargs.get('cx')
        params["q"] = query
        params["num"] = 10
        if page > 1:
            params["start"] = 1 + (page-1) * params["num"]
        return params

    async def get_soup(self, url, cache, proxy, proxy_auth):
        """
        Hijack Soup process by using json response
        @param url:
        @param cache:
        @param proxy:
        @param proxy_auth:
        @return:
        """
        raw_json = await self.get_source(url, cache, proxy, proxy_auth)
        return json.loads(raw_json)

    def parse_soup(self, soup):
        """
        Parses Json result from Google Api response
        """
        # find all li tags
        return soup.get('items', [])

    def parse_single_result(self, single_result, return_type=ReturnType.FULL, **kwargs):
        rdict = SearchItem()
        if return_type in (ReturnType.FULL, return_type.TITLE):
            rdict["titles"] = single_result.get('title')

        if return_type in (ReturnType.FULL, return_type.LINK):
            rdict["links"] = single_result.get('link')

        if return_type in (ReturnType.FULL, return_type.DESCRIPTION):
            rdict["descriptions"] = single_result.get('snippet')

        return rdict