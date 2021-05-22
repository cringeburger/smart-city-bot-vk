import json


keyboard = {
    "one_time": None,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "KEKW"
                },
                "color": "positive"
            }
        ]
    ]
}
 
keyboard = json.dumps(keyboard, ensure_ascii=False)
