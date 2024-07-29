nome = "Mateus"
sobrenome = "Oliveira"


####################################################################
# Nao mexa nesse arquivo !!
# Para resolver o TP modifique os arquivos exercicio_*.py que podem ser acessados no lado esquerdo.
####################################################################
import io
import sys

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



    escrever_cabecalho(1)
    import exercicio01
    escrever_cabecalho(2)
    import exercicio02
    escrever_cabecalho(3)
    import exercicio03
    escrever_cabecalho(4)
    import exercicio04
    escrever_cabecalho(5)
    import exercicio05
    escrever_cabecalho(6)
    import exercicio06
    escrever_cabecalho(7)
    import exercicio07
    escrever_cabecalho(8)
    import exercicio08
    escrever_cabecalho(9)
    import exercicio09
    escrever_cabecalho(10)
    import exercicio10
    escrever_cabecalho(11)
    import exercicio11
    escrever_cabecalho(12)
    import exercicio12
    escrever_cabecalho(13)
    import exercicio13
    escrever_cabecalho(14)
    import exercicio14
    escrever_cabecalho(15)
    import exercicio15
    escrever_cabecalho(16)
    import exercicio16
    print("")
    
    from gerar_submissao import gerar_submissao

    # Obtém o conteúdo capturado
    output = stdout_capture.getvalue()
    gerar_submissao(nome, sobrenome, output)

finally:
    # Restaura o stdout original
    sys.stdout = original_stdout

