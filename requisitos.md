# Requisitos implementados no protótipo

Origem: análise de requisitos do aplicativo de estacionamento do Campus (atividade anterior).

## R1 - Visualização de vagas (alunos)
- **Critério de aceitação:** ao acessar, o sistema lista as vagas e mostra as disponíveis e as indisponíveis.
- **Rastreio:** "seria ótimo se houvesse um aplicativo que mostrasse as vagas disponíveis em tempo real".
- **Arquivo:** `r1_visualizacao_vagas.py`

## R2 - Vagas de funcionários (alunos)
- **Critério de aceitação:** vagas de funcionários são identificadas e não aparecem como vaga comum.
- **Rastreio:** "os alunos às vezes estacionam em vagas reservadas para funcionários, principalmente perto da biblioteca".
- **Arquivo:** `r2_vagas_funcionarios.py`

## R3 - Facilidade de acesso (alunos)
- **Critério de aceitação:** o aplicativo é leve e o aluno não precisa fazer login toda hora.
- **Rastreio:** "os alunos não o usarão se demorar muito para abrir ou se tiverem que fazer login toda vez".
- **Arquivo:** `r3_sessao_persistente.py`

## Não implementado
- **R4 - Compatibilidade (Android/iOS):** não cabe em um protótipo de linha de comando.

## Premissas (perguntas ao cliente ainda sem resposta)
- Os dados das vagas são simulados em `dados.py` (não há sensores nem reporte manual).
- "Tempo real" não foi tratado: o estado das vagas é uma foto fixa.
- O "aviso" para vaga reservada é uma mensagem de bloqueio no terminal.
