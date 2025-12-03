# Sistema de Grafos - Rotas de Cidades 🗺️

**Disciplina:** Estrutura de Dados  
**Professor:** Anderson Soares  
**Autor:** [João Pedro Balduino Leitão]  

---

## 📹 Vídeo Demonstrativo

**Link do vídeo:** [https://www.youtube.com/watch?v=V4mlKvZ3hW0]

O vídeo demonstra:
- ✅ Execução da interface gráfica Streamlit
- ✅ Todas as operações básicas (adicionar/remover vértices e arestas)
- ✅ Execução dos 4 algoritmos (BFS, DFS, Dijkstra, Bellman-Ford)
- ✅ Explicação das decisões de implementação
- ✅ Visualização do código-fonte

**Duração:** 2-5 minutos
---

## 📋 Descrição do Projeto

Este projeto implementa uma estrutura de dados de **Grafo** com aplicação prática em um sistema de **rotas de cidades**. O sistema permite gerenciar cidades (vértices) e rotas (arestas) entre elas, além de executar algoritmos clássicos de grafos para busca e otimização de caminhos.

### Problema Resolvido
Simular um sistema de rotas entre cidades brasileiras, calculando:
- Menor caminho entre duas cidades (Dijkstra)
- Ordem de visitação (BFS e DFS)
- Detecção de ciclos negativos em rotas (Bellman-Ford)

---

## 🚀 Funcionalidades Implementadas

### ✅ Requisitos Mínimos 
- [x] Representação do grafo usando **lista de adjacência**
- [x] Adicionar vértice (cidade)
- [x] Remover vértice (cidade)
- [x] Adicionar aresta direcionada (rota) com peso (distância)
- [x] Remover aresta (rota)
- [x] Exibir o grafo em formato textual
- [x] Caso de uso: Sistema de rotas de cidades

### ✅ Funcionalidades Avançadas 

#### Algoritmos Clássicos Implementados:
1. **BFS (Busca em Largura)**
   - Apresenta ordem de visita
   - Calcula níveis de cada vértice
   - Encontra caminhos mínimos em termos de número de arestas

2. **DFS (Busca em Profundidade)**
   - Apresenta ordem de visita em profundidade
   - Útil para detectar componentes conexos

3. **Dijkstra**
   - Calcula o menor caminho entre dois vértices
   - Funciona com pesos não-negativos
   - Exibe o caminho completo e distância total

4. **Bellman-Ford**
   - Calcula distâncias a partir de um vértice
   - Detecta ciclos negativos no grafo
   - Funciona com pesos negativos

### ✅ Bônus
- [x] **Interface gráfica com Streamlit**
  - Visualização interativa do grafo
  - Execução de algoritmos com um clique
  - Gerenciamento visual de vértices e arestas
  - Log de operações em tempo real

---

## 💻 Tecnologias Utilizadas

- **Linguagem:** Python 3.8+
- **Interface Gráfica:** Streamlit 1.28+
- **Visualização de Dados:** Pandas 2.0+
- **Estruturas de dados:** 
  - `defaultdict` para lista de adjacência
  - `deque` para BFS
  - `heapq` para fila de prioridade no Dijkstra
  - `set` para controle de vértices visitados

---

## 📦 Estrutura do Projeto
```
trabalho-grafos/
│
├── src/
│   ├── graph.py          # Classe Graph com todas as operações
│   └── main.py           # Programa principal com menu interativo (terminal)
│
├── app.py                # Interface gráfica com Streamlit
├── requirements.txt      # Dependências do projeto
├── README.md             # Este arquivo
└── .gitignore           # Arquivos ignorados pelo Git
```

---

## 🎮 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes Python)

### Opção 1: Interface Gráfica com Streamlit (RECOMENDADO) 🎨

**Passo 1:** Clone o repositório
```bash
git clone [URL-DO-SEU-REPOSITORIO]
cd trabalho-grafos
```

**Passo 2:** Crie um ambiente virtual (Linux/Mac)
```bash
python3 -m venv venv
source venv/bin/activate
```

Ou no Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

**Passo 3:** Instale as dependências
```bash
pip install -r requirements.txt
```

**Passo 4:** Execute a interface gráfica
```bash
streamlit run app.py
```

A interface abrirá automaticamente no navegador em `http://localhost:8501`

**Funcionalidades da interface:**
- 📦 Carregar exemplo com cidades brasileiras
- ➕ Adicionar e remover cidades (vértices)
- 🛣️ Adicionar e remover rotas (arestas)
- 🔍 Executar todos os algoritmos (BFS, DFS, Dijkstra, Bellman-Ford)
- 📊 Visualizar o grafo completo em tabelas
- 📝 Acompanhar log de operações

---

### Opção 2: Programa em Terminal 💻

Execute o programa com menu interativo:
```bash
python src/main.py
```

**Menu disponível:**
- Adicionar/remover cidades
- Adicionar/remover rotas
- Executar algoritmos
- Visualizar grafo
- Carregar exemplo pré-configurado

---

## 📝 Exemplos de Uso

### Exemplo 1: Usando a Interface Streamlit

1. Execute `streamlit run app.py`
2. Clique em "📦 Carregar Exemplo"
3. Selecione "Dijkstra - Menor Caminho"
4. Escolha: Origem = São Paulo, Destino = Salvador
5. Clique em "▶️ Executar Algoritmo"

**Resultado:**
```
Caminho: São Paulo → Brasília → Salvador
Distância total: 2074.00 km
```

### Exemplo 2: Usando o Terminal
```
Escolha uma opção: 10
✓ Exemplo de cidades brasileiras carregado!

Escolha uma opção: 8
Cidade de origem: São Paulo
Cidade de destino: Salvador

🎯 Dijkstra: São Paulo → Salvador
Caminho: São Paulo → Brasília → Salvador
Distância total: 2074.00 km
```

### Exemplo 3: Busca em Largura (BFS)
```
📍 BFS a partir de 'São Paulo':
Ordem de visita: São Paulo → Belo Horizonte → Brasília → Curitiba → Rio de Janeiro → Salvador → Fortaleza

Níveis:
  São Paulo: nível 0
  Belo Horizonte: nível 1
  Brasília: nível 1
  Curitiba: nível 1
  Rio de Janeiro: nível 1
  Salvador: nível 2
  Fortaleza: nível 2
```

---

## 🎯 Decisões de Implementação

### Por que Lista de Adjacência?
- **Eficiência:** Melhor para grafos esparsos (poucas arestas)
- **Memória:** O(V + E) vs O(V²) da matriz de adjacência
- **Flexibilidade:** Fácil adicionar/remover arestas dinamicamente
- **Performance:** Iteração mais rápida sobre vizinhos

### Por que Grafo Direcionado?
- Rotas entre cidades geralmente têm direção (origem → destino)
- Permite modelar situações reais (mão única, pedágios, etc.)
- Mais flexível: pode simular não-direcionado adicionando arestas nos dois sentidos
- Realista para o domínio de rotas de cidades

### Estruturas de Dados Escolhidas
- **`defaultdict(list)`:** Lista de adjacência eficiente com inicialização automática
- **`set`:** Busca O(1) para verificar existência de vértices
- **`heapq`:** Fila de prioridade para Dijkstra (min-heap)
- **`deque`:** Fila eficiente para BFS com O(1) em ambas as pontas

### Complexidade dos Algoritmos
- **BFS:** O(V + E) - tempo e espaço
- **DFS:** O(V + E) - tempo e espaço
- **Dijkstra:** O((V + E) log V) - com heap binário
- **Bellman-Ford:** O(V × E) - tempo

---
## 🛠️ Dependências
```txt
streamlit>=1.28.0
pandas>=2.0.0
```

Instalação:
```bash
pip install -r requirements.txt
```

---

## 📄 Licença e Autoria

**Autor:** [João Pedro Balduino Leitão]  
**Instituição:** [UNIFSA]  
**Disciplina:** Estrutura de Dados  
**Professor:** Anderson Soares  
**Data de Entrega:** 05/12/2025

---

## 📚 Referências

- Cormen, T. H., et al. "Introduction to Algorithms" (3rd Edition)
- Documentação Python: https://docs.python.org/3/
- Documentação Streamlit: https://docs.streamlit.io/
- Algoritmos de Grafos: Material da disciplina

---
