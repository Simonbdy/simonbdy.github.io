---
layout: default
title:  "Categories"
---

# Items' categories

{% for cat in site.categories %}
  <a name="{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_en }}</a></li>
    {%- endfor -%}
  </ul>
{%- endfor -%}
