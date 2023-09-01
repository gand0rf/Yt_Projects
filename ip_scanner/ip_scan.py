import subprocess, time
from multiprocessing.pool import ThreadPool


def ping(ip: int):
    result = subprocess.Popen(['ping','-c','1','-s','1','-w','1',f'192.168.1.{ip}'],stdout=subprocess.PIPE)
    if b'1 received' in result.communicate()[0]:
        return f'192.168.1.{ip}'

def ip_clean(ip_list):
    clean_list = [ip for ip in ip_list if ip != None]
    return clean_list

def thread_scan():
    print('\nStaring thread scan...')
    with ThreadPool() as pool:
        results = pool.map(ping, range(1,255))
    print('\nThread scan is complete...')
    return ip_clean(results)

if __name__ == '__main__':

    start_time = time.perf_counter()
    alive_ip_list = thread_scan()
    end_time = time.perf_counter()

    print(f'\nFound {len(alive_ip_list)} ips:')
    for ip in alive_ip_list:
        print(f'\t{ip} is alive')
    print(f'\nTime taken: {"{:.2f}".format(end_time-start_time)} seconds')

