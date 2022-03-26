#import cloudmatica

# Calling cloudmatica without arguments returns a greeting
def test_no_args_displays_usage():
    import subprocess
    proc = subprocess.run(['python', 'src/cloudmatica/__init__.py'], capture_output=True, text=True)
    assert proc.stdout[:5] == 'usage'


# User can call shorten with url and short parameters
def test_call_shorten():
    import subprocess
    proc = subprocess.run(['python', 'src/cloudmatica/__init__.py', 'shorten', 'https://example.com', 'myshort'], capture_output=True, text=True)
    assert proc.stdout == f'https://go.cloudmatica.com/myshort\n'


# User can retrieve url based on short
def test_go():
    import subprocess
    proc = subprocess.run(['python', 'src/cloudmatica/__init__.py', 'go', 'myshort'], capture_output=True, text=True)
    assert proc.stdout == 'https://example.com\n'

# Calling shorten with an invalid url returns an error
# Calling shorten with an invalid short returns an error
# Calling list returns a list of short names and urls in descending order of popularity