salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

total_needed_capital = 0

for monthq in range(months):
    if monthq > 0:
        spend *= (1 + increase)

    needed_money = spend - salary

    if needed_money > 0:
        total_needed_capital += needed_money

total_needed_capital = round(total_needed_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_needed_capital)
