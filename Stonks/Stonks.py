import yfinance as yf

print("Введите тикер:")
stonk = yf.Ticker(input())
rating = 0

print(stonk.info['longName'], "(", stonk.info['symbol'], ")" )
print("")

print("Buisness:")
print(stonk.info['longBusinessSummary'])
print("")

print("Main holders:")
print(stonk.institutional_holders[0:3])
print("")

if (stonk.info['netIncomeToCommon'] > 0):
    pe = stonk.info['trailingPE']

    print("P/E:", pe)
    print("Сколько лет займет окупаемость ваших вложений в рамках деятельности компании")
    print("Рыночная цена акции (P) / Прибыль на акцию (EPS)")
    print("")

    if (pe < 15):
        rating += 2
    elif (pe < 25):
        rating += 1

    if stonk.info['forwardPE']:
        fpe = stonk.info['forwardPE']

        print("Forward P/E:", fpe)
        print("Показатель Р/Е на будущий период, прогноз Р/Е")
        print("Рыночная цена акции (P) / Прогнозная прибыль на акцию (EPS)")
        print("")

        if (fpe < pe):
            rating += 2
        elif (fpe == pe):
            rating += 1

if stonk.info['priceToBook']:
    pb = stonk.info['priceToBook']

    print("P/B:", pb)
    print("Сколько вы платите за акцию по отношению к её стоимости по бухгалтерскому балансу")
    print("Рыночная цена акции (P) / Стоимость акции по бухгалтерскому балансу (В)")
    print("")

    if (pb < 1):
        rating += 2
    elif (pb < 3):
        rating += 1

if stonk.info['priceToSalesTrailing12Months']:
    ps = stonk.info['priceToSalesTrailing12Months']

    print("P/S:", ps)
    print("Оценивает компанию по объему продаж - сколько вы платите за $1 выручки")
    print("Рыночная стоимость компании/Доход")
    print("")

    if (ps < 1):
        rating += 2
    elif (ps < 3):
        rating += 1

if stonk.info['payoutRatio']:
    payout = stonk.info['payoutRatio']

    print("Payout:", payout*100, "%")
    print("% затрат компании на выплату дивидендов от прибыли")
    print("Дивиденды / Чистая прибыль * 100%")
    print("")

    if (payout < 0.5):
        rating += 2
    elif (pe < 0.7):
        rating += 1

if stonk.info['dividendRate']:
    dividend = stonk.info['dividendRate']

    print("Dividend:", stonk.info['dividendRate'] / stonk.info['regularMarketPrice'] * 100, '%')
    print("Годовой % выплаты дивидендов")
    print("")

    if (dividend > 5):
        rating += 2
    elif (dividend > 4):
        rating += 1

if stonk.info['pegRatio']:
    peg = stonk.info['pegRatio']

    print("PEG:", peg)
    print("Показатель переоцененности / недооцененности компании с учетом пронозируемого изменения прибыли на акцию")
    print("(P/E) / G (годовой прогноз роста EPS)")
    print("")

    if (peg < 1):
        rating += 2
    elif (peg == 1):
        rating += 1

print("Средняя оценка акции:", rating, "из 14")


