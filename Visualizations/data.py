import pandas as pd
df = pd.read_csv('../due_Sep1/Instructions/Resources/cities.csv')
df.to_html('table.html', index=False, classes='table table-stripped')