file_read = open('Codingal.txt' ,'r')
data = file_read.read()
print(data)
file_read.close()


file_write = open('Codingal.txt' , 'w')
file_write.write('Replaced text')
file_write.close()


file_append = open('Codingal.txt' , 'a')
file_append.write('Original text')
file_append.close()
