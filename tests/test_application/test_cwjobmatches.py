from tests.test_fixtures.fixture_data_acccess import file_name_from_url
from tests.test_fixtures.fixture_data_acccess import page_source_from_file_name
from src.application.cwjobmatches import CWJobMatches
import pytest
import psycopg2

@pytest.fixture
def url():
    return "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1"

@pytest.fixture
def job_matcher():
    # monkeypatch to get file contents instead of live page source
    # from https://stackoverflow.com/questions/28127874/monkey-patching-python-an-instance-method
    job_matcher = CWJobMatches()
    job_matcher._get_html = page_source_from_file_name.__get__(job_matcher, CWJobMatches)
    return job_matcher


# test that the right file names will be used to read from in responce to url page  query
def test_file_names_from_url():
    assert file_name_from_url('https://x.com/data') == '../../tests/test_fixtures/multi_page_1.html'
    assert file_name_from_url('https://x.com/data&page=2') == '../../tests/test_fixtures/multi_page_2.html'
    assert file_name_from_url('https://x.com/data&page=3') == '../../tests/test_fixtures/multi_page_3.html'


# test that the CWJobMatches 'fetches from files' the right html for three urls
# using CWJobMatches()._get_html(self, url)
# normally that instance method is called by instance method get_jobs_from_page(self, url)
def test_file_content_from_url(url, job_matcher):
    assert '<!–– multi page 1 ––>' in job_matcher._get_html(url)
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1&page=2"
    assert '<!–– multi page 2 ––>' in job_matcher._get_html(url)
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1&page=3"
    assert '<!–– multi page 3 ––>' in job_matcher._get_html(url)


def _count_jobs(html_fragment):
    return str(html_fragment).count('class="job new " id=')


# could do with better test, but have hand inspected what comes back
def test_num_of_jobs_from_url(url, job_matcher):
    assert _count_jobs(job_matcher.get_jobs_from_page(url)) == 17
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1&page=3"
    assert _count_jobs(job_matcher.get_jobs_from_page(url)) == 0


def test_next_url(job_matcher):
    u1 = 'https://x.com/something'
    assert u1+'&page=2' == job_matcher._make_next_url(u1)
    assert u1+'&page=3' == job_matcher._make_next_url(job_matcher._make_next_url(u1))
    u2 = 'https://x.com/something&page=200'
    assert 'https://x.com/something&page=201' == job_matcher._make_next_url(u2)


# could do with better test, only relying on counts
def test_get_jobs_from_multiple_pages(url, job_matcher):
    # the three pages have 17, 4 and 0 jobs on them
    assert _count_jobs(job_matcher._get_all_jobs(url)) == 17 + 4 + 0


def test_job_matcher_iterator(url, job_matcher):
    count = 0
    for job in job_matcher.next_job(url):
        count += 1
        print('<hr/>')
        print(job)
    assert count == 17+4+0


def test_db():
    print(' ')
    print('-----------------------------------------')
    try:
        conn = psycopg2.connect("dbname=postgres")
        print(str(conn))
        cur = conn.cursor()
        print(str(cur))
        # display the PostgreSQL database server version
        cur.execute('SELECT version()')
        print('PostgreSQL database version:')
        cur.execute("SELECT title, url FROM jobs")
        result = cur.fetchone()
        print(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    print('-----------------------------------------')


