mablagh_kharid = int(input("mablagh kharid khodra vared konid:\n"))

if mablagh_kharid<20000:
    print("mablagh kharid shoma kamtar az 20000")
    print("shoma shamel takhfif nemishavid!")
    print(mablagh_kharid)
elif 20000<=mablagh_kharid<=50000:
    print("shoma shamel %10 takhfif shodid")
    mablagh_kharid = 9/10*(mablagh_kharid)
    print(int(mablagh_kharid))
else:
    print("shoma shamel %20 takhfif shodid!")
    mablagh_kharid = 4/5*(mablagh_kharid)
    print(int(mablagh_kharid))