def train_duration(distance):
    sr_speed = 70  # Средняя скорость легкового автомобиля
    time = distance / sr_speed
    return round(time, 2)


def fuel_consumption(weight):
    consumption = 5  # Средний расход топлива не груженной легковой машины
    sr_consumption = consumption + (consumption * (weight / 100))
    return round(sr_consumption, 2)


def train_cost(distance, weight):
    consumption = 5  # Средний расход топлива не груженной легковой машины
    sr_consumption = consumption + (consumption * (weight / 100))
    cost = ((distance / 100) * sr_consumption) * 52
    return round(cost, 2)
