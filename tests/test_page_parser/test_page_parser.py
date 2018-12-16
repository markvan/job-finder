from tests.fixture_data.fixture_data_acccess import single_page
from src.conversions.cw_job_matches import CWJobMatches

# monkeypatch in the job matcher class
# https://stackoverflow.com/questions/5036920/mocking-out-methods-on-any-instance-of-a-python-class
CWJobMatches.get_html = lambda self: single_page('would_be_self')


def test_parse():
    # print(single_page('would_be_self')) # just for seeing the mocking / monkeypatching
    job_matcher = CWJobMatches("https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1")
    print(job_matcher.get_html())
