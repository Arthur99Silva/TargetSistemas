def descobrir_proximo():
    # a)
    a = [1, 3, 5, 7]
    proximo_a = a[-1] + 2
    
    # b)
    b = [2, 4, 8, 16, 32, 64]
    proximo_b = b[-1] * 2
    
    # c)
    c = [0, 1, 4, 9, 16, 25, 36]
    proximo_c = (len(c))**2
    
    # d)
    d = [4, 16, 36, 64]
    proximo_d = (len(d) + 2)**2
    
    # e)
    e = [1, 1, 2, 3, 5, 8]
    proximo_e = e[-1] + e[-2]
    
    # f)
    f = [2, 10, 12, 16, 17, 18, 19]
    proximo_f = 21

    print(f"a) Próximo: {proximo_a}")
    print(f"b) Próximo: {proximo_b}")
    print(f"c) Próximo: {proximo_c}")
    print(f"d) Próximo: {proximo_d}")
    print(f"e) Próximo: {proximo_e}")
    print(f"f) Próximo: {proximo_f}")

descobrir_proximo()
