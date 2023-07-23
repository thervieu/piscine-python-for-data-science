from load_csv import load

import matplotlib.pyplot as plt

def main():
    df = load('../assets/life_expectancy_years.csv')
    df = df[df['country'] == "France"]
    values = df.values[0][1:]
    years = [eval(i) for i in df.columns[1:]]

    plt.figure(figsize=(10, 6))
    
    # Plot the data
    plt.plot(years, values, linestyle='-', color='b', label='Values')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('France Life Expectancy Projections')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
