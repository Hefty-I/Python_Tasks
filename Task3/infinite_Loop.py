import multiprocessing

def burn_cpu():
    while True:
        print("Burning CPU...")

if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count() # Gets the number of CPU cores
    print(f"Spawning {cpu_count} processes to utilize CPU...")
    for i in range(cpu_count): #
        p = multiprocessing.Process(target=burn_cpu) # Creating a new process for each CPU core
        p.start()