from src import cloudmatica

# Calling cloudmatica without arguments returns a greeting
def test_no_args_displays_usage():
    import subprocess
    proc = subprocess.run(['python', 'src/cloudmatica/__init__.py'], capture_output=True, text=True)
    assert proc.stdout[:5] == 'usage'


# endpoint is set to 127.0.0.1:8000 OR chalice url based on local OR remote
def test_get_endpoint():
    assert cloudmatica.get_endpoint() == 'http://127.0.0.1:8888'


# User can call shorten with url and short parameters
def test_call_shorten():
    import subprocess
    import random
    short = str(random.randint(0, 1000000000))
    proc = subprocess.run(['python', 'src/cloudmatica/__init__.py', 'shorten', 'https://example.com', short], capture_output=True, text=True)
    assert proc.stdout == f'https://go.cloudmatica.com/{short}\n'


# User can retrieve url based on short
def test_go():
    import subprocess
    proc = subprocess.run(['python', 'src/cloudmatica/__init__.py', 'go', 'myshort'], capture_output=True, text=True)
    assert proc.stdout == 'https://example.com\n'

# Calling shorten with an invalid url returns an error
# Calling shorten with an invalid short returns an error
# Calling list returns a list of short names and urls in descending order of popularity