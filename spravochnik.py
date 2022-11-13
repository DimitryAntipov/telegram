
from states import *
from aiogram.dispatcher import FSMContext
import requests
from aiogram import types
from create_bot import *
import csv
from keyboard import *



from datetime import datetime
key = str(f'Запись от:{datetime.now().date()}')

def add (datasave):
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{datasave}\n')

async def cmd_spravochnik(message: types.Message):
    await message.answer ('Выберете вариант обращения в справочник: \n 1 - Запись новых данных \n 2 - Поиск \n 3 - Показать весь справочник  ')
    await StatesSprav.vibor_zap_poi.set()

@dp.message_handler(state=StatesSprav.vibor_zap_poi)
async def load_city(message: types.Message, state: FSMContext):
    
        option = int(message.text)
        
        if option<1 or option > 3:
            await message.answer ('Попробуйте еще раз, такого варианта нет')
        elif option == 2:
            await message.answer ('Введите имя или фамилию человека, которого хотите найти : ')
            await StatesSprav.poisk.set()
            


        elif option == 1:
            await StatesSprav.zapis_name.set()
            await message.answer ('Введите имя человека, которого хотите добавить :')

        elif option == 3:
            with open("Phonebook.csv", newline = '') as csvfile:
                reader = csv.DictReader(csvfile,delimiter=";")
                for row in reader: 
                    resalt = 'Имя - ',row['First name'],'Фамилия - ', row['Last name'], 'Телефон - ', row ['Phone number']
                    await message.answer (resalt)
                await state.finish()
                        
                        
                                    
                        
            
            
@dp.message_handler(state=StatesSprav.poisk)
async def load_poisk(message: types.Message, state: FSMContext):
    name = message.text
    with open("Phonebook.csv", newline = '') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";")
        for row in reader:
            if row['First name'] == name or row['Last name'] == name:
                
                resalt = row['First name'],'|',row['Last name'],'|',row['Phone number']
                
                await message.answer (resalt, reply_markup=get_kb())
                              
                await state.finish()


@dp.message_handler(state=StatesSprav.zapis_name)
async def zapis_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[0] = message.text
        await message.answer ("Введите фамилию человека, которого хотите добавить : ")
        await StatesSprav.next()


@dp.message_handler(state=StatesSprav.zapis_last_name)
async def zapis_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[1] = message.text
        await message.answer ("Введите номер телефона человека, которого хотите добавить : ")
        await StatesSprav.next()
    

@dp.message_handler(state=StatesSprav.zapis_phone)
async def zapis_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[2] = message.text
        await message.answer ("Контакт записан")
        add(f'{data[0]};{data[1]};{data[2]};{key}')
        print (f'{data[0]};{data[1]};{data[2]};{key}')
        await state.finish()


