define mc = Character("", color="#800000")
#screen name_input(prompt):##############Экран ввода
#    modal True
#    frame:
#        background Frame("#800000")
#        align(0.5,0.5)
#        xsize 350 ysize 250
#        vbox:
#            xfill True#Текст выравнивается относительно кнопки по горизонту
#            yfill True#Текст выравнивается относительно кнопки по вертикали
#            text prompt xalign 0.5
#            input id "input" xalign 0.5
#            hbox:
#                xalign 0.5
#                textbutton("Готово"):
#                    action Jump(" ")
label splashscreen:
    scene black
    pause(2)
    show text "Не смотри наверх" with Dissolve(2)
    pause(2)
    hide text with Dissolve(2)
    pause(1)
    return
label main_menu:#####Пропуск меню.
    $Start()
label start:
    # scene face with Dissolve(1.3)#Растерянное лицо героя
    scene black
    show face bordered:
        xalign 0.5
        yalign 0.25
    "Не смотри наверх."
    "Не смотри наверх."
    "Не смотри наверх."
    "Не {size=+10}cмотри{/size} наверх."
    "Не {size=+15}cм{/size}о{size=+12}три{/size} нав{size=+14}ерх{/size}."
    "В страхе я говорил себе."
    "Не знаю, сколько времени я уже сижу {vspace=15}с растерянным и испуганным лицом."
    "Мое тело не слушается меня, я долго {vspace=15}и неподвижно сидел в центре комнаты."
    "Воздух в комнате с каждой секундой {vspace=15}становился все тяжелее."
    "Если бы я и мог прямо сейчас убежать - мне {vspace=15}бы не хватило смелости."
    "Прямо сейчас..."
    "Взять и рвануть изо всех сил к выходу."
    "..."
    "Но мое тело не двигалось, как бы {vspace=15}сильно я этого не хотел."
    "..."
    "Я думал лишь об одном."
    "Нельзя смотреть наверх."
    "Иначе..."
    "Оно меня убьет."
    scene dead_family with Dissolve(3)#Окровавленная семья
    scene bloody_hands with Dissolve(2)#Трясущие руки
    scene hall with Dissolve(2)#коридор выбор комнат
    scene room1 #1 комната
    scene room2 #2 комната
    scene keys with Dissolve(1)#Ключ
    scene door_exit #входная дверь
    scene door_open #открывание двери
    scene shadow # тень монстра
    scene close_door # закрытие двери
    scene door_op #опирается на дверь
    scene eyes_up #Смотрит наверх
    scene screamer #скример
return
