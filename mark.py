from markdown import Markdown
from bleach import clean

def converter(message):
	md = Markdown(encoding="utf-8", output_format="HTML5")
	return md.convert(clean(message))