#!/usr/bin/env python3
"""
AIGate DPI Bypass Post-build Script

Problem: 天翼云 WAF DPI intercepts responses containing JS syntax patterns.
Solution: Base64-encode JS files as .txt, modify index.html to fetch+decode.

Usage: python3 scripts/dpi-bypass.py [dist-dir]
Default dist-dir: ./dist
"""

import base64
import re
import sys
import os

def main():
    dist_dir = sys.argv[1] if len(sys.argv) > 1 else './dist'
    assets_dir = os.path.join(dist_dir, 'aigate-assets')
    html_path = os.path.join(dist_dir, 'index.html')

    if not os.path.exists(html_path):
        print(f'ERROR: {html_path} not found. Run `npm run build` first.')
        sys.exit(1)

    # Read index.html
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all JS script references
    js_pattern = re.compile(r'<script[^>]*\ssrc="(/aigate-assets/([^"]+\.js))"[^>]*>\s*</script>')
    matches = list(js_pattern.finditer(html))

    if not matches:
        print('No JS script references found. Already processed or no JS files.')
        return

    for match in matches:
        js_path_relative = match.group(1)  # /aigate-assets/xxx.js
        js_filename = match.group(2)       # xxx.js
        js_full_path = os.path.join(dist_dir, 'aigate-assets', js_filename)

        if not os.path.exists(js_full_path):
            print(f'WARNING: {js_full_path} not found, skipping.')
            continue

        # Read JS content and base64 encode
        with open(js_full_path, 'rb') as f:
            js_content = f.read()

        b64_content = base64.b64encode(js_content).decode('ascii')
        txt_filename = js_filename.replace('.js', '.txt')
        txt_path = os.path.join(assets_dir, txt_filename)

        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(b64_content)

        # Replace script tag with fetch+decode inline script
        replacement = f'''<script>
    // DPI bypass: load JS as base64-encoded text, decode and execute
    fetch('/aigate-assets/{txt_filename}')
      .then(function(r) {{ return r.text(); }})
      .then(function(b64) {{
        var raw = atob(b64);
        var script = document.createElement('script');
        script.type = 'module';
        script.textContent = raw;
        document.head.appendChild(script);
      }})
      .catch(function(e) {{ console.error('Failed to load app:', e); }});
    </script>'''

        html = html.replace(match.group(0), replacement)
        print(f'Converted: {js_filename} -> {txt_filename} ({len(js_content)} bytes -> {len(b64_content)} b64)')

        # Optionally remove original JS file (keep for backup)
        # os.remove(js_full_path)

    # Write updated index.html
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Done! Updated {html_path}')

if __name__ == '__main__':
    main()
