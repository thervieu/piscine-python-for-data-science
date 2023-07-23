from load_csv import load

import matplotlib.pyplot as plt

def main():
    df = load('../assets/population_total.csv')

    dfFR = df[df['country'] == "France"]
    dfBZ = df[df['country'] == "Belgium"]
    valuesFR = dfFR.values[0][1:]
    valuesBZ = dfBZ.values[0][1:]
    valuesFR = [eval(i[:len(i) - 1]) for i in valuesFR]
    valuesBZ = [eval(i[:len(i) - 1]) for i in valuesBZ]
    valuesFR = valuesFR[:250]
    valuesBZ = valuesBZ[:250]


    years = [eval(i) for i in df.columns[1:][:250]]

    plt.figure(figsize=(10, 6))
    
    # Plot the data
    plt.plot(years, valuesBZ, linestyle='-', color='b', label='Belgium')
    plt.plot(years, valuesFR, linestyle='-', color='g', label='France')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('France Life Expectancy Projections')

    # Add legend in the bottom-right corner
    plt.legend(loc='lower right')
    plt.yticks([20, 40, 60], ['20M', '40M', '60M'])

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
