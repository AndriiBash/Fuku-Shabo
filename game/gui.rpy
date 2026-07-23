################################################################################
## Ініціалізація
################################################################################


## "init offset = -2" змушує цей файл виконуватись раніше за options.rpy
## (offset = -1) і за будь-який інший файл — тому тут можна безпечно
init offset = -2

## "gui.init" відновлює стилі до стандартних значень і встановлює робочу роздільність гри (1920x1080).
init python:
    gui.init(1920, 1080)

## Перевірка на конфліктні/нестабільні властивості в екранах і трансформаціях.
define config.check_conflicting_properties = True


################################################################################
## Кольори
################################################################################


## Акцентний колір інтерфейсу (підсвічування, вибрані елементи).
define gui.accent_color = '#0099cc'

## Колір тексту кнопки в звичайному стані (без наведення/вибору).
define gui.idle_color = '#e2dcd8'

## Яскравіший/темніший відтінок для дрібного тексту 
## (той самий ефект, що й idle_color, але прочитний при меншому розмірі шрифту).
define gui.idle_small_color = '#aaaaaa'

## Колір кнопок і смуг при наведенні курсора.
define gui.hover_color = '#fac081'

## Колір кнопки, коли вона вибрана (активний екран/налаштування), але не в фокусі.
define gui.selected_color = '#f2cfc1'

## Колір кнопки, яку неможливо натиснути (недоступна).
define gui.insensitive_color = '#8888887f'

## Кольори тексту діалогу та меню вибору.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


################################################################################
## Шрифти та розміри шрифтів
################################################################################


## Шрифт назви гри в головному меню
define gui.game_title_font = "anotherdangerslantedrusbyl.otf"

## Шрифт діалогу
define gui.text_font = "DejaVuSans.ttf"

## Шрифт імені персонажа
define gui.name_text_font = "DejaVuSans.ttf"

## Шрифт інтерфейсу
define gui.interface_text_font = "Oswald-Bold.ttf"

## Розмір тексту діалогу.
define gui.text_size = 45

## Розмір імен персонажів.
define gui.name_text_size = 45

## Розмір тексту інтерфейсу поза грою.
define gui.interface_text_size = 23

## Розмір міток (заголовків розділів меню).
define gui.label_text_size = 36

## Розмір тексту сповіщень.
define gui.notify_text_size = 24

## Розмір назви гри на головному меню.
define gui.title_text_size = 65


################################################################################
## Розміри вікон меню та скролбарів
################################################################################

## Висота вікна ігрового меню (about/save/load/preferences/history).
define gui.ygame_menu_size = 820

## Позиції кастомного вертикального скролбару (vbar) для кожного екрана,
## що використовує прокрутку в game_menu — see screens.rpy.
define gui.vscroll_xpos_about = 900
define gui.vscroll_xpos_history = 1050
define gui.vscroll_xpos_preferences = 815
define gui.vscroll_ysize = 580


################################################################################
## Зображення вікон: навігація, налаштування, завантаження і т.д.
################################################################################

## Кнопка повернення.
define gui.return_button_cover_activated = "gui/return_button_activated.png"
define gui.return_button_cover_not_activated = "gui/return_button_non_activated.png"

## Фон для завантаження/збереження/історії/про гру.
define gui.about_save_load_background = "gui/bg_about_load_save.png"

## Фони панелі навігації (велика версія — головне меню, мала — підменю).
define gui.navigation_big_background = "gui/bg_navigation_mac_transperent_big.png"
define gui.navigation_small_background = "gui/bg_navigation_mac_transperent_small.png"

## Зображення для головного меню й меню гри.
define gui.main_menu_background = "gui/bg_menu_background.png"
define gui.main_menu = "gui/bg_menu.png"
define gui.menu_cat_sticker = "gui/cat_sticker.png"


################################################################################
## Головне меню — назва гри
################################################################################


## Текст назви гри, що показується на головному меню.
define gui.game_title =_("""111111111111111111111111111
11Д О П О К И  Г О Р Я Т Ь11
        111В О Г Н І11
    1111111111111111111""")


## Інтенсивність блюру фону під час показу фону для завантаження/збереження/історії/про гру.
define gui.blur_intense = 12

## Трансформація для розмиття тексту назви гри (застосовується через "at blur_text").
transform blur_text:
    blur 5

## Стиль назви гри на головному меню.
style game_title_text:
    font "anotherdangerslantedrusbyl.otf"
    size gui.title_text_size
    color "#f4d5ce"
    outlines [(5, "#000000", 10, 10)]
    bold True


################################################################################
## Діалог
################################################################################
##
## Ці змінні визначають, як діалог виводиться на екран по одному рядку.

## Висота і позиція текстового поля з діалогом.
define gui.textbox_height = 278
define gui.textbox_yalign = 1.0

## Позиція та вирівнювання імені персонажа відносно текстового поля.
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0

## Ширина/висота поля імені персонажа ("None" — визначається автоматично).
define gui.namebox_width = None
define gui.namebox_height = None

## Межі поля імені персонажа (ліво, верх, право, низ).
define gui.namebox_borders = Borders(5, 5, 5, 5)

## "True" — тло поля імені мозаїчне (tile), "False" — масштабоване.
define gui.namebox_tile = False

## Позиція діалогу відносно текстового поля.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальна ширина тексту діалогу (px).
define gui.dialogue_width = 1116

## Вирівнювання тексту діалогу (0.0 ліворуч, 0.5 центр, 1.0 праворуч).
define gui.dialogue_text_xalign = 0.0


################################################################################
## Кнопки — загальні налаштування
################################################################################


## Ширина/висота кнопки ("None" — Ren'Py визначає розмір автоматично).
define gui.button_width = None
define gui.button_height = None

## Межі кнопки (ліво, верх, право, низ).
define gui.button_borders = Borders(6, 6, 6, 6)

## "True" — тло кнопки мозаїчне, "False" — масштабоване лінійно.
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

## Колір тексту кнопки в різних станах.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Вирівнювання тексту кнопки (0.0 ліворуч, 0.5 центр, 1.0 праворуч).
define gui.button_text_xalign = 0.0

## Налаштування для окремих типів кнопок стандартного інтерфейсу.
define gui.radio_button_borders = Borders(27, 6, 6, 6)
define gui.check_button_borders = Borders(27, 6, 6, 6)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(15, 6, 15, 6)
define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Власна ширина кнопок навігації
# define gui.navigation_button_width = 250


################################################################################
## Кнопки вибору (menu-вибори у грі)
################################################################################

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


################################################################################
## Кнопки комірок збережень (save/load slots)
################################################################################


## Розмір комірки збереження
define gui.slot_button_width = 210
define gui.slot_button_height = 160

define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Розмір мініатюр (скріншотів), які показуються в комірках збереження.
define config.thumbnail_width = 180
define config.thumbnail_height = 101

## Кількість стовпців/рядків у сітці комірок збереження.
define gui.file_slot_cols = 1
define gui.file_slot_rows = 4


###############################################################################
## Позиціонування та інтервали
################################################################################


define gui.navigation_xpos = 60          ## Позиція лівого краю навігації від краю екрана.
define gui.skip_ypos = 15                ## Вертикальна позиція індикатора пропуску.
define gui.notify_ypos = 68              ## Вертикальна позиція екрана сповіщень.
define gui.choice_spacing = 33           ## Інтервал між пунктами вибору.
define gui.navigation_spacing = 6        ## Інтервал між кнопками навігації.
define gui.pref_spacing = 15             ## Відстань між групами параметрів.
define gui.pref_button_spacing = 0       ## Відстань між кнопками параметрів.
define gui.page_spacing = 0              ## Відстань між кнопками сторінок збережень.
define gui.slot_spacing = -20            ## Відстань між комірками збереження.
define gui.main_menu_text_xalign = 1.0   ## Позиція тексту головного меню.


################################################################################
## Рамки
################################################################################
##
## Вигляд рамок, що містять елементи інтерфейсу за відсутності
## накладення чи вікна.

define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)
define gui.frame_tile = False


################################################################################
## Смуги, смуги прокрутки та повзунки
################################################################################


## Висота горизонтальних / ширина вертикальних смуг.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## "True" — мозаїчне тло, "False" — лінійне масштабування.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальні межі.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Вертикальні межі.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Поведінка не прокручуваних смуг у меню гри: "hide" — приховати, "None" — показати.
define gui.unscrollable = "hide"


################################################################################
## Історія діалогів
################################################################################

## Скільки записів історії зберігає Ren'Py.
define config.history_length = 250

## Висота рядка (якщо None то висота буде встановлюватись автоматично).
define gui.history_height = None

## Відступ між рядками історії.
define gui.history_spacing = 30

## Позиція, ширина, вирівнювання імені персонажа в історії.
define gui.history_name_xpos = 233
define gui.history_name_ypos = -9
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Позиція, ширина, вирівнювання тексту діалогу в історії.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


################################################################################
## Режим NVL
################################################################################


define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_list_length = 6
define gui.nvl_height = 173
define gui.nvl_spacing = 15

define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


################################################################################
## Локалізація
################################################################################


## Правила переносу рядків. "unicode" підходить для більшості мов,
## включно з українською.
define gui.language = "unicode"