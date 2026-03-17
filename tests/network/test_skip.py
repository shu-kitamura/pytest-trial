import sys
import pytest

@pytest.mark.skip(reason="Test not implemented yet")
def test_skip():
    assert True


@pytest.mark.skipif(sys.platform != "linux" ,reason="Test not implemented yet")
def test_skip_linux():
    assert True


@pytest.mark.skipif(sys.platform != "win32" ,reason="Test not implemented yet")
def test_skip_windows():
    assert True


def test_skip_in_method():
    if True:
        pytest.skip("Skipping this test because of some condition")

    assert True
