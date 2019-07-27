---
layout: default
---

<script language="javascript">
function expand(letter) {
  const words = document.querySelectorAll('.word');
  words.forEach(word => word.style.display = (word.dataset.letter === letter) ? 'inline-block' : 'none');
}
</script>

<h1>Dico méca: <script language="javascript">document.write(urlParams.get('letter'));</script></h1>

[&#91; Go back to full list &#93;](/index)

 <a href="#" class="letters" onclick="expand('A')">A</a> &#124; <a href="#" class="letters" onclick="expand('B')">B</a> &#124; <a href="#" class="letters" onclick="expand('C')">C</a> &#124; D &#124; E &#124; F &#124; G &#124; H &#124; I &#124; J &#124; K &#124; L &#124; M &#124; N &#124; O &#124; P &#124; Q &#124; R &#124; S &#124; T &#124; U &#124; V &#124; W &#124; X &#124; Y &#124; Z &#124; 0 - 9

<script language="javascript">document.write('Words begining with the letter: '+urlParams.get('letter'));</script>

[&#91; French list &#93;]() [&#91; English list &#93;]()
<a class="word" data-letter="A">

| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}{% assign first_letter = post.name_fr | slice: 0, 1 | capitalize %}{%- if first_letter == "A" -%}
	| **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endif %}{% endfor %}

</a>
<a class="word" data-letter="B">

| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}{% assign first_letter = post.name_fr | slice: 0, 1 | capitalize %}{%- if first_letter == "B" -%}
	| **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endif %}{% endfor %}

</a>
<a class="word" data-letter="C">

| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}{% assign first_letter = post.name_fr | slice: 0, 1 | capitalize %}{%- if first_letter == "C" -%}
	| **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endif %}{% endfor %}

</a>

Source: 
<a href="https://www.wikipedia.com" target="new">Wikipedia.com</a>.



## site.url: {{ site.url }}
## site.url | absolute_url: {{ site.url | absolute_url }}
## page.url: {{ page.url }}
## site.baseurl: {{ site.baseurl }}