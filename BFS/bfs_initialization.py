from collections import deque
family_graph={} #creating graph
family_graph['Grisha']=['Andrey','Liana','Masha']
family_graph['Andrey']=['Eva','Peter',"Marina"]
family_graph['Liana']=["Max"]
family_graph['Masha']=[]
family_graph['Marina']=[]
family_graph['Eva']=[]
family_graph['Peter']=[]
family_graph['Max']=[]

#define which person is selling mango
def person_is_seller(name):
    return name[0]=="M"

#function for searching seller
def search(name):
    search_queue=deque()
    search_queue +=family_graph[name]
    searched=set() #for already checked people
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+' is selling mango')
                return True
            else:
                search_queue+=family_graph[person]
                searched.add(person)
    return False

search('Grisha')