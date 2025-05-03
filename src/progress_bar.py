from tqdm.auto import tqdm
import time
import progressbar
# first method

for i in tqdm (range(100001)):
    print(" ", end='\r')

# second way
for i, x in enumerate(list(range(100001))):
    print(i, end='\r')

loop=tqdm(total=5000, position=0, leave=False)
for k in range(5000):
    loop.set_description("processing ...".format(k))
    loop.update(1)
loop.close

# third way
for i in tqdm(range(100001)):
    print(" ", end='\r')


texto = ""
for caracter in tqdm(["a", "b", "c", "d"]):
     texto = texto + caracter