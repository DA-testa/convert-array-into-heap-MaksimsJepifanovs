# python3
import math


def build_heap(data):
    
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    cnt = 0
    i = math.floor(n/2)
    
    while True :
        i = math.floor(n/2)
        #print(i)
        ps1 = True
        ps2 = True
        while i >= 0 :

            if 2 * i + 2 <= n - 1 :
                if data[i] < data[2*i+2] :
                    pass
                    #ps2 = True
                else :
                    ps2 = False
                    if data[2*i+2] < data[2*i+1] :
                        rch = data[2*i+2]
                        data[2*i+2] = data[i]
                        data[i] = rch
                        cnt += 1
                        swaps.append([i, 2*i+2])
            #else :
                #ps2 = True

            if 2 * i + 1 <= n - 1 :
                if data[i] < data[2*i+1] :
                    pass
                    #ps1 = True
                else :
                    ps1 = False
                    if 2 * i + 2 <= n - 1 :
                        if data[2*i+1] < data[2*i+2] :
                            lch = data[2*i+1]
                            data[2*i+1] = data[i]
                            data[i] = lch
                            cnt += 1
                            swaps.append([i, 2*i+1])
                    else :
                        lch = data[2*i+1]
                        data[2*i+1] = data[i]
                        data[i] = lch
                        cnt += 1
                        swaps.append([i, 2*i+1])
                    # parent = data[math.floor(i/2)]
                    # data[math.floor(i/2)] = data[i]
                    # data[i] = parent
            #else :
                #ps1 = True

            i = i - 1

            
            
        if ps1 == True and ps2 == True : break

        #print(data)   
        
        

    # for i in range(n) :
        
    #     lp = data.index(min(leftdata))

    #     swap = [i, lp]
    #     swaps.append(swap)
    #     leftdata.remove(min(leftdata))

    #print(cnt)
    #print(data)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    n = ""
    data = []

    mode = input()
    if mode[0] == "F" :
        fname = "./tests/" + input()
        #print(fname)
        f = open(fname, "r")
        n = int(f.readline())
        data = list(map(int, f.readline().split()))
        f.close()

    if mode[0] == "I" :
        n = int(input())
        data = list(map(int, input().split()))


    # input from keyboard
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
