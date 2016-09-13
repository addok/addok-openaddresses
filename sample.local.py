from pathlib import Path

COMMON_THRESHOLD = 500
LOG_QUERIES = False
LOG_NOT_FOUND = False
FIELDS = [
    {'key': 'STREET', 'boost': 4, 'null': False, 'name': True},
    {'key': 'POSTCODE'},
    {'key': 'UNIT'},
    {'key': 'CITY'},
    {'key': 'DISTRICT'},
    {'key': 'REGION'},
    {'key': 'housenumbers'},
]
HOUSENUMBERS_PAYLOAD_FIELDS = ['id']
FILTERS = ["type", "id"]
BLOCKED_PLUGINS = ['addok.pairs', 'addok.fuzzy', 'addok.autocomplete']
QUERY_PROCESSORS = []
HOUSENUMBER_PROCESSORS = []
PROCESSORS = [
    'addok.helpers.text.tokenize',
    'addok.helpers.text.normalize',
    'addok.helpers.text.synonymize',
    'addok_trigrams.trigramize',
]
RESULTS_COLLECTORS = [
    'addok.helpers.collectors.only_commons',
    'addok.helpers.collectors.bucket_with_meaningful',
    'addok.helpers.collectors.reduce_with_other_commons',
    'addok.helpers.collectors.ensure_geohash_results_are_included_if_center_is_given',  # noqa
    'addok_trigrams.extend_results_removing_numbers',
    'addok_trigrams.extend_results_removing_one_whole_word',
    'addok_trigrams.extend_results_removing_successive_trigrams',
]
BATCH_PROCESSORS = [
    'addok_openaddresses.utils.group_addresses',
]
SEARCH_RESULT_PROCESSORS = [
    'addok.helpers.results.match_housenumber',
    'addok_openaddresses.utils.make_labels',
    'addok.helpers.results.score_by_importance',
    'addok.helpers.results.score_by_autocomplete_distance',
    'addok.helpers.results.score_by_ngram_distance',
    'addok.helpers.results.score_by_geo_distance',
]
SYNONYMS_FILENAME = 'en.txt'
OPENADDRESSES_EXTRA = {
    'CITY': ['NY', 'New York']
}
