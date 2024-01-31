import random
import time

def random_array(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0, 200))
    print("The random array:" ,arr)
    return arr

def merge(Arr,left,mid,right):
    Larr = Arr[left: mid+1]
    Rarr = Arr[mid+1: right+1]
    l=0
    r =0
    k=left
    while l<len(Larr) and r<len(Rarr) :
        if Larr[l] <Rarr[r]:
            Arr[k] =Larr[l]
            l = l+1
            k = k+1
        else:
            Arr[k] =Rarr[r]
            r = r+1
            k = k+1
    while l<len(Larr):
        Arr[k] = Larr[l]
        l = l + 1
        k = k + 1
    while r< len(Rarr):
        Arr[k]=Rarr[r]
        r=r+1
        k=k+1

def merge_sort(Arr,left,right):
    if(left<right):
        mid=(left+right)//2
        merge_sort(Arr,left,mid)
        merge_sort(Arr,mid+1,right)
        merge(Arr,left,mid,right)

def partition(Arr,first,last):
    pivot = first
    lastS1 = first
    firstUnknown = first+1
    while firstUnknown <= last:
        if(Arr[firstUnknown] < Arr[pivot]):
            lastS1 = lastS1+1
            Arr[lastS1],Arr[firstUnknown] = Arr[firstUnknown],Arr[lastS1]
        firstUnknown = firstUnknown+1
    Arr[first],Arr[lastS1] = Arr[lastS1],Arr[first]
    pivot =lastS1
    return pivot


def quick_sort(Arr,first,last):
    if(first<last):
        pivot = partition(Arr,first,last)
        quick_sort(Arr,first,pivot-1)
        quick_sort(Arr,pivot+1,last)

def selection_sort(Arr):
    size = len(Arr)
    for i in range(size):
        min = i
        for k in range(i +1,size):
            if Arr[k]<Arr[min]:
                min =k
        Arr[i],Arr[min] = Arr[min],Arr[i]

def insertion_sort(Arr):
    size =len(Arr)
    for i in range(1,size):
        temp=Arr[i]
        j=i-1
        while j>=0 and temp <Arr[j]:
            Arr[j+1]=Arr[j]
            j =j-1
        Arr[j+1]=temp

def heapify(Arr,index,size):
    max =  index
    left = 2 *index + 1
    right = 2 *index +2
    if left < size and Arr[left] >Arr[max]:
        max = left
    if right <size and Arr[right]>Arr[max]:
        max = right
    if max != index:
        Arr[index],Arr[max] = Arr[max],Arr[index]
        heapify(Arr,max,size)

def build_heap(Arr):
    size = len(Arr)
    for i in range (size-1//2,-1,-1):
        heapify(Arr,i,size)

def heap_sort(Arr):
    size =len(Arr)
    build_heap(Arr)
    for i in range(size-1,-1,-1):
        Arr[i],Arr[0] = Arr[0],Arr[i]
        heapify(Arr,0,i)


def hybrid_sort(Arr,thres):
    size = len(Arr)
    if size <= thres:
        return selection_sort(Arr)
    else:
        left = 0
        right = len(Arr)
        mid = (left + right) // 2
        hybrid_sort(Arr[:mid], thres)
        hybrid_sort(Arr[mid:], thres)
        merge(Arr,left,mid ,right)

#def kth_element(Arr,k):
 #   if k< len(Arr):
  #      #quick_sort(Arr,0,len(Arr)-1)
   #     print("The Kth element is :", Arr[k-1])

def kth_element(Arr, k):
    first = 0
    last = len(Arr) - 1
    flag =0
    index = k-1
    while flag ==0 :
        pivot= partition(Arr, first, last)
        if pivot == index:
            print("The Kth element is :", Arr[k - 1])
            flag =1
        elif pivot> index:
            last = pivot-1
        else:
            first = pivot+1

n =10
print("Length of Array used is : \n",n)
print("---------------------------MERGE SORT--------------------------")
start= time.time()
A = random_array(n)
merge_sort(A,0,len(A)-1)
print("\nMerge Sort: ", A)
end = time.time()
print("Time taken fro merge sort: ", end- start, "seconds.\n\n")

print("---------------------------QUICK SORT--------------------------")
start= time.time()
A = random_array(n)
pivot = random.randint(0, len(A))
print("Pivot is element no.: ", pivot)
A[pivot], A[0] = A[0], A[pivot]
quick_sort(A,0,len(A)-1)
print("\nQuick Sort :",A)
end = time.time()
print("Time takenfor quick sort: ", end- start, "seconds.\n\n")
k = int(input("Enter the value of k to get the kth smallest element: "))
kth_element(A,k)

print("---------------------------SELECTION SORT--------------------------")
start= time.time()
A = random_array(n)
selection_sort(A)
print("\nSelection Sort: ",A)
end = time.time()
print("Time taken for selection sort: ", end- start, "seconds.\n\n")

print("---------------------------INSERTION SORT--------------------------")
start= time.time()
A = random_array(n)
insertion_sort(A)
print("\nInsertion Sort: ",A)
end = time.time()
print("Time taken for insertion sort: ", end- start, "seconds.\n\n")

print("---------------------------HEAP SORT--------------------------")
start= time.time()
A = random_array(n)
heap_sort(A)
print("\nheap Sort: ",A)
end = time.time()
print("Time taken for heap sort: ", end- start, "seconds.\n\n")

print("---------------------------HYBRID SORT--------------------------")
m = int(input("Enter the value of k: "))
start= time.time()
A = random_array(n)
hybrid_sort(A,m)
print("\nHybrid Sort: ",A)
end = time.time()
print("Time taken for hybrid sort: ", end- start, "seconds.\n\n")

