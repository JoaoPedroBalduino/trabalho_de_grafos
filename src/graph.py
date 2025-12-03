from collections import deque, defaultdict
import heapq


class Graph:
    
    def __init__(self, directed=True):
        self.graph = defaultdict(list)  # Lista de adjacência: {vértice: [(vizinho, peso), ...]}
        self.vertices = set()  # Conjunto de vértices
        self.directed = directed
        
    # ==================== PARTE 1: OPERAÇÕES BÁSICAS DO GRAFO (7 pontos) ====================
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            if vertex not in self.graph:
                self.graph[vertex] = []
            print(f"✓ Vértice '{vertex}' adicionado.")
            return True
        print(f"✗ Vértice '{vertex}' já existe.")
        return False
    
    def remove_vertex(self, vertex):
        if vertex not in self.vertices:
            print(f"✗ Vértice '{vertex}' não encontrado.")
            return False
        
        # Remove o vértice do conjunto
        self.vertices.remove(vertex)
        
        # Remove todas as arestas que partem deste vértice
        if vertex in self.graph:
            del self.graph[vertex]
        
        # Remove todas as arestas que chegam neste vértice
        for v in self.graph:
            self.graph[v] = [(dest, weight) for dest, weight in self.graph[v] if dest != vertex]
        
        print(f"✓ Vértice '{vertex}' removido.")
        return True
    
    def add_edge(self, from_vertex, to_vertex, weight=1):
        # Adiciona vértices automaticamente se não existirem
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Adiciona aresta (origem -> destino)
        self.graph[from_vertex].append((to_vertex, weight))
        
        # Se não direcionado, adiciona aresta inversa (destino -> origem)
        if not self.directed:
            self.graph[to_vertex].append((from_vertex, weight))
        
        direction = "→" if self.directed else "↔"
        print(f"✓ Aresta {from_vertex} {direction} {to_vertex} (peso: {weight}) adicionada.")
        return True
    
    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            print(f"✗ Um dos vértices não existe.")
            return False
        
        # Remove aresta origem -> destino
        original_length = len(self.graph[from_vertex])
        self.graph[from_vertex] = [(dest, weight) for dest, weight in self.graph[from_vertex] 
                                    if dest != to_vertex]
        
        # Se não direcionado, remove aresta destino -> origem
        if not self.directed:
            self.graph[to_vertex] = [(dest, weight) for dest, weight in self.graph[to_vertex] 
                                      if dest != from_vertex]
        
        if len(self.graph[from_vertex]) < original_length:
            print(f"✓ Aresta {from_vertex} → {to_vertex} removida.")
            return True
        else:
            print(f"✗ Aresta não encontrada.")
            return False
    
    def display(self):
        print("\n" + "="*60)
        print(f"GRAFO {'DIRECIONADO' if self.directed else 'NÃO DIRECIONADO'}")
        print("="*60)
        
        if not self.vertices:
            print("Grafo vazio!")
            print("="*60 + "\n")
            return
        
        # Exibe vértices
        print(f"\n📍 Vértices ({len(self.vertices)}):")
        print(f"   {', '.join(sorted(str(v) for v in self.vertices))}")
        
        # Exibe arestas
        print(f"\n🔗 Arestas:")
        edge_count = 0
        for vertex in sorted(self.vertices):
            if self.graph[vertex]:
                for dest, weight in sorted(self.graph[vertex]):
                    arrow = "→" if self.directed else "↔"
                    print(f"   {vertex} {arrow} {dest} (peso: {weight})")
                    edge_count += 1
        
        if edge_count == 0:
            print("   Nenhuma aresta no grafo.")
        else:
            print(f"\n📊 Total: {len(self.vertices)} vértices, {edge_count} arestas")
        
        print("="*60 + "\n")
    
    def get_neighbors(self, vertex):
        if vertex not in self.vertices:
            return []
        return self.graph[vertex]
    
    def get_edge_weight(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices:
            return None
        
        for neighbor, weight in self.graph[from_vertex]:
            if neighbor == to_vertex:
                return weight
        return None
    
    # ====================  ALGORITMO DE DIJKSTRA  ====================
    
    def dijkstra(self, start_vertex, end_vertex=None):
        if start_vertex not in self.vertices:
            print(f"✗ Vértice inicial '{start_vertex}' não encontrado.")
            return None
        
        if end_vertex and end_vertex not in self.vertices:
            print(f"✗ Vértice final '{end_vertex}' não encontrado.")
            return None
        
        # Inicialização
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        # Fila de prioridade (min-heap): (distância, vértice)
        priority_queue = [(0, start_vertex)]
        visited = set()
        
        # Algoritmo principal
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Se já visitado, pular
            if current_vertex in visited:
                continue
            
            # Marcar como visitado
            visited.add(current_vertex)
            
            # Se encontrou o destino e só queremos um caminho específico, pode parar
            if end_vertex and current_vertex == end_vertex:
                break
            
            # Relaxamento das arestas (verificar vizinhos)
            for neighbor, weight in self.graph[current_vertex]:
                # Calcula nova distância
                new_distance = current_distance + weight
                
                # Se encontrou caminho mais curto, atualiza
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))
        
        # Reconstruir caminho se end_vertex foi especificado
        path = []
        if end_vertex:
            current = end_vertex
            while current is not None:
                path.insert(0, current)
                current = previous[current]
            
            # Se o primeiro vértice do caminho não é o inicial, não há caminho
            if path[0] != start_vertex:
                path = []
        
        return {
            'distances': distances,
            'previous': previous,
            'path': path if end_vertex else None
        }
    
    # ==================== ALGORITMOS EXTRAS (BÔNUS - Opcional) ====================
    
    def bfs(self, start_vertex):
        if start_vertex not in self.vertices:
            print(f"✗ Vértice '{start_vertex}' não encontrado.")
            return None
        
        visited = set()
        queue = deque([start_vertex])
        order = []
        levels = {start_vertex: 0}
        
        visited.add(start_vertex)
        
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            
            for neighbor, _ in sorted(self.graph[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    levels[neighbor] = levels[vertex] + 1
        
        return {
            'order': order,
            'levels': levels
        }
    
    def dfs(self, start_vertex):
        if start_vertex not in self.vertices:
            print(f"✗ Vértice '{start_vertex}' não encontrado.")
            return None
        
        visited = set()
        order = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            order.append(vertex)
            
            for neighbor, _ in sorted(self.graph[vertex]):
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_vertex)
        return order