def my_spliter(ls, c=' '):
    '''
    My spliter is my user-defined function for the implemntation of 
    Split function which performs splitting on the given string and 
    convert it into a list separted by space by default.i.e., if 
    no splitter is provided
    >>>my_splitter("Pluto is a planet")
       ['Pluto', 'is', 'a', 'planet']
    >>>my_splitter("18/10/1990","/")
       ['18', '10', '1990']
    '''
    resultant = []
    st = ''
    for i in range(0, len(ls)):
        if ls[i] == c:
            resultant.append(st)
            st = ''
        if ls[-1] == ls[i] and len(ls) == i+1:
            st += ls[i]
            resultant.append(st)
            st = ''
        if ls[i] != c:
            st += ls[i]
    return resultant

# help(my_spliter)
# print(my_spliter("Hello to the World of Programming"))
print(my_spliter("18/10/1990", "/"))