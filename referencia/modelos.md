# Modelos dos arquivos

Copie a estrutura. Não deixe seção sem conteúdo: escreva "nenhum encontrado" e aponte as consultas usadas.

## Cabeçalho comum

```markdown
---
ideia: <nome-da-pasta>
fase: <00 | 01 | 02 | 03 | 04>
(o relatório 05 é HTML e não leva este cabeçalho; os dados dele vão no rodapé)
data: <AAAA-MM-DD>
situacao: <completa | parcial | bloqueada>
motivo_parada: <saturação | teto | fontes bloqueadas | pedido do usuário>
entradas: <arquivo (data), arquivo (data) | nenhuma>
formato: 1
---
```

## 00-ideia.md

```markdown
# Ideia: <nome>

- **Enunciado:** <uma frase>
- **Tipo:** <software | equipamento | serviço>
- **Público:** <quem usaria>
- **Finalidade:** <vender | uso próprio | aprender>
- **Mercado e idioma:** <Brasil | global | outro>
- **Restrições:** <prazo, orçamento, plataforma, licença>
- **Eu largo se:** <opcional>
- **Confirmado pelo autor em:** <AAAA-MM-DD>

## O que a ideia entrega

| Id | Capacidade |
| --- | --- |
| C1 | ... |
```

## 01-ideias-e-demanda.md

```markdown
# Ideias parecidas e demanda: <nome>

## Sinais de demanda
| Id | Sinal | Quem e onde | Data da fonte | Fonte |

## Sinais contrários
Campanhas fracassadas, produtos descontinuados, pedidos sem resposta.
| Id | Sinal | Data da fonte | Fonte |

## Ideias parecidas sem produto obtenível
| Id | Ideia | Situação | Fonte |

## Candidatos vistos de passagem
Entrada da fase 2. Tudo o que dá para comprar, baixar, usar ou apoiar.
| Nome | Onde apareceu | Fonte |

## Fontes
| Id | URL | Acesso | Data da fonte | Tipo | Condição | Trecho literal |

## Pistas a verificar

## Cobertura da busca
| Frente | Consulta | Idioma | Páginas abertas | Linhas novas | Motivo de parada |

Ficou sem procurar: ...
Fontes bloqueadas: ...
```

## 02-produtos-existentes.md

```markdown
# Produtos e soluções existentes: <nome>

## Lista longa
Tudo "não conferido (trecho de busca)" até entrar na lista curta.
| Nome | Categoria | Uma linha | Fonte |

Categoria: comercial, gratuito, código aberto, em andamento, financiamento coletivo, abandonado.

## Lista curta
Escolhida pelo autor em <data>.
| Id | Produto | Responsável | Situação | Licença | Preço | Página principal |

## Documentos lidos
| Produto | Documento | Página ou seção | O que foi tirado | Fonte |

## Em andamento
| Projeto | Onde | Situação | Entrega prometida | Fonte |

## Capacidades por produto
Uma linha por capacidade. Inclua as de `00-ideia.md` (C1...) e as que os produtos têm e a ideia não (X1...).
| Capacidade | P1 | P2 | P3 |

## Descartados
| Nome | Motivo |

## Fontes
## Pistas a verificar
## Cobertura da busca
```

## 03-veredito.md

```markdown
# Veredito: <nome>

## Resultado
<seguir | seguir com mudanças | não seguir: use X | inconclusivo: faltam ...>

## O caso mais forte contra

## Por que o público não usaria simplesmente o que já existe
| Produto | Lacuna que impede | Evidência |

## Prós e contras
| Pró ou contra | Argumento | Evidência |

## Matriz
| Capacidade | Sua ideia | Já existe em | Em andamento em | Sinal de demanda | Classificação |

Classificação: obrigatório (presente na maioria da lista curta), paridade opcional (em alguns), diferencial (não encontrado em nenhum e com sinal de demanda), diferencial em risco (só coberto por algo em andamento).

## O que incluir
### Obrigatório para ser considerado
### Diferencial
### Paridade opcional

## O que não foi avaliado
Viabilidade técnica, custo de construção, questões legais, capacidade do autor.

## O que mudaria este veredito

## Afirmações não conferidas que pesam no resultado

## Referências
Identificadores de `01` e `02` citados.

---
## Comentário do agente principal
<separado do texto do juiz>
```

## 04-reuso-de-codigo.md

Arquivo de acréscimo. Uma entrada por necessidade.

```markdown
## <AAAA-MM-DD> <necessidade em uma frase>

- **Opções internas:** <arquivo:linha | não encontrado no repositório>
- **Decisão:** <reusar | adaptar | comprar | construir>
- **Motivo:**
- **Riscos:**

| Opção | Licença | Última atividade | Avisos de segurança | Esforço de integração | Fonte |

| Id | URL | Acesso | Condição | Trecho literal |
```

## 05-relatorio.html

One page executiva em HTML, gerada pela skill `relatorio` a partir do modelo `referencia/relatorio-modelo.html`. Não tem cabeçalho YAML: pastas, datas, modo (final ou prévia), situação das fases e a conta da temperatura vão no rodapé.

Seções, nesta ordem:

1. Título com o veredito em uma frase.
2. A ideia (de `00`) e a pesquisa realizada (totais da Cobertura de `01` e `02`).
3. Veredito com o termômetro: rótulo da faixa, medidor semicircular com uma agulha por ideia, nota de cada ideia.
4. Três motivos.
5. Mercado: quem já faz (até 10 linhas, preço e licença separados).
6. Casos do setor (linha do tempo) e quem usa e como resolve hoje.
7. Recomendação em três colunas.
8. Rodapé com fontes, modo, situação, conta da temperatura e o que não foi avaliado.

Cada linha factual leva o identificador de origem (`02:F10`, `01:N5`) em letra pequena.

## 05-relatorio.json

Conteúdo da one page, fonte única do HTML e do PDF (`scripts/relatorio_pdf.py`). Texto em português; aceita `<b>` e `<i>`; escape `&`, `<` e `>` do resto.

```json
{
  "titulo_curto": "Termômetro SAST",
  "meta": "Avaliação de oportunidade · AppSec · 12 nov 2026 · Uso interno",
  "previa": false,
  "titulo": "Ferramenta X: não é viável como produto",
  "ideia": "até 60 palavras, de 00",
  "pesquisa": "totais da Cobertura de 01 e 02",
  "veredito": "Não investir como produto",
  "cor_veredito": "#c23b28",
  "agulhas": [{"letra": "A", "t": 34, "principal": true}],
  "nota_medidor": "<b>A</b> nome: 34/100. Frase sobre o limite de 50.",
  "motivos_titulo": "Por que não é viável",
  "motivos": [{"rotulo": "Motivo 1 · Já existe", "titulo": "...", "texto": "...", "ref": "03 · 02:F18"}],
  "mercado": [{"empresa": "...", "entrega": "...", "modelo": "preço ou licença", "ref": "02:F10"}],
  "casos": [{"ano": "2025", "texto": "<b>Nome</b> comprado por ...", "ref": "01:N5"}],
  "quem_usa": [{"quem": "Organização", "texto": "como resolve", "ref": "01:D10"}],
  "leitura_casos": "uma frase",
  "recomendacao": [{"titulo": "Não fazer", "texto": "..."}],
  "rodape": "fontes, modo, situação, conta da temperatura, o que não foi avaliado"
}
```

Limites: 3 motivos, até 10 linhas de mercado, 3 colunas de recomendação. `cor_veredito` é `#2f8f5b` quando a faixa é 50 ou mais.

