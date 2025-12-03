"""
Interface Gráfica com Streamlit
Sistema de Grafos + Algoritmo de Dijkstra

Autor: [João Pedro Balduino Leitão]
"""

import streamlit as st
from src.graph import Graph
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Sistema de Grafos - Dijkstra",
    page_icon="🗺️",
    layout="wide"
)

# Inicializar o grafo na sessão
if 'graph' not in st.session_state:
    st.session_state.graph = Graph(directed=True)
    st.session_state.log = []

def add_log(message):
    """Adiciona mensagem ao log."""
    st.session_state.log.append(message)

def load_example():
    """Carrega exemplo de cidades brasileiras."""
    graph = st.session_state.graph
    
    cities = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte",
        "Brasília", "Salvador", "Curitiba", "Fortaleza"
    ]
    
    routes = [
        ("São Paulo", "Rio de Janeiro", 430),
        ("São Paulo", "Belo Horizonte", 586),
        ("São Paulo", "Curitiba", 408),
        ("Rio de Janeiro", "Belo Horizonte", 434),
        ("Belo Horizonte", "Brasília", 716),
        ("Brasília", "Salvador", 1059),
        ("Brasília", "Fortaleza", 1687),
        ("São Paulo", "Brasília", 1015),
        ("Salvador", "Fortaleza", 1075)
    ]
    
    for city in cities:
        graph.add_vertex(city)
    
    for origin, destination, distance in routes:
        graph.add_edge(origin, destination, distance)
    
    add_log(f"✅ Exemplo carregado: {len(cities)} cidades e {len(routes)} rotas")
    st.success(f"Exemplo carregado! {len(cities)} cidades e {len(routes)} rotas adicionadas.")

# Header
st.title("🗺️ Sistema de Grafos + Dijkstra")
st.markdown("""
**Trabalho de Estrutura de Dados - Prof. Anderson Soares**

**📋 Avaliação:**
- 📊 **Parte 1:** Grafo Genérico 
- 🎯 **Parte 2:** Algoritmo de Dijkstra 
""")
st.divider()

# Botões principais
col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    if st.button("📦 Carregar Exemplo", use_container_width=True):
        load_example()
        st.rerun()

with col2:
    if st.button("🗑️ Limpar Grafo", use_container_width=True):
        st.session_state.graph = Graph(directed=True)
        st.session_state.log = []
        st.success("Grafo limpo!")
        st.rerun()

st.divider()

# Layout principal em 2 colunas
col_left, col_right = st.columns([1, 1])

# ==================== COLUNA ESQUERDA - PARTE 1: GRAFO GENÉRICO ====================
with col_left:
    st.subheader("📊 PARTE 1: Grafo Genérico")
    
    # Adicionar vértices
    st.markdown("##### 📍 Gerenciar Vértices (Cidades)")
    with st.form("add_vertex_form"):
        new_vertex = st.text_input("Nome da cidade:")
        submit_vertex = st.form_submit_button("➕ Adicionar Cidade", use_container_width=True)
        
        if submit_vertex and new_vertex:
            if st.session_state.graph.add_vertex(new_vertex):
                add_log(f"✅ Cidade '{new_vertex}' adicionada")
                st.success(f"Cidade '{new_vertex}' adicionada!")
                st.rerun()
    
    # Listar vértices
    if st.session_state.graph.vertices:
        st.write("**Cidades cadastradas:**")
        vertices_list = sorted(list(st.session_state.graph.vertices))
        
        for vertex in vertices_list:
            col_v1, col_v2 = st.columns([3, 1])
            with col_v1:
                st.write(f"• {vertex}")
            with col_v2:
                if st.button("🗑️", key=f"del_v_{vertex}"):
                    st.session_state.graph.remove_vertex(vertex)
                    add_log(f"❌ Cidade '{vertex}' removida")
                    st.rerun()
    else:
        st.info("Nenhuma cidade cadastrada ainda.")
    
    st.divider()
    
    # Adicionar arestas
    st.markdown("##### 🛣️ Gerenciar Arestas (Rotas)")
    
    if len(st.session_state.graph.vertices) >= 2:
        with st.form("add_edge_form"):
            vertices_list = sorted(list(st.session_state.graph.vertices))
            
            col_e1, col_e2, col_e3 = st.columns(3)
            
            with col_e1:
                from_vertex = st.selectbox("Origem:", vertices_list, key="from")
            
            with col_e2:
                to_vertex = st.selectbox("Destino:", vertices_list, key="to")
            
            with col_e3:
                weight = st.number_input("Distância (km):", min_value=1, value=100)
            
            submit_edge = st.form_submit_button("➕ Adicionar Rota", use_container_width=True)
            
            if submit_edge:
                if from_vertex != to_vertex:
                    st.session_state.graph.add_edge(from_vertex, to_vertex, weight)
                    add_log(f"✅ Rota {from_vertex} → {to_vertex} ({weight}km) adicionada")
                    st.success(f"Rota adicionada: {from_vertex} → {to_vertex} ({weight}km)")
                    st.rerun()
                else:
                    st.error("Origem e destino devem ser diferentes!")
    else:
        st.info("Adicione pelo menos 2 cidades para criar rotas.")
    
    # Listar arestas
    if st.session_state.graph.graph:
        st.write("**Rotas cadastradas:**")
        edges_data = []
        for vertex in sorted(st.session_state.graph.vertices):
            for neighbor, weight in st.session_state.graph.graph[vertex]:
                edges_data.append({
                    "Origem": vertex,
                    "Destino": neighbor,
                    "Distância": f"{weight}km"
                })
        
        if edges_data:
            df_edges = pd.DataFrame(edges_data)
            st.dataframe(df_edges, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhuma rota cadastrada ainda.")

# ==================== COLUNA DIREITA - PARTE 2: DIJKSTRA ====================
with col_right:
    st.subheader("🎯 PARTE 2: Algoritmo de Dijkstra")
    
    if len(st.session_state.graph.vertices) >= 2:
        vertices_list = sorted(list(st.session_state.graph.vertices))
        
        st.markdown("##### 🔍 Encontrar Menor Caminho")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            start_vertex = st.selectbox("Cidade de origem:", vertices_list, key="dijkstra_start")
        with col_d2:
            end_vertex = st.selectbox("Cidade de destino:", vertices_list, key="dijkstra_end")
        
        if st.button("▶️ Executar Dijkstra", use_container_width=True, type="primary"):
            result = st.session_state.graph.dijkstra(start_vertex, end_vertex)
            
            if result:
                st.markdown("---")
                if result['path']:
                    st.success("**✅ Caminho encontrado pelo Dijkstra!**")
                    
                    # Exibir caminho
                    st.markdown("**📍 Caminho:**")
                    st.info(" → ".join(result['path']))
                    
                    # Exibir distância total
                    st.markdown("**📏 Distância Total:**")
                    st.metric("Quilômetros", f"{result['distances'][end_vertex]:.2f} km")
                    
                    # Exibir detalhes do caminho
                    st.markdown("**📊 Detalhes do Caminho:**")
                    path_data = []
                    for i, city in enumerate(result['path']):
                        path_data.append({
                            "Etapa": i + 1,
                            "Cidade": city,
                            "Distância Acumulada": f"{result['distances'][city]:.2f} km"
                        })
                    df_path = pd.DataFrame(path_data)
                    st.dataframe(df_path, use_container_width=True, hide_index=True)
                    
                    add_log(f"🎯 Dijkstra: {start_vertex} → {end_vertex} = {result['distances'][end_vertex]:.2f}km")
                else:
                    st.warning("⚠️ Não há caminho entre as cidades selecionadas.")
                    add_log(f"⚠️ Dijkstra: Sem caminho de {start_vertex} para {end_vertex}")
        
        st.divider()
        
        # Visualizar grafo completo
        st.markdown("##### 📊 Visualização do Grafo")
        
        if st.button("👁️ Exibir Grafo Completo", use_container_width=True):
            st.write("**Tipo:** Grafo Direcionado")
            st.write(f"**Total de Vértices:** {len(st.session_state.graph.vertices)}")
            st.write(f"**Vértices:** {', '.join(sorted(st.session_state.graph.vertices))}")
            
            st.write("**Arestas:**")
            edges_data = []
            for vertex in sorted(st.session_state.graph.vertices):
                for neighbor, weight in st.session_state.graph.graph[vertex]:
                    edges_data.append({
                        "Origem": vertex,
                        "→": "→",
                        "Destino": neighbor,
                        "Peso (km)": weight
                    })
            
            if edges_data:
                df_all_edges = pd.DataFrame(edges_data)
                st.dataframe(df_all_edges, use_container_width=True, hide_index=True)
                st.write(f"**Total de Arestas:** {len(edges_data)}")
            else:
                st.info("Nenhuma aresta cadastrada.")
        
        st.divider()
        
        # Algoritmos extras (opcional)
        st.markdown("##### 🔬 Algoritmos Extras (Opcional)")
        
        extra_algo = st.selectbox(
            "Selecione um algoritmo extra:",
            ["", "BFS - Busca em Largura", "DFS - Busca em Profundidade"]
        )
        
        if extra_algo:
            extra_start = st.selectbox("Vértice inicial:", vertices_list, key="extra_start")
            
            if st.button(f"▶️ Executar {extra_algo}", use_container_width=True):
                if extra_algo == "BFS - Busca em Largura":
                    result = st.session_state.graph.bfs(extra_start)
                    if result:
                        st.success("**Resultado do BFS:**")
                        st.write(f"**Ordem de visita:** {' → '.join(result['order'])}")
                        st.write("**Níveis:**")
                        for city, level in sorted(result['levels'].items(), key=lambda x: x[1]):
                            st.write(f"  • {city}: nível {level}")
                        add_log(f"🔍 BFS executado a partir de '{extra_start}'")
                
                elif extra_algo == "DFS - Busca em Profundidade":
                    result = st.session_state.graph.dfs(extra_start)
                    if result:
                        st.success("**Resultado do DFS:**")
                        st.write(f"**Ordem de visita:** {' → '.join(result)}")
                        add_log(f"🔍 DFS executado a partir de '{extra_start}'")
    
    else:
        st.info("📍 Adicione pelo menos 2 cidades para usar o Dijkstra.")
    
    st.divider()
    
    # Log de operações
    st.markdown("##### 📝 Log de Operações")
    
    if st.session_state.log:
        log_text = "\n".join(st.session_state.log[-10:])  # Últimas 10 operações
        st.text_area("", value=log_text, height=180, disabled=True)
    else:
        st.info("Nenhuma operação realizada ainda.")
