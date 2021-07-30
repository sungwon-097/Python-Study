#Make password

address = 'http://naver.com'
print(address)

temp=address.replace("http://", "")
temp=temp[:temp.find(".")]
password=temp[:3]+str(len(temp))+str(temp.count('e'))+"!"
print(password)


'''
url='http://naver.com'
my_str=url.replace("http://","")
my_str=mystr[:mystr.index(".")]
password=my_str[:3]+str(len(my_str))+str(password.count('e'))+"!"
print(password)

'''