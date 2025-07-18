import os
from flask import Flask, render_template_string

app = Flask(__name__)

# --- PASTE YOUR FORM'S EMBED URL HERE ---
# In Google Forms, click Send > select the "<>" (Embed HTML) tab > copy the URL from the 'src' attribute.
FORM_EMBED_URL = "https://docs.google.com/forms/d/e/YOUR_UNIQUE_FORM_ID/viewform?embedded=true"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Access Form</title>
    <style>
        body, html { margin: 0; padding: 0; height: 100%; overflow: hidden; }
        iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0; }
    </style>
</head>
<body>
    <iframe src="{{ form_url }}">Loading...</iframe>
</body>
</html>
"""

@app.route('/')
def secure_form():
    return render_template_string(HTML_TEMPLATE, form_url=FORM_EMBED_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=False)
