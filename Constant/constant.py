numToAlp_dict={i:chr(ord('A')+i) for i in range(26)}
for i in range(26):
    numToAlp_dict.update({i*10+j+26:(chr(ord('A')+i)+str(j)) for j in range(10)})
# 0-285