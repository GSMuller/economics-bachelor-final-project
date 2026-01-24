# Descentralização Monetária Pós-Bretton Woods: Derivativos, Blockchain e Ancoragem Sintética

Este repositório contém o arcabouço teórico e a análise documental para um Trabalho de Conclusão de Curso em Economia sobre a descentralização monetária após o fim de Bretton Woods (1971), examinando como derivativos financeiros funcionam como mecanismos sintéticos de ancoragem monetária na ausência do padrão-ouro, com foco especial em blockchain, Bitcoin e protocolos DeFi.

**Área do Conhecimento:** Macroeconomia e Desenvolvimento Socioeconômico  
**Modalidade:** Pesquisa Teórico-Analítica (Bibliográfica/Documental)

---

## Questão de Pesquisa

**Como derivativos financeiros e tecnologias descentralizadas (blockchain/DeFi) emergiram como substitutos funcionais do padrão-ouro na coordenação monetária internacional após 1971?**

### Argumento Central

Derivativos financeiros emergiram como substitutos funcionais do padrão-ouro, criando ancoragem sintética através de coordenação de mercado, com blockchain/DeFi representando a próxima evolução desse processo de descentralização monetária.

###Abordagem Metodológica

### Natureza da Pesquisa
**Qualitativa com elementos quantitativos**
- Revisão bibliográfica sistemática
- Análise documental (acordos internacionais, relatórios de bancos centrais)
- Análise comparativa de sistemas monetários
- Objetivos: Exploratória, descritiva e explicativa

### Dados e Fontes

**Dados Históricos:**
- Séries históricas de volumes de derivativos (BIS - Bank for International Settlements)
- Volatilidade cambial pré/pós-Bretton Woods (1960-1990)
- Documentação de acordos internacionais (Acordos de Bretton Woods, Nixon Shock)

**Dados Contemporâneos:**
- TVL (Total Value Locked) em protocolos DeFi
- Capitalização de mercado Bitcoin e principais criptomoedas
- Volumes de stablecoins e contratos inteligentes
- Relatórios técnicos de protocolos blockchain

### Estratégia de Análise

1. **Revisão Histórica**  
   Sistema de Bretton Woods → Nixon Shock (1971) → Emergência dos derivativos

2. *DOCS/
│   ├── Cronograma-TCC.pdf          # Cronograma de execução
│   └── Referencias-Preliminares.md # Bibliografia inicial
├── Papers/
│   ├── bretton-woods/              # Literatura sobre Bretton Woods
│   ├── derivatives/                # Teoria de derivativos
│   ├── blockchain/                 # Blockchain e criptomoedas
│   └── defi/                       # Finanças descentralizadas
├── data/
│   ├── historical/
│   │   ├── bis_derivatives/        # Dados BIS de derivativos
│   │   ├── exchange_rates/         # Taxas de câmbio históricas
│   │   └── monetary_agreements/    # Documentos de acordos monetários
│   └── contemporary/
│       ├── defi_tvl/               # Total Value Locked em DeFi
│       ├── crypto_market/          # Dados de criptomoedas
│       └── stablecoins/            # Dados de stablecoins
├── notebooks/
│   ├── 01_historical_analysis.ipynb     # Análise do período Bretton Woods
│   ├── 02_derivatives_evolution.ipynb   # Evolução dos derivativos
│   ├── 03_blockchain_analysis.ipynb     # Análise de blockchain/Bitcoin
│   ├── 04_defi_protocols.ipynb          # Protocolos DeFi
│   └── 05_comparative_synthesis.ipynb   # Síntese comparativa
├── src/
│   ├── __init__.py
│   ├── config.py                   # Configurações e constantes
│   ├── data_collection.py          # Coleta de dados (APIs, web scraping)
│   ├── historical_analysis.py      # Análise histórica
│   ├── defi_analysis.py            # Análise de protocolos DeFi
│   └── visualization.py            # Gráficos e visualizações
├── outputs/
│   ├── figures/                    # Gráficos e visualizações
│   ├── tables/                     # Tabelas analíticas
│   └── reports/                    # Relatórios intermediários
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Estrutura Proposta do Trabalho

### Capítulo 1: Introdução
- Contextualização histórica
- Problema de pesquisa
- Objetivos e justificativa

### Capítulo 2: Bretton Woods e o Padrão-Ouro
- Sistema de Bretton Woods (1944-1971)
- Nixon Shock e o fim da conversibilidade
- Consequências macroeconômicas da descentralização

### Capítulo 3: Derivativos como Ancoragem Sintética
- Teoria de derivativos financeiros
- Evolução do mercado de derivativos (1970-2020)
- Mecanismos de coordenação e gestão de risco

### Capítulo 4: Blockchain e Descentralização Monetária
- Fundamentos de blockchain e criptomoedas
- Bitcoin como reserva de valor descentralizada
- Protocolos DeFi e stablecoins

### Capítulo 5: Análise Comparativa
- Padrão-ouro vs. Derivativos vs. Blockchain
- Mecanismos de ancoragem monetária
- Coordenação entre agentes econômicos

### Capítulo 6: Conclusões
- Síntese dos achados
- Implicações teóricas e práticas
- Limitações e agenda de pesquisa futura

---

## Principais Referências Teóricas

- **Teoria Monetária Internacional:** Mundell, Krugman, Obstfeld
- **Sistema de Bretton Woods:** Bordo, Eichengreen
- **Derivativos Financeiros:** Hull, Black-Scholes, Merton
- **Blockchain e Criptomoedas:** Nakamoto, Buterin, Szabo
- **DeFi:** Schär, Harvey, Ramachandran & Santoro
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
