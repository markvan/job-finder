from flask import Flask, render_template, request, redirect
from src.application.indeedjobmatches import IndeedJobMatches
from src.application.cwjobspagegetter import CWJobsPageGetter
from src.application.menu import Menu

from tests.test_fixtures.fixture_data_acccess import page_source_from_file_name

def create_job_matcher(production):
    job_matcher: IndeedJobMatches = IndeedJobMatches()
    if not production:
        # monkeypatch to get file contents instead of live page source
        # from https://stackoverflow.com/questions/28127874/monkey-patching-python-an-instance-method
        job_matcher._get_html = page_source_from_file_name.__get__(job_matcher, CWJobMatches)
    return job_matcher


app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('/find/cto', code=302)


@app.route("/find/<term>")
def find(term):
    url = 'https://www.indeed.co.uk/jobs?as_and=&as_phr=&as_any=&as_not=&as_ttl=' + term + '&as_cmp=&jt=contract&st=&as_src=&salary=&radius=10&l=london&fromage=3&limit=500&sort=date&psf=advsrch'
    production = True
    job_matcher = create_job_matcher(production)
    out = '''
    <link rel="stylesheet" type="text/css" href="/static/page.css">
    <div id="page-wrap">
    <div class="job-container">
    '''
    found_at_least_one_job = False
    for job in job_matcher.next_job(url):
        out += job
        found_at_least_one_job = True
    if not found_at_least_one_job:
        out += '<h2>No ' + term + ' jobs at the moment</h2>'
    return out + ' </div>' + Menu.generate() + '</div>'




if __name__ == "__main__":
    app.run()