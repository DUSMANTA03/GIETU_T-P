def forex(inr,forex):
    if forex=="euro":
        print(inr*0.01417)
    elif forex=="pound":
        print(inr*0.0100)
    elif forex=="dollar":
        print(inr*0.2140)
    else:
        print(-1)
forex(10000,"euro")
forex(300,"pound")
forex(300,"dollar")
forex(300,"yen")
