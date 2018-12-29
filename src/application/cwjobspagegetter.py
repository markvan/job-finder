import requests

class CWJobsPageGetter:

    cookies = {
        'isMobile': '0',
        'SessionCookie': 'c29b5f6e-80a9-4f24-a80d-6a1e2e5f4a9f',
        'sc_vid': 'c35054f472526b35333419d333830c1e',
        's_fid': '7EB1A0DBF71A6D72-14E66F40D3B03C85',
        's_cc': 'true',
        'CookieComplianceAccepted': '1',
        'LOCATIONJOBTYPEID': 'null',
        'INEU': '1',
        'AutoShowJbeModal': '1',
        'AnonymousUser': 'MemberId=c46cfbd6-6c12-4af5-bab3-b400b8469e28&IsAnonymous=False',
        '2EASPXAUTH': '016BB5CE205F7B04849E7C8765343864C39F346BEF281B7E90B63D2EE52E875B982FF480D8E2FB8AC0216A3B3414B7AC77E6B6818BBE3F7043A0169A7FA4067BA5570E438FBC15E3B7E6598CA2DDBBAA97F95E3442C5F96144A5916C2E44560934E21705C640FE10EF43C830D7203A3AC1E436FF51AEE98CEE417EA452B51247A37C8E8419FE747193245B6102656FB86D23AE8857A9750B618F33F92CB10450E958AEEADBBF48664A37777750654A28E2EE10329DDBD2E6BD16C12C7FC08C2CF0666879187F530617BA2B3803AB4D57DB874BE5804182E1C4A8DCDEA839C87036877537B8C0BF359185D1F07CBCFCF3EB5E694D2352C482213896CB2131434423FD531D',
        'AnalyticsCookie': 'IsNewEmail=False',
        'IsFirstCvUpload': 'False',
        'SavedJobsDoneInitialMergeOnLogin': '1',
        'OCAActive': 'q/F3dnRMLsksS1VONjFLTktKMdM1SzY00jVJTDPVTUpMMtZNMjEwSLIwMbNMNbIAAA==',
        'CONSENTMGR': 'c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1543853408004%7Cconsent:true',
        'JBM_COOKIE': '84471527%2C84449939%2C84471758%2C84250907%2C84401679%2C84464674%2C84456916%2C84220127%2C84487905%2C84491786%2C84486174%2C84491540%2C84502813%2C84503782%2C84494092%2C84503747%2C84499947%2C84500321%2C84514268%2C84506767%2C84523218%2C84526005%2C84516932%2C84456006%2C84415745%2C84493060%2C84540310%2C84539505%2C84551451%2C84565288%2C84556169%2C84568694%2C84568930%2C84566415%2C84585209',
        'SearchKeywords': 'Efx Java Developer',
        'SearchSession': 'SessionGuid=91c13a29-fd18-4429-b69a-460ace3b5685&LogSource=NAT&SearchType=Normal&PageNo=1&ItemsPerPage=20&TotalJobNo=309&JobIds=[84514233,84581506,84624326,84595853,84557795,84556302,84626051,84559228,84611972,84600928,84569255,84437664,84561447,84318334,84310999,84631388,84616510,84607710,84585917,84575590]',
        'SearchResults': '84632908,84623727,84605561,84564612,84558978,84614632,84634764,84595014,84399617,84432630,84625999,84622828,84615431,84591249,84437187',
        'TJG-Engage': '1',
        'SoftLoginCookie': 'EWzUzyvZFTAEEeDIlbW1n7nbNy8O2LFv1Q7Rldary5p6IwHgRwdyvf5%2fB8jwt72uMDerCPJfDhJD7wjiShTjqcD5fEeh57dLjUMMv71JDfRFnI6yDMk9cK0qf0qeUgJAh0gbpkbHjaXGU6e7w0xc8oQFr8A%2f%2fPDamV4dNVsh3lxwWQOS%2bhDrpLVpEF6b9K2b%2bMJ%2fJa50Z6EJlykQFJdVGln1m5Y4H65OR0dzejGsfiOOjT5fHCQKo7S6W3B4Zz3z',
        'SoftLoginDiagnostics': 'sAEyVT6z9igLiiqd4zvniXKf5B%2fo9tH9bVngTX0YyOr2CQQElEkvEu%2b%2b8cSYEvzJlyA1XSHGtujOz3zBA7XfZ7hPMNy18fcmEfWqwvWEZgDTomMfxhJseJgc2rxM1YMP7L3j603ap2tAjytEqsRHuJPuvyZ8gdl9mKrUJ2OUZKY6nuyg4j1oTgKvLhfanwlpp3jKifyir9SEEJaJzBC7HQS8J%2bzZbBzxFYeF4g67CEDVXAec1rkTymNHo9rZkaieijglHzkg5hT5mSyPpiBNQ8qx6TBRnmB95tgND1m4FnmgEoc7%2bO73VhGnLGBe1fAlKuLPVvU66OKRf2vU1SWNYN9wdZO5HB8MFBUUihVvaB3nwkliBGxF3P8xfYv8jfHWUjpFTEBrmDN15Xhr8x%2bNytJfMQ6bD9s8D5iKYOFtkQi1jXJsbiIZDCML%2bTkVvZe97AVwROfYkBFONL6nJM2Jow%3d%3d',
        'FreshUserTemp': 'https://www.cwjobs.co.uk/',
        'gpv_pn': '%2Fdefault.aspx',
        'utag_main': 'v_id:0162911d4131001e5f4a0961f7660407900460710093c$_sn:86$_ss:1$_st:1545476553469$dc_visit:85$ses_id:1545474753469%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$appnexus_sync_session:1545474753469%3Bexp-session',
        's_ppvl': '%2FJobSearch%2FResults.aspx%2C45%2C45%2C3071%2C1392%2C666%2C1440%2C900%2C1%2CP',
        's_ppv': '%2Fdefault.aspx%2C41%2C41%2C997%2C1392%2C666%2C1440%2C900%2C1%2CP',
        's_sq': 'stepstone-tjg-cw-uk%3D%2526c.%2526a.%2526activitymap.%2526page%253D%25252Fdefault.aspx%2526link%253DProject%252520Manager%2526region%253D84491791%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253D%25252Fdefault.aspx%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.cwjobs.co.uk%25252Fjob%25252Fproject-manager%25252Fpremier-group-recruitment-job84491791%25253FKeywords%25253DProduct%252525%2526ot%253DA',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.cwjobs.co.uk/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    }

    @classmethod
    def get(cls, url):
        response = requests.get(url, headers=cls.headers, cookies=cls.cookies)
        return response.content