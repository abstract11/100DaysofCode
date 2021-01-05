print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pep_s = 2
pep_m_l = 3
ex_ch = 1
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            b1 = small_pizza + pep_s + ex_ch
            print(f"Your final bill is: ${b1}")
        else:
            b1 = small_pizza + pep_s
            print(f"Your final bill is: ${b1}")
    else:
        b1 = small_pizza
        print(f"Your final bill is: ${b1}")

if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            b1 = medium_pizza + pep_m_l + ex_ch
            print(f"Your final bill is: ${b1}")
        else:
            b1 = medium_pizza + pep_m_l
            print(f"Your final bill is: ${b1}")
    else:
        b1 = medium_pizza
        print(f"Your final bill is: ${b1}")

if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            b1 = large_pizza + pep_m_l + ex_ch
            print(f"Your final bill is: ${b1}")
        else:
            b1 = large_pizza + pep_m_l
            print(f"Your final bill is: ${b1}")
    else:
        b1 = large_pizza
        print(f"Your final bill is: ${b1}")
