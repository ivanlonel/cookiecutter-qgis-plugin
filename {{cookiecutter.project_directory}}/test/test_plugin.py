{%- if cookiecutter.use_qgis_plugin_tools|lower != "n" -%}
from {{cookiecutter.plugin_package}}.qgis_plugin_tools.tools.resources import plugin_name


def test_plugin_name():
    assert plugin_name() == "{{cookiecutter.plugin_name|replace(' ', '')}}"
{%- else -%}
from {{cookiecutter.plugin_package}}.plugin import Plugin


def test_plugin_name():
    assert Plugin.name == "{{cookiecutter.plugin_name|replace(' ', '')}}"
{%- endif %}
