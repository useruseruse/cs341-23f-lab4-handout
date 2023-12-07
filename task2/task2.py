from hash_utils import *
import random, string

# Write your code to generate two letters here
base_text = "NoWorkLifeBalance, Inc. Bob should be "
# alice_text = "NoWorkLifeBalance, Inc. Bob should be promoted"
# bob_text = "NoWorkLifeBalance, Inc. Bob should be fired"
min_sub = 10000000
hash_dict_promoted = {}
hash_dict_fired = {}

# alice_hash = shf64(alice_text)
# bob_hash = shf64(bob_text)
base_hash = shf64(base_text)

# store (hash key and value in table)
# hash_dict[alice_hash] = alice_text
# hash_dict[bob_hash] = bob_text




while(True):
    
    # if(alice_hash==bob_hash):
    #     shf64_alice = alice_text
    #     shf64_bob = bob_text
    #     break
    promoted = "promoted "
    fired = "fired "
    
    N = random.randint(1,8)
    M = random.randint(1,8)

    random_str1 = promoted +''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    random_str2 = fired + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(M))
    str1_hash = shf64(random_str1)
    str2_hash = shf64(random_str2)

    if(random_str1 == random_str2):
        continue

    if(str1_hash == str2_hash):
        print("case 1: collision happens!")
        print("random_str1",random_str1)
        print("random_str2",random_str2)

        str = hash_dict_promoted[str1_hash]
        str2 = hash_dict_fired[str2_hash]

        break

    elif(str1_hash in hash_dict_fired.keys()):
        print("collision happens!")
        str = hash_dict_fired[str1_hash]
        print("random_str1",random_str1 )
        print("random_str2",str )
        break

    # fired 의 hash 가 promoted 의 hash dict에 있는 어떤 값과 일치할 경우. 
    elif(str2_hash in hash_dict_promoted.keys()):
        print("collision happens!")
        str = hash_dict_promoted[str2_hash]   
       
        print("random_str2",random_str2)
        print("random_str2",str)
        break

 
    hash_dict_promoted[str1_hash] = random_str1
    hash_dict_fired[str2_hash] = random_str2
    

# Write your solution here
shf24_alice = None
shf24_bob = None

shf64_alice = None
shf64_bob = None

shf96_alice = None
shf96_bob = None