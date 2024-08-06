####################################################################
# Nao mexa nesse arquivo
# Para resolver o TP modifique os arquivos exercicio_*.py que
# podem ser acessados no lado esquerdo.
####################################################################

import io
import os
import re
import sys

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from weasyprint import HTML

from identificacao import nome, sobrenome

if not nome or not sobrenome:
    print(
        "Você deve adicionar seu nome e sobrenome na variável 'nome' e 'sobrenome'"
    )
    raise Exception(
        "Você deve adicionar seu nome e sobrenome na variável 'nome' e 'sobrenome'"
    )


def listar_exercicios():
    exercicios = [
        f for f in os.listdir('./') if f.endswith(".py") and "exercicio" in f
    ]
    exercicios.sort()

    return exercicios


def submissao_filename(nome, sobrenome, ext='pdf'):
    return f"{nome.replace(' ','_')}_{sobrenome.replace(' ', '_')}_TP2.{ext}"


# Function to read content from .py files
def build_exercicios_html(outputs):
    py_files_content = ""
    files = listar_exercicios()

    for filename, output in zip(files, outputs):
        with open(os.path.join('./', filename), "r") as file:
            highlighted_code = highlight(file.read(), PythonLexer(),
                                         HtmlFormatter())
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
                white-space: pre-wrap; 
                word-wrap: break-word; 
                width: 100%;
            }}
        </style>
    </head>
    <body>
        <h1> Introdução a programação com Python - TP1 </h1>
        <h2>Nome: {nome} {sobrenome}</h2>

        {build_exercicios_html(split_exercicios(std_output))}
    </body>
    </html>
    """

    html_with_style = html_content
    HTML(string=html_with_style).write_pdf(submissao_filename(nome, sobrenome))


def split_exercicios(std_output):
    # Define a expressão regular para capturar o texto entre as seções de exercício
    pattern = re.compile(
        r"\*{5} Exercício \d+ \*{5}\s+\n(.*?)\s+(?=\*{5} Exercício \d+ \*{5}|$)",
        re.DOTALL)

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

    arquivos = listar_exercicios() + [submissao_filename(nome, sobrenome)]

    zip_filename = submissao_filename(nome, sobrenome, 'zip')

    #Zip files
    import zipfile
    with zipfile.ZipFile(zip_filename, 'w') as zip:
        for arquivo in arquivos:
            zip.write(arquivo)


def escrever_cabecalho(i):
    WIDTH = 30
    print("")
    print(f"***** Exercício {i:02d} *****".center(WIDTH))


class DualWriter:

    def __init__(self, *writers):
        self.writers = writers

    def write(self, message):
        for writer in self.writers:
            writer.write(message)
            writer.flush()

    def flush(self):
        for writer in self.writers:
            writer.flush()


# Cria um objeto StringIO para capturar a saída
stdout_capture = io.StringIO()

# Salva a referência do stdout original
original_stdout = sys.stdout

# Cria um DualWriter que escreve tanto para o StringIO quanto para o stdout original
dual_writer = DualWriter(original_stdout, stdout_capture)

try:
    # Redireciona o stdout para o DualWriter
    sys.stdout = dual_writer
    arquivos_exercicios = listar_exercicios()
    arquivos_exercicios.sort()
    for i in range(len(arquivos_exercicios)):
        escrever_cabecalho(i + 1)
        __import__(f"exercicio{i+1:02d}")
    print("")

    # Obtém o conteúdo capturado
    output = stdout_capture.getvalue()
    gerar_submissao(nome, sobrenome, output)

finally:
    # Restaura o stdout original
    sys.stdout = original_stdout
