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

## Aplicação: canal dark no YouTube

**Regra de produção:** nenhum vídeo nasce de título copiado ou traduzido. Todo título passa por **molde (5 peças) → troca do objeto e do medo → escolha de um dos 5 ângulos**.

**Como usar as 5 peças num canal dark:**
- *Número alto*: listas de 15 a 30 itens seguram retenção e dão sensação de vídeo completo (bom para vídeos de 8 a 20 min).
- *Autoridade emprestada*: médicos, policiais, engenheiros, enfermeiras, historiadores. O canal dark não tem rosto, então a autoridade emprestada substitui a do apresentador. **Não inventar citação**: "o que enfermeiras relatam", e não "a enfermeira Maria disse".
- *Medo útil*: saúde, dinheiro, segurança, golpe, perda. Os nichos dark que mais rodam vivem disso.

**Exemplo do método (do curso):** "25 esconderijos que ladrões nunca verificam" → "23 lugares que ladrões checam primeiro" (inverso) → "17 esconderijos para quem mora em apartamento" (público excluído).

## Melhorias para a ferramenta (UMBRA → YouTube Intelligence)
O UMBRA já tem `yt_intelligence_garimpo`, `extract_moldes`, `generate_titles`, `judge` e a fila de produção, ou seja, o esqueleto do método. O que falta:
1. **Dissecador das 5 peças**: no molde extraído, marcar número, objeto, segredo, autoridade e medo, e dizer quais trocar.
2. **"Fila de copiadores"**: para cada outlier, buscar o mesmo título e mostrar as cópias em ordem de publicação, com as views de cada uma. Com 3 ou mais cópias fracas, marcar **assunto com dono**.
3. **Gerador dos 5 ângulos obrigatórios**: cada molde gera um título por ângulo (inverso, público excluído, teste em 1ª pessoa, outro medo, outro nicho).
4. **Trava anti-tradução**: reprovar o título gerado quando for tradução literal do original.
5. **Peso de recência** no garimpo: views por dia desde a publicação, não views totais.
