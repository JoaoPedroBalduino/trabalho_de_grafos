"""
Programa Principal - Sistema de Rotas de Cidades
Demonstração de Grafo Genérico + Algoritmo de Dijkstra
"""

from graph import Graph


def print_menu():
    """Exibe o menu principal."""
    print("\n" + "="*60)
    print("  SISTEMA DE GRAFOS - ESTRUTURA DE DADOS")
    print("="*60)
    print("PARTE 1 - GRAFO GENÉRICO (7 pontos):")
    print("  1. Adicionar cidade (vértice)")
    print("  2. Remover cidade (vértice)")
    print("  3. Adicionar rota (aresta com peso)")
    print("  4. Remover rota (aresta)")
    print("  5. Exibir grafo completo")
    print("\nPARTE 2 - ALGORITMO DE DIJKSTRA (3 pontos):")
    print("  6. Executar Dijkstra (menor caminho)")
    print("\nOUTRAS OPÇÕES:")
    print("  7. Carregar exemplo de cidades brasileiras")
    print("  8. BFS - Busca em Largura (opcional)")
    print("  9. DFS - Busca em Profundidade (opcional)")
    print("  0. Sair")
    print("="*60)


def load_example(graph):
    """Carrega um exemplo de grafo com cidades brasileiras."""
    print("\n🔄 Carregando exemplo...")
    
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
    
    print(f"\n✅ Exemplo carregado com sucesso!")
    print(f"📍 {len(cities)} cidades adicionadas")
    print(f"🔗 {len(routes)} rotas adicionadas")


def main():
    """Função principal do programa."""
    print("\n" + "="*60)
    print("🗺️  SISTEMA DE GRAFOS - ROTAS DE CIDADES")
    print("="*60)
    print("Trabalho de Estrutura de Dados")
    print("Professor: Anderson Soares")
    print("\nAVALIAÇÃO:")
    print("- Parte 1: Grafo Genérico (7 pontos)")
    print("- Parte 2: Algoritmo de Dijkstra (3 pontos)")
    print("="*60)
    
    # Cria grafo direcionado
    graph = Graph(directed=True)
    
    while True:
        print_menu()
        choice = input("\n👉 Escolha uma opção: ").strip()
        
        # PARTE 1 - GRAFO GENÉRICO
        if choice == "1":
            city = input("📍 Nome da cidade: ").strip()
            if city:
                graph.add_vertex(city)
        
        elif choice == "2":
            city = input("🗑️  Nome da cidade a remover: ").strip()
            graph.remove_vertex(city)
        
        elif choice == "3":
            origin = input("📍 Cidade de origem: ").strip()
            destination = input("📍 Cidade de destino: ").strip()
            try:
                distance = float(input("📏 Distância em km: ").strip())
                graph.add_edge(origin, destination, distance)
            except ValueError:
                print("✗ Distância inválida! Use um número.")
        
        elif choice == "4":
            origin = input("📍 Cidade de origem: ").strip()
            destination = input("📍 Cidade de destino: ").strip()
            graph.remove_edge(origin, destination)
        
        elif choice == "5":
            graph.display()
        
        # PARTE 2 - DIJKSTRA
        elif choice == "6":
            if len(graph.vertices) < 2:
                print("\n✗ Adicione pelo menos 2 cidades primeiro!")
                continue
                
            print("\n" + "="*60)
            print("🎯 ALGORITMO DE DIJKSTRA - MENOR CAMINHO")
            print("="*60)
            start = input("📍 Cidade de origem: ").strip()
            end = input("📍 Cidade de destino: ").strip()
            
            result = graph.dijkstra(start, end)
            
            if result:
                print("\n" + "="*60)
                print("📊 RESULTADO DO DIJKSTRA")
                print("="*60)
                
                if result['path']:
                    print(f"\n✅ Caminho encontrado!")
                    print(f"📍 Rota: {' → '.join(result['path'])}")
                    print(f"📏 Distância total: {result['distances'][end]:.2f} km")
                    
                    # Mostra distâncias intermediárias
                    print(f"\n📊 Distâncias acumuladas:")
                    for i, city in enumerate(result['path']):
                        print(f"   {i+1}. {city}: {result['distances'][city]:.2f} km")
                else:
                    print("\n✗ Não há caminho entre as cidades informadas.")
                
                print("="*60)
        
        # OUTRAS OPÇÕES
        elif choice == "7":
            load_example(graph)
        
        elif choice == "8":
            start = input("📍 Cidade inicial para BFS: ").strip()
            result = graph.bfs(start)
            if result:
                print(f"\n📍 BFS a partir de '{start}':")
                print(f"Ordem de visita: {' → '.join(result['order'])}")
                print("\nNíveis:")
                for city, level in sorted(result['levels'].items(), key=lambda x: x[1]):
                    print(f"  {city}: nível {level}")
        
        elif choice == "9":
            start = input("📍 Cidade inicial para DFS: ").strip()
            result = graph.dfs(start)
            if result:
                print(f"\n📍 DFS a partir de '{start}':")
                print(f"Ordem de visita: {' → '.join(result)}")
        
        elif choice == "0":
            print("\n" + "="*60)
            print("👋 Encerrando o programa. Até logo!")
            print("="*60)
            break
        
        else:
            print("\n✗ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()