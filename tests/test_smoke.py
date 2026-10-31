def test_version():
    import alertgate
    assert alertgate.__version__ == "0.1.0"

def test_import():
    import alertgate
    assert isinstance(alertgate.__version__, str)