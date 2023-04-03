from PageSteps import PageObject
from confest import browser
import datetime
import time

def test_soglaie_enter(browser):
    soglasie = PageObject(browser)
    soglasie.press_button('Купить полис')
    time.sleep(1)
    soglasie.press_button('ОСАГО')
    soglasie.press_button('Расчёт без ввода номера')
    soglasie.press_button('Ford')
    soglasie.press_button('Edge')

    # Вкладка "Характеристики"
    soglasie.input_field_click('Мощность (л.с.)', '150')
    current_date = datetime.datetime.now() + datetime.timedelta(days=1)
    date_polis = current_date.strftime('%d.%m.%Y')
    soglasie.input_field_click('Дата начала действия полиса', date_polis)
    soglasie.input_field_pressEnter('Город регистрации собственника', 'г Москва')
    soglasie.input_select_click('Год выпуска', '2019')
    soglasie.press_button('Далее')

    # Вкладка "Водители"
    soglasie.switch_press('Неограниченное количество водителей')
    soglasie.input_field_pressEnter('Фамилия Имя Отчество', 'Панкратов Владимир Ильич')
    soglasie.input_field_click('Дата рождения', '10.05.1986')
    soglasie.input_field_click('Серия и номер Паспорта РФ', '4509 458586')
    soglasie.input_from_selection('Тип идентификационного номера', 'Номер шасси')
    soglasie.input_field_click('Идентификационный номер', '58685478966584565')
    soglasie.press_button('Далее')

    # Вкладка "Использование"
    purpose_use_car = 'Личные'
    soglasie.value_field('Цель использования ТС', purpose_use_car)
    soglasie.input_from_selection('Тип страхования', 'Следование к месту регистрации или прохождения ТО (до 20 дней)')
    soglasie.compare_date('Дата начала действия полиса', 'Дата окончания действия полиса')
    soglasie.press_button('Далее')

    # Вкладка "Документ о регистрации ТС"
    soglasie.input_field_click('Серия и номер ПТС', '12ЕО 256826')
    soglasie.input_field_click('Дата выдачи', '12.01.2023')
    time.sleep(1)
    soglasie.press_button('Далее')

    # Вкладка "Собственник"
    soglasie.switch_press('Собственник является страхователем')
    soglasie.input_field_click('Дата выдачи', '12.05.2020')
    soglasie.input_field_click('Кем выдан', 'ОВД города Москвы')
    soglasie.input_field_pressEnter('Адрес', 'г Москва, ул Зеленодольская, д 3')
    soglasie.press_button('Далее')

    # Вкладка "Страхователь"
    soglasie.input_field_click('E-mail', 'soglasie@mail.ru')
    soglasie.input_field_click('Телефон', '9985856566')
    soglasie.press_button('Подтверждаю корректность указанных данных')
