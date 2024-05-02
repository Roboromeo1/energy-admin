import Webpage as wb
import pandas as pd
import config_file as cf

# Create an instance of PowerSystemParameters
user_input = wb.PowerSystemParameters()

# Display the input form
user_input.display()

# Get the pq_curve attribute
pq_curve = user_input.get_pq_curve()
# pq_curve_df = pd.read_excel(pq_curve)
# print(pq_curve_df)


pq = cf.PQcurve("OEM", "SMVA", pq_curve, 40)
pq.load_PQcurve()
pq.config_PQcurve()
pq.plot_pq_curve()
