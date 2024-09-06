if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(arr)
    
    biggest_score = max(arr)
    
    arr = [score for score in arr if score != biggest_score]
        
    runner_up =  max(arr) 
    print(runner_up)
    
