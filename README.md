# Protótipo - Aplicativo de estacionamento do Campus

Protótipo em linha de comando (Python 3, sem bibliotecas externas) com dados simulados de vagas.
Cobre três requisitos: **R1** listar vagas disponíveis/indisponíveis, **R2** identificar vagas
reservadas (funcionários/PCD) e avisar o aluno, **R3** manter a sessão para não pedir login toda vez.
R4 (Android/iOS) não foi implementado. A lista completa está em `requisitos.md`.
Cada requisito fica em seu próprio arquivo (`r1_...`, `r2_...`, `r3_...`); `main.py` é o ponto de entrada.

Como executar (na pasta deste README): `python3 main.py`
A saída mostra uma linha `[OK]` para cada requisito que comprova o comportamento.
