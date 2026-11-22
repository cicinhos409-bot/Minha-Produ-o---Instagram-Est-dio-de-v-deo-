# Funções para o YouTube Intelligence (UMBRA), tiradas do curso

Todas as funções sugeridas nas análises das aulas 1 a 9, **sem repetição** e organizadas pela ordem do método.
Coluna **Base no UMBRA** = função que já existe e pode ser estendida (`yt_intelligence_*`).

**Regra geral para todas as funções**: número sem fonte não entra; o que a IA gerar vem marcado como **"não conferido"** até o usuário confirmar.

---

## Etapa 1 — Garimpar outliers
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 1 | **Multiplicador automático** | Calcula a **mediana** dos últimos 15–30 vídeos do canal e marca cada vídeo com views ÷ mediana | 🔥 ≥ 10× · 🚀 ≥ 50× (mediana, não média: o outlier distorce a média) | 3 | `channel`, `garimpo` |
| 2 | **Views/dia e views/mês** | Mostra a velocidade de cada vídeo, não só o total | Ordenar o garimpo por velocidade (mais recente = mais quente) | 1, 8 | `garimpo` |
| 3 | **Radar de vídeos frescos** | Lista vídeos do nicho dos últimos 7–14 dias por views/dia, com a coluna **views ÷ inscritos** | Filtro de canal pequeno (< 10 mil / < 50 mil inscritos); views ÷ inscritos > 10× = algoritmo entregando para fora | 4 | `discover`, `garimpo` |
| 4 | **Filtro por tamanho do canal** | Prioriza outliers de canais pequenos e médios | Outlier em canal pequeno prova demanda do assunto | 3 | `garimpo` |
| 5 | **Classificador dos 3 tipos** | Marca o outlier como **destoa** / **canal em alta** / **novo subindo rápido** | Prioridade: novo subindo (< 7 dias) > canal em alta > destoa | 6 | `judge` |
| 6 | **Detector de canal fora da curva** | Idade do canal, nº de vídeos > 100 mil, crescimento de inscritos, frequência de postagem | Vários vídeos explodindo = "achou o caminho"; "cresceu por tema, não por volume" | 4, 6 | `channel` |
| 7 | **Classificador de nicho** | A partir de print ou URL do canal, responde "que nicho é esse?" em 2 palavras | Encaixa o canal na seção certa do banco | 8 | `channel` |

## Etapa 2 — Mapear o nicho e a concorrência
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 8 | **Analisador de fila (as 3 contagens)** | Ao colar um título, busca e classifica cada resultado em **cópia idêntica** / **variação** / **jeito novo** (similaridade de texto), com views, data e inscritos | Veredito: quase tudo cópia = **porta aberta**; vários bons fazendo diferente = **ficando ocupada**; 3 ou mais cópias fracas = "assunto com dono só por cópia" | 1, 4 | `opportunities` |
| 9 | **Linha do tempo da fila** | Gráfico views × data de postagem dos vídeos com o mesmo título | Mostra até quando quem chegou ainda ganhava | 4 | — |
| 10 | **Destaque do concorrente de verdade** | Aponta quem mudou o jeito e foi bem, e extrai o que mudou (número, promessa, autoridade) como molde | "Copie o jeito, não o título" | 4 | `extract_moldes` |
| 11 | **Detector de tema com dono** | Avisa quando 2 ou mais canais diferentes estouraram no mesmo tema | Ex.: casa limpa + casa organizada | 6 | `opportunities` |
| 12 | **Detector/sugestor de subnicho** | Agrupa os outliers de um canal por tema e sugere o canal de nicho menor | 2 ou mais outliers no mesmo tema = subnicho comprovado (ex.: catarata, pressão, cirurgia) | 3, 4 | `channel` |
| 13 | **Busca multi-idioma** | Traduz o tema e busca em PT / ES / IT / DE / PL / TR, marcando cada vídeo como **literal** ou **adaptado**, com views e data | Só literal com poucas views = **brecha de mercado aberta** | 2, 3 | `discover` |
| 14 | **Fila de chegada por idioma** | Quantos vídeos parecidos saíram **depois** do primeiro naquele idioma e quanto fizeram | Ex.: "8 vídeos, o melhor ~1.000 → fila fechada" | 7 | — |
| 15 | **Classificador de quem atende** | Marca cada canal da busca (este mês, por popularidade) como **instituição/médico**, **especialista** ou **canal sem aparecer** | Médico forte em confiança e fraco em narrativa não fecha a porta | 5 | `discover` |
| 16 | **Alerta de janela aberta / chegar primeiro** | Monitora canais em alta em inglês; avisa quando um tema/hábito novo estoura lá e não existe no idioma do canal | Canal sem aparecer < 1.000 inscritos com > 10 mil no mês = "a corrida começou"; janela de **24–72 h** | 5, 7 | `run_worker` |
| 17 | **Confirmação fora do canal** | Pesquisa o tema fora do canal e soma as views dos maiores vídeos | Mede o tamanho real do assunto | 3 | `discover` |

## Etapa 3 — Medir a demanda
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 18 | **Assistente de afunilamento** | A partir de um ângulo, gera os ângulos menores e o número de cada um (casos/ano, pesquisas) **com fonte obrigatória** | Sem fonte → "sem fonte"; a IA pode errar número | 5 | `ai_chat` |
| 19 | **Comparador Google Trends** | Compara 2–5 temas como **Assunto**, em **Pesquisa do YouTube**, 90 dias, no mundo e por país | Alerta quando escolher "Termo de pesquisa" em vez de "Assunto" (ex.: catarata = cachoeira) | 5 | — |
| 20 | **Tendência da curva** | Classifica o interesse como estável / subindo / caindo | Estável ou subindo = bom | 5 | — |
| 21 | **Ficha das 4 perguntas** | Nota e justificativa para: **volume**, **canal dominante**, **RPM estimado do idioma**, **encaixe cultural** | Ex.: inverno rigoroso não roda no Brasil | 2 | `judge` |

## Etapa 4 — Estudar a fundo
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 22 | **Analisador de capa + título** | Recebe miniatura + título e responde: por que clica, qual público, que ângulos explorar | Prompt da aula 6 | 6 | `analyze_thumbnail_text` |
| 23 | **Classificador de ângulo** | Marca o título como **identificação + mistério** / **educativo genérico** / **lista com autoridade** | Preferir identificação + mistério; educativo genérico está saturado | 3 | `judge` |
| 24 | **Escada assunto → hábito** | Do assunto (com dono), gera hábitos comuns do dia a dia, cada um com dado + fonte | "Fonte não conferida" até o usuário confirmar | 6 | `ai_chat` |
| 25 | **Validação em lote dos hábitos** | Busca cada hábito no formato do título e devolve o maior vídeo existente | Ex.: "arrumar a cama → 7 mil = vazio" | 6 | `discover` |
| 26 | **Extrator de padrão do canal em alta** | Lê os títulos dos vídeos estourados e devolve o molde comum | Ex.: "If you [hábito], you have these rare traits" | 6 | `extract_moldes` |

## Etapa 5 — Montar o título
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 27 | **Dissecador de título** | Modo **5 peças** (número, objeto, segredo, autoridade, medo, dizendo quais viajam) e modo **3 peças** (identificação, promessa, autoridade); gera o **esqueleto** com a identificação em branco | Promessa e autoridade ficam; identificação troca | 1, 7 | `extract_moldes`, `list_moldes` |
| 28 | **Gerador dos 5 ângulos** | Para cada molde, gera 1 título por ângulo: inverso, público excluído, teste em 1ª pessoa, outro medo, outro nicho | Obrigatório gerar os 5 | 1 | `generate_titles` |
| 29 | **Preenchedor de esqueleto** | Cruza o esqueleto com a lista de hábitos e gera 1 título por hábito | Só hábitos com fonte conferida | 7 | `generate_titles` |
| 30 | **Variador de finais com rodízio** | Gera finais alternativos e impede o mesmo final em vídeos seguidos | Lista de 6–10 finais ("eis o porquê", "isso revela…", "existe uma razão psicológica…", "você tem esses 5 traços"…) | 7 | `generate_titles` |
| 31 | **Gerador de gancho de identificação** | Aplica moldes como "Se você [sintoma/situação comum], seu corpo está te avisando" ao assunto vencedor | Só sintomas/situações com fonte | 5 | `generate_titles` |
| 32 | **Classificador 2×2 (os 4 caminhos)** | Diz se a ideia é **cópia** / **brecha de mercado** / **ângulo novo** / **brecha dupla** | Alerta vermelho em "cópia" | 2 | `judge` |
| 33 | **Travas anti-cópia** | (a) reprova **tradução literal** do original e sugere autoridade/referência local; (b) reprova **cópia disfarçada** (mesma identificação, só o final mudou); (c) avisa quando o hábito/tema **já tem dono** naquele idioma | Identificação troca SEMPRE; final é opcional | 1, 2, 7 | `judge` |
| 34 | **Verificador de dono por hábito e idioma** | Para cada título gerado, busca em EN/PT/ES/DE/IT e marca **livre / com dono**, com o maior vídeo e a data | Pesquisa vem antes do título | 7 | `discover` |

## Etapa 6 — Banco de brechas e prioridade
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 35 | **Banco de brechas nativo** | Canais por nicho, numerados, **uma ficha por outlier**, com os campos: canal, título (texto puro), views/tempo/views por mês, dono repetiu?, concorrentes, 3 títulos, 2 idiomas, 4 perguntas, situação, data da última conferência | Situação: na fila / produzindo / no ar / descartado | 5, 8 | `add_production`, `list_production`, `save_item` |
| 36 | **Fichas preenchidas automaticamente** | Ficha de outlier (aula 3), de mapeamento (aula 4), de medição (aula 5) e de estudo (aula 6) preenchidas e salvas no banco | — | 3–6 | `save_item` |
| 37 | **Verificador "o dono repetiu?"** | Lê os vídeos publicados depois do outlier e diz se algum repetiu o assunto/formato e quanto fez | Dono não repetiu = formato aberto | 8 | `channel` |
| 38 | **Placar de concorrência** | Resume a busca do título em **só cópia fraca** / **adaptados bem** / **canais fortes** | Alimenta a nota de prioridade | 8 | `opportunities` |
| 39 | **Nota de prioridade (0–9)** | Views/mês (≥ 100 mil = 3 · 30–100 mil = 2 · < 30 mil = 1) + dono não repetiu (2) + só cópia fraca (2 / adaptados 1 / fortes 0) + idioma livre (2 / candidato 1 / ocupado 0) | Fila ordenada pela nota | 8 | `judge` |
| 40 | **Lembrete de reconferência** | Ficha "na fila" há mais de 15 dias → reabrir o canal e reavaliar (dono passou a repetir? apareceram concorrentes?) | Brecha aberta hoje pode fechar no mês seguinte | 8 | `run_worker` |
| 41 | **Fluxo com retorno automático** | Garimpar → Dissecar → Mapear → Validar → Ocupar; se Validar achar o espaço ocupado, volta ao Mapear e sugere o próximo ângulo ou idioma | — | 2 | `navigate` |

## Etapa 7 — Medir o canal e decidir (insistir ou largar)
| # | Função | O que faz | Regra / limite | Aula | Base no UMBRA |
|---|---|---|---|---|---|
| 42 | **Painel de fase do canal** | Lê o nº de vídeos e o Alcance (impressões, CTR, views) e mostra a fase com a decisão | < 10 continua · 10–20 sem evolução = alerta · ~30 sem evolução = corta | 9 | — (precisa da API do YouTube Analytics) |
| 43 | **Diagnóstico automático** | Impressões ~0 → **assunto/brecha errada**; impressões altas + CTR < 2% → **título/capa**; parado 3 semanas + 30 vídeos → **cortar** | Régua do YouTube: metade fica entre 2% e 10% de CTR | 9 | — |
| 44 | **Detector de sinal** | Marca o vídeo com 3× ou mais a mediana do canal e sugere "faz mais do que deu certo", gerando novos títulos com o mesmo molde | Corte de 3× é sugestão (o curso não fixa) | 9 | `generate_titles` |
| 45 | **Reescritor de título/capa para vídeos no ar** | Com CTR baixo, gera novas versões com a fórmula de 3 peças e registra antes e depois | Trocar um de cada vez (título, depois capa), esperar 3–7 dias | 9 | `generate_titles` |
| 46 | **Ligação com o banco** | No alerta, destaca a próxima brecha da fila; no corte, move o canal para "descartado" com o aprendizado anotado | — | 9 | `list_production` |
| 47 | **Alerta anti-teimosia** | Canal com muitos vídeos, sem evolução e títulos copiados → "quantidade sem mudança é teimosia" | — | 9 | `judge` |
| 48 | **Registro do porquê** | Ao marcar um vídeo como sinal, pede qual peça explica o resultado (identificação, promessa, autoridade, capa) e guarda no molde | Repetir a peça, não o título | 9 | `extract_moldes` |

---

## Por onde começar (sugestão de ordem de desenvolvimento)
Se for implementar aos poucos, estas 10 funções entregam o método inteiro no básico:
1. **#1 Multiplicador** + **#2 Views/dia**: achar outliers de verdade.
2. **#3 Radar de vídeos frescos**: achar o que está quente agora.
3. **#8 Analisador de fila**: saber se a porta está aberta.
4. **#13 Busca multi-idioma**: achar a brecha de mercado.
5. **#27 Dissecador** + **#29 Preenchedor de esqueleto**: título pronto.
6. **#33 Travas anti-cópia** + **#34 Verificador de dono**: não cair na cópia.
7. **#35 Banco de brechas** + **#39 Nota de prioridade**: saber o que fazer primeiro.

Depois: Trends (#19), alerta de chegar primeiro (#16) e o painel do canal (#42–#43).
