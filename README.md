# Mudança no Regime Monetário Pós-1971: Expectativas, Volatilidade e Comportamento dos Mercados

Este repositório contém o arcabouço teórico e a análise empírica para um Trabalho de Conclusão de Curso em Economia sobre como a mudança no regime monetário internacional após 1971 (fim de Bretton Woods / Choque Nixon) alterou as expectativas dos agentes, a volatilidade macroeconômica e o comportamento dos mercados financeiros.

---

## Questão de Pesquisa

**Como a mudança no regime monetário internacional pós-1971 afetou as expectativas e o comportamento econômico dos agentes?**

### Hipóteses Centrais
- **H1 — Volatilidade:** A volatilidade macro/financeira aumenta após 1971 (ex: câmbio, inflação, taxas de juros).
- **H2 — Expectativas:** Os preços tornam-se mais prospectivos e sensíveis a novas informações (maior variância, maior dependência do regime).
- **H3 — Quebra Estrutural:** As principais séries temporais apresentam quebras estruturais estatisticamente significativas em torno de 1971 (ou dentro de uma janela de transição curta).

---

## Visão Geral Metodológica

### Dados (candidatos típicos)
- Taxas de câmbio (índice USD ou taxas bilaterais principais)
- Inflação (IPC)
- Taxas de juros (taxa de política monetária / rendimentos de longo prazo)
- Preços de commodities (controle opcional)
- Produto / desemprego (controles macroeconômicos opcionais)

### Estratégia Empírica
1. **Comparação descritiva de regimes** (pré vs. pós 1971)
2. **Testes de quebra estrutural**  
   - Teste de Chow (quebra conhecida)
   - Bai–Perron / múltiplas quebras (quebras desconhecidas)
3. **Modelagem de volatilidade**  
   - Volatilidade móvel
   - Família ARCH/GARCH (se aplicável)
4. **Testes de robustez**  
   - Janelas alternativas de quebra (ex: 1969–1973)
   - Séries / países alternativos

---

## Estrutura do Repositório

```text
.
├── data/
│   ├── raw/                # Conjuntos de dados originais (não editar)
│   └── processed/          # Conjuntos de dados limpos/mesclados usados na análise
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_descriptive_analysis.ipynb
│   ├── 04_break_tests.ipynb
│   └── 05_volatility_models.ipynb
├── src/
│   ├── __init__.py
│   ├── config.py           # Caminhos, constantes, janelas de quebra
│   ├── utils.py            # Auxiliares (io, gráficos, transformações)
│   ├── cleaning.py         # Pipeline de limpeza de dados
│   ├── breaks.py           # Testes de quebra estrutural
│   └── volatility.py       # Estimação de volatilidade (rolling/GARCH)
├── outputs/
│   ├── figures/            # Gráficos exportados dos notebooks/scripts
│   └── tables/             # Tabelas de regressão, resultados de testes
├── requirements.txt
├── LICENSE
└── README.md
