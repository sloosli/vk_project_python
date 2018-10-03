#!/usr/bin/python3

from time import sleep
from datetime import datetime

import vk_api

from settings import token


def get_users(user_ids):
    
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    
    return vk.users.get(user_ids=user_ids, fields='last_seen')
    


def get_platform(pl_id):
    pl_type = [
    'мобильная версия',
    'приложение для iPhone',
    'приложение для iPad',
    'приложение для Android',
    'приложение для Windows Phone',
    'приложение для Windows 10',
    'полная версия сайта' ]

    return pl_type[pl_id - 1]



def last_seen(user_ids, count = 1, output = 'output.txt', timeout = 300):
    
    outfile = open(output, 'a')

    for i in range(count):
        
        users = get_users(user_ids)
        
        for user in users:
            
            outfile.write(user['first_name']+' '+
            	          user['last_name']+'\n')
            
            time  = (
            	    datetime.fromtimestamp(
                    user['last_seen']['time'])
                    .strftime('%Y-%m-%d %H:%M:%S') 
                    )
            platform = get_platform(user['last_seen']['platform'])

            outfile.write(time + ' ' + platform)
            
            current_time = (
            	    datetime.today()
                    .strftime('%Y-%m-%d %H:%M:%S')
                    )
            
            outfile.write('\n' + current_time + '\n\n')
        sleep(timeout)
    
    outfile.close()



def start():
    print('Введите id пользователя')
    user_ids = input()

    print('Введите количество повторений')
    count = int(input())

    timeout = 0
    if count != 1:
        print('Введите таймаут в секундах')
        timeout = int(input())

    last_seen(user_ids=user_ids, count=count, timeout=timeout)



if __name__ == '__main__':
	start()