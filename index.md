---
layout: default
---

# Dico méca

> Work in progress.


| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}
    | **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "FR_" %}- [{{ cat | remove: 'FR_' | remove: 'Fr_' | remove: 'fr_'| capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%}<br />English: <br />{%- for cat in post.categories -%}{% assign lang = cat | slice: 0, 3 %}{% if lang == "EN_" %}- [{{ cat | remove: 'EN_' | remove: 'En_' | remove: 'en_' | capitalize}}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{% endif %}{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endfor %}

Source: 
<a href="https://www.wikipedia.com" target="new">Wikipedia.com</a>.


> Work in progress.