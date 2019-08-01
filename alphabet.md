---
layout: default
---

<script language="javascript">
function expand(letter) {
  const words = document.querySelectorAll('.divTable');
  words.forEach(divTable => divTable.style.display = (divTable.dataset.letter === letter) ? 'table' : 'none');
}
</script>

<h1>Dico méca: Alphabetical order (French)</h1>

[&#91; Go back to full list &#93;](/index) [&#91;Go to category page&#93;](/categories) 

<div>
 <a href="#" class="letters" onclick="expand('ALL')">Full list</a> &#124; <a href="#" class="letters" onclick="expand('A')">A</a> &#124; <a href="#" class="letters" onclick="expand('B')">B</a> &#124; <a href="#" class="letters" onclick="expand('C')">C</a> &#124; <a href="#" class="letters" onclick="expand('D')">D</a> &#124; <a href="#" class="letters" onclick="expand('E')">E</a> &#124; <a href="#" class="letters" onclick="expand('F')">F</a> &#124; <a href="#" class="letters" onclick="expand('G')">G</a> &#124; <a href="#" class="letters" onclick="expand('H')">H</a> &#124; <a href="#" class="letters" onclick="expand('I')">I</a> &#124; <a href="#" class="letters" onclick="expand('J')">J</a> &#124; <a href="#" class="letters" onclick="expand('K')">K</a> &#124; <a href="#" class="letters" onclick="expand('L')">L</a> &#124; <a href="#" class="letters" onclick="expand('M')">M</a> &#124; <a href="#" class="letters" onclick="expand('N')">N</a> &#124; <a href="#" class="letters" onclick="expand('O')">O</a> &#124; <a href="#" class="letters" onclick="expand('P')">P</a> &#124; <a href="#" class="letters" onclick="expand('Q')">Q</a> &#124; <a href="#" class="letters" onclick="expand('R')">R</a> &#124; <a href="#" class="letters" onclick="expand('S')">S</a> &#124; <a href="#" class="letters" onclick="expand('T')">T</a> &#124; <a href="#" class="letters" onclick="expand('U')">U</a> &#124; <a href="#" class="letters" onclick="expand('V')">V</a> &#124; <a href="#" class="letters" onclick="expand('W')">W</a> &#124; <a href="#" class="letters" onclick="expand('X')">X</a> &#124; <a href="#" class="letters" onclick="expand('Y')">Y</a> &#124; <a href="#" class="letters" onclick="expand('Z')">Z</a><br /><br />
</div>

<!-- All -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- for post in sorted_post -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="ALL">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="ALL"><div>No entry found.{%- endif -%}
</div>
</div>

<!-- A -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "A" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="A">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="A"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- B -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "B" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="B">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="B"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- C -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "C" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="C">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="C"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- D -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "D" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="D">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="D"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- E -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "E" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="E">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="E"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- F -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "F" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="F">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="F"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- G -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "G" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="G">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="G"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- H -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "H" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="H">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="H"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- I -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "I" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="I">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="I"><div>No entry found with letter I.{%- endif -%}
</div>
</div>

<!-- J -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "J" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="J">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="J"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- K -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "K" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="K">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="K"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- L -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "L" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="L">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="L"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- M -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "M" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="M">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="M"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- N -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "N" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="N">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="N"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- O -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "O" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="O">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="O"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- P -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "P" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="P">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="P"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- Q -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "Q" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="Q">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="Q"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- R -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "R" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="R">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="R"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- S -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "S" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="S">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="S"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- T -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "T" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="T">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="T"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- U -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "U" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="U">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="U"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- V -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "V" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="V">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="V"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- W -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "W" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="W">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="W"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- X -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "X" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="X">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="X"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- Y -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "Y" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="Y">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="Y"><div>No entry found with this letter.{%- endif -%}
</div>
</div>

<!-- Z -->
{%- assign sorted_post = site.posts | sort: 'title' -%}
{%- assign i = 0 -%}
{%- assign exist = 0 -%}
{%- for post in sorted_post -%}
{%- assign first_letter = post.name_fr | slice: 0, 1 | capitalize -%}
{%- if first_letter == "Z" -%}
{%- assign exist = 1 -%}
{%- if i == 0 -%}
<div class="divTable" data-letter="Z">
	<div class="divTableBody">
		<div class="divTableRow divTableHead">
			<div class="divTableCell"><strong>Name</strong></div>
			<div class="divTableCell"><strong>Categories</strong></div>
			<div class="divTableCell"><strong>Definition</strong></div>
			<div class="divTableCell"><strong>Illustrations</strong></div>
		</div>
{%- assign i = 1 -%}
{%- endif-%}
<div class="divTableRow divContentRow">
	<div  name="{{- post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' -}}" border="1" border-color="grey" class="divTableCell"><strong><span class="FR">{{- post.name_fr -}}</span><hr class="trait"><span class="EN">{{- post.name_en -}}</span></strong></div>
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
	<div class="divTableCell">{%- if post.desc_fr -%}<span class="FR">{{- post.desc_fr | truncatewords: 4, " [...]"  -}}</span> Read more.<br />{%- endif -%}
		{%- if post.desc_en -%}<hr class="trait">
		<span class="EN">{{- post.desc_en | truncatewords: 4, " [...]" -}}</span> Read more.<br />{%- endif -%}{%- if post.src -%}[{{- post.src -}}]{%- endif -%}</div>
	<div class="divTableCell">
		{%- for img in post.img -%}
			<a href="/assets/img/{{- img -}}" target="_blank"><img class="img" src="/assets/img/{{- img | strip_newlines -}}"></a>
			<br />
		{%- endfor -%}
	</div>
</div>
{%- endif -%}
{%- endfor -%}
{%- if exist == 0 -%}<div class="divTable" data-letter="Z"><div>No entry found with this letter.{%- endif -%}
</div>
</div>


<br />
Source: 
<a href="https://www.wikipedia.com" target="_blank">Wikipedia.com</a>.

