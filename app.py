# powercalc_app.py

import streamlit as st
import plotly.graph_objects as go

def main():
    st.title("PowerCalc: Estimate Your Electricity Consumption")
    website_link = "https://energybrije.com/"
    st.sidebar.markdown(f'<a href="{website_link}">Visit My Website</a>', unsafe_allow_html=True)
    st.sidebar.header("Estimate Your Electricity Consumption")
    # Appliance sliders and operating hours
    #st.header("Appliance Power Consumption and Operating Hours")
    st.write("PowerCalc is an intuitive web application that empowers users to estimate their electricity consumption and make informed decisions. Users can adjust sliders for each appliance to set its power consumption (in watts), average monthly operating hours, and the number of equipment. Based on either the monthly electricity consumption or the available area for solar panels, PowerCalc suggests the required solar kW capacity. It also generates a pie chart to visualize the distribution of electricity consumption across different appliances. Designed for common people, PowerCalc simplifies the process of calculating monthly electricity bills and encourages sustainable energy choices. 🌞💡🏡")
    # Create two columns for equipment details
    col1, col2, col3 = st.columns(3)

    col1.header(":green[Add Power Consumption]")
    col2.header(":green[No. of Hours Run/Month]")
    col3.header(":green[No. of Equipment]")

    # Air Conditioner (1.5 ton)
    ac_power = col1.slider("Air Conditioner Power (Watts)", 600, 10000, 3154)
    ac_hours = col2.slider("Air Conditioner Hours/Month", min_value=0, max_value=744, value=60)
    ac_days = col3.slider("No. of AC", min_value=0, max_value=5, value=1)
    

    # Ceiling Fan
    fan_power = col1.slider("Ceiling Fan Power (Watts)", 0, 100, 70)
    fan_hours = col2.slider("Ceiling Fan Hours/Month", min_value=0, max_value=744, value=465)
    fan_days = col3.slider("No. of Ceiling Fan", min_value=0, max_value=10, value=5)

    # TV
    tv_power = col1.slider("TV Power (Watts)", 0, 400, 100)
    tv_hours = col2.slider("TV Hours/Month", min_value=0, max_value=744, value=124)
    tv_days = col3.slider("No. of TV", min_value=0, max_value=6, value=2)

    # RO Water Purifier
    ro_power = col1.slider("RO Water Purifier Power (Watts)", 25, 100, 45)
    ro_hours = col2.slider("RO Water Purifier Hours/Month", min_value=0, max_value=744, value=50)
    ro_days = col3.slider("No. of RO Water Purifier", min_value=0, max_value=5, value=1)

    # Personal Air Cooler
    cooler_power = col1.slider("Personal Air Cooler Power (Watts)", 50, 150, 60)
    cooler_hours = col2.slider("Personal Air Cooler Hours/Month", min_value=0, max_value=744, value=100)
    cooler_days = col3.slider("No. of Personal Air Cooler", min_value=0, max_value=31, value=12)

    # CFL/LED Bulbs
    bulb_power = col1.slider("CFL/LED Bulbs Power (Watts)", 5, 150, 15)
    bulb_hours = col2.slider("CFL/LED Bulbs Hours/Month", min_value=0, max_value=744, value=250)
    bulb_days = col3.slider("No. of CFL/LED Bulbs", min_value=0, max_value=20, value=8)

    # Tube Lights
    tube_power = col1.slider("Tube Lights Power (Watts)", 20, 200, 45)
    tube_hours = col2.slider("Tube Lights Hours/Month", min_value=0, max_value=744, value=250)
    tube_days = col3.slider("No. of Tube Lights", min_value=0, max_value=10, value=2)

    # Top-Load Washing Machine
    washer_power = col1.slider("Washing Machine Power (Watts)", 200, 1500, 500)
    washer_hours = col2.slider("Washing Machine Hours/Month", min_value=0, max_value=744, value=50)
    washer_days = col3.slider("No. of Washing Machine", min_value=0, max_value=3, value=1)

    # Submersible Pump
    submersible_power = col1.slider("Submersible Pump Power (Watts)", 200, 2500, 800)
    submersible_hours = col2.slider("Submersible Pump Hours/Month", min_value=0, max_value=744, value=15)
    submersible_days = col3.slider("No. of Submersible Pump", min_value=0, max_value=2, value=1)

    # Refrigerator (Fridge)
    fridge_power = col1.slider("Refrigerator Power (Watts)", 200, 1000, 400)
    fridge_hours = col2.slider("Refrigerator Hours/Month", min_value=0, max_value=744, value=300)
    fridge_days = col3.slider("No. of Refrigerator", min_value=0, max_value=5, value=1)

    # Electric Press (Iron)
    iron_power = col1.slider("Electric Press Power (Watts)", 1000, 3000, 2000)
    iron_hours = col2.slider("Electric Press Hours/Month", min_value=0, max_value=744, value=10)
    iron_days = col3.slider("No. of Electric Press", min_value=0, max_value=3, value=1)

    # Desktop Computer
    computer_power = col1.slider("Desktop Computer Power (Watts)", 100, 800, 200)
    computer_hours = col2.slider("Desktop Computer Hours/Month", min_value=0, max_value=744, value=240)
    computer_days = col3.slider("No. of Desktop Computer", min_value=0, max_value=5, value=2)


    # Slow EV Charger
    ev_charger_power = col1.slider("Slow EV Charger Power (Watts)", 1500, 30000, 1500)
    ev_charger_hours = col2.slider("Slow EV Charger Hours/Month", min_value=0, max_value=744, value=180)
    ev_charger_days = col3.slider("No. of Slow EV Charger", min_value=0, max_value=2, value=1)

    # Calculate total consumption
    total_consumption_wh_ac = (ac_power * ac_hours * ac_days)
    total_consumption_wh_fan = (fan_power * fan_hours * fan_days)
    total_consumption_wh_tv = (tv_power * tv_hours * tv_days)
    total_consumption_wh_ro = (ro_power * ro_hours * ro_days)
    total_consumption_wh_cooler = (cooler_power * cooler_hours * cooler_days)
    total_consumption_wh_bulb = (bulb_power * bulb_hours * bulb_days)
    total_consumption_wh_tube = (tube_power * tube_hours * tube_days)
    total_consumption_wh_washer = (washer_power * washer_hours * washer_days)
    total_consumption_wh_submersible = (submersible_power * submersible_hours * submersible_days)
    total_consumption_wh_fridge = (fridge_power * fridge_hours * fridge_days)
    total_consumption_wh_iron = (iron_power * iron_hours * iron_days)
    total_consumption_wh_computer = (computer_power * computer_hours * computer_days)
    total_consumption_wh_ev = (ev_charger_power * ev_charger_hours * ev_charger_days)

    appliances = [total_consumption_wh_ac,total_consumption_wh_fan,total_consumption_wh_tv,total_consumption_wh_ro,total_consumption_wh_cooler,total_consumption_wh_bulb,total_consumption_wh_tube,total_consumption_wh_washer,total_consumption_wh_submersible, total_consumption_wh_fridge, total_consumption_wh_iron, total_consumption_wh_computer, total_consumption_wh_ev]
    total_consumption_wh =  sum(appliances)
    total_consumption_kwh = total_consumption_wh / 1000
    

    # Estimate monthly cost (you can customize the rate)
    st.sidebar.markdown(f"**Monthly Consumption:** {total_consumption_kwh} (kWh)", unsafe_allow_html=True)
    utility_rate_per_kwh = st.sidebar.number_input("Enter Unit Rate in INR",1.0, 20.0, 7.0)  # Example rate in INR (adjust as needed)
    monthly_cost = total_consumption_kwh * utility_rate_per_kwh
    st.sidebar.markdown(f"<font color='blue'><b>Estimated Monthly Cost:</b> ₹{monthly_cost:.2f}</font>", unsafe_allow_html=True)

    # Sample data for the pie chart
    labels = ["ac","fan","tv","ro","cooler","bulb","tube","washer","submersible", "fridge","iron", "computer", "ev"]
    sizes = appliances

    # Create the Plotly figure
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])

    # Customize the layout (optional)
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=12)

    st.header("Energy Consumption Breakdown (wh)")
    # Display the pie chart in Streamlit
    st.plotly_chart(fig)

    ########################################

    st.sidebar.title("Solar Panel Calculator")

    # Sidebar: User input selection
    user_input = st.sidebar.radio("Select Input Type", ["Monthly Electricity (kWh)", "Available Area (m²)"])

    if user_input == "Monthly Electricity (kWh)":
        monthly_electricity_kwh = total_consumption_kwh 
        solar_panel_electricity_generation_perday = st.sidebar.number_input("Solar Panel Electricity Generation per day",1,7,5)
        number_of_day_sun_available = st.sidebar.number_input("Number of Day Sun Available per Month", 0, 31, 22)
        monthly_sun_elec_production_hours = solar_panel_electricity_generation_perday * number_of_day_sun_available
        solar_panel_capacity_kw = monthly_electricity_kwh/monthly_sun_elec_production_hours
    else:
        available_area_m2 = st.sidebar.number_input("Enter Total Available Roof Area (m²)", min_value=10, value=25)
        solar_panel_capacity_kw = calculate_solar_panel_capacity_from_area(available_area_m2)

    st.sidebar.markdown(f"**Required Solar Panel Capacity:** {solar_panel_capacity_kw:.2f} kW")

# def calculate_solar_panel_capacity(monthly_electricity_kwh):
#     # Assuming 16% efficiency and 1 kW panel requires 10 m²
#     panel_efficiency = 0.16
#     panel_area_per_kw = 10.0
#     required_capacity_kw = monthly_electricity_kwh / (30 * panel_efficiency * panel_area_per_kw)
#     return required_capacity_kw

def calculate_solar_panel_capacity_from_area(available_area_m2):
    # Assuming 1 kW panel requires 10 m²
    panel_area_per_kw = st.sidebar.number_input("Solar Panel Area Required per kw", 0,20,10)
    required_capacity_kw = available_area_m2 / panel_area_per_kw
    return required_capacity_kw

if __name__ == "__main__":
    main()

