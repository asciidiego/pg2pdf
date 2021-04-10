import urllib.request
import html_text

essay_canonical_name = input(
    """
Please, enter the canonical name of Paul Graham essay.
    
For example, for extracting the text of "What You Wish You'd Known"
(http://www.paulgraham.com/hs.html), you'd input "hs".

>> """
)

essay_url = f"http://www.paulgraham.com/{essay_canonical_name}.html"

response = urllib.request.urlopen(essay_url)
response_as_html = response.read().decode("utf-8")
parsed_text = html_text.extract_text(response_as_html)

print(parsed_text)
