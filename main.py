from multiprocessing import Process

def f(num):
    while True:
        print(num)

if __name__ == '__main__':
    p = Process(target=f, args=(1,))
    p2 = Process(target=f, args=(2,))
    p.start()
    p2.start()
    p.join()
    p2.join()
