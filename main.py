# ============================================================
# PLANO (Passo 1)
# Requisitos escolhidos (do mais simples ao mais complexo):
#   1) R1 - Visualização de vagas ........ ~10 min
#   2) R2 - Vagas de funcionários ........ ~15 min
#   3) R3 - Facilidade de acesso (sessão)  ~20 min
# R4 (Android/iOS) fica de fora: não faz sentido em linha de comando.
# Uso de IA: para gerar a estrutura inicial dos arquivos e revisar o código.
# ============================================================
from dados import VAGAS
import r1_visualizacao_vagas
import r2_vagas_funcionarios
import r3_sessao_persistente


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def main():
    titulo("R1 - Visualização de vagas")
    r1_visualizacao_vagas.executar(VAGAS)

    titulo("R2 - Vagas de funcionários")
    r2_vagas_funcionarios.executar(VAGAS)

    titulo("R3 - Facilidade de acesso (sessão persistente)")
    r3_sessao_persistente.executar()


if __name__ == "__main__":
    main()


# ============================================================
# AUTOAVALIAÇÃO (Passo 3)
# Critérios atingidos:
#   1) Lista de requisitos em requisitos.md (R1, R2, R3) ......... SIM
#   2) Um arquivo por requisito, separado do ponto de entrada .... SIM
#   3) Ponto de entrada único (python3 main.py), sem editar código SIM
#   4) Pelo menos 3 commits com mensagem por requisito/etapa ..... SIM (5 commits)
#   5) README com até 10 linhas (o que faz, requisitos, execução)  SIM
#   6) Executa sem erro e a saída comprova cada requisito ........ SIM
# Critérios não atingidos: nenhum. Limitação: R4 ficou de fora e os
# dados das vagas são simulados (sem sensores, sem "tempo real").
#
# Requisito mais difícil de traduzir em código: R3. "Não precisar fazer
# login toda hora" não diz por quanto tempo a sessão vale. Resolvi
# assumindo 30 dias (VALIDADE_DIAS) e guardando a sessão em sessao.json;
# para testar a expiração sem esperar, a função aceita um "agora" simulado.
# Também precisei decidir o que é "leve": medi o tempo de abertura em ms.
#
# Uso de IA: ajudou a montar a estrutura do codigo em python.
# ============================================================
