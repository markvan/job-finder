from flask import Flask, render_template
from src.application.cwjobmatches import CWJobMatches
from tests.test_fixtures.fixture_data_acccess import page_source_from_file_name

def create_job_matcher(production):
    job_matcher: CWJobMatches = CWJobMatches()
    if not production:
        # monkeypatch to get file contents instead of live page source
        # from https://stackoverflow.com/questions/28127874/monkey-patching-python-an-instance-method
        job_matcher.get_html = page_source_from_file_name.__get__(job_matcher, CWJobMatches)
    return job_matcher


app = Flask(__name__)

@app.route("/")
def hello():
    url = "https://www.cwjobs.co.uk/jobs/contract/innovation/in-london?postedwithin=1"
    production = True
    job_matcher = create_job_matcher(production)
    out = '''
    <link rel="stylesheet" type="text/css" href="static/page.css">
    <div class="job-container">
    '''
    for job in job_matcher.next_job(url):
        out += ('<hr/>' + job)
    return out + " </div>"

@app.route('/template')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()