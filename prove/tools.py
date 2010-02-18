from textwrap import wrap

def assert_response_contains(fragment, response):
    "assert that a response contains a given string"
    assert fragment in response.content, wrap("""
        Response should contain '%s' but doesn't:\n%s
        """ % (fragment, response.content))
