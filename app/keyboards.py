from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_menu, get_foods


check_soups = [int(i) for i in range(1, 13)]
check_woks = [int(i) for i in range(13, 30)]
check_snacks =[int(i) for i in range(30, 36)]
check_drinks = [int(i) for i in range(36, 46)]


start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Режим работы")],
    [KeyboardButton(text="Расположение")],
    [KeyboardButton(text="Условия доставки и самовызова")],
    [KeyboardButton(text="Меню"),
    KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Контакты")]
], resize_keyboard=True, input_field_placeholder="Выберите команду...")

contacts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Менеджер", url="https://t.me/cafe_hanoi_73")],
    [InlineKeyboardButton(text="Разработчик", url='https://t.me/MaxLikeVolleyball')],
])

location = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Открыть карту", url="https://yandex.ru/maps/org/hanoi/97574318406")]
])

manager = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Менеджер', url="https://t.me/cafe_hanoi_73")]
])

async def menu():
    all_menu = await get_menu()
    keyboard = InlineKeyboardBuilder()
    for every_menu in all_menu:
        keyboard.add(InlineKeyboardButton(text=every_menu.name, callback_data=f"menu_{every_menu.id}"))
    """keyboard.add(InlineKeyboardButton(text="Вернуться к меню", callback_data='to_main'))"""
    return keyboard.adjust(2).as_markup()

async def soups():
    all_foods = await get_foods()
    all_foods1 = await get_foods()
    keyboard = InlineKeyboardBuilder()
    check_same = []
    for soup in all_foods:
        check_same.append(soup.name)
    check_multi = []
    for every_soup in all_foods1:
        if every_soup.name not in check_multi and every_soup.category == "Супы":
            keyboard.add(InlineKeyboardButton(text=f"{every_soup.name}", callback_data=f"soup_multi_{every_soup.id}"))
            check_multi.append(every_soup.name)
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def pho_bo():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for pho in all_foods:
        if pho.name == "Фо Бо":
            keyboard.add(InlineKeyboardButton(text=f"{pho.name} | {pho.size} | {pho.price}р", callback_data=f"single_soup_{pho.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def mien_bo():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for mien in all_foods:
        if mien.name == "Миен Бо":
            keyboard.add(InlineKeyboardButton(text=f"{mien.name} | {mien.size} | {mien.price}р", callback_data=f"single_soup_{mien.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
    
async def bun_bo():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for bun in all_foods:
        if bun.name == "Бун Бо":
            keyboard.add(InlineKeyboardButton(text=f"{bun.name} | {bun.size} | {bun.price}р", callback_data=f"single_soup_{bun.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def tom_yum():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for tom in all_foods:
        if tom.name == "Том Ям":
            keyboard.add(InlineKeyboardButton(text=f"{tom.size} | {tom.price}р | {tom.add}", callback_data=f"single_soup_{tom.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def pho_ga():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for fo_ga in all_foods:
        if fo_ga.name == "Фо Га":
            keyboard.add(InlineKeyboardButton(text=f"{fo_ga.name} | {fo_ga.size} | {fo_ga.price}р", callback_data=f"single_soup_{fo_ga.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def sot_vang():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for sot in all_foods:
        if sot.name == "Шот Ванг":
            keyboard.add(InlineKeyboardButton(text=f"{sot.name} | {sot.size} | {sot.price}р", callback_data=f"single_soup_{sot.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def pho_sot_vang():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for sot in all_foods:
        if sot.name == "Фо Шот Ванг":
            keyboard.add(InlineKeyboardButton(text=f"{sot.name} | {sot.size} | {sot.price}р", callback_data=f"single_soup_{sot.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

    
async def woks():
    all_foods = await get_foods()
    all_foods1 = await get_foods()
    keyboard = InlineKeyboardBuilder()
    check_same = []
    for wok in all_foods:
        check_same.append(wok.name)
    check_multi = []
    for every_wok in all_foods1:
        if every_wok.category == "Вторые" and every_wok.name not in check_multi:
            keyboard.add(InlineKeyboardButton(text=f"{every_wok.name}", callback_data=f"wok_multi_{every_wok.id}"))
            check_multi.append(every_wok.name)
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def com_rang():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for com in all_foods:
        if com.name == "Кым Ранг":
            keyboard.add(InlineKeyboardButton(text=f"{com.price}р | {com.add}", callback_data=f"single_wok_{com.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться ко Вторым", callback_data="menu_2"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def mien_sao():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for sao in all_foods:
        if sao.name == "Миен Сао":
            keyboard.add(InlineKeyboardButton(text=f"{sao.price}р | {sao.add}", callback_data=f"single_soup_{sao.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться ко Вторым", callback_data="menu_2"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def mi_sao():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for mi in all_foods:
        if mi.name =="Ми Сао":
            keyboard.add(InlineKeyboardButton(text=f"{mi.price}р | {mi.add}", callback_data=f"single_wok_{mi.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться ко Вторым", callback_data="menu_2"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def pho_sao():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for pho in all_foods:
        if pho.name == "Фо Сао":
            keyboard.add(InlineKeyboardButton(text=f"{pho.price}р | {pho.add}", callback_data=f"single_wok_{pho.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться ко Вторым", callback_data="menu_2"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def bun_nem():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for bun in all_foods:
        if bun.name == "Бун Нэм":
            keyboard.add(InlineKeyboardButton(text=f"{bun.name} | {bun.size} | {bun.price}р | {bun.add}", callback_data=f"single_wok_{bun.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться ко Вторым", callback_data="menu_2"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def snacks():
    all_foods = await get_foods()
    all_foods1 = await get_foods()
    keyboard = InlineKeyboardBuilder()
    check_same = []
    for snack in all_foods:
        check_same.append(snack.name)
    check_multi = []
    for every_snack in all_foods1:
        if every_snack.category == "Закуски" and check_same.count(every_snack.name) == 1:
            keyboard.add(InlineKeyboardButton(text=f"{every_snack.name} | {every_snack.size} | {every_snack.price}р", callback_data=f"single_snack_{every_snack.id}"))
        elif every_snack.category == "Закуски" and check_same.count(every_snack.name) > 1 and every_snack.name not in check_multi:
            keyboard.add(InlineKeyboardButton(text=f"{every_snack.name}", callback_data=f"snack_multi_{every_snack.id}")) 
            check_multi.append(every_snack.name)
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def nem():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for nem in all_foods:
        if nem.name == "Нэм":
            keyboard.add(InlineKeyboardButton(text=f"{nem.name} | {nem.size} | {nem.price}р", callback_data=f"single_snack_{nem.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Закускам", callback_data="menu_3"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def drinks():
    all_foods = await get_foods()
    keyboard = InlineKeyboardBuilder()
    for every_drink in all_foods:
        if every_drink.category == "Напитки":
            keyboard.add(InlineKeyboardButton(text=f"{every_drink.name} | {every_drink.price}р", callback_data=f"single_drink_{every_drink.id}"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
      
      
async def after_pick(id):
    keyboard = InlineKeyboardBuilder()
    if int(id) in check_soups:
        keyboard.add(InlineKeyboardButton(text="Вернуться к Супам", callback_data="menu_1"))
    elif int(id) in check_woks:
        keyboard.add(InlineKeyboardButton(text="Вернуться ко Вторым", callback_data="menu_2"))
    elif int(id) in check_snacks:
        keyboard.add(InlineKeyboardButton(text="Вернуться к Закускам", callback_data="menu_3"))
    else:
        keyboard.add(InlineKeyboardButton(text="Вернуться к Напиткам", callback_data="menu_4"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data='to_main'))
    keyboard.add(InlineKeyboardButton(text="Корзина", callback_data="basket"))
    return keyboard.adjust(2).as_markup()

async def send_order():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Доставка", callback_data="send_order"))
    keyboard.add(InlineKeyboardButton(text="Самовызов", callback_data="send_order_no_delivery"))
    keyboard.add(InlineKeyboardButton(text="Очистить корзину", callback_data="clear"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()

async def send_order_no_delivery():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Самовызов", callback_data="send_order_no_delivery"))
    keyboard.add(InlineKeyboardButton(text="Очистить корзину", callback_data="clear"))
    keyboard.add(InlineKeyboardButton(text="Вернуться к Меню", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()

async def clear_basket():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Очистить корзину", callback_data="clear"))
    return keyboard.adjust(2).as_markup()
    
async def confirm_order():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Подтвердить заказ", callback_data="confirm_order"))
    keyboard.add(InlineKeyboardButton(text="Очистить данные", callback_data="clear_state"))
    return keyboard.adjust(2).as_markup()

async def confirm_order_no_delivery():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Подтвердить заказ", callback_data="confirm_order_in_cafe"))
    keyboard.add(InlineKeyboardButton(text="Очистить данные", callback_data="clear_state_in_cafe"))
    return keyboard.adjust(2).as_markup()

send_number = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить номер телефона', request_contact = True)]
])