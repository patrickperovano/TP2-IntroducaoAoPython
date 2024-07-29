
import os
import re
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from weasyprint import HTML


# Function to read content from .py files
def build_exercicios_html(directory, outputs):
    py_files_content = ""
    files = [f for f in os.listdir(directory) if f.endswith(".py") and "exercicio" in f]
    files.sort()
    for filename, output in zip(files, outputs):
        with open(os.path.join(directory, filename), "r") as file:
            highlighted_code = highlight(file.read(), PythonLexer(), HtmlFormatter())
            py_files_content += f"<h1>{filename}</h1><pre>{highlighted_code}</pre><br>"        
            py_files_content += f"<h2>Saída</h2><pre class=terminal>{output}</pre><br>"
    return py_files_content


def gerar_pdf(nome, sobrenome, std_output):
    # Generate HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            {HtmlFormatter().get_style_defs('.highlight')}
        </style>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0.0cm;
            }}
            .highlight>pre{{
                white-space: pre-wrap; 
                word-wrap: break-word; 
                width: 100%;
            }}
            .terminal {{
                background-color: #000000;
                color: #00FF00;
                font-family: monospace;
            }}
        </style>
    </head>
    <body>
        {build_exercicios_html('./', split_exercicios(std_output))}
    </body>
    </html>
    """

    with open(f"{nome}_{sobrenome}.html", "w") as o:
        o.write(html_content)
        
    html_with_style = html_content
    HTML(string=html_with_style).write_pdf(f"{nome}_{sobrenome}_TP1.pdf")


def split_exercicios(std_output):
    # Define a expressão regular para capturar o texto entre as seções de exercício
    pattern = re.compile(r"\*{5} Exercício \d+ \*{5}\s+\n(.*?)\s+(?=\*{5} Exercício \d+ \*{5}|$)", re.DOTALL)

    # Encontra todas as correspondências
    matches = pattern.findall(std_output)

    exercicios = []
    # Mostra as correspondências encontradas
    for i, match in enumerate(matches, 1):
        exercicios.append(match.strip())

    assert len(matches) == 16

    return exercicios

    

def gerar_submissao(nome, sobrenome, std_output):
    split_exercicios(std_output)
    gerar_pdf(nome, sobrenome, std_output)