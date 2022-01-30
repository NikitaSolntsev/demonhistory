define m = DynamicCharacter("name", color="#c8ffc8")
screen name_input(prompt):
    modal True
    frame:
        background Frame("#800000")
        align(0.5,0.5)
        xsize 250 ysize 250
        vbox:
            xfill True#Текст выравнивается относительно кнопки по горизонту
            yfill True#Текст выравнивается относительно кнопки по вертикали
            text prompt xalign 0.5
            input id "input" xalign 0.5
            hbox:
                xalign 0.5
                textbutton("Готово"):
                    action Jump("begin")
label start:
    $ name = renpy.input("Введи имя: ", screen = "name_input", length=10)
    return
label begin:
    ""
    return
