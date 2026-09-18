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
# Uso de IA: ajudou a montar a estrutura do codigo em python.
# ============================================================
