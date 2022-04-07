from collections import deque
 
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # 모든 노드에 대해 동일한 값을 갖는 휴리스틱 함수.
    def h(self, n):
        H = {
            'Elevator(82CB)': 1,
            'ML401(862F)': 1,
            'ML402(844B)': 1,
            'ML402_corner(8262)': 1,
            'ML403_corner(85C3)': 1,
            'ML403(819D)': 1,
            'ML416(81ED)': 1,
            'ML415(8603)': 1
        }
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):

        open_lst = set([start])  # 방문한 적이 있는 노드 목록(이웃이 항상 검사되는 것은 아님)
                                 # start부터 시작됨.                                    
        closed_lst = set([])  # 방문한 노드의 목록(이웃은 항상 검사 완료됨.)
 
        poo = {}  # 시작부터 다른 모든 노드 까지의 현재 거리를 갖고 있음.
                  # 기본 값은 +무한대 임.
        poo[start] = 0
 
        par = {}  # 모든 노드의 adjac 매핑을 포함함.
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # f()값이 가장 낮은 노드를 찾는다
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return None
 
            if n == stop:   # 만약 현재 노드가 stop인 경우 처음부터 다시시작함.
                reconst_path = []  
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # 현재 노드의 모든 이웃에 대해 수행함.
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:  # 현재 노드가 open_lst와 closed_lst 두 곳에 모두 존재하지 않는 경우
                    open_lst.add(m)                          #현재 노드를 open_lst에 추가함. 
                    par[m] = n
                    poo[m] = poo[n] + weight
               
               #그렇지 않으면 먼저 n을 방문한 다음 m을 방문하는 것이 더 빠른지 확인함.
                else:  
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n        # 만약 그렇다면 par 데이터와 poo 데이터를 업데이트 함.
 
                        if m in closed_lst:  # 노드가 closed_lst에 있으면 open_lst로 이동.
                            closed_lst.remove(m)
                            open_lst.add(m)
                            
            open_lst.remove(n)  #open_lst에서 n을 제거하고 closed_lst에 추가함.(그것의 이웃은 모두 검사완료된 상태.)
            closed_lst.add(n)   
 
        print('Path does not exist!')
        return None

# B-F 최단경로
adjac_lis = {
    'Elevator(82CB)': [('ML403_corner(85C3)', 780)],
    'ML401(862F)': [('ML402(844B)', 570), ('ML416(81ED)', 430)],
    'ML402(844B)': [('ML402_corner(8262)', 120), ('ML416(81ED)', 320)],
    'ML402_corner(8262)': [('Elevator(82CB)', 450), ('ML403_corner(85C3)', 680), ('ML415(8603)', 890)],
    'ML403_corner(85C3)': [('ML403(819D)', 400), ('ML415(8603)', 310)],
    'ML416(81ED)': [('ML403_corner(85C3)', 1040), ('ML415(8603)', 975)],
    'ML415(8603)': [('ML403_corner(85C3)', 310), ('ML403(819D)', 300)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('ML401(862F)', 'ML403(819D)')


'''
# A-G 최단경로
adjac_lis = {
    'Elevator(82CB)': [('ML402_corner(8262)', 450), ('ML403_corner(85C3)', 780)],
    'ML401(862F)': [('G', 430)],
    'ML402(844B)': [('ML401(862F)', 570), ('ML416(81ED)', 320)],
    'ML402_corner(8262)': [('ML402(844B)', 120), ('ML416(81ED)', 400)],
    'ML403_corner(85C3)': [('ML403(819D)', 400), ('H', 310), ('ML416(81ED)', 1040)],
    'ML403(819D)': [('ML415(8603)', 300)],
    'ML415(8603)': [('ML416(81ED)', 975)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('Elevator(82CB)', 'ML416(81ED)')
'''
