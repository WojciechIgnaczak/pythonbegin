# Algorytm Dijkstry - najkrotsza sciezka

mapa={
    "A":{'B':2,"D":4},
    "B":{'C':3,"D":3},
    "C":{'E':2},
    "D":{'C':3,"E":4},
    "E":{}
}


#ustaw najkrotsze odleglosci od wierzcholka
def algorytm_dijkstry(graph,start,goal):
    #wszystkie wezly oznacz jako nieodwiedzone, stworz zbior nieodwiedzonych wezlow
    
    #ustaw odleglosc wezla poczatkowego na 0 reszty na inf
    shortest_distance = {vortex: float('infinity') for vortex in graph}
    shortest_distance[start]=0
    predecessors={}
    #nieodwiedzone wierzcholki
    unvisited=graph.copy()
    
    # petle nieodwiedzonych wierzcholkow, sprawdzac petle o wierzcholku najmniejszej odleglosci
    #wierzcholek z najmniejsza odlegloscia 
    while unvisited:
        current_min_vortex=None
        for  vortex in unvisited:
            if current_min_vortex is None:
                current_min_vortex = vortex
            elif shortest_distance[vortex]< shortest_distance[current_min_vortex]:
                current_min_vortex = vortex
    #sprawdzanie wszystkich sasiadow aktualnego wierzcholka
        for neighbour,cost in graph[current_min_vortex].items():
            if cost + shortest_distance[current_min_vortex]< shortest_distance[neighbour]:
                shortest_distance[neighbour]=cost + shortest_distance[current_min_vortex]
                predecessors[neighbour]= current_min_vortex
    # usunac z listy przetworzony wierzcholek
        unvisited.pop(current_min_vortex)
    # odtworzenie sciezki od startu do celu
    current_vortex=goal
    path=[]
    while current_vortex !=start:
        path.append(current_vortex)
        current_vortex=predecessors[current_vortex]
    path.append(start)
    return path[::-1],shortest_distance[goal]

path, distance= algorytm_dijkstry(mapa,'A','E')
print(f"sciezka: {path}, dlugosc: {distance}")