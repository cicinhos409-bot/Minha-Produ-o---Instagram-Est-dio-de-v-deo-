# Módulo 1 · Aula 1 — "O assunto tem dono"

## Ideia central
**O formato se replica, o assunto se ocupa.** Copiar o título ou o assunto de um vídeo que explodiu (ou só traduzir) não funciona. O algoritmo já tem a prova de que o original é a melhor resposta. Quem copia o formato e troca o assunto fica com a audiência sem disputar com ninguém.

Prova da aula: o original tinha 616 mil views. Cópias literais ficaram entre 19 e 127 views. A tradução literal para o português fez 44. Só os primeiros a chegar, mexendo numa peça, ainda pegaram algo (254 mil e 40 mil).

## As 5 peças do título
| Peça | Exemplo | Viaja para outro nicho? |
|---|---|---|
| 1. Número alto | 25 | Sim |
| 2. Objeto concreto | esconderijos | Não (depende do tema) |
| 3. Segredo / curiosidade | "que ladrões nunca verificam" | Sim |
| 4. Autoridade emprestada | "policiais aposentados usam" | Sim |
| 5. Medo útil | segurança da casa/dinheiro | Não (depende do tema) |

## Os 5 jeitos de mudar o ângulo
1. **Inverso**: em vez de "onde esconder", "onde o ladrão olha primeiro".
2. **Público excluído**: "para quem mora em apartamento", "para idosos que moram sozinhos".
3. **Prova/teste em 1ª pessoa**: "testei 10 esconderijos com um ex-ladrão".
4. **Outro medo, mesmo gatilho**: o mesmo medo aplicado a outra pessoa.
5. **Formato inteiro em outro nicho**: "21 coisas que enfermeiras nunca fazem…". Precisa checar se há demanda.

Também conta: adaptar em vez de traduzir (autoridade local, como o "comissário AD" na Alemanha) e escolher onde publicar.

## Processo
1. **Garimpar**: achar um vídeo explodindo, recente e com muitas views.
2. **Dissecar**: separar as 5 peças.
3. **Achar o assunto vizinho**: outro ângulo ou outro público com o mesmo medo ou curiosidade.
4. **Ocupar primeiro**.

## Próxima aula (prometido)
O que é uma "brecha", as 3 condições para ela existir e por que levar para outro país pode dobrar as chances.

---

## Aplicação no nosso projeto (Reels @cicero.cf.ofcl)

**1. O curso é de YouTube, mas a lógica vale para Reels.** No Reels quem faz o papel do título é o **gancho** (a 1ª frase falada + o texto na tela + a capa). As 5 peças devem estar no gancho.

**2. Vários dos nossos temas são "assuntos com dono".** Furinho da janela do avião, furo da caneta, a caixa-preta é laranja, por que a cebola faz chorar, origem do OK: são curiosidades já exploradas por milhares de perfis. Pela aula, isso explica alcance baixo. Daqui em diante, cada tema clássico passa por um dos 5 ângulos antes de virar roteiro.

**3. Peças que hoje usamos pouco:**
- *Número alto*: quase não usamos ("3 erros…", "4 passos" são números baixos).
- *Autoridade emprestada*: não usamos. Ex.: "pilotos", "engenheiros", "a NASA". **A atribuição tem que ser verdadeira** (regra do CLAUDE.md: fatos reais, nada inventado).
- *Medo útil*: quase não usamos. No nosso funil, o medo útil do comprador é "não ter tempo / ter vergonha de aparecer / ficar para trás com a IA".

**4. Exemplos de tema vizinho (mesmo formato, porta nova):**
- Clássico: "Por que a cebola faz chorar" →
  - Inverso: "Por que a cebola gelada quase não faz chorar" (o frio deixa mais lenta a reação que solta o gás; o fato é real).
  - Teste em 1ª pessoa: "Testei 4 truques pra não chorar cortando cebola; só um funciona de verdade" (óculos de natação bloqueiam o gás).
- Para o nosso público comprador (canal dark / sem aparecer):
  - Autoridade + segredo: "7 coisas que canais dark grandes nunca mostram no vídeo".
  - Inverso: "Os 5 erros que fazem o Instagram esconder seu vídeo". Usar só o que for verificável, sem promessa de ganho.

## Melhorias para a ferramenta (UMBRA / Intelligence)
O UMBRA já tem `garimpo`, `extract_moldes`, `generate_titles` e `judge`, que batem com o passo a passo do curso. O que vale acrescentar:
1. **Dissecador das 5 peças**: dado um título viral, marcar cada peça e dizer quais viajam e quais trocar.
2. **Detector de assunto ocupado**: buscar cópias do mesmo título/tema e mostrar a "fila" (views do 1º, 2º, 3º…). Se já houver 3 ou mais cópias, avisar "assunto com dono".
3. **Gerador de 5 ângulos**: para cada molde, gerar obrigatoriamente uma versão por ângulo (inverso, público excluído, teste em 1ª pessoa, outro medo, outro nicho).
4. **Trava anti-tradução**: avisar quando o título gerado for tradução literal e sugerir a autoridade local equivalente.
5. **Nota de recência**: priorizar no garimpo vídeos recentes com muitas views ("assunto em alta agora").
