import datetime
import json

from java import jclass
from PIL import Image
from ru.travelfood.simple_ui import NoSQL as noClass


def clear_base(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    db_birds = noClass("birds")
    db_birds.destroy()
    db_saw_birds = noClass("saw_birds")
    db_saw_birds.destroy()
    return hashMap


def init(hashMap, _files=None, _data=None):
    db_birds = noClass("birds")
    for i in range(0, 2):
        bird = {
            'photo': '',
            'name': "птица " + str(i),
            'feather_color': "Серые" + str(i),
        }
        db_birds.put(bird['name'], json.dumps(bird, ensure_ascii=False), True)
    return hashMap


def birds_on_open(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    db_birds = noClass("birds")
    cards = {
        "customcards": {
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "match_parent",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "Elements": [
                            {

                                "type": "Picture",
                                "show_by_condition": "",
                                "Value": "@pic",
                                "NoRefresh": False,
                                "document_type": "",
                                "mask": "",
                                "Variable": "",
                                "TextSize": "16",
                                "TextColor": "#DB7093",
                                "TextBold": True,
                                "TextItalic": False,
                                "BackgroundColor": "",
                                "width": "75",
                                "height": "75",
                                "weight": 0
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@key",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@feather_color",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
    cards["customcards"]["cardsdata"] = []
    keys = db_birds.getallkeys()
    jkeys = json.loads(keys)
    for key in jkeys:
        strbird = db_birds.get(key)
        json_bird = json.loads(strbird)
        bird = {
            'pic': '~' + str(json_bird['photo']),
            'key': str(key),
            'feather_color': str(json_bird['feather_color']),
        }
        cards["customcards"]["cardsdata"].append(bird)
    hashMap.put("birds", json.dumps(cards))
    return hashMap


def birds_on_input(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    db_birds = noClass("birds")
    if hashMap.get("listener") == "btn_add":
        hashMap.put("ShowScreen", "Добавление Птицы")
    elif hashMap.get("listener") == "CardsClick":
        key = hashMap.get("selected_card_key")
        strbird = db_birds.get(key)
        json_bird = json.loads(strbird)
        hashMap.put("name", json_bird['name'])
        hashMap.put("feathercolor", json_bird['feather_color'])
        hashMap.put("ShowDialog", "Карточка птицы")
    elif hashMap.get("listener") == "saw_btn":
        global saw_bird_key
        saw_bird_key = hashMap.get("selected_card_key")
    return hashMap


def add_bird_on_open(hashMap, _files=None, _data=None):
    hashMap.put("mm_local","")
    hashMap.put("mm_compression","70")
    hashMap.put("mm_size","65")
    hashMap.put("name", '')
    hashMap.put("feathercolor", '')
    return hashMap


def add_bird_on_input(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    db_birds = noClass("birds")
    if hashMap.get("listener") == "btn_save":
        bird = {
            "name": hashMap.get("name"),
            "feather_color": hashMap.get("feathercolor"),
            'photo': hashMap.get("path"),
            'saw_count': 0,
        }
        if len(bird['name']) == 0:
            hashMap.put('toast', 'Введите название птицы')
        elif len(bird['feather_color']) == 0:
            hashMap.put('toast', 'Введите цвет перьев птицы')
        else:
            db_birds.put(bird['name'], json.dumps(bird, ensure_ascii=False), True)
            hashMap.put('ShowScreen', 'Список Птиц')
    elif hashMap.get("listener") == 'btn_back':
        hashMap.put("ShowScreen", "Список Птиц")
    elif hashMap.get("listener") == "photo":
        hashMap.put("path", str(hashMap.get("photo_path")))
    return hashMap


def saw_birds_on_open(hashMap, _files=None, _data=None):
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    db_saw_birds = noClass("saw_birds")
    cards = {
        "customcards": {
            "layout": {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "match_parent",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "Elements": [
                            {

                                "type": "Picture",
                                "show_by_condition": "",
                                "Value": "@pic",
                                "NoRefresh": False,
                                "document_type": "",
                                "mask": "",
                                "Variable": "",
                                "TextSize": "16",
                                "TextColor": "#DB7093",
                                "TextBold": True,
                                "TextItalic": False,
                                "BackgroundColor": "",
                                "width": "75",
                                "height": "75",
                                "weight": 0
                            },
                            {

                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@key",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@date",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@saw_count",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
    cards["customcards"]["cardsdata"] = []
    birds_keys = db_saw_birds.getallkeys()
    json_birds_keys = json.loads(birds_keys)
    for key in json_birds_keys:
        str_bird = db_saw_birds.get(key)
        json_bird = json.loads(str_bird)
        bird = {
            'pic': '~' + str(json_bird['photo']),
            'key': str(json_bird['name']),
            'date': str(json_bird['date']),
            'saw_count': json_bird['saw_count'],
        }
        cards["customcards"]["cardsdata"].append(bird)
    hashMap.put("saw_birds", json.dumps(cards))
    return hashMap


def saw_birds_on_input(hashMap, _files=None, _data=None):
    global saw_bird_key
    noClass = jclass("ru.travelfood.simple_ui.NoSQL")
    db_birds = noClass("birds")
    db_saw_birds = noClass("saw_birds")
    if hashMap.get("listener") == "btn_add_saw":
        saw_keys = db_saw_birds.getallkeys()
        str_bird = db_birds.get(saw_bird_key)
        json_bird = json.loads(str_bird)
        bird = {
            "name": str(saw_bird_key),
            'photo': str(json_bird['photo']),
            'feather_color': str(json_bird['feather_color']),
            'saw_count': json_bird['saw_count'] + 1,
        }
        db_birds.put(saw_bird_key, json.dumps(bird, ensure_ascii=False), True)
        saw_bird = {
            "name": str(saw_bird_key),
            'photo': str(json_bird['photo']),
            'date': str(datetime.datetime.now()),
            'saw_count': str(json_bird['saw_count'] + 1),
        }
        db_saw_birds.put(
            str(len(saw_keys) + 1),
            json.dumps(saw_bird, ensure_ascii=False),
            True
        )
        saw_bird_key = ''
    return hashMap
