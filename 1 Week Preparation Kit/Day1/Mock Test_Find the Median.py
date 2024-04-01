def findMedian(arr):
 # Write your code here
 arr.sort()
 n=len(arr)
 if n%2==1:
 return arr[n//2]
 else:
 middle1=arr[n//2-1]
 middle2=arr[n//2]
 return (middle1+middle2)/2