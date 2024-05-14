def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Umieszczamy każdy element w odpowiednim kubełku
    for num in arr:
        index = int(num * n)
        print(f"index: {index}, num:{num}, n:{n}")
        buckets[index].append(num)

    # Sortujemy zawartość każdego kubełka
    for bucket in buckets:
        insertion_sort(bucket)

    # Łączymy posortowane kubełki
    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr

# Przykładowe użycie
arr = [4,6,4,6,3,5453,23]
sorted_arr = bucket_sort(arr)
print("Posortowana lista:", sorted_arr)