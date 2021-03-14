import random
def rps():
    user = input("'r' for rock\n'p' for paper\n's' for scissors\n")
    comp = random.choice(['r','p','s'])
    print("computer choice:"+comp)
    if user == comp :
        return "Its a tie!"
    if win(user,comp):
         return "You won!!!!!"
 
    return "You Lost :(("     
    
def win(player, opponent):
    #r>s,p>r,s>p
    if((player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p')):
        return True
      
print(rps())