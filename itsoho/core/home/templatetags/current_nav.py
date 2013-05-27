# -*- coding: utf-8 -*-
from django import template


register = template.Library()


def parse_bool_value(value, name):
    """Django templates do not know what a boolean is,
    and anyway we need to support the 'merge' option."""
    if value is None:
        return value
    value = value.lower()
    if value in ('true', '1'):
        return True
    elif value in ('false', '0'):
        return False
    else:
        raise template.TemplateSyntaxError(
            '"%s" argument must be one of the strings '
            '"true" or "false" not "%s"' % (name, value))


@register.tag
def current_nav(parser, token):

    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 2:
        raise template.TemplateSyntaxError, "%r tag requires at least one argument" % template_tag

    args = args[1:]

    strict = None
    with_class = None
    urls = []

    for arg in args:
        arg = arg.split('=', 1)
        if len(arg) == 1:
            urls.append(arg[0])
        else:
            if arg[0] == 'strict':
                strict = arg[1]
            elif arg[0] == 'with_class':
                with_class = arg[1]
            else:
                raise template.TemplateSyntaxError, "%r tag unknow argument %s" % (template_tag, arg[0])

    if not urls:
        raise template.TemplateSyntaxError, "%r tag requires at least one url argument" % template_tag

    return NavSelectedNode(strict, with_class, urls)


class NavSelectedNode(template.Node):
    def __init__(self, strict, with_class, urls):
        self.strict = strict
        self.with_class = with_class
        self.urls = urls

    def render(self, context):

        def resolve_var(x):
            if x is None:
                return None
            else:
                try:
                    return template.Variable(x).resolve(context)
                except template.VariableDoesNotExist:
                    # Django seems to hide those; we don't want to expose
                    # them either, I guess.
                    raise

        strict = parse_bool_value(resolve_var(self.strict), 'strict')
        if strict is None:
            strict = True

        with_class = parse_bool_value(resolve_var(self.with_class), 'with_class')
        if with_class is None:
            with_class = True

        path = context['request'].path
        for url in self.urls:
            pValue = template.Variable(url).resolve(context)
            if (pValue == '/' or pValue == '') and not (path  == '/' or path == ''):
                return ""
            if path == pValue or (not strict and pValue in path):
                if with_class:
                    return ' class="active"'
                return ' active'
        return ""
