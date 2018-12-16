def growing_plant(upSpeed, downSpeed, desiredHeight):
    ph = 0
    count = 0
    if (ph == desiredHeight):
        return 1
    else:
        while ph < desiredHeight:
            ph+=upSpeed
            if (ph >= desiredHeight):
                count+=1
                break
            else:
                ph-=downSpeed
                count+=1
    return count
