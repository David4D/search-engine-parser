"""@desc
    Parser for Bing search results
"""
from ..base import BaseSearch, ReturnType, SearchItem


class Search(BaseSearch):
    """
    Searches Bing for string
    """
    name = "Presearch"
    search_url = "https://engine.presearch.org/search?"
    summary = "Presearch is a community-powered, decentralized search engine that provides better results while " \
              "protecting your privacy and rewarding you when you search. "

    def get_params(self, query=None, page=None, offset=None, **kwargs):
        params = {}
        params["q"] = query
        params["page"] = page
        return params  # https://engine.presearch.org/search?q=query&page=1

    def parse_soup(self, soup):
        """
        Parses Presearch for a search query.
        """
        # find all li tags
        return soup.find_all('div', class_='ml-4 mb-4 md:mb-6 max-w-2xl pr-4')

    def parse_single_result(self, single_result, return_type=ReturnType.FULL, **kwargs):
        """
        Parses the source code to return

        :param single_result: single result found in <li class="b_algo">
        :type single_result: `bs4.element.ResultSet`
        :return: parsed title, link and description of single result
        :rtype: dict
        """
        rdict = SearchItem()
        h2_tag = single_result.find('h3')
        link_tag = h2_tag.find('a')

        if return_type in (ReturnType.FULL, return_type.TITLE):
            rdict["titles"] = link_tag.text

        if return_type in (ReturnType.FULL, return_type.LINK):
            link = link_tag.get('href')
            rdict["links"] = link

        if return_type in (ReturnType.FULL, return_type.DESCRIPTION):
            caption = single_result.find('div', class_='text-gray-800')
            rdict["descriptions"] = caption.text

        return rdict
