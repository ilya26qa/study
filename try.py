import psutil

def get_chromedriver_path():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'chromedriver' in proc.info['name']:
            return proc.exe()
    return None

# Используем функцию для получения пути к chromedriver
chromedriver_path = get_chromedriver_path()

if chromedriver_path:
    print(f'Путь к chromedriver: {chromedriver_path}')
else:
    print('chromedriver не найден в процессах.')