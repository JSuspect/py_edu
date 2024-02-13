from pexpect import pxssh
from time import sleep
import getpass
import pathlib


path_dir = pathlib.Path('/mnt/c/Users/SBakhvalov/Documents/_wsl_dir/devout')

print('Проверяю пути... \n')
sleep(5)

if path_dir.exists():
    print(f'Папка "{path_dir.name}" по пути "{path_dir.parent}" уже существует!')
else:
    path_dir.mkdir(parents=True, exist_ok=True)
    if path_dir.exists() and path_dir.is_dir():
        print(f'Папка "{path_dir.name}" создана по пути "{path_dir.parent}"!')
    else:
        print(f'Не удалось создать папку "{path_dir.name}" по пути "{path_dir.parent}"')



devices = {
    'RT-01': {'prompt': 'RT-01>', 'prompt_exec': 'RT-01#', 'ip': '192.168.0.100'},
    'RT-02': {'prompt': 'RT-02>', 'prompt_exec': 'RT-02#', 'ip': '192.168.0.101'},
}

commands = ['term length 0', 'show version', 'show run', 'show ip interface brief' ]

username = input('Username: ')
password = getpass.getpass('Password: ')

# Цикл перебора устройств
for dev in devices.keys():
    output_file = dev + ' ' + devices[dev]['ip'] + '.txt'
    dev_prompt = devices[dev]['prompt']
    dev_prompt_en = devices[dev]['prompt_exec']
    child = pxssh.pxssh()
    child.login(devices[dev]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    # Вводить Enable нет необходимости c privilege 15
    #child.sendline('enable')
    #child.expect(dev_prompt_en)

    # Цикл перебора команд с записью вывода
    file_path = path_dir / output_file
    with open(file_path, mode='wb') as file:
        for command in commands:
            child.sendline(command)
            child.expect(dev_prompt_en)
            file.write(child.before)
    child.logout()