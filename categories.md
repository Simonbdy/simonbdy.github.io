---
layout: default
title:  "Categories"
---

# Items' categories


<table>
	<tr><th>Français : </th><th>English: </th></tr>
	<tr><td>
{% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "FR_" %}<strong>- <a href="#{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/',''}}">{{ cat[0] | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_' | capitalize}}</a></strong><br />{% endif %}{% endfor %}
	</td><td>
{% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "EN_" %}<strong>- <a href="#{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/',''}}">{{ cat[0] | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}</a></strong><br />{% endif %}{% endfor %}
	</td></tr>
</table>

<table>
	<tr><th>Français : </th><th>English: </th></tr>
	<tr><td>
{% for cat in site.categories %}
  <a name="{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_en }}</a></li>
    {%- endfor -%}
  </ul>
{%- endfor -%}
	</td><td>Content</td></tr>
</table>
