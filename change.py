def makeChange(cents):
    if not(1 <= cents <= 100):
        return "Please Enter you amount again"
    
    rounded_cents = round(cents/5) * 5

    quarters = rounded_cents // 25
    remainder = rounded_cents % 25
    dime = remainder // 10
    remainder = remainder % 10
    nickel = remainder // 5

    if (quarters >= 1):
        result =  f"Quarters: {quarters}"

    if (dime >= 1):
        result = f"Quarters: {quarters} \nDime: {dime}"
    
    if (nickel >= 1):
        result = f"Quarters: {quarters} \nDime: {dime} \nNickel: {nickel}"

    return result

rounded_cents = makeChange(90)
print(rounded_cents)