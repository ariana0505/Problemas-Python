def _apply_iva(amount:float , iva:float):
    if iva == 0:
        iva = 21
    
    discount = amount * iva/100
    return discount

discount = _apply_iva(1342, 0)
print(discount)