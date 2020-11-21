nchars = 256 
def distchar(str, n): 
	count = [0] * nchars  
	for i in range(n): 
		count[ord(str[i])] += 1
	
	max_dist = 0
	for i in range(nchars): 
		if (count[i] != 0): 
			max_dist += 1	
	
	return max_dist 

def Substr(str): 

	n = len(str)
	max_dist= distchar(str, n) 
	min = n
	for i in range(n): 
		for j in range(n): 
			subs = str[i:j] 
			subs_len = len(subs) 
			subchar = distchar(subs,subs_len) 
			if (subs_len < min and max_dist == subchar): 
				min = subs_len 

	return min 

if __name__ == "__main__": 
    str=input()
    l = Substr(str) 
    print(l)
