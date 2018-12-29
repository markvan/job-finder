from flask import Flask, render_template, request, redirect
from src.application.cwjobmatches import CWJobMatches
from src.application.cwjobspagegetter import CWJobsPageGetter
from src.application.menu import Menu

from tests.test_fixtures.fixture_data_acccess import page_source_from_file_name

def create_job_matcher(production):
    job_matcher: CWJobMatches = CWJobMatches()
    if not production:
        # monkeypatch to get file contents instead of live page source
        # from https://stackoverflow.com/questions/28127874/monkey-patching-python-an-instance-method
        job_matcher._get_html = page_source_from_file_name.__get__(job_matcher, CWJobMatches)
    return job_matcher


app = Flask(__name__)

@app.route("/")
@app.route('/')
def hello():
    return redirect('/find/cto', code=302)


@app.route("/find/<term>")
def find(term):
    url = 'https://www.cwjobs.co.uk/jobs/contract/' + term + '/in-london?postedwithin=1'
    production = True
    job_matcher = create_job_matcher(production)
    out = '''
    <link rel="stylesheet" type="text/css" href="/static/page.css">
    <div id="page-wrap">
    <div class="job-container">
    '''
    found_at_least_one_job = False
    for job in job_matcher.next_job(url):
        out +=  job
        found_at_least_one_job = True
    if not found_at_least_one_job:
        out += '<h2>No ' + term + ' jobs at the moment</h2>'
    return out + ' </div>' + Menu.generate() + '</div>'


'''
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
'''


if __name__ == "__main__":
    app.run()