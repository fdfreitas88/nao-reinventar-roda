# nao-reinventar-roda

Plugin do Claude Code para pesquisar antes de construir. Cada fase grava um arquivo em `./pesquisa-ideia/<nome-da-ideia>/`, e toda afirmação leva URL, data de acesso e a condição "conferido" ou "não conferido".

## Skills

| Comando | O que faz | Arquivo |
| --- | --- | --- |
| `/nao-reinventar-roda:1-demanda <ideia em uma frase>` | Registra a ideia e procura ideias parecidas, sinais de demanda e sinais contrários | `00-ideia.md`, `01-ideias-e-demanda.md` |
| `/nao-reinventar-roda:2-existentes <pasta>` | Levanta produtos existentes e em andamento; lê fabricante, documentação e datasheet da lista curta | `02-produtos-existentes.md` |
| `/nao-reinventar-roda:3-veredito <pasta>` | Juiz de contexto limpo entrega resultado, prós e contras e matriz do que incluir | `03-veredito.md` |
| `/nao-reinventar-roda:relatorio <pasta> [<pasta> ...]` | Gera uma one page executiva (C-level) em HTML e PDF com ideia, veredito, termômetro de espaço de mercado, motivos, quem já faz, casos do setor, quem usa e recomendação. Não busca nada novo | `05-relatorio.html`, `.pdf`, `.json` |
| `/nao-reinventar-roda:reuso-de-codigo <necessidade>` | Procura biblioteca, API ou serviço pronto antes de escrever código | `04-reuso-de-codigo.md` |

Nenhuma skill dispara sozinha. As fases 2 e 3 param quando falta o arquivo da fase anterior e mostram o comando a rodar.

## Instalação

```sh
claude plugin marketplace add fdfreitas88/nao-reinventar-roda
claude plugin install nao-reinventar-roda@nao-reinventar-roda
```

Para instalar de uma cópia local, troque `fdfreitas88/nao-reinventar-roda` pelo caminho da pasta.

Depois de editar os arquivos, suba a versão em `.claude-plugin/plugin.json` e reinstale.

## Exemplo

```text
/nao-reinventar-roda:1-demanda sensor de temperatura para rack com alerta por mensagem
/nao-reinventar-roda:2-existentes sensor-rack
/nao-reinventar-roda:3-veredito sensor-rack
/nao-reinventar-roda:relatorio sensor-rack
```

A fase 1 mostra o registro da ideia e espera a confirmação antes de buscar. A fase 2 mostra uma lista longa de candidatos e pede que você escolha de 3 a 5 para a leitura detalhada. A fase 3 grava o resultado: "seguir", "seguir com mudanças", "não seguir: use X" ou "inconclusivo".

O relatório transforma as fases numa página para a diretoria. A temperatura de 0 a 100 mede quanto espaço livre sobra para a ideia como produto e sai de uma conta fixa sobre a matriz da fase 3, mostrada no rodapé. Pode ser gerado depois da fase 1, marcado como prévia, e aceita até três pastas para comparar versões da mesma ideia.

A fase 2 também oferece o relatório como opção 4, na escolha da lista curta e no encerramento. O PDF (A4, uma página) é gerado por `scripts/relatorio_pdf.py` e precisa de `python3 -m pip install reportlab`.

## Estrutura

- `skills/`: uma pasta por fase.
- `agents/pesquisador.md`: busca uma frente dentro de um teto e devolve linhas com fonte.
- `agents/veredito.md`: juiz que lê só `00`, `01` e `02`.
- `referencia/regras.md`: regras comuns a todas as fases.
- `referencia/modelos.md`: modelos dos arquivos gerados.
- `referencia/relatorio-modelo.html`: modelo HTML da one page executiva.
- `scripts/relatorio_pdf.py`: gera o PDF da one page a partir de `05-relatorio.json`.

## Limites

- Não estima tamanho de mercado.
- Não avalia viabilidade técnica, custo de construção nem questões legais.
- "Não encontrado" vale só para as buscas listadas em cada arquivo.

## Autor e licença

Criado por Felipe Freitas.

Licença MIT: você pode usar, copiar, modificar e redistribuir, desde que mantenha o aviso de copyright e o texto da licença em toda cópia ou parte substancial. Veja o arquivo `LICENSE`.
