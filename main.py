sonar = 0
cuteBot.forward()

def on_forever():
    global sonar
    sonar = cuteBot.ultrasonic(cuteBot.SonarUnit.INCHES)
    if sonar > 2 and sonar < 15:
        basic.pause(2000)
        cuteBot.motors(randint(-50, -100), 0)
        basic.pause(500)
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(30, 0)
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(0, 30)
    elif cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        cuteBot.motors(30, 300)
    else:
        pass
basic.forever(on_forever)
