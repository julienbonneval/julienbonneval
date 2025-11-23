from datetime import datetime

with open("README.md", "r") as f:
    content = f.read()

today = datetime.now().strftime("%A, %B %d, %Y")

new_content = content.replace("{{date}}", today)

with open("README.md", "w") as f:
    f.write(new_content)
