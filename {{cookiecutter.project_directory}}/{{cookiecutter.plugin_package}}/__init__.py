{%- if cookiecutter.use_qgis_plugin_tools|lower != "n" -%}
import os
{% endif -%}
from typing import TYPE_CHECKING
{% if cookiecutter.use_qgis_plugin_tools|lower != "n" %}
from {{cookiecutter.plugin_package}}.qgis_plugin_tools.infrastructure.debugging import (  # noqa: F401
    setup_debugpy,
    setup_ptvsd,
    setup_pydevd,
)

debugger = os.environ.get("QGIS_PLUGIN_USE_DEBUGGER", "").lower()
if debugger in {"debugpy", "ptvsd", "pydevd"}:
    locals()["setup_" + debugger]()
{% endif %}
if TYPE_CHECKING:
    from qgis.gui import QgisInterface

    from {{cookiecutter.plugin_package}}.plugin import Plugin


# pylint: disable-next=unused-argument
def classFactory(iface: "QgisInterface") -> "Plugin":  # noqa: N802
    # pylint: disable-next=import-outside-toplevel
    from {{cookiecutter.plugin_package}}.plugin import Plugin

    return Plugin()
