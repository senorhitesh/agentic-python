def infinte():
    count =0
    while True:
        count +=1
        yield f"hey your count #{count}"

refill = infinte()
for _  in range(40):
    print(next(refill))

