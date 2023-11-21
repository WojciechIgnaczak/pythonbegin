# Instrukcje formatowania dat i czasu przy użyciu strftime() i strptime() są elastyczne. Dyrektywy najczęsciej używane przy formatowaniu:

# %Y : rokz pełną liczba cyfr "2023"
# %m : miesiąc jako liczba z zerem wiodących od 01 do 12
# %d dzien miesiaca z zerem wiodącym od 01 do 31
# %H godzina(zegar 24h) jako liczba z zerem wiodącym od 00 do 23
# %I godzina(zegar 12h) jako liczba z zerem wiodącym 0d 01 do 12
# %M minuta jako liczba z zerem wiodącym od 00 do 59
# %S sekunda jako liczba z zerem wiodącym od 00 do 59
# %f mikrosekundy jako liczba z zerem wiodącym od 000000 do 999999
#itd. wiecej na stronie w slack
# każda może byc użyta w metodzie strftime( ) do formatowania obiektu datetime w python lub w metodzie strptime() do parsowania stringu w celu utwozenia obiektu datetime
#strona do dyrektyw dat
https://man7.org/linux/man-pages/man3/strftime.3.html