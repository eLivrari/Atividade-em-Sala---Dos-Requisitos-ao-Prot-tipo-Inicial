"""R1 - Visualização de vagas: lista as vagas e mostra disponíveis e indisponíveis. Utilizado IA para gerar o codigo"""


def listar_vagas(vagas):
    """Imprime todas as vagas com o status e devolve os totais."""
    print(f"{'Vaga':<6}{'Local':<14}{'Status'}")
    for v in vagas:
        status = "Indisponível" if v["ocupada"] else "Disponível"
        print(f"{v['id']:<6}{v['local']:<14}{status}")

    total = len(vagas)
    indisponiveis = sum(1 for v in vagas if v["ocupada"])
    return {"total": total, "disponiveis": total - indisponiveis, "indisponiveis": indisponiveis}


def executar(vagas):
    resumo = listar_vagas(vagas)
    print(f"\nTotal: {resumo['total']} | Disponíveis: {resumo['disponiveis']} "
          f"| Indisponíveis: {resumo['indisponiveis']}")
    assert resumo["disponiveis"] + resumo["indisponiveis"] == resumo["total"]
    print("[OK] R1: vagas listadas com status e contagem consistente.")
