---
layout: default
title:  "Categories"
---

# Items' categories


<table>
	<tr><th>Français : </th><th>English: </th></tr>
	<tr><td>
{% for cat in site.categories %}<strong>- <a href="#{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ cat[0] | capitalize }}</a></strong><br />{% endfor %}
	</td><td>Content</td></tr>
</table>

<table>
	<tr><th>Français : </th><th>English: </th></tr>
	<tr><td>
{% for cat in site.categories %}
  <a name="fr_{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_en }}</a></li>
    {%- endfor -%}
  </ul>
{%- endfor -%}
	</td><td>Content</td></tr>
</table>