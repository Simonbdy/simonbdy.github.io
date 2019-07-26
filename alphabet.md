---
layout: default
---

<script language="javascript">
	var urlParams = new URLSearchParams(location.search);
</script>

<h1>Dico méca: <script language="javascript">document.write(urlParams.get('letter'));</script></h1>

[&#91; Go back to full list &#93;](/index)

<script language="javascript">document.write('Words begining with the letter: '+urlParams.get('letter'));</script>

[&#91; French list &#93;]() [&#91; English list &#93;]()

| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}{% assign first_letter = post.name_fr | slice: 0, 1 | capitalize %}{%- if first_letter == "A" -%}
	| **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endif %}{% endfor %}

Source: 
<a href="https://www.wikipedia.com" target="new">Wikipedia.com</a>.



## {{ site.url | }}
## {{ page.url }}