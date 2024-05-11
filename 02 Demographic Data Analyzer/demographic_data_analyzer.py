import pandas as pd
df = pd.read_csv('./adult_data.csv')

def calculate_demographic_data(print_data=True):
    # Read data from file
    
    df['race'].describe()

    race_count = df['race'].value_counts()

    #Race count begins
    print(race_count)

    print(race_count.dtypes)

    if isinstance(race_count, pd.Series):
        print("The variable is a Pandas Series.")
    else:
        print("The variable is not a Pandas Series.")

    #average age of men calcuation begins
    male_data = df[df['sex'] == 'Male']

    average_age_men = round(male_data['age'].mean(),1)

    print(average_age_men)

    #percentage bachelors count begin
    percentage_bachelors = round(df['education'].value_counts()['Bachelors']/df['education'].count()*100,1)
    print(percentage_bachelors)

    #high education rich count begins
    salary_count = df['salary'].value_counts()
    print(salary_count)

    high_degree = ['Bachelors','Masters','Doctorate']
    high_education = df[df['education'].isin(high_degree)]
    count_high_education = high_education['salary'].count()

    count_high_education_rich = high_education[high_education['salary'] == '>50K']['salary'].count()

    higher_education_rich = round(count_high_education_rich/count_high_education*100,1)
    print(higher_education_rich)

    #lower education rich
    lower_education = df[~df['education'].isin(high_degree)]

    b = lower_education['salary'].count()

    df_lower_education_rich = lower_education[lower_education['salary'] == '>50K']

    a = df_lower_education_rich['salary'].count()

    lower_education_rich = round(a/b*100,1)
    print(lower_education_rich)

    min_work_hours = df['hours-per-week'].min()
    print(min_work_hours)

    df_pay_hr = df[['hours-per-week','salary']]
    df_pay_hr.head()

    df_1hr = df_pay_hr[df_pay_hr['hours-per-week'] == min_work_hours]
    num_min_workers = df_1hr['salary'].count()

    count_1hr_rich =df_1hr[df_1hr['salary'] == '>50K']['salary'].count()

    rich_percentage = count_1hr_rich/num_min_workers*100
    print(rich_percentage)

    df_country = df[['native-country','salary']]

    df_rich_country = df_country[df_country['salary'] == '>50K']

    c = df_rich_country['native-country'].value_counts()
    c.sort_index()

    d = df['native-country'].value_counts()
    d.sort_index()

    e = c/d*100

    e.sort_values()

    highest_earning_country_percentage = round(e.max(),1)
    print(highest_earning_country_percentage)

    print(type(e))

    highest_earning_country = e.idxmax()
    print(highest_earning_country)

    df_India =df[['native-country','salary','occupation']]

    df_India1 = df_India[df_India['native-country'] == 'India'][df_India['salary'] == '>50K']

    top_IN_occupation = df_India1['occupation'].value_counts().idxmax()
    print(top_IN_occupation)


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
