def a_star(start,end,heu,adj):
    list=[]
    parent_node={}
    distance_node={}
    parent_node[start]=None
    distance_node[start]=0    
    heapq.heappush(list,(0,start))
    while list:
        current_loc=heapq.heappop(list)[1]
        if current_loc==end:
            break
        for i in adj[current_loc]:
            val=distance_node[current_loc] + int(adj[current_loc][i])
            if i not in distance_node or val< distance_node[i]:
                distance_node[i]=val
                total_val=int(heu[i])+val
                heapq.heappush(list,(total_val,i))
                parent_node[i]=current_loc
    return parent_node, distance_node   


def ad_dict(datas):
    heu={}
    adj={}
    for i in datas:
        read=i.split()
        heu[read[0]]=read[1]
        if read[0] not in adj:
            adj[read[0]]={}
        for j in range (2,len(read),2):
            adj[read[0]][read[j]]=read[j+1]
    return heu,adj
  
        
import heapq 
inputs=open("Lab-01\input.txt","r")
heuristic,adj=ad_dict(inputs)
start=input("Enter the starting destination:")
final="Bucharest"
if start and final in heuristic:
    path,value=a_star(start,final,heuristic,adj)
    back_path=[]
    back_path.append(final)
    child_node=final
    while child_node != start:
        prev_node=path[child_node]
        back_path.append(prev_node)
        child_node=prev_node
    if len(back_path)==0:
        print("No Path Found")
    else:
        back_path.reverse()
        for i in range (0,len(back_path)-1,1):
            print(f"{back_path[i]}->",end=" ")
        print(back_path[-1])
    print(f"Total Distance: {value[final]}")  
else:
    print("No Path Found")