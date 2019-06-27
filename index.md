---
layout: default
---

# Dico méca

> ![WIP](/assets/img/wip.png) Work in progress.


| **Categories** | **Nom (fr)** | **Name (en)** | **Définition (fr)** | **Definition (en)** | **Illustrations** | **Sources** |
| :--- | :---: | :---: | :--- | :--- | :---: | --- |
{% assign sorted_post = site.posts | sort: 'title' %}
{%- for post in sorted_post -%}
    | <a name="{{ post.title }}"></a>{%- for cat in post.categories -%}- [{{ cat | capitalize }}](categories.html#{{ cat | downcase | replace:'é','e' | replace:' ','-' }} )<br />{%- endfor -%} | **{{ post.name_fr }}** | **{{ post.name_en }}** | {{ post.desc_fr }} | {{ post.desc_en }} | {%- for img in post.img -%}<a href="{{ img }}" target="new">![]({{ img }})</a><br />{%- endfor -%} | - |{{ post.src }}<br />
{% endfor %}

> ![WIP](/assets/img/wip.png) Work in progress.