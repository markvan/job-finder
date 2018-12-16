from tests.fixture_data.fixture_data_acccess import single_page
from src.conversions.cw_job_matches import CWJobMatches

#mock inside the job matcher class
CWJobMatches.get_jobs = lambda self: "single_page"


def test_parse():
    CWJobMatches
    print(single_page(1))
CWJobMatches