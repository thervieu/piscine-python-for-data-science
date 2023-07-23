from load_csv import load

import math
import matplotlib.pyplot as plt

def main():
    df_life = load('../assets/life_expectancy_years.csv')
    df_life = df_life[['country', '1900']]
    arr_life = df_life['1900'].tolist()

    df_gdp = load('../assets/income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df_gdp = df_gdp[['country', '1900']]
    arr_gdp = df_gdp['1900'].tolist()
    
    print(len(arr_gdp))
    print(len(arr_life))
    
    # Create temporary lists to store the updated values
    temp_array1 = []
    temp_array2 = []

    # Loop through the arrays using zip
    for value1, value2 in zip(arr_life, arr_gdp):
        # Check if the value in array1 is not NaN
        if not math.isnan(value1):
            # Append the non-NaN values to the temporary lists
            temp_array1.append(value1)
            temp_array2.append(value2)

    # Update the original arrays with the non-NaN values
    arr_life = temp_array1
    arr_gdp = temp_array2

    plt.figure(figsize=(10, 6))
    # Plot the data
    plt.scatter(arr_gdp, arr_life)

    plt.xscale('log')
    plt.xlim(300)
    # Add labels and title
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
