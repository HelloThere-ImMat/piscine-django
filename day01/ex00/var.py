def my_var() :
    text = " has a type "

    var1 = 42
    print(f"{var1} {text} {type(var1)}")
    var2 = "42"
    print(f"{var2} {text} {type(var2)}")
    var3 = "quarante-deux"
    print(f"{var3} {text} {type(var3)}")
    var4 = 42.0
    print(f"{var4} {text} {type(var4)}")
    var5 = True
    print(f"{var5} {text} {type(var5)}")
    var6 = [42]
    print(f"{var6} {text} {type(var6)}")
    var7 = { 42 : 42}
    print(f"{var7} {text} {type(var7)}")
    var8 = (42,)
    print(f"{var8} {text} {type(var8)}")
    var9 = set()
    print(f"{var9} {text} {type(var9)}")

if __name__ == '__main__':
    my_var()