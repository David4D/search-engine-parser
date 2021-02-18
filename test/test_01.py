
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.googlenews import Search as GoogleNewSearch
from search_engine_parser.core.engines.yahoo import Search as YahooSearch
from search_engine_parser.core.engines.googlescholar import Search as GoogleScholarSearch
from search_engine_parser.core.engines.duckduckgo import Search as DuckDuckGoSearch
from search_engine_parser.core.engines.ask import Search as AskSearch
from search_engine_parser.core.engines.bing import Search as BingSearch
from search_engine_parser.core.engines.yandex import Search as YandexSearch
from search_engine_parser.core.engines.coursera import Search as CourseraSearch
from search_engine_parser.core.base import BaseSearch

gsearch = GoogleSearch()
gnsearch = GoogleNewSearch()
asksearch = AskSearch()
bsearch = BingSearch()
ydsearch = YandexSearch()
ysearch = YahooSearch()
ddgsearch = DuckDuckGoSearch()
csearch = CourseraSearch()
gssearch = GoogleScholarSearch()


base_search = BaseSearch()
# base_search.clear_cache(all_cache=True)

key_words = "marketing marque"

try:
    # gresults = gsearch.search(search_args[0], proxy='http://192.168.2.9:3128')
    gresults = gsearch.search(key_words)
except:
    gresults = None
try:
    gnresults = gnsearch.search(key_words)
except:
    gnresults = None
try:
    yresults = ysearch.search(key_words)
except:
    yresults = None
try:
    ydresults = ydsearch.search(key_words)
except:
    ydresults = None
try:
    gsresults = gssearch.search(key_words)
except:
    gsresults = None
try:
    ddresults = ddgsearch.search(key_words)
except:
    ddresults = None
try:
    askresults = asksearch.search(key_words)
except:
    askresults = None
try:
    bresults = bsearch.search(key_words)
except:
    bresults = None
try:
    cresults = csearch.search(key_words)
except:
    cresults = None


results = {  # 150+100+100+95+55 -> Moyenne 100
        "Google Scholar": {'results': gsresults},
        "Google": {'results': gresults},
        "Google News": {'results': gnresults},
        "Ask": {'results': askresults},
        "DuckDuck Go": {'results': ddresults},
        "Yahoo": {'results': yresults},
        "Yandex": {'results': ydresults},
        "Bing": {'results': bresults},
        "Coursera": {'results': cresults},
    }

search_results = {}
for engine, engine_results in results.items():
    print(f"-------------{engine}------------")
    if engine_results['results']:  # S'il y a des résultats
        for result in engine_results['results']:
            link = result.get('links')
            print(link)