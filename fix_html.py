import re

file_path = 'c:/Users/hadi/wes/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the card action div and remove the button inside, keeping price
# We look for <div class="card-action"> ... <span class="price">...</span> ... <button ...>...</button> ... </div>
# And replace it with just the price in the div.

# This regex finds the whole card-action block and extracts the price
pattern = r'<div class="card-action">\s*<span class="price">([^<]+)</span>[\s\S]*?</div>'
replacement = r'<div class="card-action"><span class="price">\1</span></div>'

new_content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
