# dfs.py

# 0. 그래프 생성
myGraph = graph = {'A':['B','C','D'], 
         'B':['A','E'], 
         'C':['A','F','G'], 
         'D':['A','H'], 
         'E':['B','I'], 
         'F':['C','J'],
         'G':['C'],
         'H':['D'], 
         'I':['E'], 
         'J':['F']}

# 0. 함수로 정의해서 그래프와 시작노드 입력 받기
def my_dfs(graph, start_node):

    # 1. 탐색할 노드를 담을 스택 자료형 생성
    stack = list() # 빈 리스트(스택) 생성

    # 2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
    visited = list() # 방문 확인용 리스트

    # 3. 탐색 시작 노드(첫번째 노드)를 스택에 삽입
    stack.append(start_node)

    while stack: # 6. "stack에 방문할 노드가 남지 않을때까지" 라는 뜻

        # 4.방문할 노드를 스택에서 하나씩 꺼내기
        node = stack.pop()

        # 5. 스택에서 꺼낸 노드가 방문한 노드가 아니면, 그 인접 노드를 스택에 삽입하고 방문 처리
        if node not in visited:
            visited.append(node) # 방문 처리
            stack.extend(reversed(graph[node])) # 인접 노드를 스택에 삽입 / 한 번에 여러 인접 노드를 스택에 삽입하기 위해 append 대신 extend 사용
    
    print(f"dfs - {visited}")
    return visited # 모든 노드가 있어야 함

# 6. 스택에 방문할 노드가 남지 않을때까지 3~5의 과정 반복
# while 문 사용

my_dfs(myGraph, 'B')