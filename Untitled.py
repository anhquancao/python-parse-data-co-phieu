import csv



row_header = dict()
col_header = dict()
matrix = list()
r_matrix = list()


with open('Return/Return_l2-Table 1.csv','rb') as file:
    i = 0
    contents = csv.reader(file)   
    for row in contents:
        matrix.append(row)
        col_header[row[1]] = i
        i += 1
    row_header = dict(enumerate(matrix[0]))
    row_header = dict((v,k) for k,v in row_header.iteritems())


with open('src/CFODM_TA-Table 1.csv','rb') as file:
    contents = csv.reader(file)
    for row in contents:
        r_matrix.append(row)
    r_row_header = dict(enumerate(r_matrix[0]))
    #r_row_header = dict((v[1:],k) for k,v in r_row_header.iteritems())
    print r_row_header
    row = 1
    for line in r_matrix[1:]:
        col = 0
        for item in line: 
            if item:
                title = 'R'+ r_row_header[col][1:]
                #print title
                col_index = row_header[title]
                row_index = col_header.get(item,'')
                #print 'col_index = ' + str(col_index)
                #print 'row_index = '+ str(row_index)
                if row_index:
                    r_matrix[row][col] = matrix[row_index][col_index]
                else:
                    r_matrix[row][col] = 'not found: ' + item;                          
            col += 1
        row += 1
        
print 'output'
with open('result_l2/CFODM_TA-Table 1_result.csv', 'w') as f:
    for row in r_matrix:                                                        
        f.write(','.join(row)+'\n')
