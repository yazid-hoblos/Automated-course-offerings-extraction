def output_csv(col_names,vals):
    #Write data into csv file
    i=0
    with open('output.csv','w') as o:
        for x in range(22):
            o.write(col_names[x]+',')
        o.write(col_names[22]+'\n')
        
        while i < len(vals):
            for x in range(22):
                o.write(vals[i]+',')
                i+=1
            o.write(vals[i]+'\n')  
            i+=1  

    # Mutate data
    with open ('output.csv','r') as data, open ('mutated_data.csv','w') as results:
        cols = data.readline().strip().split(',')
        cols[0]='Availibility'
        cols[2]='Subject'
        cols[3]='Course Number'
        cols[4]='Section'
        cols[5]='Campus'
        cols[6]='Credits'
        cols[7]='Course Title'
        cols[10]='Capacity'
        cols[11]='Registered Seats'
        cols[12]='Remaining Seats'
        
        results.write(','.join(cols)+'\n')
        l1=data.readline().strip().split(',')
        l2=data.readline().strip().split(',')
        while len(l1) > 1 and len(l2) > 1:
            if l2[1] == ' ':
                days1=l1[8]
                l1[8]+=f" / {l2[8]}"
                l1[9]+=f" ({days1}) / {l2[9]} ({l2[8]})"
                l1[19]+=f" ({days1}) | {l2[19]} ({l2[8]})" 
                l1[20]+=f" ({days1}) / {l2[20]} ({l2[8]})"
                l1[21]+=f" ({days1}) / {l2[21]} ({l2[8]})" 
                results.write(','.join(l1)+'\n')
                l1=data.readline().strip().split(',')
            else:
                results.write(','.join(l1)+'\n')  
                l1=l2
            l2=data.readline().strip().split(',')

        if l1[1] != ' ':
            results.write(','.join(l1))