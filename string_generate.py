import string 
import random 

 
N = 10


res = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase +
							string.digits +string.punctuation, k = N)) 
 
print("The generated random string : " + str(res))
