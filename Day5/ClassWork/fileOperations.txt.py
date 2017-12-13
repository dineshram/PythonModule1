#https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3#step-1-%E2%80%94-creating-a-text-file

path = 'sampleData1.txt'

days_file = open(path,'r')
#print(days_file.read())

#<file>.readline() returns the next line of the file, returning the text up to and including the next newline character. More simply put, this operation will read a file line-by-line.
#print(days_file.readline())
#print(days_file.readline())

#<file>.readlines() returns a list of the lines in the file, where each item of the list represents a single line.
#print(days_file.readlines())

title = 'Days of the Week\n'
new_path = 'new_days.txt'
new_days = open(new_path,'w')
new_days.write(title)
print(title)
days = days_file.read()
new_days.write(days)
print(days)

days_file.close()
new_days.close()



'r' : use for reading
'w' : use for writing
'x' : use for creating and writing to a new file
'a' : use for appending to a file
'r+' : use for reading and writing to the same file
