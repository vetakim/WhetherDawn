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

def dms2rads(d, m, s):
    '''degrees, minutes, seconds to radians'''
    degs = d + m / MINUTES + s / SECONDS
    return radians(degs)

def getJDN(_date):
    '''get julian day by grigorian date'''
    a = trunc(( 14 - _date.month ) / 12)
    # years since March 1 -4800
    y = _date.year + JULIANYEAR - a
    # months since March 1 -4800
    m = _date.month + MONTHES * a - MARCH
    jdn = _date.day + (153 * m + 2) / 5 + y * 365.2425 - 32045
    return trunc(jdn)

def getSunHourAngle(phi, _lambda, H):
    '''getting the sun hour angle'''
    # altitude of the center of the solar disc
    delta = asin(sin(_lambda) * sin(radians(23.44)))
    a = -radians(0.83)
    # hour angle with refraction
    w = acos((sin(a) - sin(phi) * sin(delta)) / cos(phi) / cos(delta))
    # hour angle with observer's elevation correction
    w += radians(-2.076) * sqrt(H) / radians(60)
    return w

def getJulianTransit(_date, L):
    '''get julian transit'''
    # mean solar noon
    J = getJDN(_date) - degrees(L) / GRADUSES
    # solar mean anomaly
    M = ((357.5291 + 0.98560028 * J) % GRADUSES)
    # equation of the center
    C = 1.9148 * sin(M) + 0.0200 * sin(2 * M) + 0.0003 * sin(3 * M)
    # ecliptic longitude
    la = (( M + C + HALFGRADUSES + PERIHELION ) % GRADUSES)
    # solar transit
    Jtr = MIDNIGHT + J + 0.0053 * sin(M) - 0.0069 * sin(2 * la)
    return Jtr

def getDawnTime(B, L, H, _date):
    '''
    @brief calculating sunrise time for the date _date in point with
    geodetic coordinates (B, L, H)

    @param B - point latitude
    @param L - point longitude
    @param H - point height
    '''
    dawn = getJulianTransit(_date, L) - getSunHourAngle(B, L, H)
    return datetime.fromtimestamp( ( dawn - 2440587.5 ) * 86400)

def getNightfallTime(B, L, H, _date):
    '''
    @brief calculating sunset time for the date _date in point with
    geodetic coordinates (B, L, H)

    @param B - point latitude
    @param L - point longitude
    @param H - point height
    '''
    fall = getJulianTransit(_date, -L) + getSunHourAngle(B, L, H)
    return datetime.fromtimestamp( ( fall - 2440587.5 ) * 86400)

