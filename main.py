from client import Client
from vklad import SuperVklad, CapitalVklad


if __name__ == '__main__':
    ivan = Client('Иван Петров', 500000, 8, 12)
    elena = SuperVklad('Елена Петрова', 700000, 9, 12)
    ekaterina = SuperVklad('Екатерина Долгова', 66000, 8, 16)
    sergey = CapitalVklad('Сергей Иванов', 650000, 12, 14)

    print(ivan)
    print(ivan.vklad(), '\n')
    print(elena)
    print(elena.vklad(), '\n')
    print(ekaterina)
    print(ekaterina.vklad(), '\n')
    print(sergey)
    print(sergey.vklad(), '\n')


# 10.2.3. Банковские вклады
# Банк предлагает ряд вкладов для физических лиц:
# Срочный вклад: расчет прибыли осуществляется по формуле простых процентов;
# Бонусный вклад: бонус начисляется в конце периода как % от прибыли, если вклад больше определенной суммы;
# Вклад с капитализацией процентов.
# Реализуйте приложение, которое бы позволило подобрать клиенту вклад по заданным параметрам.
