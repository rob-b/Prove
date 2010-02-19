from prove.tools import ok_, inline, eq_
from django.template import Template, Context
import re

__all__ = ('assert_contains', 'assert_doesnt_contain',
           'assert_response_contains', 'assert_response_doesnt_contain',
           'assert_regex_contains', 'assert_render_matches', 'assert_code',
           'assert_render', 'assert_doesnt_render', 'assert_render_contains',
           'assert_render_doesnt_contain')

template_tag_libraries = []
def render(template, **kwargs):
    "Return the rendering of a given template including loading of template tags"
    template = "".join(["{%% load %s %%}" % lib for lib in template_tag_libraries]) + template
    return Template(template).render(Context(kwargs)).strip()

def assert_contains(needle, haystack):
    "Assert that one value (the haystack) contains another value (the needle)"
    return ok_(needle in haystack,
               "Content should contain `%s' but doesn't:\n%s" % (needle, haystack))

def assert_doesnt_contain(needle, haystack):
    "Assert that one value (the hasystack) does not contain another value (the needle)"
    return ok_(needle not in haystack, "Content should not contain `%s' but does:\n%s" % (needle, haystack))


def assert_response_contains(fragment, response):
    "Assert that a response contains a given string"
    assert fragment in response.content, inline("""
        Response should contain '%s' but doesn't:\n%s
        """ % (fragment, response.content))

def assert_response_doesnt_contain(fragment, response):
    "Assert that a response does not contain a given string"
    assert fragment not in response.content, inline("""
        Response should not contain '%s' but does:\n%s
        """ % (fragment, response.content))


def assert_regex_contains(pattern, string, flags=None):
    "Assert that the given regular expression matches the string"
    flags = flags or 0
    assert re.search(pattern, string, flags) != None

def assert_render_matches(template, match_regexp, vars={}):
    """Assert that the output from rendering a given template with a given context
    matches a given regex"""
    r = re.compile(match_regexp)
    actual = Template(template).render(Context(vars))
    ok_(r.match(actual), "Expected: %s\nGot: %s" % (
        match_regexp, actual
    ))

def assert_code(response, code):
    "Assert that a given response returns a given HTTP status code"
    eq_(code, response.status_code,
        "HTTP Response status code %d expected, but got %d" % (code,
                                                               response.status_code))

def assert_render(expected, template, **kwargs):
    "Asserts than a given template and context render a given fragment"
    eq_(expected, render(template, **kwargs))

def assert_doesnt_render(expected, template, **kwargs):
    "Asserts than a given template and context don't render a given fragment"
    eq_(expected, render(template, **kwargs))

def assert_render_contains(expected, template, **kwargs):
    "Asserts than a given template and context rendering contains a given fragment"
    assert_contains(expected, render(template, **kwargs))

def assert_render_doesnt_contain(expected, template, **kwargs):
    "Asserts than a given template and context rendering does not contain a given fragment"
    assert_doesnt_contain(expected, render(template, **kwargs))

