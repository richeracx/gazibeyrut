import re

file_path = 'c:/Users/hadi/wes/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: Find <div class="card-action"><span class="price">...</span></div>
# And append the button before the closing div
pattern = r'(<div class="card-action">\s*<span class="price">([\d\.]+) ₺</span>)\s*</div>'
# We need to capture the price to pass to the function if needed, or just use JS to find it. 
# Simpler: Just append the button.
# Using a lambda replacement to get the price for the onclick handler.
def replacer(match):
    base_html = match.group(1)
    price = match.group(2)
    # Ensure no existing button to prevent duplicates if ran multiple times
    if 'button' in base_html: 
        return match.group(0)
    
    button_html = f'''
                  <button class="btn-fat-turquoise" onclick="addToCart(this.closest('.menu-card').querySelector('h4').innerText, {price})">
                    <i class="fas fa-plus"></i> EKLE
                  </button></div>'''
    return base_html + button_html

new_content = re.sub(pattern, replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
