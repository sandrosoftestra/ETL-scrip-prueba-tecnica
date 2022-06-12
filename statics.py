def max(max_old, max_new):
    """
    Define el maximo
    """
    if max_old != True and max_new > max_old:
        return max_new
    elif max_old != True and max_new <= max_old:
        return max_old
    elif max_old == True:
        return max_new


def min(min_old, min_new):
    """
    Define el minimo
    """
    if min_old != True and min_new < min_old:
        return min_new
    elif min_old != True and min_new >= min_old:
        return min_old
    elif min_old == True:
        return min_new


def mean(media_old, media_new):
    """
    Define la media
    """
    if media_old == True:
        return media_new
    return (media_old+media_new)/2
