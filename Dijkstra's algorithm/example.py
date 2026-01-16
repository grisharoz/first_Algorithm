import math

#creating graph hash table
graph={}
graph['beginning']={}
graph['beginning']['a']=6
graph['beginning']['b']=2
print(list(graph['beginning'].keys())) #finding all neighbours

#what ist the weight of a's neighbours (find it)
graph['a']={}
graph['a']['final']=1

#what ist the weight of b's neighbours (find it)
graph['b']={}
graph['b']['a']=3
graph['b']['end']=5
graph['end']={}

#creating costs hash table
infinity=math.inf
costs={}
costs['a']=6
costs['b']=2
costs['final']=infinity

#creating parents hash table
parents={}
parents['a']='beginning'
parents['b']='beginning'
parents['final']=None

proceed=set() #already used nodes

#creating function of finding lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost=infinity #costs are endless
    lowest_cost_node=None
    for node in costs:
        if cost[node]<lowest_cost and node in proceed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

node=find_lowest_cost_node(costs)
while node!=None:
    cost=costs[node]
    neighbours=graph[node]
    for n in neighbours.keys():
        new_cost=cost+neighbours[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    proceed.add(node)
    node=find_lowest_cost_node(costs)

