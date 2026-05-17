import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

target = """        </a>
        <div class="nav-links">"""

replacement = """        </a>
        <button class="mobile-menu-btn" aria-label="Menu" onclick="toggleMenu()">
            <img src="menu-sparkles.png" alt="Menu" style="height: 30px; width: auto;">
        </button>
        <div class="nav-links" id="navLinks">"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Target not found in {file}")
