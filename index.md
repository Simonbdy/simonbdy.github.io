---
layout: default
---
<a name="top"></a>

# Dico méca: Full list

> Work in progress.

[&#91;Go to category page&#93;](/categories) Browse by letters: [&#91;French&#93;](/alphabet_fr) [&#91;English&#93;](/alphabet_en)

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
			<a href="{{- post.url -}}.html#img"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
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

<hr class="trait">

[&#91;Go to category page&#93;](/categories) Browse by letters: [&#91;French&#93;](/alphabet_fr) [&#91;English&#93;](/alphabet_en)

<figure><a href="#top"><div class="fixed">Top</div></a></figure>