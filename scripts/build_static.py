#!/usr/bin/env python3
"""
Static Site Builder
Converts Jekyll templates to static HTML without Jekyll runtime
"""

import os
import re
import shutil
from datetime import datetime

def read_file(filepath):
    """Read file contents"""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except:
        return ""

def process_includes(content, includes_dir):
    """Process Jekyll include tags"""
    def replace_include(match):
        include_name = match.group(1).strip()
        include_path = os.path.join(includes_dir, f"{include_name}.html")
        return read_file(include_path)
    
    return re.sub(r'{%\s*include\s+([^%]+)%}', replace_include, content)

def process_variables(content, variables):
    """Process Jekyll variables"""
    for key, value in variables.items():
        content = content.replace(f'{{{{ site.{key} }}}}', value)
        content = content.replace(f'{{{{ {key} }}}}', value)
    return content

def build_home_page(posts, layouts_dir, includes_dir):
    """Build homepage"""
    layout = read_file(os.path.join(layouts_dir, 'default.html'))
    home_template = read_file(os.path.join(layouts_dir, 'home.html'))
    
    # Process includes
    layout = process_includes(layout, includes_dir)
    
    # Build post list
    post_list = []
    for i, post in enumerate(posts[:5]):
        post_list.append(f"""
        <article class="article-item">
            <div class="article-meta">
                <span class="article-category">{post.get('category', 'Analysis')}</span>
                <span class="article-date">{post.get('date', '')}</span>
            </div>
            <h3 class="article-title"><a href="{post.get('url', '#')}">{post.get('title', 'Untitled')}</a></h3>
            <p class="article-excerpt">{post.get('excerpt', '')}</p>
            <a href="{post.get('url', '#')}" class="read-more">Read analysis →</a>
        </article>
        """)
    
    # Build ticker widget
    tickers = [
        ('SOFI', '$15.23', '-4.0%', 'down'),
        ('NVDA', '$108.50', '-1.2%', 'down'),
        ('XOM', '$116.20', '+1.2%', 'up'),
        ('PLTR', '$74.80', '-2.2%', 'down')
    ]
    
    ticker_html = ""
    for name, price, change, direction in tickers:
        ticker_html += f'<span class="ticker-strip-item"><strong>{name}</strong> {price} <span class="ticker-{direction}">{change}</span></span>\n        <span class="ticker-strip-divider">|</span>\n        '
    
    # Insert content into layout
    home_content = home_template.replace('{{ content }}', '\n'.join(post_list))
    home_content = home_content.replace('{{ site.title }}', 'Market Pulse Scanner')
    home_content = home_content.replace('{{ site.description }}', 'Daily stock market analysis with AI-assisted research and monitoring')
    home_content = home_content.replace('{{ site.time | date: "%A, %B %d, %Y" }}', datetime.now().strftime('%A, %B %d, %Y'))
    
    # Add ticker strip
    home_content = home_content.replace(
        '<div class="ticker-strip-content">',
        f'<div class="ticker-strip-content">\n        <span class="ticker-strip-label">Today\'s Watchlist:</span>\n        {ticker_html}'
    )
    
    final = layout.replace('{{ content }}', home_content)
    final = final.replace('{{ "/" | relative_url }}', '/')
    final = final.replace('{{ "/performance/" | relative_url }}', '/performance.html')
    final = final.replace('{{ "/archive/" | relative_url }}', '/archive.html')
    final = final.replace('{{ "/about/" | relative_url }}', '/about.html')
    final = final.replace('{{ "/assets/main.css" | relative_url }}', 'assets/main.css')
    
    return final

def copy_assets(src_dir, dest_dir):
    """Copy CSS and other assets"""
    assets_src = os.path.join(src_dir, 'assets')
    assets_dest = os.path.join(dest_dir, 'assets')
    
    if os.path.exists(assets_src):
        shutil.copytree(assets_src, assets_dest, dirs_exist_ok=True)

def build_static_site():
    """Main build function"""
    site_dir = os.path.expanduser('~/.openclaw/workspace/projects/stock-scanner-site')
    output_dir = '/tmp/market-pulse-site'
    
    # Clean output
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    layouts_dir = os.path.join(site_dir, '_layouts')
    includes_dir = os.path.join(site_dir, '_includes')
    posts_dir = os.path.join(site_dir, '_posts')
    
    # Get sample posts
    posts = []
    if os.path.exists(posts_dir):
        for filename in sorted(os.listdir(posts_dir), reverse=True)[:5]:
            if filename.endswith('.md'):
                posts.append({
                    'title': filename.replace('.md', '').replace('-', ' ').title(),
                    'url': f'posts/{filename.replace(".md", ".html")}',
                    'date': 'March 28, 2026',
                    'excerpt': 'Sample excerpt from article...',
                    'category': 'Analysis'
                })
    
    # Build homepage
    homepage = build_home_page(posts, layouts_dir, includes_dir)
    
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(homepage)
    
    # Copy assets
    copy_assets(site_dir, output_dir)
    
    # Create zip
    zip_path = '/tmp/market-pulse-site.zip'
    shutil.make_archive('/tmp/market-pulse-site', 'zip', output_dir)
    
    print(f"✅ Static site built!")
    print(f"Location: {output_dir}")
    print(f"Zip: {zip_path}")
    
    return output_dir, zip_path

if __name__ == '__main__':
    build_static_site()
