{{ fullname }}
-------------------------------------------------------------------------------

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   

{% block methods %}

Methods
-------

{{ methods }}

.. autosummary::
   :toctree:

{% for item in methods %}
   {%- if not item.startswith('_') or item in ['__call__'] %}
   ~{{ name }}.{{ item }}
   {%- endif -%}
{%- endfor %}
{% endblock %}
