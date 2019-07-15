---
layout: default
---

# Dico méca

> ![WIP](/assets/img/wip.png) Work in progress.


| **Nom (fr)** | **Name (en)** | **Categories** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :---: | :---: | :--- | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}
    | **{{ post.name_fr }}** | **{{ post.name_en }}** | Français : <br />{%- for cat in post.categories_fr -%}- [{{ cat | capitalize }}](categories.html#fr_{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{%- endfor -%}<br />English: <br />{%- for cat in post.categories_en -%}- [{{ cat | capitalize }}](categories.html#en_{{ cat | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }} ) <br />{%- endfor -%} | {{ post.desc_fr }} | {{ post.desc_en }} | <a name="{{ post.title | downcase | replace:'é','e' | replace:' ','_' | replace:',','-' | replace:'/','' }}"></a>{%- for img in post.img -%}<a href="/assets/img/{{ img }}" target="new">!["Image died..."](/assets/img/{{ img }})</a><br />{%- endfor -%} | {{ post.src }}<br />
{% endfor %}

Source: 
<a href="https://www.wikipedia.com" target="new">Wikipedia.com</a>.


> ![WIP](/assets/img/wip.png) Work in progress.