---
layout: page
title: Archive
permalink: /archive/
---

## Post Archive

All previous market scans and analysis.

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <span class="post-meta">{{ post.date | date: "%B %d, %Y" }}</span>
      <h3>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h3>
      {%- if post.tags -%}
      <div class="post-tags">
        {%- for tag in post.tags -%}
          <span class="tag">{{ tag }}</span>
        {%- endfor -%}
      </div>
      {%- endif -%}
    </li>
  {% endfor %}
</ul>
