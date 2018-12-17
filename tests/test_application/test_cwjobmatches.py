from tests.fixtures.fixture_data_acccess import file_name_from_url
from tests.fixtures.fixture_data_acccess import page_source_from_file_name
from src.application.cwjobmatches import CWJobMatches


# test that the right file names will be used to read from in responce to url page  query
def test_file_names_from_url():
    assert file_name_from_url('https://x.com/data') == '../../tests/fixtures/multi_page_1.html'
    assert file_name_from_url('https://x.com/data&page=2') == '../../tests/fixtures/multi_page_2.html'
    assert file_name_from_url('https://x.com/data&page=3') == '../../tests/fixtures/multi_page_3.html'


def create_job_matcher():
    # monkeypatch to get file contents instead of live page source
    # from https://stackoverflow.com/questions/28127874/monkey-patching-python-an-instance-method
    job_matcher = CWJobMatches()
    job_matcher.get_html = page_source_from_file_name.__get__(job_matcher, CWJobMatches)
    return job_matcher


# test that the CWJobMatches 'fetches from files' the right html for three urls
# using CWJobMatches().get_html(self, url)
# normally that instance method is called by instance method get_jobs(self, url)
def test_file_content_from_url():
    job_matcher = create_job_matcher()
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1"
    assert '<!–– multi page 1 ––>' in job_matcher.get_html(url)
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1&page=2"
    assert '<!–– multi page 2 ––>' in job_matcher.get_html(url)
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1&page=3"
    assert '<!–– multi page 3 ––>' in job_matcher.get_html(url)


def _count_jobs(html_fragment):
    return html_fragment.count('class="job new " id=')


# could do with better test, but have hand inspected what comes back
def test_num_of_jobs_from_url():
    job_matcher = create_job_matcher()
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1"
    assert _count_jobs(job_matcher.get_jobs(url)) == 17
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1&page=3"
    assert _count_jobs(job_matcher.get_jobs(url)) == 0

def test_next_url():
    job_matcher = create_job_matcher()
    u1 = 'https://x.com/something'
    assert u1+'&page=1' == job_matcher._get_next_url(u1)
    assert u1+'&page=2' == job_matcher._get_next_url(job_matcher._get_next_url(u1))
    u2 = 'https://x.com/something&page=200'
    assert 'https://x.com/something&page=201' == job_matcher._get_next_url(u2)


