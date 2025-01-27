import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Expanded List of Cities (now 40 cities)
cities = [
    'Delhi', 'Mumbai', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 'Pune', 'Ahmedabad', 'Jaipur', 'Goa',
    'Lucknow', 'Chandigarh', 'Indore', 'Coimbatore', 'Patna', 'Surat', 'Kanpur', 'Nagpur', 'Vadodara', 'Agra',
    'Vadodara', 'Visakhapatnam', 'Trivandrum', 'Madurai', 'Vijayawada', 'Rajkot', 'Bhopal', 'Mysore', 'Meerut',
    'Ranchi', 'Guwahati', 'Udaipur', 'Jodhpur', 'Jammu', 'Shimla', 'Bhubaneswar', 'Srinagar', 'Dehradun', 'Dibrugarh',
    'Tiruchirappalli'
]

# Expanded Airlines List (now 10 airlines)
airlines = ['Indigo', 'Air India', 'SpiceJet', 'GoAir', 'Vistara', 'AirAsia', 'Akasa Air', 'Singapore Airlines',
            'Qatar Airways', 'Emirates']

# Airline advantages (ratings out of 5)
airline_advantages = {
    'Indigo': {'Customer Service': 4, 'Comfort and Space': 3, 'Price': 5, 'Entertainment': 3, 'Inflight Meals': 3},
    'Air India': {'Customer Service': 4, 'Comfort and Space': 4, 'Price': 3, 'Entertainment': 4, 'Inflight Meals': 4},
    'SpiceJet': {'Customer Service': 3, 'Comfort and Space': 3, 'Price': 4, 'Entertainment': 2, 'Inflight Meals': 3},
    'GoAir': {'Customer Service': 3, 'Comfort and Space': 3, 'Price': 3, 'Entertainment': 2, 'Inflight Meals': 2},
    'Vistara': {'Customer Service': 5, 'Comfort and Space': 5, 'Price': 4, 'Entertainment': 5, 'Inflight Meals': 5},
    'AirAsia': {'Customer Service': 4, 'Comfort and Space': 3, 'Price': 4, 'Entertainment': 3, 'Inflight Meals': 3},
    'Akasa Air': {'Customer Service': 4, 'Comfort and Space': 3, 'Price': 5, 'Entertainment': 3, 'Inflight Meals': 3},
    'Singapore Airlines': {'Customer Service': 5, 'Comfort and Space': 5, 'Price': 4, 'Entertainment': 5,
                           'Inflight Meals': 5},
    'Qatar Airways': {'Customer Service': 5, 'Comfort and Space': 5, 'Price': 4, 'Entertainment': 5,
                      'Inflight Meals': 5},
    'Emirates': {'Customer Service': 5, 'Comfort and Space': 5, 'Price': 4, 'Entertainment': 5, 'Inflight Meals': 5},
}

# Flight prices (for new airlines, sample prices)
flight_prices = {
    'Indigo': {'General': 3000, 'Secondary': 4500, 'High Class': 7000},
    'Air India': {'General': 3500, 'Secondary': 5000, 'High Class': 7500},
    'SpiceJet': {'General': 2500, 'Secondary': 4000, 'High Class': 6500},
    'GoAir': {'General': 2700, 'Secondary': 4200, 'High Class': 6800},
    'Vistara': {'General': 4000, 'Secondary': 5500, 'High Class': 8000},
    'AirAsia': {'General': 2800, 'Secondary': 4300, 'High Class': 6800},
    'Akasa Air': {'General': 2900, 'Secondary': 4400, 'High Class': 6900},
    'Singapore Airlines': {'General': 6000, 'Secondary': 8500, 'High Class': 12000},
    'Qatar Airways': {'General': 6500, 'Secondary': 9000, 'High Class': 12500},
    'Emirates': {'General': 6200, 'Secondary': 8700, 'High Class': 11800},
}

# Expanded Routes for 40 cities (with random airline routes)
routes = {
    ('Delhi', 'Mumbai'): ['Indigo', 'Air India', 'SpiceJet', 'GoAir', 'Vistara', 'AirAsia', 'Emirates'],
    ('Delhi', 'Bengaluru'): ['Indigo', 'Air India', 'Vistara', 'SpiceJet', 'Singapore Airlines'],
    ('Mumbai', 'Bengaluru'): ['Indigo', 'GoAir', 'Vistara', 'AirAsia'],
    ('Delhi', 'Kolkata'): ['Air India', 'SpiceJet', 'GoAir', 'Vistara'],
    ('Bengaluru', 'Kolkata'): ['Indigo', 'Air India', 'SpiceJet', 'GoAir'],
    ('Chennai', 'Hyderabad'): ['Air India', 'Indigo', 'SpiceJet', 'Vistara'],
    ('Chennai', 'Goa'): ['Vistara', 'Indigo', 'GoAir'],
    ('Hyderabad', 'Goa'): ['Indigo', 'GoAir', 'Akasa Air'],
    ('Pune', 'Ahmedabad'): ['Indigo', 'SpiceJet'],
    ('Jaipur', 'Goa'): ['Air India', 'SpiceJet', 'Akasa Air'],
    ('Lucknow', 'Chandigarh'): ['GoAir', 'SpiceJet'],
    ('Indore', 'Coimbatore'): ['Vistara', 'Emirates'],
    ('Patna', 'Surat'): ['Indigo', 'GoAir'],
    ('Kanpur', 'Nagpur'): ['AirAsia', 'Indigo'],
    ('Vadodara', 'Agra'): ['SpiceJet', 'Vistara'],
    ('Visakhapatnam', 'Trivandrum'): ['Indigo', 'Air India'],
    ('Madurai', 'Vijayawada'): ['Akasa Air', 'SpiceJet'],
    ('Rajkot', 'Bhopal'): ['GoAir', 'Air India'],
    ('Mysore', 'Meerut'): ['Vistara', 'AirAsia'],
    ('Ranchi', 'Guwahati'): ['Indigo', 'GoAir'],
    ('Udaipur', 'Jodhpur'): ['Vistara', 'SpiceJet'],
    ('Jammu', 'Shimla'): ['Air India', 'GoAir'],
    ('Bhubaneswar', 'Srinagar'): ['Vistara', 'Indigo'],
    ('Dehradun', 'Dibrugarh'): ['Air India', 'Akasa Air'],
    ('Tiruchirappalli', 'Delhi'): ['GoAir', 'SpiceJet'],
    # (More routes can be added similarly)
}

# Nearby airports (updated with additional nearby airports)
nearby_airports = {
    'Jaipur': 'Delhi',
    'Pune': 'Mumbai',
    'Ahmedabad': 'Mumbai',
    'Goa': 'Bengaluru',
    'Lucknow': 'Delhi',
    'Chandigarh': 'Delhi',
    'Indore': 'Bengaluru',
    'Coimbatore': 'Chennai',
    'Patna': 'Kolkata',
    'Surat': 'Mumbai',
    'Kanpur': 'Delhi',
    'Nagpur': 'Mumbai',
    'Vadodara': 'Mumbai',
    'Visakhapatnam': 'Hyderabad',
    'Madurai': 'Chennai',
    'Vijayawada': 'Hyderabad',
    'Rajkot': 'Ahmedabad',
    'Bhopal': 'Indore',
    'Mysore': 'Bengaluru',
    'Meerut': 'Delhi',
    'Ranchi': 'Kolkata',
    'Guwahati': 'Kolkata',
    'Udaipur': 'Ahmedabad',
    'Jodhpur': 'Jaipur',
    'Jammu': 'Delhi',
    'Shimla': 'Chandigarh',
    'Bhubaneswar': 'Kolkata',
    'Srinagar': 'Jammu',
    'Dehradun': 'Delhi',
    'Dibrugarh': 'Guwahati',
    'Tiruchirappalli': 'Chennai',
}

# Language texts (added Marathi, Hindi, and English)
language_text = {
    'english': {
        'heading': "🚀 Flight Price Prediction System ✈",
        'origin_label': "📍 Select Your Departure City (Origin)",
        'destination_label': "📍 Select Your Arrival City (Destination)",
        'date_label': "📅 Select Your Travel Date",
        'button_text': "🎟 FIND FLIGHTS",
        'flights_header': "### ✈ Available Flights for Your Date:",
        'comparison_header': "### 📊 Airline Comparison (Features & Ratings)",
        'recommended_airline': "### Recommended Airlines for You: ",
        'no_flights_message': "❌ No flights available on this route. Here are some nearby airports:",
        'nearby_airport_message': "🔍 Try flying from {starting_city} to {alternative_airport}.",
        'no_nearby_airports_message': "❌ No nearby airports available based on your destination.",
        'best_airline': "### Best Airline for Your Trip: {best_airline}",
    },
    'hindi': {
        'heading': "🚀 फ्लाइट किमतीं की पूर्वानुमान प्रणाली ✈",
        'origin_label': "📍 अपनी प्रस्थान शहर चुनें",
        'destination_label': "📍 अपनी आगमन शहर चुनें",
        'date_label': "📅 अपनी यात्रा की तारीख चुनें",
        'button_text': "🎟 फ्लाइट खोजें",
        'flights_header': "### ✈ आपकी तारीख के लिए उपलब्ध फ्लाइट्स:",
        'comparison_header': "### 📊 एअरलाइन्स की तुलना (विशेषताएँ और रेटिंग)",
        'recommended_airline': "### आपकी यात्रा के लिए सिफारिश की गई एअरलाइन्स: ",
        'no_flights_message': "❌ इस मार्ग पर कोई फ्लाइट उपलब्ध नहीं है। यहां कुछ नजदीकी हवाई अड्डे हैं:",
        'nearby_airport_message': "🔍 {starting_city} से {alternative_airport} तक उड़ान भरने की कोशिश करें।",
        'no_nearby_airports_message': "❌ आपके गंतव्य के अनुसार कोई नजदीकी हवाई अड्डा नहीं है।",
        'best_airline': "###  आपकी यात्रा के लिए सिफारिश की गई एअरलाइन्स: {best_airline}",
    },
    'marathi': {
        'heading': "🚀 फ्लाइट किमतींचा अंदाज प्रणाली ✈",
        'origin_label': "📍 आपले प्रस्थान शहर निवडा (सुरवात)",
        'destination_label': "📍 आपले आगमन शहर निवडा (गंतव्य)",
        'date_label': "📅 आपली प्रवासाची तारीख निवडा",
        'button_text': "🎟 फ्लाइट शोधा",
        'flights_header': "### ✈ आपल्या तारखेसाठी उपलब्ध फ्लाइट्स:",
        'comparison_header': "### 📊 एअरलाइन्सची तुलना (वैशिष्ट्ये आणि रेटिंग)",
        'recommended_airline': "###  आपल्यासाठी शिफारसीत एअरलाइन्स: ",
        'no_flights_message': "❌ या मार्गावर फ्लाइट उपलब्ध नाही. येथे काही नजीकचे विमानतळ आहेत:",
        'nearby_airport_message': "🔍 {starting_city} ऐवजी {alternative_airport} वरून प्रवास करा.",
        'no_nearby_airports_message': "❌ आपल्या गंतव्याच्या आधारावर कोणतेही नजीकचे विमानतळ उपलब्ध नाही.",
        'best_airline': "###  आपल्यासाठी शिफारसीत एअरलाइन्स: {best_airline}",
    }
}


# UI implementation
def main():
    st.title(language_text['english']['heading'])

    # Select language
    language_choice = st.selectbox("Select Language / भाषा चुनें / भाषा निवडा", ["English", "Hindi", "Marathi"])
    if language_choice == "Hindi":
        selected_lang = "hindi"
    elif language_choice == "Marathi":
        selected_lang = "marathi"
    else:
        selected_lang = "english"

    # Cities and Routes
    origin_city = st.selectbox(language_text[selected_lang]['origin_label'], cities)
    destination_city = st.selectbox(language_text[selected_lang]['destination_label'], cities)
    travel_date = st.date_input(language_text[selected_lang]['date_label'])
    find_flights_button = st.button(language_text[selected_lang]['button_text'])

    if find_flights_button:
        # Show Available Flights
        if (origin_city, destination_city) in routes:
            available_flights = routes[(origin_city, destination_city)]
            st.header(language_text[selected_lang]['flights_header'])
            st.write(f"🛫 Available Flights: {', '.join(available_flights)}")

            # Show Flight Price Details
            for flight in available_flights:
                st.write(f"{flight}:")
                st.write(f"  - General Class Price: ₹{flight_prices[flight]['General']}")
                st.write(f"  - Secondary Class Price: ₹{flight_prices[flight]['Secondary']}")
                st.write(f"  - High Class Price: ₹{flight_prices[flight]['High Class']}")

            # Show Airline Comparison
            st.header(language_text[selected_lang]['comparison_header'])
            for flight in available_flights:
                st.write(f"{flight}:")
                for feature, rating in airline_advantages[flight].items():
                    st.write(f"  - {feature}: {rating}/5")

            # Recommend Best Airline
            best_airline = available_flights[0]
            st.write(language_text[selected_lang]['best_airline'].format(best_airline=best_airline))
        else:
            st.write(language_text[selected_lang]['no_flights_message'])
            alternative_airport = nearby_airports.get(origin_city)
            if alternative_airport:
                st.write(language_text[selected_lang]['nearby_airport_message'].format(starting_city=origin_city,
                                                                                       alternative_airport=alternative_airport))
            else:
                st.write(language_text[selected_lang]['no_nearby_airports_message'])


if __name__ == '__main__':
    main()