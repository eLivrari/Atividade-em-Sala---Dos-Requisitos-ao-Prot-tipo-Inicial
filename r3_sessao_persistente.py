"""R3 - Facilidade de acesso: login uma vez só, sessão salva em arquivo."""
import json
import os
import time

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sessao.json")
VALIDADE_DIAS = 30

#Utilizado IA para geração das funçôes
def fazer_login(email, agora=None):
    """Registra a sessão do aluno (simula o login, sem senha)."""
    if "@" not in email:
        raise ValueError("E-mail inválido.")
    agora = agora if agora is not None else time.time()
    dados = {"email": email, "expira_em": agora + VALIDADE_DIAS * 86400}
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f)


def sessao_ativa(agora=None):
    """Devolve o e-mail da sessão se ainda for válida; senão None."""
    agora = agora if agora is not None else time.time()
    if not os.path.exists(ARQUIVO):
        return None
    with open(ARQUIVO, encoding="utf-8") as f:
        dados = json.load(f)
    return dados["email"] if dados["expira_em"] > agora else None


def abrir_app(email_para_login, agora=None):
    """Simula abrir o app: só pede login se não houver sessão válida."""
    inicio = time.perf_counter()
    email = sessao_ativa(agora)
    precisou_login = email is None
    if precisou_login:
        fazer_login(email_para_login, agora)
        email = email_para_login
    ms = (time.perf_counter() - inicio) * 1000
    return email, precisou_login, ms


def executar():
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)  # começa do zero para a demonstração ser repetível
    email = "aluno@campus.edu.br"

    _, login1, ms1 = abrir_app(email)
    print(f"1a abertura: pediu login? {login1} ({ms1:.2f} ms)")
    assert login1 is True

    _, login2, ms2 = abrir_app(email)
    print(f"2a abertura: pediu login? {login2} ({ms2:.2f} ms)")
    assert login2 is False

    no_futuro = time.time() + (VALIDADE_DIAS + 1) * 86400
    _, login3, _ = abrir_app(email, agora=no_futuro)
    print(f"Abertura após {VALIDADE_DIAS + 1} dias: pediu login? {login3}")
    assert login3 is True
    print("[OK] R3: login só na 1a vez (e quando a sessão expira); abertura rápida.")
