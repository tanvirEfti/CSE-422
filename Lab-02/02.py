#Task01
import random
    
def chromo_func(loss,profit,size):
    dic={
        "loss":loss,
        "profit":profit,
        "size":size,       
    }
    return dic



def ini_popu(size):
    popu=[]
    for i in range (size):
        loss = random.randint(1, 99)
        profit = random.randint(1,99)
        trade = random.randint(1, 99)
        popu.append(chromo_func(loss,profit,trade))
    return popu

def encode_chromo(chromos):
    decode = ""
    for i, j in chromos.items():
        if len(str(j)) == 2:
            decode += str(j)
        else:
            decode += '0' + str(j)
    return decode

def fit(cap,chromos,change):
    loss = int(chromos[ : 2])
    profit = int(chromos[2 : 4])
    trade = int(chromos[4 : ])
    stored_capital=cap
    for i in change:
        investment = (cap * trade) / 100
        stored_capital -= investment
        if i > -(loss) and i < profit:
            investment += (investment * i) / 100
        else:
            if i < 0:
                investment += (investment * i) / 100
            else:
                investment += (investment * i) / 100
        stored_capital += investment

    return stored_capital - cap


def crossover(parent):
    child=[]
    random_split=random.randint(1,5)
    parent_1_part1=parent[0][:random_split]
    parent_1_part2=parent[0][random_split:]
    parent_2_part1=parent[1][:random_split]
    parent_2_part2=parent[1][random_split:]
    
    offspring_1=parent_1_part1 + parent_2_part2
    child.append(offspring_1)
    offspring_2=parent_2_part1 + parent_1_part2
    child.append(offspring_2)
    
    return child


   
def mutation(child,rate=0.05):
    mutated=[]

    for i in (child):
        s=int(i[0:2])
        p=int(i[2:4])
        t=int(i[4:])
         
        if random.random()<rate:
            choice=random.choice([s,p,t])
            if choice==s:
                s=random.randint(1,99)
            elif choice==p:
                p=random.randint(1,99)
            elif choice==t:
                t=random.randint(1,99)
        new = chromo_func(s,p,t)
        mutated.append(new)
    return mutated       
                
def genetic_algo(initial_capital, price_changed, population_size, generations):
    count = 0
    final_profit = 0
    best_sequence_chromo = ""
    population = ini_popu(population_size)
    task2_list =[]
    for i in population:
        task2_list.append(encode_chromo(i)) # population is in dictionary so, encode is used to convert it into string.
    
    while count < generations:
        ideal = {}
        highest_possible_profit = 0
        lst=[]
        lst2 = list((ideal.values()))
        
        for i in population:
            encode = encode_chromo(i)
            highest_possible_profit = fit(initial_capital, encode, price_changed)
            if highest_possible_profit > final_profit:
                final_profit = highest_possible_profit
                best_sequence_chromo = encode
            ideal[highest_possible_profit] = encode
        
        lst2 = list((ideal.values()))
        lst3 = []  # it will be iterated at the end
        
        while len(lst3) < population_size:
                if len(lst2) >= 2:
                    lst= random.sample(lst2, 2) 
                    crossover_val = crossover(lst)
                    mutated_list = mutation(crossover_val)
                    
                
                for k in mutated_list:
                    mutatuion_string = encode_chromo(k)
                    loss = int(mutatuion_string[:2])
                    profit = int(mutatuion_string[2:4])
                    trade = int(mutatuion_string[4:])
                    
                    final_dict = chromo_func(loss, profit, trade)   
                    lst3.append(final_dict)

        population = lst3
        count += 1

    print(f"Best Strategy:")
    print(f"Stop_Loss: {best_sequence_chromo[:2]}, Take_Profit: {best_sequence_chromo[2:4]}, Trade_Size: {best_sequence_chromo[4:]}")
    print(f"Final Profit: {final_profit}")
    
    return task2_list #For task 2 only

    

        

initial_capital = 1000
population_size = 4
generations = 10
price_changes = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
result = genetic_algo(initial_capital, price_changes, population_size, generations)


#Task02

def multipoint_crossover(parent):
    child1=""
    child2=""
    lst=[]
    
    point1=random.randint(1,len(parent[0])-2)
    point2=random.randint(point1+1,len(parent[0])-1)
    
    offspring1_1=parent[0][:point1]
    offspring1_2=parent[0][point1:point2:]
    offspring1_3=parent[0][point2:]
    
    offspring2_1=parent[1][:point1]
    offspring2_2=parent[1][point1:point2:]
    offspring2_3=parent[1][point2:]
    
    child1+=offspring1_1+offspring2_2+offspring1_3
    child2+=offspring2_1+offspring1_2+offspring2_3
    
    lst.append(child1)
    lst.append(child2)  
    return(lst)

task2_call=random.sample(result,2)
crossover_val_multipoint = multipoint_crossover(task2_call)
print(f"After doing multipoint crossover, new offsprings are: {crossover_val_multipoint[0]}, {crossover_val_multipoint[1]}")




