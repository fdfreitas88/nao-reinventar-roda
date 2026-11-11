---
name: reuso-de-codigo
description: Reuso de código do nao-reinventar-roda. Antes de escrever código, procura no repositório e na web uma biblioteca, API ou serviço pronto e registra a decisão (reusar, adaptar, comprar ou construir) com fonte. Não serve para pesquisar ideia ou produto; para isso use as fases 1 a 3.
argument-hint: <a necessidade técnica em uma frase>
disable-model-invocation: true
---

# Reuso de código

Leia primeiro `${CLAUDE_PLUGIN_ROOT}/referencia/regras.md` (seções 3, 4 e 9) e o modelo `04-reuso-de-codigo.md` em `${CLAUDE_PLUGIN_ROOT}/referencia/modelos.md`.

Necessidade: $ARGUMENTS

Esta skill não tem pré-requisito e não usa subagentes. Teto fixo: 6 buscas e 4 páginas abertas.

## Passos

1. **Definir a necessidade** em uma frase: entrada, saída, escala, linguagem e restrições. Uma restrição sempre entra: a licença que o projeto aceita. Se o projeto é comercial e fechado, GPL e AGPL em dependência são bloqueio; diga isso ao comparar. Se a licença do projeto não estiver clara, pergunte.
2. **Registro anterior.** Se existir `04-reuso-de-codigo.md` em uma pasta de `./pesquisa-ideia/` ou em `./docs/`, procure uma entrada para a mesma necessidade. Havendo, mostre a decisão e pergunte se ainda vale, antes de gastar buscas.
3. **Opções internas.** Procure no repositório código que já faz isso. Fonte interna é `arquivo:linha`.
4. **Opções externas.** Procure no registro de pacotes da linguagem, em repositórios públicos e em serviços ou APIs oficiais. Para os 2 ou 3 melhores candidatos, abra a página e confira: licença, data da última versão ou do último commit, avisos de segurança, e se faz o que a necessidade pede.
5. **Comparar** em: ajuste à necessidade, maturidade, manutenção, segurança, licença, custo, esforço de integração, dependência do fornecedor.
6. **Decidir** um caminho: reusar, adaptar, comprar ou construir. Construir exige justificativa escrita. "Não encontrei" só vale com as consultas listadas.
7. **Registrar.** Acrescente a entrada ao fim de `04-reuso-de-codigo.md`, sem apagar as anteriores. Local: a pasta da ideia, se o usuário indicou uma ou só existe uma; senão, `./docs/04-reuso-de-codigo.md`. Antes de criar um arquivo novo no repositório, diga o caminho.
8. **Responder** com: opções checadas, decisão, motivo, riscos e o caminho do registro.

## Quando pular

Tarefa trivial (menos de uma função curta), ou o usuário já disse para escrever do zero. Nesses casos diga em uma linha que pulou e por quê.

## Racionalizações a recusar

| Pensamento | Resposta |
| --- | --- |
| "Lembro que essa biblioteca resolve" | Memória não conta. Abra a página e confira licença, data e o que ela faz hoje. |
| "Achei uma, não preciso olhar as outras" | Sem comparação não há decisão. Leve ao menos duas opções à tabela, ou registre que só uma foi encontrada e com quais consultas. |
| "A licença deve servir" | Licença é lida na fonte, não presumida. Sem licença conferida, a opção não pode ser a escolhida. |
| "Não achei nada, então construo" | Só vale com as consultas listadas e o teto gasto. Com busca bloqueada, a decisão é "não foi possível verificar". |
| "O repositório é popular, então é mantido" | Popularidade não é manutenção. Registre a data da última versão ou do último commit. |
| "Já decidimos isso antes" | Mostre a entrada do registro e a data. Se não há entrada, não houve decisão. |
