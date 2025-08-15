from urepr import uformat

def test_uformat():
    assert uformat(1, 0.1) == '1.00+/-0.10'
    assert uformat(1, 0.1, 'L') == r'1.00 \pm 0.10'