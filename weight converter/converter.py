def convertkilograms(from_unit, weight):
    if from_unit == "g":
        weight = weight/1000;
    elif from_unit == "lbs":
        weight = weight*0.45359237;
    elif from_unit == "oz":
        weight = weight*0.0283495;
    elif from_unit == "kg":
        pass;
    else:
        return None;
    return weight;


def result(output, to_unit):
    if to_unit == "g":
        output = output*1000;
    elif to_unit == "lbs":
        output = output*2.20462;
    elif to_unit == "oz":
        output = output*35.27396195;
    elif to_unit == "kg":
        pass;
    else:
        return None;
    return output;

    