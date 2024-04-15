from appJar import *


##
start = gui("6 Лабораторная работа, 4 вариант")
start.setSize("800x600")
start.addLabel("lb1", "Ниже представленные три кнопки с выбором типа автомобиля")
start.addLabel("lb2", "Заполнив необходимые данные вы получите расчет расхода топлива, "
                      "длительность и стоимость поезди")
##

##
start.addLabel("leg", "Загрузка  - 0.0")
start.addLabel("rost", "Расстояние(км) - 0.0")
start.addLabel("l1", "Расход топлива составит - 0.0, cтоимость "
                     "и время поездки составляет - 0.0, руб. и 0.0 ч. соответственно ")
start.setLabelBg("l1", "orange")
##


def leg_avt(win):
    import a_car
    ##
    start.setLabel("leg", "Загрузка автомобиля - 0.0")
    start.setLabel("rost", "Расстояние(км) - 0.0")
    ##

    def ves(name):
        weight = float(start.getScale("Загрузка автомобиля(кг)"))
        distance = float(start.getScale("Расстояние(км)"))
        start.setLabel("leg", f"Загрузка автомобиля - {weight}")
        start.setLabel("rost", f"Расстояние(км) - {distance}")
        a_car.train_duration(distance)
        a_car.fuel_consumption(weight)
        start.setLabel("l1", f"Расход топлива составит - {a_car.fuel_consumption(weight)}, время поездки и стоимость "
                             f"составляет - {a_car.train_duration(distance)} ч., {round((distance / 100) * a_car.fuel_consumption(weight) * 52, 2)} руб. соответственно")
        return weight

    ##
    start.clearAllScales(callFunction=False)
    ##
    start.addLabelScale("Загрузка автомобиля(кг)")
    start.setScaleRange("Загрузка автомобиля(кг)", 0, 350)
    start.showScaleIntervals("Загрузка автомобиля(кг)", 25)
    start.showScaleValue("Загрузка автомобиля(кг)", show=True)
    start.setScaleBg("Загрузка автомобиля(кг)", "green")
    ##

    ##
    start.addLabelScale("Расстояние(км)")
    start.setScaleRange("Расстояние(км)", 0, 700)
    start.showScaleIntervals("Расстояние(км)", 100)
    start.showScaleValue("Расстояние(км)", show=True)
    start.setScaleBg("Расстояние(км)", "green")
    ##
    start.setScaleChangeFunction("Загрузка автомобиля(кг)", ves)
    start.setScaleChangeFunction("Расстояние(км)", ves)
    ##


def gruz_avt(win):
    import truck

    ##
    start.setLabel("leg", "Загрузка грузовика - 0.0")
    start.setLabel("rost", "Расстояние(км) - 0.0")
    ##

    def gruz(name):
        weight = float(start.getScale("Загрузка грузовика(кг)"))
        distance = float(start.getScale("Расстояние(км)(грз)"))
        start.setLabel("leg", f"Загрузка грузовика - {weight}")
        start.setLabel("rost", f"Расстояние(км) - {distance}")
        truck.train_duration(distance)
        truck.fuel_consumption(weight)
        start.setLabel("l1", f"Расход топлива составит - {truck.fuel_consumption(weight)}, время поездки и стоимость "
                             f"составляет - {truck.train_duration(distance)} ч., {round((distance / 100) * truck.fuel_consumption(weight) * 52, 2)} руб. соответственно")
        return weight

    ##
    start.addLabelScale("Загрузка грузовика(кг)")
    start.setScaleRange("Загрузка грузовика(кг)", 0, 350)
    start.showScaleIntervals("Загрузка грузовика(кг)", 25)
    start.showScaleValue("Загрузка грузовика(кг)", show=True)
    ##

    ##
    start.addLabelScale("Расстояние(км)(грз)")
    start.setScaleRange("Расстояние(км)(грз)", 0, 1500)
    start.showScaleIntervals("Расстояние(км)(грз)", 100)
    start.showScaleValue("Расстояние(км)(грз)", show=True)
    ##

    ##
    start.clearAllScales(callFunction=False)
    start.setScaleChangeFunction("Загрузка грузовика(кг)", gruz)
    start.setScaleChangeFunction("Расстояние(км)(грз)", gruz)
    ##


def pas_avt(win):
    import passenger_car

    ##
    start.setLabel("leg", "Загрузка пассажирского автомобиля(кг) - 0.0")
    start.setLabel("rost", "Расстояние(км) - 0.0")
    ##

    def ves(name):
        weight = float(start.getScale("Загрузка пассажирского автомобиля(кг)"))
        distance = float(start.getScale("Расстояние(км)(пас)"))
        start.setLabel("leg", f"Загрузка пассажирского автомобиля(кг) - {weight}")
        start.setLabel("rost", f"Расстояние(км) - {distance}")
        passenger_car.train_duration(distance)
        passenger_car.fuel_consumption(weight)
        start.setLabel("l1", f"Расход топлива составит - {passenger_car.fuel_consumption(weight)}, время поездки и стоимость "
                             f"составляет - {passenger_car.train_duration(distance)} ч., {round((distance / 100) * passenger_car.fuel_consumption(weight) * 52, 2)} руб. соответственно")
        return weight

    ##
    start.clearAllScales(callFunction=False)
    start.addLabelScale("Загрузка пассажирского автомобиля(кг)")
    start.setScaleRange("Загрузка пассажирского автомобиля(кг)", 0, 350)
    start.showScaleIntervals("Загрузка пассажирского автомобиля(кг)", 25)
    start.showScaleValue("Загрузка пассажирского автомобиля(кг)", show=True)
    start.setScaleBg("Загрузка пассажирского автомобиля(кг)", "red")
    ##

    ##
    start.addLabelScale("Расстояние(км)(пас)")
    start.setScaleRange("Расстояние(км)(пас)", 0, 500)
    start.showScaleIntervals("Расстояние(км)(пас)", 100)
    start.showScaleValue("Расстояние(км)(пас)", show=True)
    start.setScaleBg("Расстояние(км)(пас)", "red")

    ##
    start.setScaleChangeFunction("Загрузка пассажирского автомобиля(кг)", ves)
    start.setScaleChangeFunction("Расстояние(км)(пас)", ves)
    ##


start.addButtons(["Легковой", "Грузовой", "Пассажирский"], [leg_avt, gruz_avt, pas_avt])

##
start.go()
start.stop()