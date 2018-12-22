from flask import Flask, render_template, request
from src.application.cwjobmatches import CWJobMatches
from src.application.cwjobspagegetter import CWJobsPageGetter
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
    url = "https://www.cwjobs.co.uk/jobs/contract/agile/in-london?postedwithin=1"
    production = True
    job_matcher = create_job_matcher(production)
    out = '''
    <link rel="stylesheet" type="text/css" href="static/page.css">
    <div class="job-container">
    '''
    for job in job_matcher.next_job(url):
        out +=  job
    return out + " </div>"

@app.route('/template')
def home():
    return render_template('home.html')

@app.route('/getjob/')
def getjob():
    print(request)
    url = request.args.get('url')
    r = CWJobsPageGetter.get(url)
    r2 = r.replace(b'href="/', b'href="https://www.cwjobs.co.uk/')
    r3 = r2.replace(b'src="/', b'src="https://www.cwjobs.co.uk/')
    return r3



if __name__ == "__main__":
    app.run()