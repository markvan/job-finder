from src.junk_from_before.convert import convertDecimalToHexadecimal

def test_convertDecimalToHexadecimal():
    assert convertDecimalToHexadecimal(9) == '9'

from  src.conversions.cw_job_matches import CWPages

def test_page():
    pg = CWPages()