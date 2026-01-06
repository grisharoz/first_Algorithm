from collections import deque
graph={}
graph['you']=['Alice','Bob','Carol']
graph['Alice']=['Mike','Tom']
graph['Bob']=['Tobias','Lukas']
graph['Carol']=['Rob']
graph['Mike']=[]
graph['Tom']=[]
graph['Tobias']=[]
graph['Lukas']=[]
graph['Rob']=[]

search_queue=deque() #create neu queue
search_queue+=graph['you'] #all neighbours include in the search