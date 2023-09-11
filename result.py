def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}",end="")


def dollars_to_float(d):  
    t  = d.strip()
    t2 = t.replace("$"," ")
    r=float(t2)
    return (r)


def percent_to_float(p):
    y  = p.strip()
    y2 = y.replace("%", " ")
    r=float(y2)
    return (r/100)

main()
