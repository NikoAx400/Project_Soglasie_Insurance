


press_continue = f"//*[text() = 'Далее']"



class osagoLocators():
    def variable_click(text):
        return f'//*[text() = "{text}"]'

    def input_field(text):
        return f"//*[text() = '{text}']//ancestor-or-self::*[contains(@class, 'input-')]//input"

    def select_field(text):
         return f"//*[text() = '{text}']//ancestor-or-self::*[contains(@class, 'select')]//input"

    def select_switcher(text):
        return f"//*[text() = '{text}']//ancestor-or-self::*[@class = 'switcher']//label"











































    # def buy_polis(text):
    #     return f'//*[contains(@class, "container")]//*[contains(@class, "header__bottom-buttons")]//*[text() = "{text}"]'
    #
    # def insurance_auto(text):
    #     return f"//*[contains(@class, 'card services')]//*[text() = '{text}']"
    #
    # def without_number(text):
    #     return f"//*[contains(@class, 'avtokod__search with-auth')]//*[text() = '{text}']"
    #
    # def choosing_car(text):
    #     return f"//*[text() = '{text}']"
    #
    # def input_field(name_field):
    #     return f"//*[text() = '{name_field}']//ancestor-or-self::*[contains(@class, 'input-')]//input"
    #
    # def full_name(text):
    #     return f"//*[text() = '{text}']//ancestor-or-self::*[contains(@class, 'input-')]//input"


    press_continue = f"//*[text() = 'Далее']"
