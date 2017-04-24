from datetime import datetime
from math import *

JULIANYEAR = 4800
MONTHES = 12
MARCH = 3
MINUTES = 60
GRADUSES = 360
HALFGRADUSES = 180
SECONDS = 3600
PERIHELION = 102.9372
MIDNIGHT = 2451545.5

def juliantime2unix(jd):
    '''converting julian date to unix time'''
    return ( jd - 2440587.5 ) * 86400

def dms2rads(d, m, s):
    '''degrees, minutes, seconds to radians'''
    degs = d + m / MINUTES + s / SECONDS
    return radians(degs)

def rads2dms(rads):
    mindeg = modf(degrees(rads))
    deg = mindeg[1]
    secmin = modf(mindeg[0] * 60)
    minutes = secmin[1]
    sec = secmin[0] * 60
    return deg, minutes, sec


def getJDN(_date):
    '''get julian day by grigorian date'''
    a = ( 14 - _date.month ) // 12
    # years since March 1 -4800
    y = _date.year + JULIANYEAR - a
    # months since March 1 -4800
    m = _date.month + MONTHES * a - MARCH
    jdn = _date.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn

def getSunHourAngle(B, EL, H):
    '''getting the sun hour angle'''
    delta = asin(sin(EL) * sin(radians(23.44)))
    a = radians(-0.83 - 2.076 * sqrt(H) / 60)
    # hour angle with refraction
    w = acos((sin(a) - sin(B) * sin(delta)) / cos(B) / cos(delta))
    return w

def getJulianTransit(_date, L):
    '''get julian transit'''
    # mean solar noon
    n = getJDN(_date) - MIDNIGHT + 0.0008
    J = n - degrees(L) / GRADUSES
    # solar mean anomaly
    M = (357.5291 + 0.98560028 * J) % GRADUSES
    M = radians(M)
    # equation of the center (graduses yielded)
    C = 1.9148 * sin(M) + 0.0200 * sin(2 * M) + 0.0003 * sin(3 * M)
    # ecliptic longitude
    M = degrees(M)
    la = ( M + C + 180 + 102.9372 ) % 360
    # solar transit
    M, C, la = radians(M), radians(C), radians(la)
    Jtr = MIDNIGHT + J + 0.0053 * sin(M) - 0.0069 * sin(2 * la)
    return Jtr, la

def getDawnTime(B, L, H, _date):
    '''
    @brief calculating sunrise time for the date _date in point with
    geodetic coordinates (B, L, H)

    @param B - point latitude
    @param L - point longitude
    @param H - point height
    '''
    jtr, el = getJulianTransit(_date, L)
    w = getSunHourAngle(B, el, H)
    dawn = jtr - degrees(w) / GRADUSES
    return datetime.fromtimestamp(juliantime2unix(dawn))

def getNightfallTime(B, L, H, _date):
    '''
    @brief calculating sunset time for the date _date in point with
    geodetic coordinates (B, L, H)

    @param B - point latitude
    @param L - point longitude
    @param H - point height
    '''
    jtr, el = getJulianTransit(_date, L)
    w = getSunHourAngle(B, el, H)
    fall = jtr + degrees(w) / GRADUSES
    return datetime.fromtimestamp(juliantime2unix(fall))


