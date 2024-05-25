def temp_convert(temp,unit):
    if unit=='c'or unit=='C':
        f=(9*temp+160)/5
        k=temp+273
        print(f"{temp}degree celcius={f}degree fahrenheit")
        print(f"{temp}degree celcius={k}degree kelvin")
    elif unit=='f' or unit=='F':
        c=(temp-32)*5/9
        k=(temp-32)*5/9+273
        print(f"{temp}degree fahrenheit={c}degree celcius")
        print(f"{temp}degree fahrenheit={k}degree kelvin")
    elif unit=='k' or unit=='K':
        c=(temp-273)
        f=(temp-273)*9/5+32
        print(f"{temp}degree kelvin={c}degree celcius")
        print(f"{temp}degree kelvin={f}degree fahrenheit")
temp=float(input("Enter temp:"))
unit=input("Enter unit of measure:")
temp_convert(temp,unit)
