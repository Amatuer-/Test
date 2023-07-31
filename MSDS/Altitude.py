def largestAltitude(gain):
    start = 0
    altitude = 0
    length = len(gain) - 1
    i = 0
    new = []
    new.append(start)
    # print(new)
    # new[0] = 0
    while i <= length:
        # print(i)
        altitude = altitude + gain[i]
        # print(altitude)
        new.append(altitude)

        i += 1

    return max(new)



if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    res = largestAltitude(gain)
    print(res)