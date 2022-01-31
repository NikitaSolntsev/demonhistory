#define mc = Character("", color="#800000")
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
init:
    python:
        import math
        class Shaker(object):
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                self.child = child
            def __call__(self, t, sizes):
                # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                # в целые.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x
                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
                xpos = xpos - xanchor
                ypos = ypos - yanchor
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                return (int(nx), int(ny), 0, 0)
        def _Shake(start, time, child=None, dist=100.0, **properties):
            move = Shaker(start, child, dist=dist)
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)
        Shake = renpy.curry(_Shake)
    $ sshake = Shake((0, 0, 0, 0), 3.0, dist=10)
image face_animation:
    "face bordered"
    pause .5
    "face bordered2"
    pause .2
    "face bordered3"
    pause .2
    "face bordered"
    pause .5
    "face bordered4"
    pause .5
    "face bordered3"
    pause .5
    "face bordered2"
    pause .3
    "face bordered4"
    pause .5
    "face bordered"
    pause .5
    "face bordered3"
    pause .2
    "face bordered2"
    pause .2
    "face bordered"
    pause .5
    repeat
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
    scene black
    show face_animation with Dissolve(1):
        xalign 0.5
        yalign 0.25
    "Не смотри наверх."
    "Не смотри наверх."
    "{size=+10}Н{/size}е с{size=+10}мо{/size}три н{size=+10}аве{/size}рх." with sshake
    "Не {size=+10}cмотри{/size} наверх." with sshake
    "Не {size=+15}cм{/size}о{size=+12}три{/size} нав{size=+14}ерх{/size}." with sshake
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
    hide face_animation with Dissolve(2)
    show dead_family with fade(3):#Окровавленная семья
        xalign 0.5
        yalign 0.25
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
