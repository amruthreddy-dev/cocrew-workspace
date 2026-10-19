import os
import base64

project_dir = r'C:\Users\Amruthreddy\.gemini\antigravity\scratch\cocrew-workspace'
logo_path = os.path.join(project_dir, 'cocrew-workspace-logo.jpg')
with open(logo_path, 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')
data_uri = f'data:image/jpeg;base64,{b64_logo}'

# Read index.html and replace logo path with data_uri so artifact is 100% portable
index_path = os.path.join(project_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace relative image with embedded data_uri
html_portable = html.replace('src="cocrew-workspace-logo.jpg"', f'src="{data_uri}"')

# Also read styles.css and inline it so it doesn't depend on external CSS loading in iframe
styles_path = os.path.join(project_dir, 'styles.css')
with open(styles_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

html_portable = html_portable.replace('<link rel="stylesheet" href="styles.css">', f'<style>\n{css_content}\n</style>')

artifact_target = r'C:\Users\Amruthreddy\.gemini\antigravity\brain\e685e2a3-f5ae-4d21-9ab3-8c988c8a310a\landing_page_showcase.html'
with open(artifact_target, 'w', encoding='utf-8') as f:
    f.write(html_portable)

print('Successfully generated portable standalone landing page artifact at:', artifact_target)
