import this
#python program to  add prime number between 1 to 20"
# total_prime_number=0
prime_number =[]
for num in range(1, 20):
    if num > 1: 
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            prime_number.append(num)
            # total_prime_number +=num
            
print(f"The addition of prime number between 1 to 20 is {prime_number}")
            
  