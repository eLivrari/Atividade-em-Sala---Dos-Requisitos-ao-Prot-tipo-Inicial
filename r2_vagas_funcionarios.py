"""R2 - Vagas de funcionários: identifica vagas reservadas e avisa o aluno."""

ROTULOS = {
    "comum": "Comum",
    "funcionario": "RESERVADA - Funcionário",
    "deficiente": "RESERVADA - PCD",
}

# Quais tipos de vaga cada perfil pode usar
PERMISSOES = {
    "aluno": {"comum"},
    "funcionario": {"comum", "funcionario"},
    "pcd": {"comum", "deficiente"},
}


def listar_vagas_reservadas(vagas):
    """Imprime as vagas reservadas com rótulo próprio (nunca como vaga comum)."""
    reservadas = [v for v in vagas if v["tipo"] != "comum"]
    for v in reservadas:
        print(f"Vaga {v['id']:<3}{v['local']:<12}{ROTULOS[v['tipo']]}")
    return reservadas


def validar_estacionamento(vaga, perfil):
    """Devolve (permitido, mensagem) para um perfil que quer usar a vaga."""
    if vaga["ocupada"]:
        return False, f"Vaga {vaga['id']} está indisponível."
    if vaga["tipo"] not in PERMISSOES[perfil]:
        return False, (f"AVISO: vaga {vaga['id']} ({vaga['local']}) é "
                       f"{ROTULOS[vaga['tipo']]}. Não estacione aqui como {perfil}.")
    return True, f"Vaga {vaga['id']} liberada para {perfil}."


def executar(vagas):
    reservadas = listar_vagas_reservadas(vagas)
    assert all(v["tipo"] != "comum" for v in reservadas)

    por_id = {v["id"]: v for v in vagas}
    testes = [(3, "aluno", True), (4, "aluno", False), (10, "funcionario", True)]
    print()
    for id_vaga, perfil, esperado in testes:
        permitido, msg = validar_estacionamento(por_id[id_vaga], perfil)
        print(f"[{perfil} -> vaga {id_vaga}] {msg}")
        assert permitido == esperado
    print("[OK] R2: vagas reservadas identificadas e aluno bloqueado nelas.")
