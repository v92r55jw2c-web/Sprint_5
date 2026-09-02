from selenium.webdriver.common.by import By

# Кнопка "Личный кабинет"
BUTTON_PERSONAL_ACCOUNT = (By.CSS_SELECTOR,'a[href="/account"]')

# Кнопка Зарегистрироваться в личном кабинете
BUTTON_REGISTRATION_ON_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/register"]')

# Поле Имя при регистрации
NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')

# Поле Email при регистрации
EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

# Поле Пароль при регистрации
PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

#Кнопка Зарегистрироваться в форме регистрации
BUTTON_REGISTRATION = (By.XPATH,'//button[text()="Зарегистрироваться"]')

# Сообщение об ошибке при некорректном пароле
PASSWORD_ERROR = (By.XPATH, '//p[text()="Некорректный пароль"]')

# Кнопка Войти через личный кабинет
BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')

# Кнопка Войти в аккаунт на главной странице
BUTTON_LOGIN_HOME_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]')

# Поле Email при входе
EMAIL_LOG_IN = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

# Поле Пароль при входе
PASSWORD_LOG_IN = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

# Кнопка Оформить заказ
BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')

# Кнопка Войти в форме регистрации
BUTTON_LOGIN_REGISTRATION = (By.XPATH, '//a[@href="/login"]')

# Кнопка восстановления пароля
BUTTON_RECOVERY_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')

# Кнопка Войти в форме воостановления пароля
BUTTON_LOGIN_RECOVERY_PASSWORD = (By.XPATH, '//a[@href="/login"]')

# Кнопка Профиль в личном кабинете
BUTTON_PROFILE_ON_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account/profile"]')

# Кнопка Конструктор
BUTTON_BUILDER = (By.XPATH, '//p[text()="Конструктор"]')

# Кнопка Stellar Burgers
BUTTON_STELLAR_BURGERS = (By.CSS_SELECTOR, 'a[href="/"]')

# Кнопка Выйти 
BUTTON_LOG_OUT = (By.XPATH, '//button[text()="Выход"]')

# Раздел Булки для клика
SECTION_BUNS = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")][.//span[text()="Булки"]]')

# Активный раздел Булки
SECTION_BUNS_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "tab_tab_type_current__2BEPc")][.//span[text()="Булки"]]')

# Раздел Соусы для клика
SECTION_SAUCES = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")][.//span[text()="Соусы"]]')

# Активный раздел Соусы
SECTION_SAUCES_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "tab_tab_type_current__2BEPc")][.//span[text()="Соусы"]]')

# Раздел Начинки для клика
SECTION_FILLINGS = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")][.//span[text()="Начинки"]]')

# Активный раздел Начинки
SECTION_FILLINGS_ACTIVE = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG") and contains(@class, "tab_tab_type_current__2BEPc")][.//span[text()="Начинки"]]')