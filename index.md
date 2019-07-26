---
layout: default
---

# Dico méca

> Work in progress.

[Go to category page](/categories)

 [A](/alphabet.html#A) &#124; B &#124; C &#124; D &#124; E &#124; F &#124; G &#124; H &#124; I &#124; J &#124; K &#124; L &#124; M &#124; N &#124; O &#124; P &#124; Q &#124; R &#124; S &#124; T &#124; U &#124; V &#124; W &#124; X &#124; Y &#124; Z &#124; 0 - 9

| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}
    | **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endfor %}

Source: 
<a href="https://www.wikipedia.com" target="new">Wikipedia.com</a>.

[Go to category page](/categories)

> Work in progress.