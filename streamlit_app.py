import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
from transformers import pipeline
from PIL import Image

# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

img = Image.open("logo.png")
st.image(img)

st.title('Zabawa z językiem naturalnym')

st.header('Wprowadzenie do zajęć')

st.subheader('O Streamlit')

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')

st.write('Ta aplikacja ma za zadanie odgadywać wydźwięk emocjonalny danego tekstu, oraz tłumaczyć język angielski na niemiecki')

st.subheader('Instrukcja obsługi')
st.write('W sekcji "przetwarzanie języka naturalnego" wybierz interesującą Cie opcję - badanie wydźwięku emocjonalnego, lub tłumacz z angielskiego na polski. wpisz w odpowiednim oknie tekst w języku angielskim, a następnie naciśnij ctrl+enter i poczekaj na wynik.')

st.subheader('Smaczki user experience')
st.write('Gdy będziesz czekał na przetłumaczenie wpisanego tekstu, pod polem tekstowym pojawi się:')
st.warning('Tłumaczę...')
st.write('Jeżeli algorytm nie zdoła przetłumaczyć Twojego tekstu na język niemiecki, wyświetli się informacja:')
st.error('Nie udało się')
st.write('Jeżeli tekst został poprawnie przetłumaczony, dostaniesz na ekranie masę balonów, wynik oraz informację:')
st.success('Zrobione')
st.write('Streamlit zwraca dane w formie słownika. Za sprawdzenie, czy wynik jest prawidłowy odpowiada kod:')
st.code("if answer[0]['translation_text'] == text:", language='python')
st.write('gdzie zmienna "text" przechowuje informację, jaką wpisaliśmy do okienka niżej.')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

st.header('Przetwarzanie języka naturalnego')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie języka angielskiego na niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

if option == 'Tłumaczenie języka angielskiego na niemiecki':
    text = st.text_area(label="Wpisz tekst")
    if text:
        if text == '':
            st.warninig('Wprowadź jakieś dane!')
        else:
            with st.spinner(text='Tłumaczę...'):
                translator = pipeline('translation_en_to_de')
                answer = translator(text)
                if answer[0]['translation_text'] == text:
                    st.error('Nie udało się')
                else:
                    st.balloons()
                    st.write(answer)
                    st.success('Zrobione')

st.subheader('Mój numer indeksu:')
st.write('s19567')
#st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
#st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
#st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
#st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
#st.write('🐞 Na końcu umieść swój numer indeksu')
#st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
#st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
