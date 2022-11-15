import requests
from bs4 import BeautifulSoup

# read the problem name for which user wants the input/ output
# open the input file
input1 = open('input1.txt', 'r')
problem_name = input1.readlines()
input1.close()
# print(problem_name)

# TODO : we may place a checker wheather the problem name is valid or not

# fetch the html content from the web page of codeforces
request_url = requests.get('https://codeforces.com/contest/1721/problem/'+problem_name[0])
request_url = request_url.content

# parse the content
soup = BeautifulSoup(request_url, 'html.parser')
# this is beutiful soup object
# this object provides various properties and makes the extraction easy

# prettify displayes the html content in more redable manner
# so that we can find the things we want easily
# print(soup.prettify)



# print(soup)
# title = soup.title
# title is tag, title.string is a navigable string special for bs4
# paras = soup.find_all('p') 
# para = soup.find('p') 
# first para element

# print(soup.find('div')['class'])
# print(title.get_text)

# using class name we can get corresponding elements
# in codeforces case
# modifing input file
input_list = []
inputs = soup.find_all('div', class_= 'input')
for input in inputs:
  temp = input.get_text()
  # print(temp)
  temp = temp[6:]
  #6 index se utha rhe hai 6 k baad k index 
  input_list.append(temp)


# clearing the input and output files
with open('input1.txt', 'r+') as f:
    f.truncate(0)
with open('output1.txt', 'r+') as f:
    f.truncate(0)

for input in input_list:
  with open('input1.txt', 'a') as f:
    f.write(input + " ")
    
# saving the correct/ expected output
output_list = []

# in soup object search for div's tag having class name as 'output'
outputs = soup.find_all('div', class_= 'output')
print(outputs)
for output in outputs:
  # get the inner text
  temp = output.get_text()
  temp = temp[7:]
  output_list.append(temp)

# print(output_list)
with open('output1.txt', 'a') as f:
    f.write("Expected output \n")

# write the expected output in the output.txt file
for output in output_list:
  with open('output1.txt', 'a') as f:
    f.write(output)

with open('output1.txt', 'a') as f:
    f.write("\nObtained output \n")


