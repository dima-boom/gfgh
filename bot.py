try:
	import telebot, vk_api, time, requests, os, vk_captchasolver as vc
	from telebot import types
	from time import sleep

	bot = telebot.TeleBot('5260266554:AAHlg7gQWVfFAjRr8ifwm-mtlqOIC_w8kic')

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('Старт')
	item2 = types.KeyboardButton('Стоп')
	markup.add(item1)
	markup.add(item2)
	l = 0
	def ferma():
		global l
		kkkk ={'1': {'key': 'a916f73a8382d9f8cee44213d81424be1c67c6162f4df4df', 'tok': 'f74968049cffd89e9b7adf4cad6cbb08d8a086429ac944f719dcd3cf645d0c461eac79788df294516e4d2'}, 
		    '2': {'key': '85f45e160dfa323b82b873e5816688b91f867128319a40cb', 'tok': '16878cd1c90c49e1950a6e220462999df4c497d3213d40a9c1be2380fbe03435fd386b8efaffb02e4fe87'}, 
		    '3': {'key': '840ce86fb4b8345126de6210a3cc7cba6b476e72402ceb26', 'tok': '1f2f3e0266c4abf5347e495a47b1a16eb1055204ff8fd5f4488f09f6d4d87bdbeef2c8a07d59fc4166ff6'},
		    '4': {'key': '1efbde4e594949f0a0c7c40035256bd35a5a16d23bebaffc', 'tok': '7e01e4d5d1bf29359d0b4a3d26ea81a827a835ea24c7df7ccbcb499faa1a553124b8e71b1969579ec4398',
		    '5': {'key': '2968856eefd49ac43bcddcdb0c3105479f66f84b8dc2d1e9', 'tok': '8f11044a15305eed4bfc91d24b43e9325e9ac7b47ba15d9bee3e1236eea4a73b19688c0b211e4c6f1fbbb'}}}
		j = 0
		while True:
			if l == 1:
			    if j == 5:
			    	j=0
			    j+=1
			    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-Api-Key': kkkk[str(j)]['key']}
			    url = 'https://api-public.bosslike.ru/v1/bots/tasks/'
			    res = requests.get(url, params={'service_type': 1, 'task_type': 3}, headers=headers)
			    info = res.json()['data']['items']
			    for i in info:
			        try:
			            ids = i['id']
			            nach = requests.get(f'https://api-public.bosslike.ru/v1/bots/tasks/{ids}/do/', headers=headers)
			            balik = nach.json()['data']['user_price']
			            if int(balik) < 6:
			            	continue
			            nach = nach.json()['data']['social_metadata']['id']
			            vk_session = vk_api.VkApi(token=kkkk[str(j)]['tok'])
			            vk = vk_session.get_api()
			            try:
			                if str(i['name']['action']) == 'Подписаться на страницу':
			                	vk.groups.join(group_id=nach)
			                else:
			                	vk.friends.add(user_id=nach)
			            except vk_api.Captcha:
			                cycle = True
			                while cycle:
			                    try:
			                        if str(i['name']['action']) == 'Подписаться на страницу':
			                        	vk.groups.join(group_id=nach)
			                        else:
			                        	vk.friends.add(user_id=nach)
			                        yes +=1
			                    except vk_api.Captcha as cptch:
			                        result_solve_captcha = vc.solve(sid=int(cptch.sid), s=1)
			                        try:
			                            cptch.try_again(result_solve_captcha)
			                            cycle = False
			                            yes +=1
			                        except vk_api.Captcha as cptch2:
			                            pass
			                    except:
			                        pass
			            except:
			                pass
			            sleep(1)
			            check = requests.get(f'https://api-public.bosslike.ru/v1/bots/tasks/{int(ids)}/check/', headers=headers)
			        except:
			            requests.get(f'https://api-public.bosslike.ru/v1/bots/tasks/{ids}/hide/', headers=headers)
			else:
				bot.send_message(message.from_user.id, f"Закончена!", reply_markup=markup)
				return


	@bot.message_handler()
	def get_text_messages(message):
	    global l
	    messages = message.from_user.id
	    mess = message.text.lower()
	    if mess == "/start":
	        bot.send_message(messages, f"Работает!", reply_markup=markup)
	    elif mess[0:5] == 'старт':
	    	if l == 0:
	    		l=1
	    		bot.send_message(messages, f"Запущено!", reply_markup=markup)
	    		ferma()
	    	else:
	    		bot.send_message(messages, f"И так запущено!", reply_markup=markup)
	    elif mess == 'стоп':
	    	if l == 1:
	    		l=0
	    		bot.send_message(messages, f"Остановка..", reply_markup=markup)
	    	else:
	    		bot.send_message(messages, f"Останавливать нечего!", reply_markup=markup)
	bot.polling(none_stop=True, interval=0)
except:
	os.system('python bot.py')
