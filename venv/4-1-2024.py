import datetime
import string
import json

#do bash: cd //eos/STUDENTs$/334535/Desktop/pythonbegin
#usuwanie katalogu: rm -rf nazwakatalogu
#cat [nazwapliku]   -pokazuje co jest w pliku

# pip list  -lista zainstalowanych biblioek
# pip freeze -lista zainstalowanych biblioek z wersjami
# pip freeze > requirements.txt -lista zainstalowanych biblioek z wersjami wrzuca do pliku txt
# pip install -r requirements.txt   -instaluje wszystkie biblioteki  z pliku txt

#TESTOWANIE
# python -m venv test   -tworzy środowisko o nazwie "test", izoluje środowisko dla danego pliku
#source [nazwa środowiska ]/Scripts/activate   -uruchomienie środowiska
# deactivate    -deaktywuje srodowisko testowe
# pip unistall -r requirements.txt      -odinstalowuje biblioteki tylko dla środowiska testowego
# pip install -r requirements.txt   -instalowuje biblioteki tylko dla środowiska testowego
# python -m pytest [nazwaplikju do testowania]      -uruchomienie testu