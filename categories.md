---
layout: default
title:  "Tags"
---

# Items' categories

{% for cat in site.categories %}
  <h3>{{ cat[0] | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title }}">{{ post.title }}</a></li>
    {%- endfor -%}
  </ul>
{%- endfor -%}
