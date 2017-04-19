# WhetherDawn
Django project for calculating times of sunsets, sunrises and, may be, with weather info.

There must be:

- sunsets;
- sunrises;
- weather info.

*We use simple astronomy formulas to calculate sunrise and sunset time for
any place on the Earth and some more complicated formulas to estimate how
light it will be in determined time.*

## How it works
We have four entities as the input data: three geodetic coordinates of
user's geoposition (B, L, H) and a date, when the event of sunset or
sunrise is to happen.

There are two functions in astronomy module that gives us sunset and
sunrise time:
- getDawnTime(B, L, H, date)
- getNightfallTime (B, L, H, date)

*Usually in geodesy B is a latitude, L is a longitude and H is a height of
a point placed on the Earth*

