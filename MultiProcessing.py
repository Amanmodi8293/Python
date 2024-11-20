import multiprocessing
import concurrent.futures
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    r = requests.get(url)
    open(f"files/{name}.jpg", 'wb').write(r.content)
    print(f"Finished Downloading {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"
    pros = []

    # for i in range(50):
    #     # downloadFile(url , i)
    #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [ i for i in range(60)]
        result = executor.map(downloadFile, l1, l2)
        for r in result:
          print(r)