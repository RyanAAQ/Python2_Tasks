def converter(temperature, unit, threshold):

    if unit.lower() == "f":
        converted = (temperature - 32) * 5 / 9
        
    elif unit.lower() =="c":
        converted = (temperature * 9 / 5) + 32
        
    else:
        converted = (temperature * 9 / 5) + 32
        
    if converted < threshold:
        return "Cold advisory"
        
    else:
        return "Heat alert"
        
        
