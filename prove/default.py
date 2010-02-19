from prove.tools import to_list, ok_, fail, inline

__all__ = ('assert_form_error',)

def assert_form_error(response, form, field, errors):
    """Asserts that a form used to render the response has a specific field
    error"""
    contexts = to_list(response.context)
    if not contexts:
        raise AssertionError('Response did not use any contexts to render the'
                             ' response')
    errors = to_list(errors)
    found_form = False
    for i, context in enumerate(contexts):
        if form not in context:
            continue
        found_form = True
        for err in errors:
            if field:
                if field in context[form].errors:
                    field_errors = context[form].errors[field]
                    ok_(err in field_errors,
                        inline("""The field '%s' on form '%s' in context
                               %d does not contain the error '%s'
                               (actual errors: %s)""" %
                               (field, form, i, err, repr(field_errors))))

                elif field in context[form].fields:
                    fail(inline("""The field '%s' on form '%s' in context %d
                                contains no errors""" % (field, form, i)))
                else:
                    fail(inline("""The form '%s' in context %d does not contain
                                the field '%s'""" % (form, i, field)))
            else:
                non_field_errors = context[form].non_field_errors()
                ok_(err in field_errors,
                    inline("""The form '%s' in context %d does not contain
                           the non-field error '%s' (actual errors: %s)""" %
                           (form, i, err, non_field_errors)))
    if not found_form:
        fail("The form '%s' was not used to render the response" % form)

