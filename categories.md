---
layout: default
title:  "Categories"
---

# Items' categories

[&#91; Full list &#93;](/index) Browse by letters: [&#91;English&#93;](/alphabet_en) [&#91;French&#93;](/alphabet_fr)

<div class="divTable" style="display: table;">
  <div class="divTableBody">
    <div class="divTableHead">
      <div class="divTableCellHead"><strong>French</strong></div>
      <div class="divTableCellHead"><strong>English</strong></div>
    </div>
<div class="divTableRow divContentRow">
  <div border="1" border-color="grey" class="divTableCell">{% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "FR_" %}<strong>- <a href="#{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/',''}}">{{ cat[0] | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_' | capitalize}}</a></strong><br />{% endif %}{% endfor %}</div>
  <div class="divTableCell">
    {% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "EN_" %}<strong>- <a href="#{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/',''}}">{{ cat[0] | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}</a></strong><br />{% endif %}{% endfor %}
  </div>
</div>
</div>
</div>
<br />
<div class="divTable" style="display: table;">
  <div class="divTableBody">
    <div class="divTableHead">
      <div class="divTableCellHead"><strong>French</strong></div>
      <div class="divTableCellHead"><strong>English</strong></div>
    </div>
<div class="divTableRow divContentRow">
  <div border="1" border-color="grey" class="divTableCell">{% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "FR_" %}
  <a name="{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_' | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_fr }}</a></li>
    {%- endfor -%}
  </ul>
 {% endif %}{%- endfor -%}</div>
  <div class="divTableCell">
    {% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "EN_" %}
  <a name="{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_en }}</a></li>
    {%- endfor -%}
  </ul>
 {% endif %}{%- endfor -%}
  </div>
</div>
</div>
</div>
<!--
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
{% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "FR_" %}
  <a name="{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_' | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_fr }}</a></li>
    {%- endfor -%}
  </ul>
 {% endif %}{%- endfor -%}
	</td><td>
{% for cat in site.categories %}{% assign lang = cat[0] | slice: 0, 3 %}{% if lang == "EN_" %}
  <a name="{{ cat[0] | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>
  <h3>{{ cat[0] | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize }}</h3>
  <ul>
    {%- for post in cat[1] -%}
      <li><a href="index.html#{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}">{{ post.name_en }}</a></li>
    {%- endfor -%}
  </ul>
 {% endif %}{%- endfor -%}
</td></tr>
</table>
-->