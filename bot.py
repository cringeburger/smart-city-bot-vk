from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, requests

from random import random

import json
import time

# Custom
import resources

with open("resources/answers.json", "r", encoding="utf-8") as read_file:
	intents = json.load(read_file)

vk_session = VkApi(token=resources.token)
longpoll = VkBotLongPoll(vk_session, resources.group_id)
vk = vk_session.get_api()


def send_message(vk_session, user_id, message=None, attachment=None, keyboard=None):
	vk.messages.send(
		random_id=round(random() * 10 ** 9),
		user_id=user_id,
		message=message,
		attachment=attachment,
		keyboard=keyboard
	)


while True:
	try:
		for event in longpoll.listen():
			if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
				respns = event.obj['message']['text'].lower()
				for intent in intents['intents']:
					for pattern in intent['patterns']:
						if respns == pattern:
							send_message(vk_session, int(
								event.obj['message']['from_id']), intent['response'], keyboard=resources.keyboard)		
	except (requests.exceptions.ReadTimeout, requests.exceptions.SSLError):
		time.sleep(1)
		print('Timeout\n')
		continue
