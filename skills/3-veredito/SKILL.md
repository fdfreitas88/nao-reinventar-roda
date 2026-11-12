---
name: 3-veredito
description: Fase 3 do nao-reinventar-roda. Um juiz de contexto limpo lê os achados das fases 1 e 2 e entrega o veredito, a tabela de prós e contras e a matriz do que a ideia entrega, do que já existe, do que está em andamento e do que incluir. Use depois da fase 2.
argument-hint: <nome-da-pasta-da-ideia>
disable-model-invocation: true
---

# Fase 3: veredito

Leia primeiro `${CLAUDE_PLUGIN_ROOT}/referencia/regras.md` e `${CLAUDE_PLUGIN_ROOT}/referencia/modelos.md`. As regras de lá valem aqui e não são repetidas.

Ideia: $ARGUMENTS

## Passos

1. **Localizar e travar.** Resolva a pasta e confira `00`, `01` e `02` pela seção 2 das regras. Faltando algum, pare com a mensagem de lá e o comando da fase que falta. Avise sobre entrada parcial ou com mais de 30 dias.
2. **Chamar o juiz.** Lance um subagente do tipo `nao-reinventar-roda:veredito`. Se esse tipo não estiver disponível, use um subagente de uso geral e mande-o ler `${CLAUDE_PLUGIN_ROOT}/agents/veredito.md` antes de agir. O prompt é exatamente este, com os três valores preenchidos e nada mais:

   ```
   Pasta da ideia: <caminho absoluto>
   Data de hoje: <AAAA-MM-DD>
   Modelos: <caminho absoluto de referencia/modelos.md>
   ```

   Não inclua resumo da conversa, opinião do autor, nem a sua. O juiz não pode saber o que o autor espera ouvir.
3. **Gravar.** Grave `03-veredito.md` com o cabeçalho comum seguido do texto devolvido, sem editar, cortar nem suavizar. Se o juiz devolveu "entrada ausente", pare e relate.
4. **Conferir a forma, não o conteúdo.** Verifique se todas as seções do modelo vieram e se cada argumento cita um identificador de `01` ou `02`. Faltando, peça ao mesmo juiz que complete; não complete você.
5. **Comentário.** Se você discorda de algo ou sabe de contexto que o juiz não tinha, escreva na seção "Comentário do agente principal", depois da linha de separação. Nunca altere o resultado do juiz.
6. **Encerrar.** Responda com: caminho, o resultado em uma linha, o caso mais forte contra em duas linhas, o que incluir (obrigatório e diferencial) e o que não foi avaliado.

   - Se o resultado for "inconclusivo", mostre o que falta e o comando para refazer a fase correspondente.
   - Para a one page executiva, o comando é `/nao-reinventar-roda:relatorio <nome-da-pasta>`.
   - Se o usuário seguir para a implementação, o comando é `/nao-reinventar-roda:reuso-de-codigo <necessidade>`.

## Não faça

- Não rode o veredito no contexto principal. Sem subagente disponível, pare e diga isso.
- Não busque na web nesta fase. Dado que falta é motivo de "inconclusivo", não de busca nova.
- Não troque o resultado por "viável" ou "inviável": custo, técnica e questões legais não foram avaliados.
