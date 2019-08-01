---
layout: default
---
<a name="top"></a>

# Dico méca: Full list

> Work in progress.

[&#91;Go to category page&#93;](/categories) Browse by letters: [&#91;French&#93;](/alphabet_fr) [English]

<!-- All -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign first_line = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- if post -%}
{%- assign exist = 1 -%}
{%- if first_line == 0 -%}
<div class="divTable" style="display: table;">
	<div class="divTableBody">
		<div class="divTableHead">
			<div class="divTableCellHead"><strong>Name</strong></div>
			<div class="divTableCellHead"><strong>Categories</strong></div>
			<div class="divTableCellHead"><strong>Definition</strong></div>
			<div class="divTableCellHead"><strong>Illustrations</strong></div>
		</div>
{%- assign first_line = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div border="1" border-color="grey" class="divTableCell"><a name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}"><div class="anchor"></div></a><a href="{{- post.url -}}.html"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></a></div>
	<div class="divTableCell">
		{%- for cat in post.categories -%}
			{%- assign lang = cat | slice: 0, 3 -%}
			{%- if lang == "FR_" -%}
				<span class="FR">- <a href="categories.html#{{- cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}">{{- cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize | strip_newlines -}}</a></span><br />
			{%- endif -%}
		{%- endfor -%}
		<hr class="trait">
		{%- for cat in post.categories -%}
			{%- assign lang = cat | slice: 0, 3 -%}
			{%- if lang == "EN_" -%}
				<span class="EN">- <a href="categories.html#{{- cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}">{{- cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize| strip_newlines }}</a></span><br />
			{%- endif -%}
	{%- endfor -%}
	</div>
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span><a href="{{- post.url -}}.html"><p class="readmore">&#91;Read more&#93;</p></a>{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span><a href="{{- post.url -}}.html"><p class="readmore">&#91;Read more&#93;</p></a>{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="ALL"><div>No entry found.{%- endif -%}
</div>
</div>

<br />
Source: 
<a href="https://www.wikipedia.com" target="_blank">Wikipedia.com</a>.


<!--
 [A](/alphabet.html#A) &#124; B &#124; C &#124; D &#124; E &#124; F &#124; G &#124; H &#124; I &#124; J &#124; K &#124; L &#124; M &#124; N &#124; O &#124; P &#124; Q &#124; R &#124; S &#124; T &#124; U &#124; V &#124; W &#124; X &#124; Y &#124; Z &#124; 0 - 9

| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}
    | **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endfor %}

Source: 
<a href="https://www.wikipedia.com" target="new">Wikipedia.com</a>.
-->

[Go to category page](/categories) 


> Work in progress.

bonsoir
<a href="#top"><div class="fixed">Top</div></a>
bonsoir