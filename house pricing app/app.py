# import html
import folium.map
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import folium
import geopandas as gpd
from streamlit_folium import st_folium
from folium import  LayerControl
from folium.plugins import Draw
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from shapely.geometry import shape
from joblib import load
import plotly.graph_objects as go
import plotly.express as px
import category_encoders as ce
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import io
import pandas as pd
import category_encoders as ce





class HousingApp:
    
    def __init__(self):
        # Load the machine learning model once during initialization

        try:
            st.session_state.model = load('./model/final-units-only-rf-regression v1.7.pk1')
            print("Model loaded successfully with joblib.")
        except Exception as e:
            print(f"Error loading file with joblib: {e}")

        self.map_html = "map.html"
        self.df = pd.DataFrame(
        {'lat': [30.0444] ,  
        'lon': [31.2357] } 
    )
        self.inputs = {}
   
        pass
        # coordinates for each center
        self.center_coords = {
            "Cairo": {
                "Hadayek Al Zaiton": [30.0716, 31.2911],
                "El Shorouk": [30.2388, 31.5543],
                "El Marg": [30.1394, 31.3062],
                "Maadi Degla": [29.9826, 31.2326],
                "Abaseya": [30.0901, 31.2503],
                "New Nozha": [30.1063, 31.2842],
                "Dar Al Salam": [30.0764, 31.2375],
                "Al Kalaa": [30.0913, 31.2542],
                "Basateen": [30.0979, 31.2548],
                "Abdo Basha": [30.0904, 31.2782],
                "Nasr City": [30.0866, 31.3074],
                "15th Of May City": [30.0402, 31.2364],
                "5th Settlement": [30.0172, 31.3237],
                "Heliopolis": [30.0746, 31.3354],
                "3rd Settlement": [30.0195, 31.3288],
                "Ezbet El Nakhl": [30.1042, 31.2828],
                "Katamiah": [30.0659, 31.2774],
                "El Herafieen": [30.0595, 31.2338],
                "Down Town": [30.0444, 31.2357],
                "New Maadi": [29.9843, 31.2304],
                "Zamalek": [30.0500, 31.2210],
                "1st Settlement": [30.0205, 31.3226],
                "Helwan": [29.9784, 31.2354],
                "Al Zeitoun": [30.0803, 31.2712],
                "Masaken Sheraton": [30.1177, 31.3048],
                "Hadayek Helwan": [29.9740, 31.2375],
                "Ghamrah": [30.0868, 31.2476],
                "Rod El Farag": [30.1017, 31.2417],
                "Al Matareya": [30.0867, 31.2577],
                "Al Kasr Al Einy": [30.0498, 31.2362],
                "New Cairo-1": [30.0205, 31.3226],
                "Ain Shams": [30.0704, 31.2590],
                "Garden City": [30.0438, 31.2378],
                "Mirage City": [30.0172, 31.3154],
                "Amiria": [30.0664, 31.2566],
                "Al Azhar": [30.0426, 31.2585],
                "Sayeda Zeinab": [30.0522, 31.2344],
                "Almaza": [30.0784, 31.3314],
                "Fustat": [30.0466, 31.2330],
                "Hadayek Maadi": [29.9890, 31.2302],
                "Al Rehab": [30.0178, 31.3195],
                "Al Moski": [30.0430, 31.2367],
                "Manial Al Rodah": [30.0670, 31.2232],
                "Maadi": [29.9794, 31.2310],
                "El Tahrir": [30.0444, 31.2357],
                "New El Marg": [30.1394, 31.3062],
                "Gesr Al Suez": [30.1048, 31.2848],
                "Abdeen": [30.0415, 31.2363],
                "Mokattam": [29.9720, 31.2354],
                "Al Salam City": [30.0265, 31.2384],
                "Misr El Kadima": [30.0545, 31.2381],
                "Helmiet Elzaitoun": [30.0692, 31.2476],
                "Al Daher": [30.0852, 31.2542],
                "Hadayek Al Qobah": [30.0457, 31.2364],
                "Shubra": [30.1074, 31.2440],
                "Cornish Al Nile": [30.0444, 31.2357],
                "Badr City": [30.0426, 31.2387],
                "Ramsis": [30.0480, 31.2359],
                "Madinty": [30.0465, 31.2364],
                "Helmeya": [30.0530, 31.2371]
            },
            "Giza": {
                "6th of October": [29.9786, 31.0720],
                "Mansoureya": [29.9362, 31.0193],
                "Hawamdya": [29.8731, 31.0412],
                "Tirsa": [29.8921, 31.0504],
                "Abou Rawash": [29.9514, 31.1073],
                "Omraneya": [29.9380, 31.0396],
                "Smart Village": [29.9876, 31.0472],
                "Kerdasa": [29.9815, 31.0901],
                "Saft El Laban": [29.9658, 31.0293],
                "Dokki": [30.0380, 31.2176],
                "Al Saf": [29.9123, 31.0451],
                "Sheikh Zayed": [29.9835, 31.0472],
                "Sakiat Mekki": [29.9268, 31.0213],
                "Mohandessin": [30.0455, 31.2162],
                "Al Kom Al Ahmer": [29.9196, 31.0525],
                "Imbaba": [30.0368, 31.2171],
                "Bolak Al Dakrour": [29.9658, 31.2054],
                "Al Monib": [30.0663, 31.2187],
                "Berak Alkiaam": [29.9523, 31.0541],
                "Al Moatamadia": [29.9724, 31.0745],
                "Shabramant": [29.9321, 31.0604],
                "Warraq": [30.0667, 31.2292],
                "Giza": [30.0444, 31.2357],
                "Manial": [30.0676, 31.2211],
                "Haram": [29.9833, 31.1333],
                "Agouza": [30.0597, 31.2128],
                "Faisal": [29.9851, 31.1370],
                "Al Wahat": [29.9457, 31.0684],
                "Hadayeq El Ahram": [29.9544, 31.0853],
                "Aossim": [29.9726, 31.0904],
                "Al Nobariah": [29.9586, 31.0447],
                "Badrashin": [29.9523, 31.0651],
                "Kit Kat": [29.9745, 31.2216],
                "Al Barageel": [29.9611, 31.0667],
                "Al Manashi": [29.9586, 31.0651]
            },
            "Alexandria": {
                "Miami": [30.0206, 31.2181],
                "Smouha": [30.0457, 31.2168],
                "Abees": [30.0495, 31.2283],
                "Alexandria": [29.9187, 31.2001],
                "Sedi Gaber": [30.0361, 31.2133],
                "El Borg El Kadem": [29.9338, 31.2147],
                "Sedi Bisher": [30.0416, 31.2133],
                "Al Bitash": [30.0700, 31.2235],
                "Stanly": [30.0706, 31.2130],
                "El-Agamy": [29.9550, 31.2492],
                "San Stefano": [30.0588, 31.2230],
                "Mahtet El-Raml": [29.9177, 31.2028],
                "Al A'mriah": [30.0168, 31.2210],
                "Kafr Abdu": [30.0287, 31.2055],
                "El-Montazah": [30.0056, 31.2450],
                "El Mahrousa": [29.9307, 31.2080],
                "El-Max": [29.9741, 31.2322],
                "El Aseel": [30.0484, 31.2273],
                "El Wabour": [30.0289, 31.2261],
                "El Mandara": [30.0204, 31.2368],
                "Bacchus": [30.0111, 31.2090]
            },
            "Qalyubia": {
                "Benha": [30.4598, 31.1857],
                "Shibin El Kom": [30.5701, 31.1590],
                "Tukh": [30.5521, 31.1083],
                "Qalyub": [30.4118, 31.2204],
                "Kafr Shokr": [30.4345, 31.1826],
                "El-Khanka": [30.2668, 31.3390],
                "Qaha": [30.2873, 31.3053],
                "Shebin El Koom": [30.5700, 31.1590],
                "Kafr El Sheikh": [30.4557, 31.1831],
                "Toukh": [30.5521, 31.1083],
                "El-Khanka": [30.2668, 31.3390],
                "El-Khanka": [30.2668, 31.3390],
                "Shibin El Kom": [30.5701, 31.1590],
                "Benha": [30.4598, 31.1857],
                "Qalyub": [30.4118, 31.2204],
                "Kafr Shokr": [30.4345, 31.1826],
                "El-Khanka": [30.2668, 31.3390],
                "Toukh": [30.5521, 31.1083],
                "El-Khanka": [30.2668, 31.3390]
            },
            "Al Fayoum": {
                "Sonores": [29.3035, 30.8272],
                "Ebshoy": [29.3061, 30.7730],
                "Kofooer Elniel": [29.3420, 30.8060],
                "New Fayoum": [29.3056, 30.8261],
                "Atsa": [29.2925, 30.8445],
                "Sanhoor": [29.2752, 30.7954],
                "Tameaa": [29.2912, 30.7940],
                "Al Fayoum": [29.3031, 30.8457],
                "Sersenaa": [29.3083, 30.7961],
                "El Aagamen": [29.3120, 30.8143],
                "Manshaa Abdalla": [29.2847, 30.8219],
                "Youssef Sadek": [29.2956, 30.8346],
                "Manshaa Elgamal": [29.3097, 30.7952]
            },
            "Al Gharbia": {
                "Alsanta": [30.8383, 31.1749],
                "Al Mahala Al Kobra": [30.9532, 31.1461],
                "Al Gharbia": [30.8203, 31.1727],
                "Samanood": [30.8271, 31.1643],
                "Tanta": [30.7774, 31.0087],
                "Qotoor": [30.8327, 31.1652],
                "Zefta": [30.7862, 31.0893],
                "Basyoon": [30.8632, 31.1144],
                "Kafr Alziat": [30.7883, 31.0738]
            },
            "Al Meniya": {
                "Minya": [30.7519, 28.1154],
                "Samaloot": [30.7850, 28.0600],
                "Eladwa": [30.7733, 28.0900],
                "Mghagha": [30.7820, 28.1783],
                "Matai": [30.7481, 28.1706],
                "Malawi": [30.6605, 28.0833],
                "Bani Mazar": [30.7265, 28.2328],
                "Dermwas": [30.7656, 28.2069],
                "Abo Korkas": [30.7583, 28.1900]
            },
            "Al Monufia": {
                "Shohada": [30.5413, 30.5975],
                "Menoof": [30.5265, 30.6547],
                "Tala": [30.5713, 30.7166],
                "Shebin El Koom": [30.5833, 30.7666],
                "Sadat City": [30.3758, 30.5683],
                "Al Monufia": [30.5000, 30.6000],
                "Quesna": [30.5208, 30.7400],
                "Berket Al Sabei": [30.5166, 30.8200],
                "Ashmoon": [30.5900, 30.7800]
            },
            "Al Sharqia": {
                "Al Salhiya Al Gedida": [30.6066, 31.5969],
                "Abu Hammad": [30.6783, 31.5092],
                "Abu Kbeer": [30.6472, 31.3900],
                "Hehya": [30.6000, 31.4000],
                "Awlad Saqr": [30.6166, 31.2500],
                "Al Hasiniya": [30.5000, 31.4000],
                "Faqous": [30.5500, 31.4500],
                "Darb Negm": [30.6666, 31.5833],
                "Al Ibrahimiya": [30.5666, 31.6666],
                "Zakazik": [30.5828, 31.4694],
                "Kafr Saqr": [30.6333, 31.2833],
                "Mashtool Al Sooq": [30.5564, 31.2978],
                "Belbes": [30.6166, 31.0500],
                "Meniya Alqamh": [30.6778, 31.2500],
                "Al Sharqia": [30.5666, 31.5833],
                "10th of Ramdan City": [30.5600, 31.4600]
            },
            "Aswan": {
                "Aswan": [32.8860, 24.0889],
                "Draw": [32.8872, 24.0994],
                "El Klabsha": [32.8900, 24.0900],
                "Al Sad Al Aali": [32.8725, 24.0950],
                "Abu Simbel": [32.8833, 22.3333],
                "Nasr Elnoba": [32.8666, 23.2500],
                "Edfo": [32.8761, 24.5275],
                "Markaz Naser": [32.8700, 24.0666],
                "Kom Ombo": [32.9644, 24.1550]
            },
            "Asyut": {
                "Dayrout": [31.1814, 27.0872],
                "Asyut": [31.1851, 27.1817],
                "El Qusya": [31.2494, 27.1561],
                "Assuit Elgdeda": [31.2278, 27.2478],
                "Elfath": [31.2181, 27.2383],
                "El Ghnayem": [31.1878, 27.0983],
                "Sahel Selim": [31.2725, 27.1561],
                "Abnoub": [31.2394, 27.2856],
                "El Badari": [31.2383, 27.1231],
                "Abou Teag": [31.2058, 27.2972],
                "Serfa": [31.2078, 27.2225],
                "Manflout": [31.1894, 27.2900]
            },
            "Bani Souaif": {
                "Bani Souaif": [32.4383, 29.0861],
                "El Wastaa": [32.4622, 29.0269],
                "El Korimat": [32.4106, 29.0733],
                "El Fashn": [32.4583, 29.1386],
                "Naser": [32.4500, 29.1000],
                "Ahnaseaa": [32.4256, 29.0858],
                "New Bani Souaif": [32.4300, 29.0800],
                "Bebaa": [32.4328, 29.0706],
                "Smostaa": [32.4400, 29.0950]
            },
            "Damietta": {
                "Kafr Saad": [31.5367, 31.7486],
                "Ras El Bar": [31.4236, 31.8483],
                "Fareskor": [31.4783, 31.7400],
                "Al Zarkah": [31.4986, 31.7592],
                "Damietta": [31.8161, 31.8214],
                "New Damietta": [31.8028, 31.8258]
            },
            "Ismailia": {
                "Elsalhia Elgdida": [30.5911, 32.2522],
                "Al Kasaseen": [30.6278, 32.2536],
                "Abo Sultan": [30.6061, 32.2861],
                "El Tal El Kebir": [30.6900, 32.2222],
                "Abu Swer": [30.6214, 32.2678],
                "Qantara Gharb": [30.6792, 32.3086],
                "Qantara Sharq": [30.6475, 32.2828],
                "Nfeesha": [30.6769, 32.2833],
                "Ismailia": [30.5892, 32.2661],
                "Srabioom": [30.5819, 32.2556],
                "Fayed": [30.6111, 32.3800]
            },
            "Kafr El Sheikh": {
                "Hamool": [31.1128, 30.9700],
                "Kafr El Sheikh": [31.1161, 30.9661],
                "Al Riadh": [31.1719, 30.9556],
                "Qeleen": [31.1414, 30.9208],
                "Desouq": [31.1742, 30.9206],
                "Seedy Salem": [31.1833, 30.9300],
                "Bela": [31.2078, 30.9406],
                "Fooh": [31.1350, 30.9361],
                "Metobas": [31.1242, 30.9306],
                "Borollos": [31.1656, 30.9347],
                "Balteem": [31.1683, 30.9536]
            },
            "Luxor": {
                "El Karnak": [25.7219, 32.6286],
                "El Korna": [25.7192, 32.6244],
                "Armant Sharq": [25.7083, 32.5794],
                "Esnaa": [25.5444, 32.7122],
                "Luxor": [25.6872, 32.6394],
                "Armant Gharb": [25.7006, 32.5708]
            },
            "Matrooh": {
                "Matrooh": [31.3542, 27.2414],
                "El Hamam": [31.1450, 27.0878],
                "Sidi Barrani": [31.0914, 27.0000],
                "Fuka": [31.3061, 27.2592],
                "El Alamein": [30.8494, 27.9894]
            },
            "New Valley": {
                "Kharga": [25.4394, 30.5331],
                "Dakhla": [25.6411, 28.6222],
                "Baris": [25.5911, 29.4772],
                "Farafra": [25.6222, 27.9686],
                "Paris": [25.5661, 30.4811],
                "El Kharga": [25.4372, 30.5325]
            },
            "محافظه بورسعيد": {
                "Qesm El Zohor": [31.26065, 32.265987],
                "Qesm El Shark": [31.2670, 32.3120],
                "Qesm El Arab": [31.263805, 32.296114],
                "Qesm El Manakh": [31.265639, 32.284398],
                "Qesm El Manasra West Port Said": [31.287426, 32.211485],
                "قسم اول بورفؤاد": [31.246709, 32.319975]
            },
            "Red Sea": {
                "Hurghada": [27.2572, 33.8125],
                "El Gouna": [27.3972, 33.6611],
                "Quseir": [26.1806, 34.2361],
                "Safaga": [26.7594, 33.9664],
                "Marsa Alam": [25.0000, 34.8833]
            },
            "Suez": {
                "Suez": [29.9667, 32.5494],
                "Port Said": [31.2653, 32.3021],
                "El Arbaeen": [29.9667, 32.5500],
                "Al Gabbal": [29.9706, 32.5600]
            },
            "Aswan": {
                "Aswan": [24.0889, 32.8997],
                "Kom Ombo": [24.3564, 32.9661],
                "Edfu": [24.9806, 32.8792],
                "Derr": [24.2761, 32.7000],
                "Nubia": [24.0156, 32.8878]
            },
            "Luxor": {
                "Luxor": [25.6872, 32.6394],
                "Esna": [25.5444, 32.7122],
                "Armant": [25.7006, 32.5708],
                "Karnak": [25.7219, 32.6286],
                "Thebes": [25.7175, 32.6008]
            },
            "Qena": {
                "Qena": [26.1592, 32.7206],
                "Nag Hammadi": [25.8422, 32.3500],
                "Luxor": [25.6872, 32.6394],
                "Qift": [25.7275, 32.5581],
                "Dandara": [25.8264, 32.5164]
            },
            "Sohag": {
                "Sohag": [26.5581, 31.6944],
                "Juhayna": [26.5811, 31.6994],
                "Tima": [26.5708, 31.6550],
                "Naga Hammadi": [25.8422, 32.3500],
                "Balyana": [26.5100, 31.6400]
            },
            "North Sinai": {
                "Arish": [30.5750, 34.4661],
                "Sheikh Zuweid": [30.5000, 34.5667],
                "Rafah": [31.0661, 34.2758],
                "Bir al-Abd": [30.6856, 34.2400],
                "El-Hassana": [30.5700, 34.3400],
                "El-Nakhl": [30.5864, 34.3564],
                "El-Qasima": [30.5500, 34.3400],
                "El-Sheikh Zuweid": [30.5000, 34.5667]
            },
            "South Sinai": {
                "Sharm El Sheikh": [27.9158, 34.3299],
                "Dahab": [28.5114, 34.5147],
                "Nuweiba": [29.0147, 34.6750],
                "Taba": [29.5272, 34.7886],
                "Saint Catherine": [28.5675, 33.9919],
                "Ras Sidr": [29.0708, 32.7206],
                "Abu Redis": [28.8594, 33.6164],
                "Abu Zenima": [28.9894, 33.4919]
            }
        }

        self.governorates_centers = {
            "Cairo": [
                "Hadayek Al Zaiton",
                "El Shorouk",
                "El Marg",
                "Maadi Degla",
                "Abaseya",
                "New Nozha",
                "Dar Al Salam",
                "Al Kalaa",
                "Basateen",
                "Abdo Basha",
                "Nasr City",
                "15th Of May City",
                "5th Settlement",
                "Heliopolis",
                "3rd Settlement",
                "Ezbet El Nakhl",
                "Katamiah",
                "El Herafieen",
                "15th of May City",
                "Down Town",
                "EL Marg",
                "New Maadi",
                "Zamalek",
                "1st Settlement",
                "Helwan",
                "Al Zeitoun",
                "Masaken Sheraton",
                "Hadayek Helwan",
                "Ghamrah",
                "Rod El Farag",
                "Al Matareya",
                "Al Kasr Al Einy",
                "Cairo",
                "New Cairo-1",
                "Ain Shams",
                "Garden City",
                "Mirage City",
                "Amiria",
                "Al Azhar",
                "Sayeda Zeinab",
                "Almaza",
                "Fustat",
                "Hadayek Maadi",
                "Al Rehab",
                "Al Moski",
                "Manial Al Rodah",
                "Maadi",
                "El Tahrir",
                "New El Marg",
                "Gesr Al Suez",
                "Abdeen",
                "Mokattam",
                "Al Salam City",
                "Misr El Kadima",
                "Helmiet Elzaitoun",
                "Al Daher",
                "Hadayek Al Qobah",
                "Shubra",
                "Cornish Al Nile",
                "Badr City",
                "Ramsis",
                "Madinty",
                "Helmeya"
            ],
            "Giza": [
                "6th of October",
                "Mansoureya",
                "Hawamdya",
                "Tirsa",
                "Abou Rawash",
                "Omraneya",
                "Smart Village",
                "Kerdasa",
                "Saft El Laban",
                "Dokki",
                "Al Saf",
                "Sheikh Zayed",
                "Sakiat Mekki",
                "Mohandessin",
                "Al Kom Al Ahmer",
                "Imbaba",
                "Bolak Al Dakrour",
                "Al Monib",
                "Berak Alkiaam",
                "Al Moatamadia",
                "Shabramant",
                "Warraq",
                "Giza",
                "Manial",
                "Haram",
                "Agouza",
                "Qism el Giza",
                "Faisal",
                "Al Wahat",
                "Hadayeq El Ahram",
                "6th Of October",
                "Aossim",
                "Al Nobariah",
                "Badrashin",
                "Kit Kat",
                "Al Barageel",
                "Al Manashi"
            ],
            "Alexandria": [
                "Miami",
                "Smouha",
                "Abees",
                "Alexandria",
                "Sedi Gaber",
                "El Borg El Kadem",
                "Sedi Bisher",
                "Al Bitash",
                "Stanly",
                "El-Agamy",
                "San Stefano",
                "Mahtet El-Raml",
                "Al A'mriah",
                "Bangar EL Sokar",
                "Manshia",
                "Sedi Kreir",
                "Kafer Abdou",
                "Borg El Arab",
                "Roshdy",
                "Abu Keer",
                "Glem",
                "Al Nahda Al Amria",
                "Awaied-Ras Souda",
                "Mandara",
                "City Center",
                "Azarita",
                "Maamora",
                "Al Soyof",
                "Sporting",
                "Khorshid",
                "Luran",
                "Asafra",
                "Zezenya",
                "Muntazah"
            ],
            "Al Beheira": [
                "Hosh Issa",
                "Rashid",
                "Shubrakhit",
                "Edko",
                "Damanhour",
                "Etay Al Barud",
                "Al Beheira",
                "Abu Hummus",
                "Kom Hamadah",
                "Abou Al Matamer",
                "Al Delengat",
                "El Nubariyah",
                "Kafr El Dawwar",
                "Edfina",
                "Wadi Al Natroun",
                "Al Mahmoudiyah",
                "Al Rahmaniyah"
            ],
            "Al Daqahliya": [
                "Meet Ghamr",
                "Belqas",
                "Nabroo",
                "Manzala",
                "Shrbeen",
                "Al Daqahliya",
                "El Sinblaween",
                "Menit El Nasr",
                "Dekernes",
                "Aga",
                "Talkha",
                "Al Mansoura"
            ],
            "Al Fayoum": [
                "Sonores",
                "Ebshoy",
                "Kofooer Elniel",
                "New Fayoum",
                "Atsa",
                "Sanhoor",
                "Tameaa",
                "Al Fayoum",
                "Sersenaa",
                "El Aagamen",
                "Manshaa Abdalla",
                "Youssef Sadek",
                "Manshaa Elgamal"
            ],
            "Al Gharbia": [
                "Alsanta",
                "Al Mahala Al Kobra",
                "Al Gharbia",
                "Samanood",
                "Tanta",
                "Qotoor",
                "Zefta",
                "Basyoon",
                "Kafr Alziat"
            ],
            "Al Meniya": [
                "Minya",
                "Samaloot",
                "Eladwa",
                "Mghagha",
                "Matai",
                "Malawi",
                "Bani Mazar",
                "Dermwas",
                "Abo Korkas"
            ],
            "Al Monufia": [
                "Shohada",
                "Menoof",
                "Tala",
                "Shebin El Koom",
                "Sadat City",
                "Al Monufia",
                "Quesna",
                "Berket Al Sabei",
                "Ashmoon"
            ],
            "Al Sharqia": [
                "Al Salhiya Al Gedida",
                "Abu Hammad",
                "Abu Kbeer",
                "Hehya",
                "Awlad Saqr",
                "Al Hasiniya",
                "Faqous",
                "Darb Negm",
                "Al Ibrahimiya",
                "Zakazik",
                "Kafr Saqr",
                "Mashtool Al Sooq",
                "Belbes",
                "Meniya Alqamh",
                "Al Sharqia",
                "10th of Ramdan City"
            ],
            "Aswan": [
                "Aswan",
                "Draw",
                "El Klabsha",
                "Al Sad Al Aali",
                "Abu Simbel",
                "Nasr Elnoba",
                "Edfo",
                "Markaz Naser",
                "Kom Ombo"
            ],
            "Asyut": [
                "Dayrout",
                "Asyut",
                "El Qusya",
                "Assuit Elgdeda",
                "Elfath",
                "El Ghnayem",
                "Sahel Selim",
                "Abnoub",
                "El Badari",
                "Abou Teag",
                "Serfa",
                "Manflout"
            ],
            "Bani Souaif": [
                "Bani Souaif",
                "El Wastaa",
                "El Korimat",
                "El Fashn",
                "Naser",
                "Ahnaseaa",
                "New Bani Souaif",
                "Bebaa",
                "Smostaa"
            ],
            "Damietta": [
                "Kafr Saad",
                "Ras El Bar",
                "Fareskor",
                "Al Zarkah",
                "Damietta",
                "New Damietta"
            ],
            "Ismailia": [
                "Elsalhia Elgdida",
                "Al Kasaseen",
                "Abo Sultan",
                "El Tal El Kebir",
                "Abu Swer",
                "Qantara Gharb",
                "Qantara Sharq",
                "Nfeesha",
                "Ismailia",
                "Srabioom",
                "Fayed"
            ],
            "Kafr El Sheikh": [
                "Hamool",
                "Kafr El Sheikh",
                "Al Riadh",
                "Qeleen",
                "Desouq",
                "Seedy Salem",
                "Bela",
                "Fooh",
                "Metobas",
                "Borollos",
                "Balteem"
            ],
            "Luxor": [
                "El Karnak",
                "El Korna",
                "Armant Sharq",
                "Esnaa",
                "Luxor",
                "Armant Gharb"
            ],
            "Matrooh": [
                "Matrooh",
                "El Hamam",
                "Sidi Barrani",
                "Fuka",
                "El Alamein"
            ],
            "New Valley": [
                "Kharga",
                "Dakhla",
                "Baris",
                "Farafra",
                "Paris",
                "El Kharga"
            ],
            "محافظه بورسعيد": [
                "Qesm El Zohor",
                "Qesm El Shark",
                "Qesm El Arab",
                "Qesm El Manakh",
                "Qesm El Manasra West Port Said",
                "قسم اول بورفؤاد"
            ],
            "Red Sea": [
                "Hurghada",
                "El Gouna",
                "Quseir",
                "Safaga",
                "Marsa Alam"
            ],
            "Suez": [
                "Suez",
                "Port Said",
                "El Arbaeen",
                "Al Gabbal"
            ],
            "Aswan": [
                "Aswan",
                "Kom Ombo",
                "Edfu",
                "Derr",
                "Nubia"
            ],
            "Luxor": [
                "Luxor",
                "Esna",
                "Armant",
                "Karnak",
                "Thebes"
            ],
            "Qena": [
                "Qena",
                "Nag Hammadi",
                "Luxor",
                "Qift",
                "Dandara"
            ],
            "Sohag": [
                "Sohag",
                "Juhayna",
                "Tima",
                "Naga Hammadi",
                "Balyana"
            ],
            "North Sinai": [
                "Arish",
                "Sheikh Zuweid",
                "Rafah",
                "Bir al-Abd",
                "El-Hassana",
                "El-Nakhl",
                "El-Qasima",
                "El-Sheikh Zuweid"
            ],
            "South Sinai": [
                "Sharm El Sheikh",
                "Dahab",
                "Nuweiba",
                "Taba",
                "Saint Catherine",
                "Ras Sidr",
                "Abu Redis",
                "Abu Zenima"
            ]
            }

        st.session_state.selected_center = ''        
        st.session_state.selected_governorate = ''
        st.session_state.selected_district = ''
        st.session_state.drawn_data = None

        st.set_page_config(layout="wide")

        st.session_state.nearest_hospital_dist = None
        st.session_state.nearest_edu_dist = None
        st.session_state.nearest_finantial_dist = None
        st.session_state.nearest_waterway_dist = None   
        st.session_state.nearest_otherFacility_dist = None
        st.session_state.nearest_road_dist = None


    def display_gis_and_data(self):
        # Load and prepare the image
        image_bytes = io.BytesIO()
        image = Image.open('./data/logo.jpg')
        image.save(image_bytes, format='JPEG')

        # Create a column layout to center the image
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(image_bytes, caption='', width=300)  # Adjust width as needed
        
        with col2:
            st.write('#### About App')
            st.write('this project in to predict the value of the assets such as “real estate, agricultural lands, commercial shops, etc. ”    in the meantime according to several attributes “area number of bedrooms and toilets, GIS layers”, we can enhance to predict the assets value in the future')
            st.write('we used “random forest regressor model” as we want high complexity to find relation between this several attributes also that the data is not uniform or in form of linear graphs so we used it  to make prediction and it’s a tree based model mainly based on decision tree.')
            st.write('The accuracy is 0.98%')
            st.write('When we have accurate Varity in the data the model performance will increase.')

        st.write("### GIS Section")

        
        with st.spinner("Loading map..."):
            # Initialize variables
            selected_lat = None
            selected_long = None
            st.session_state.selected_governorate = "Select a governorate..."
            st.session_state.selected_center = "Select a center..."
            st.session_state.selected_district = "Select a district..."
            col1, col2 = st.columns(2)

            with col2:



                st.session_state.selected_governorate = st.selectbox(":اختار المحافظه", ["Select a governorate..."] + list(self.governorates_centers.keys()))

                if st.session_state.selected_governorate != "Select a governorate...":
                    centers = self.governorates_centers[st.session_state.selected_governorate]
                    st.session_state.selected_center = st.selectbox(":اختار المركز", ["Select a center..."] + centers)

                    if st.session_state.selected_center != "Select a center...":
                        selected_lat, selected_long = self.center_coords[st.session_state.selected_governorate][st.session_state.selected_center]
                        st.session_state.selected_district = st.selectbox(":اختار المنطقه", ["Select a district..."] + ['اول بورفؤاد'])
                        
                        # Create a DataFrame for selected location
                        self.df = pd.DataFrame(
                            {'lat': [selected_lat],
                            'lon': [selected_long]}
                        )
                        st.write(st.session_state.selected_governorate, ",", st.session_state.selected_center)

                if (st.session_state.selected_district == "Select a district..."):
                    st.warning('you have to select the governorate, center and district first.')
                else:
                    st.success('selected successfully')
        

            with col1:     
                # Initial map centered on Egypt
                egypt_center = [26.8206, 30.8025]
                default_zoom = 6

                # Use selected center if available, otherwise show Egypt
                if selected_lat and selected_long:
                    center = [selected_lat, selected_long]
                    zoom_start = 15
                else:
                    center = egypt_center
                    zoom_start = default_zoom

                # Create the map
                base_map = folium.Map(location=center, zoom_start=zoom_start, tiles='OpenStreetMap')

                
                # Load the shapefile
                hospitals_shapefile_path = 'data/hotosm_egy_health_facilities_points_shp/hotosm_egy_health_facilities_points_shp.shp'
                hospitals_gdf = gpd.read_file(hospitals_shapefile_path)
                # Set CRS if known
                hospitals_gdf.crs = 'EPSG:4326' 
                
                # Load the shapefile
                educational_shapefile_path = 'data/hotosm_egy_education_facilities_points_shp/hotosm_egy_education_facilities_points_shp.shp'
                educational_gdf = gpd.read_file(educational_shapefile_path)
                # Set CRS if known
                educational_gdf.crs = 'EPSG:4326' 

                # Load the shapefile
                finantial_shapefile_path = 'data/hotosm_egy_financial_services_points_shp/hotosm_egy_financial_services_points_shp.shp'
                finantial_gdf = gpd.read_file(finantial_shapefile_path)
                # Set CRS if known
                finantial_gdf.crs = 'EPSG:4326' 
                
                # Load the shapefile
                waterways_shapefile_path = 'data/hotosm_egy_waterways_lines_shp/hotosm_egy_waterways_lines_shp.shp'
                waterways_gdf = gpd.read_file(waterways_shapefile_path)
                # Set CRS if known
                waterways_gdf.crs = 'EPSG:4326' 
                
                # Load the shapefile
                otherFacilities_shapefile_path = 'data/hotosm_egy_points_of_interest_points_shp/hotosm_egy_points_of_interest_points_shp.shp'
                otherFacilities_gdf = gpd.read_file(otherFacilities_shapefile_path)
                # Set CRS if known
                otherFacilities_gdf.crs = 'EPSG:4326' 
                
                # # Load the shapefile
                roads_shapefile_path = 'data/portsaid_roads_lines_shp/port_lines.shp'
                roads_gdf = gpd.read_file(roads_shapefile_path)
                # Set CRS if known
                roads_gdf.crs = 'EPSG:4326' 



                # Save the map to an HTML file
                base_map.save('health_facilities_map.html')


                # Add a draw control to the base map
                draw = Draw(export=False)
                draw.add_to(base_map)  # Attach directly to the base map

                # Add LayerControl to the map
                LayerControl().add_to(base_map)

                # Display the map with Streamlit
                map_data = st_folium(base_map, width=700, height=500)

                if map_data and map_data['all_drawings']:
                    st.session_state.drawn_data = map_data['all_drawings']
                else:
                    st.session_state.drawn_data = None

                if map_data and 'all_drawings' in map_data:
                    drawn_shapes = map_data['all_drawings']
                    if drawn_shapes:
                        # Calculate the index of the last element
                        last_index = len(drawn_shapes) - 1
                        
                        # Extract the last shape
                        last_shape = drawn_shapes[last_index]
                        
                        # Check the type of the last shape's geometry
                        if last_shape['geometry']['type'] == 'Point':
                            coords = last_shape['geometry']['coordinates']
                            point = Point(coords[0], coords[1])
                        elif last_shape['geometry']['type'] == 'Polygon':
                            geojson_data = last_shape
                            polygon = shape(geojson_data['geometry'])
                            centroid = polygon.centroid
                            point = Point(centroid.x, centroid.y)

                        # Calculate distance to each hospital
                        hospitals_gdf['distance'] = hospitals_gdf.geometry.distance(point)
                        # Calculate distance to each educational asset
                        educational_gdf['distance'] = educational_gdf.geometry.distance(point)
                        # Calculate distance to each finantial asset
                        finantial_gdf['distance'] = finantial_gdf.geometry.distance(point)
                        # Calculate distance to each waterways asset
                        waterways_gdf['distance'] = waterways_gdf.geometry.distance(point)
                        # Calculate distance to each otherFacilities asset
                        otherFacilities_gdf['distance'] = otherFacilities_gdf.geometry.distance(point)
                        # Calculate distance to each road
                        roads_gdf['distance'] = roads_gdf.geometry.distance(point)

                        # Find the nearest hospital
                        nearest_hospital = hospitals_gdf.loc[hospitals_gdf['distance'].idxmin()]
                        # Find the nearest educational asset
                        nearest_edu = educational_gdf.loc[educational_gdf['distance'].idxmin()]
                        # Find the nearest finantial asset
                        nearest_finantial = finantial_gdf.loc[finantial_gdf['distance'].idxmin()]
                        # Find the nearest waterway
                        nearest_waterway = waterways_gdf.loc[waterways_gdf['distance'].idxmin()]
                        # Find the nearest otherFacilities
                        nearest_otherFacility = otherFacilities_gdf.loc[otherFacilities_gdf['distance'].idxmin()]
                        # Find the nearest road
                        nearest_road = roads_gdf.loc[roads_gdf['distance'].idxmin()]

                        st.session_state.nearest_hospital_dist = nearest_hospital['distance']*111
                        st.session_state.nearest_edu_dist = nearest_edu['distance']*111
                        st.session_state.nearest_finantial_dist = nearest_finantial['distance']*111
                        st.session_state.nearest_waterway_dist = nearest_waterway['distance']*111
                        st.session_state.nearest_otherFacility_dist = nearest_otherFacility['distance']*111
                        st.session_state.nearest_road_dist = nearest_road['distance']*111


                        # distances data taple print
                        distancesData = {
                            "Facility": [
                                "Nearest Hospital",
                                "Nearest Educational Facility",
                                "Nearest Financial Facility",
                                "Nearest Waterway",
                                "Nearest Other Facility",
                                "Nearest Road"
                            ],
                            "Distance (km)": [
                                st.session_state.nearest_hospital_dist,
                                st.session_state.nearest_edu_dist,
                                st.session_state.nearest_finantial_dist,
                                st.session_state.nearest_waterway_dist,
                                st.session_state.nearest_otherFacility_dist,
                                st.session_state.nearest_road_dist
                            ]
                        }
                        distancesDataframe = pd.DataFrame(distancesData)
                        st.table(distancesDataframe)

                        st.success('shape drawn successfully')

                    else:
                        st.warning("You have to draw shape or point for your asset")
                else:
                    st.write("No shapes available.")




                    
        st.write("### Data Analysis and Visualization")
        with st.spinner("Loading charts..."):
            # Define ranges for rent and sale (for reference, not used directly in this code)
            rent_ranges = ['1000-3500', '3500-3800', '3800-4350', '4350+']
            sale_ranges = ['0.5M-0.9M', '0.9M-1M', '1M-1.1M', '1.1M+']

            # Load data from CSV
            data_file = './data/stramlit.csv'
            data = pd.read_csv(data_file)

            # Ensure the relevant columns are present
            expected_columns = ['GovName', 'SecName', 'SsecName', 'sale_Value', 'rental_Value']
            for col in expected_columns:
                if col not in data.columns:
                    raise ValueError(f"Missing expected column: {col}")

            # Select only the columns you need for charts
            data_filtered = data[expected_columns]

            # Process the data for charts
            # Assuming that 'Rent' and 'Sales' are already numeric
            if st.session_state.selected_center != 'Select a center...':
                rent_data = data_filtered[(data_filtered['SecName'] == st.session_state.selected_center)][['GovName', 'SecName', 'rental_Value']].copy()
                sale_data = data_filtered[(data_filtered['SecName'] == st.session_state.selected_center)][['GovName', 'SecName', 'sale_Value']].copy()
            else:
                rent_data = data_filtered[['GovName', 'SecName', 'rental_Value']].copy()
                sale_data = data_filtered[['GovName', 'SecName', 'sale_Value']].copy()

            # Add a range column for visualization (if needed)
            def parse_range_value(value_str):
                """Convert a range string with 'M' (millions) to an integer value."""
                if 'M' in value_str:
                    return int(float(value_str.replace('M', '')) * 1_000_000)
                return int(value_str)

            def categorize_value(value, ranges, labels):
                for i, r in enumerate(ranges):
                    if '-' in r:
                        min_val, max_val = map(parse_range_value, r.split('-'))
                    else:
                        min_val = parse_range_value(r.split('+')[0])
                        max_val = float('inf')
                    if min_val <= value < max_val:
                        return labels[i]
                return labels[-1]
            
            rent_data['Range'] = rent_data['rental_Value'].apply(lambda x: categorize_value(x, rent_ranges, rent_ranges))
            sale_data['Range'] = sale_data['sale_Value'].apply(lambda x: categorize_value(x, sale_ranges, sale_ranges))

            # Streamlit layout
            col1, col2 = st.columns(2)

            with col1:
                # Rent Pie Chart
                st.write("#### Pie Chart of Rent Categories")
                rent_pie_data = rent_data['Range'].value_counts().reset_index()
                rent_pie_data.columns = ['Range', 'Count']
                fig = px.pie(rent_pie_data, names='Range', values='Count', title='Rent Categories Distribution', color='Range')
                st.plotly_chart(fig)

            with col2:
                # Rent Line Chart
                st.write("#### Line Chart of Rent Values")
                count_data = rent_data['Range'].value_counts().sort_index().reset_index()
                count_data.columns = ['Range', 'Count']
                fig = px.line(count_data, x='Range', y='Count', markers=True, title='Number of Assets by Rent Range')
                st.plotly_chart(fig)

            col1, col2 = st.columns(2)

            with col1:
                # Sale Pie Chart
                st.write("#### Pie Chart of Sale Categories")
                sale_pie_data = sale_data['Range'].value_counts().reset_index()
                sale_pie_data.columns = ['Range', 'Count']
                fig = px.pie(sale_pie_data, names='Range', values='Count', title='Sale Categories Distribution', color='Range')
                st.plotly_chart(fig)

            with col2:
                # Sale Line Chart
                st.write("#### Line Chart of Sale Values")
                count_data = sale_data['Range'].value_counts().sort_index().reset_index()
                count_data.columns = ['Range', 'Count']
                fig = px.line(count_data, x='Range', y='Count', markers=True, title='Number of Assets by Sale Price Range')
                st.plotly_chart(fig)


    def handle_existing_property(self):
        df = pd.read_excel("./data/cama.xlsx")

        data_list = df.values.tolist()
        
        
        st.write("### Existing Property")
        property_id = st.number_input("Please enter the property ID", key="property_id" , value=0, min_value=0,step=1)

        if st.button("Generate Expected Rent and Sale", type='primary'):
            if property_id:
                # Filter data for the given property ID
                asset_data = df[df['ASSET_ID'] == property_id]
                
                if not asset_data.empty:
                    # Extract rent and sale values
                    currentRentPrice = asset_data['rental_Value'].values[0]
                    currentSellingPrice = asset_data['sale_Value'].values[0]
                    
                    # Display rent and sale values
                    st.write(f"Estimated Rent is: {currentRentPrice}")
                    st.write(f"Estimated Sale is: {currentSellingPrice}")
                else:
                    st.write("No asset found with the given property ID.")
            else:
                st.error("Please enter a valid numerical property ID before generating values.")

    def handle_new_property(self):
        st.write("### New Property")
        if ((st.session_state.drawn_data is None) & (st.session_state.selected_district == 'Select a district...')):
            st.error('Make sure that you selected the governorate, center, and drew on the map your asset before filling this form.')
        elif (st.session_state.selected_district == 'Select a district...'):
            st.error('You have to select the governorate, center, and district first.')
        elif (st.session_state.drawn_data is None):
            st.error('You have to add property on map.')
        
        feature_vector = []
        inputs_dict = {}

        # Define number inputs
        inputs = [
            ("مساحة العقار (متر مربع)", 0, 2000),
            ("عدد الغرف", 0, 15),
            ("عدد الحمامات", 0, 5),
            ("الدور", 0, 30),
        ]

        # Define boolean options with placeholders
        boolean_options = [
            ("الفرش", "Select an option", "مفروشه", "غير مفروشه"),
            ("بداخل مول", "Select an option", "نعم", "لا"),
            ("بداخل كمباوند", "Select an option", "نعم", "لا"),
            ("عداد مياه", "Select an option", "يوجد", "لا يوجد"),
            ("عداد غاز", "Select an option", "يوجد", "لا يوجد"),
        ]

        # Define dropdowns
        dropdowns = [
            ("نوع العقار", ["Select an option", "وحدة سكنية"]),
            ("نوع العقد", ["Select an option", "ايجاري تمليكي", "ايجار جديد", "حق انتفاع"]),
            ("نوع التشطيب", ["Select an option", "بدون تشطيب", "نصف تشطيب", "تشطيب كامل"]),
            ("مستوي التشطيب", ["Select an option", 'عادية', 'متوسطة', 'عالية' , 'غير معروف']),
            # Removed "اتجاه العقار" from here
        ]

        # Create mappings for each dropdown to assign values from 1 to 3
        value_mappings = {
            "نوع التشطيب": {"بدون تشطيب": 0, "نصف تشطيب": 2, "تشطيب كامل": 1},
            "مستوي التشطيب": {'عادية': 0, 'متوسطة': 3, 'عالية': 1 , 'غير معروف':2},
            "اتجاه العقار": {"غير معروف": 1, "غربي": 0},  # This will still be used in the value mapping
        }

        # Collect number inputs
        for name, min_val, max_val in inputs:
            value = st.number_input(name, min_value=min_val, max_value=max_val, value=None)
            inputs_dict[name] = value if value is not None else 0
            feature_vector.append(float(value) if value is not None else 0.0)

        # Collect boolean inputs
        for name, placeholder, true_label, false_label in boolean_options:
            selected_value = st.selectbox(name, [placeholder, true_label, false_label])
            boolean_value = 1 if selected_value == true_label else 0
            inputs_dict[name] = boolean_value
            feature_vector.append(float(boolean_value))  # Convert boolean to 0/1



        # Collect dropdown selections
        for name, options in dropdowns:
            selected_value = st.selectbox(name, options)
            inputs_dict[name] = selected_value if selected_value != "Select an option" else None
            if name != "نوع العقد" and name != "نوع العقار":
                # Assign a value from 1 to 3 if the option is not "Select an option"
                if selected_value != "Select an option" and name in value_mappings:
                    feature_vector.append(value_mappings[name].get(selected_value, 0))

        # Add "اتجاه العقار" directly to the feature vector with a value of 1
        feature_vector.append(1)

        # Print the feature vector for debugging
        # st.write("Feature Vector (before encoding):", feature_vector)

        # Ensure distances are available in session state
        distances_filled = all(
            key in st.session_state and st.session_state[key] is not None
            for key in [
                'nearest_hospital_dist', 'nearest_edu_dist', 'nearest_finantial_dist',
                'nearest_waterway_dist', 'nearest_otherFacility_dist'
            ]
        )

        if distances_filled:
            # Prepare the DataFrame for encoding
            encoding_df = pd.DataFrame({
                'ASSET_SUB_TYPE_DESC': [inputs_dict["نوع العقار"]],
                'CONTRACT_DESC': [inputs_dict["نوع العقد"]],
                'FINISHUNG_LEVEL_NAME': [inputs_dict["نوع التشطيب"]],
                'Feature_Appartment_NAME': [inputs_dict["مستوي التشطيب"]],
                # Removed 'اتجاه العقار' from here
                'GovName': [st.session_state.selected_governorate],
                'SecName': [st.session_state.selected_center],
                'SsecName': [st.session_state.selected_district],
            })
            historical_data = pd.read_csv('./data/stramlit.csv')  # Adjust the path if necessary

            # One-hot encoding for 'GovName', 'SecName', 'SsecName', and 'ASSET_SUB_TYPE_DESC'
            one_hot_columns = ['GovName', 'SecName', 'SsecName', 'ASSET_SUB_TYPE_DESC']
            encoded_one_hot = pd.get_dummies(encoding_df[one_hot_columns])
            # st.write(encoded_one_hot)
            feature_vector.extend(encoded_one_hot.iloc[0].astype(float).values.tolist())

            class MeanTargetEncoder(ce.TargetEncoder):
                def __init__(self, mean_values, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.mean_values = mean_values

                def transform(self, X, y=None):
                    # Replace categories with mean target values
                    return X.map(self.mean_values).fillna(0).astype(float)

            # Compute mean target values for each category in 'CONTRACT_DESC' and 'APPARTMENTS_FLOOR_NO'
            mean_values_contract_desc = historical_data.groupby('CONTRACT_DESC')['rental_Value'].mean()
            # st.write(mean_values_contract_desc)

            # Initialize encoders with mean values
            encoder_contract_desc = MeanTargetEncoder(mean_values_contract_desc)

            # Apply target encoding using the mean values
            encoding_df['CONTRACT_DESC_Encoded'] = encoder_contract_desc.transform(encoding_df['CONTRACT_DESC'])

            # st.write(encoding_df['CONTRACT_DESC_Encoded'])
            
            # Append target encoded values
            feature_vector.append(float(encoding_df['CONTRACT_DESC_Encoded'].values[0]))

            # Append other distance-related features
            feature_vector.extend([
                float(st.session_state.nearest_road_dist),
                float(st.session_state.nearest_waterway_dist),
                float(st.session_state.nearest_otherFacility_dist),
                float(st.session_state.nearest_edu_dist),
                float(st.session_state.nearest_finantial_dist),
                float(st.session_state.nearest_hospital_dist),
            ])
        else:
            st.error("Required distance data is missing.")
            return

        # Convert feature_vector to numpy array and ensure it's 2D
        feature_vector = np.array([float(val) if isinstance(val, (int, float, np.number)) else 0.0 for val in feature_vector]).reshape(1, -1)
        
        # Print the feature vector for debugging
        #st.write("Feature Vector (after encoding):", feature_vector)

        # Submit button
        if st.button("Submit Property"):
            # Check if all fields are filled
            all_filled = all(value is not None for value in inputs_dict.values())

            if all_filled:
                try:
                    # Predict using the model
                    prediction = st.session_state.model.predict(feature_vector)
                    rent_value,sale_value  = prediction[0]

                    final_sale_value = round(sale_value) 
                    final_rent_value = round(rent_value)

                    # Ensure directory exists
                    directory = './data'
                    os.makedirs(directory, exist_ok=True)

                    # Write to CSV
                    with open(f'{directory}/stramlit.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(feature_vector[0].tolist() + [final_sale_value, final_rent_value])

                    # Display prediction results
                    st.write(f"Prediction Results:")
                    st.write(f"Sale Value: {final_sale_value}")
                    st.write(f"Rent Value: {final_rent_value}")
                    st.write("You have submitted a new property.")
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")
            else:
                st.error("Please fill in all fields before submitting.")



    def main(self):
        st.title("Housing Prices Prediction")
        
        self.display_gis_and_data()
        
        property_options = ["Choose property type", "Existing Property", "New Property"]
        selection1 = st.selectbox("Select your property type", property_options, index=0, format_func=lambda x: "Choose property type" if x == property_options[0] else x)

        if 'previous_selection' not in st.session_state:
            st.session_state.previous_selection = property_options[0]

        if selection1 != st.session_state.previous_selection:
            st.session_state.previous_selection = selection1
            if selection1 == "Choose property type":
                st.write("*Please Select")

        if selection1 == "Existing Property":
            self.handle_existing_property()

        if selection1 == "New Property":
            self.handle_new_property()



if __name__ == "__main__":
    app = HousingApp()
    app.main()
