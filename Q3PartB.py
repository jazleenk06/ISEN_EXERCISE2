def reactor_core_warning(core_temp):
    result =""
    if core_temp < 300:
        result = "Danger! Core temp too low"
    elif core_temp < 650:
        result  = "Warning! Core temp low. Decreased efficiency."
    elif core_temp < 800:
        result = "Reactor core operating at standard temperatures"
    elif core_temp < 950:
        result = "Reactor core operating at increased temperatures"
    elif core_temp < 1100:
        result = "Warning! Core temp High. Deploy control rods."
    else:
        result = "Danger! Core temp too high"

    return result