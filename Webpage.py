import streamlit as st

class PowerSystemParameters:
    def __init__(self):
        self.voltage = None
        self.capacity = None
        self.OEM = None
        self.SMVA = None
        self.pq_curve = None
        self.harmonic_planning_limit = None
        self.flicker_limit = None
        self.voltage_unbalance_limit = None
        self.frequency_protection_curve = None
        self.voltage_protection_curve = None
        self.k_factor = None
        self.lvrt_threshold = None
        self.hvrt_threshold = None
        self.rise_time = None
        self.settling_time = None
        self.pf_droop = None
        self.voltage_control_droop = None

    def display(self):
        # Title and instructions
        st.title('Power System Parameters')
        st.write('Please enter the following parameters:')

        # Input textboxes for each parameter
        self.voltage = st.text_input('Voltage', '')
        self.capacity = st.text_input('Capacity', '')
        self.OEM = st.text_input('OEM', '')
        self.SMVA = st.text_input('SMVA', '')
        self.pq_curve = st.file_uploader('PQ Curve (Excel file)', type=['xlsx'])
        self.harmonic_planning_limit = st.file_uploader('Harmonic Planning Limit (Excel file)', type=['xlsx'])
        self.flicker_limit = st.text_input('Flicker Limit', '')
        self.voltage_unbalance_limit = st.text_input('Voltage Unbalance Limit', '')
        self.frequency_protection_curve = st.file_uploader('Frequency Protection Curve (Excel file)', type=['xlsx'])
        self.voltage_protection_curve = st.file_uploader('Voltage Protection Curve (Excel file)', type=['xlsx'])
        self.k_factor = st.text_input('K Factor', '')
        self.lvrt_threshold = st.text_input('LVRT Threshold', '')
        self.hvrt_threshold = st.text_input('HVRT Threshold', '')
        self.rise_time = st.text_input('Rise Time', '')
        self.settling_time = st.text_input('Settling Time', '')
        self.pf_droop = st.file_uploader('P(f) Droop (Excel file)', type=['xlsx'])
        self.voltage_control_droop = st.file_uploader('Voltage Control Droop (Excel file)', type=['xlsx'])

        # Button to submit the form
        submitted = st.button('Submit')

        # Display submitted values
        if submitted:
            st.write('Submitted Values:')
            st.write(f'Voltage: {self.voltage}')
            st.write(f'Capacity: {self.capacity}')
            st.write(f'OEM: {self.OEM}')
            st.write(f'SMVA: {self.SMVA}')
            st.write(f'PQ Curve: {self.pq_curve.name if self.pq_curve is not None else "Not uploaded"}')
            st.write(f'Harmonic Planning Limit: {self.harmonic_planning_limit.name if self.harmonic_planning_limit is not None else "Not uploaded"}')
            st.write(f'Flicker Limit: {self.flicker_limit}')
            st.write(f'Voltage Unbalance Limit: {self.voltage_unbalance_limit}')
            st.write(f'Frequency Protection Curve: {self.frequency_protection_curve.name if self.frequency_protection_curve is not None else "Not uploaded"}')
            st.write(f'Voltage Protection Curve: {self.voltage_protection_curve.name if self.voltage_protection_curve is not None else "Not uploaded"}')
            st.write(f'K Factor: {self.k_factor}')
            st.write(f'LVRT Threshold: {self.lvrt_threshold}')
            st.write(f'HVRT Threshold: {self.hvrt_threshold}')
            st.write(f'Rise Time: {self.rise_time}')
            st.write(f'Settling Time: {self.settling_time}')
            st.write(f'P(f) Droop: {self.pf_droop.name if self.pf_droop is not None else "Not uploaded"}')
            st.write(f'Voltage Control Droop: {self.voltage_control_droop.name if self.voltage_control_droop is not None else "Not uploaded"}')

    def get_voltage(self):
        return self.voltage

    def get_capacity(self):
        return self.capacity

    def get_OEM(self):
        return self.OEM

    def get_SMVA(self):
        return self.SMVA

    def get_pq_curve(self):
        return self.pq_curve

    def get_harmonic_planning_limit(self):
        return self.harmonic_planning_limit

    def get_flicker_limit(self):
        return self.flicker_limit

    def get_voltage_unbalance_limit(self):
        return self.voltage_unbalance_limit

    def get_frequency_protection_curve(self):
        return self.frequency_protection_curve

    def get_voltage_protection_curve(self):
        return self.voltage_protection_curve

    def get_k_factor(self):
        return self.k_factor

    def get_lvrt_threshold(self):
        return self.lvrt_threshold

    def get_hvrt_threshold(self):
        return self.hvrt_threshold

    def get_rise_time(self):
        return self.rise_time

    def get_settling_time(self):
        return self.settling_time

    def get_pf_droop(self):
        return self.pf_droop

    def get_voltage_control_droop(self):
        return self.voltage_control_droop



