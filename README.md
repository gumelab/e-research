# 📊 e-Research

**e-Research** é uma suíte de ferramentas para coleta, limpeza, estruturação e análise de dados provenientes de plataformas digitais como Google, YouTube e X (antigo Twitter). Foi desenvolvido para facilitar pesquisas computacionais em ciências humanas e sociais digitais, com foco na análise de narrativas, padrões de engajamento e redes discursivas.

---

## 🧱 Estrutura do Projeto

O repositório está organizado em três módulos principais, cada um com scripts e notebooks próprios:

```
e-research/
├── Custon Search Google/
│   ├── DataCleaning1.ipynb
│   └── Search/
│       ├── GoogleSearchEngine.ipynb
│       ├── *.xlsx (planilhas temáticas)
│
├── Youtube Data API/
│   ├── BancoDadosYoutube.ipynb
│   ├── Subpastas por tarefa (1-Search, 2-DataCleaning1, etc.)
│   ├── ModeladoTemas/
│   │   └── TopicModeling.ipynb
│   └── Histogramas-WordClouds/
│       └── DataAnalysis.ipynb
│
└── X (Twitter)/
    ├── data collection/
    │   ├── constants.py
    │   └── routines.py
    └── analysis/
        ├── maps.py
        ├── wordclouds.py
        └── networks from twitter.ipynb
```

---

## 🔍 Módulo 1: Google Custom Search

Este módulo realiza **buscas automatizadas no Google** com base em categorias definidas (ex: "Dignity", "Narcos", "Los80"). Ele inclui:

- 📁 `Search/`: planilhas com categorias de busca e notebook `GoogleSearchEngine.ipynb` para consultas via API.
- 📓 `DataCleaning1.ipynb`: notebook de limpeza e preparação dos dados coletados.

---

## 📺 Módulo 2: YouTube Data API

Este é o módulo mais extenso. Permite **coletar e estruturar dados de vídeos, canais, comentários e metadados** do YouTube.

- 📥 **Coleta de dados**: notebooks para busca de vídeos (`1-Search`), playlists, canais e comentários.
- 🧹 **Limpeza e fusão de dados**: notebooks como `DataCleaning1.ipynb`, `UnionDatos.ipynb`.
- 🧠 **Análises avançadas**:
  - `Similaridad.ipynb` (cosseno),
  - `SimilaridadLevenshtein.ipynb`,
  - `Filtro.ipynb` (filtragem específica),
  - `TopicModeling.ipynb` (modelagem de temas com LDA ou BERTopic),
  - `DataAnalysis.ipynb` (visualizações com histogramas e nuvens de palavras).

---

## 🐦 Módulo 3: X (Twitter)

Ferramentas para **coleta de tweets, análise textual e geração de visualizações**:

- 📥 `data collection/`: `constants.py` e `routines.py` para conexão com a API e coleta estruturada.
- 📊 `analysis/`:
  - `wordclouds.py`: geração de nuvens de palavras.
  - `maps.py`: visualização geográfica (quando aplicável).
  - `networks from twitter.ipynb`: análise de redes e interações.

---

## 🛠 Requisitos

Você precisará de:

- Python 3.8+
- Jupyter Notebook
- Bibliotecas como:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`
  - `tweepy`, `google-api-python-client`, `nltk`, `scikit-learn`
  - `wordcloud`, `networkx`, `gensim`, `openpyxl`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🧾 Licença

Este projeto é distribuído sob a [GNU](LICENSE).

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

---

## 📬 Contato

https://www.gumelab.net/
