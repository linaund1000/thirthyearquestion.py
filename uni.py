a = 1 
b = 2 
c = 3
t = 7

def get_number(a,b,c,t):
    d = {}
    
    def options_dic(x,y):
        options = {}
        options[x+y]= f'{x}+{y}'
        options[x-y]=f'{x}-{y}' 
        options[x*y]=f'{x}*{y}' 
        options[x/y]= f'{x}/{y}'
        return options
    
    d[a] = options_dic(b,c)

    d[b] = options_dic(a,c)

    d[c] = options_dic(b,a)

        
    for i in d.keys():
        for a in d[i]:
            
            if a+i == t:
                print(d[i][a])
                print(f'+{i}')
                return a+i
            elif a-i == t:
                print(d[i][a])
                print(f'-{i}')
                return a-i
            elif a*i == t:
                print(d[i][a])
                print(f'*{i}')
                return a*i
            elif a/i == t:
                print(d[i][a])
                print(f'/{i}')
                return a/i            
            
print(get_number(a,b,c,t))
