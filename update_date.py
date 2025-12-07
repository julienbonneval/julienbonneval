from datetime import datetime
import re

today = datetime.now().strftime("%A, %B %d, %Y")

with open("README.md", "r") as f:
    content = f.read()

new_content = re.sub(
    r"(<!-- date-start -->\s*)(.*?)(\s*<!-- date-end -->)",
    rf"\1{today}\3",
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(new_content)
