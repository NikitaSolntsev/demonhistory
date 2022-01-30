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
    show text "Не смотри вверх" with Dissolve(2)
    pause(2)
    hide text with Dissolve(2)
    pause(1)
    return
label main_menu:#####Пропуск меню.
    $Start()
label start:
    "Я не должен смотреть вверх."
    " "
