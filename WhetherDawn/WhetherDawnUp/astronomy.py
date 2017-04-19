from datetime import datetime

def getDawnTime(B, L, H, _date):
    '''
    @brief calculating sunrise time for the date _date in point with
    geodetic coordinates (B, L, H)

    @param B - point latitude
    @param L - point longitude
    @param H - point height
    '''
    return datetime(_date.year, _date.month, _date.day, 6, 0, 0)

def getNightfallTime(B, L, H, _date):
    '''
    @brief calculating sunset time for the date _date in point with
    geodetic coordinates (B, L, H)

    @param B - point latitude
    @param L - point longitude
    @param H - point height
    '''
    return datetime(_date.year, _date.month, _date.day, 22, 0, 0)
