import psutil


def is_process_running(names):
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name and name.lower() in [p.lower() for p in names]:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def get_process_start_time(names):
    for proc in psutil.process_iter(['name', 'create_time']):
        try:
            name = proc.info['name']
            if name and name.lower() in [p.lower() for p in names]:
                return int(proc.info['create_time'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return None
