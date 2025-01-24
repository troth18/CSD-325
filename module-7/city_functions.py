def city_country(city, country, population = None, language = None):
    #If population and language are included returns all arguments
    if population and language:
        return f"{city}, {country} - Population: {population}, {language}"
    #If population is included returns all arguments except language
    elif population:
        return f"{city}, {country} - Population: {population}"
    #If language is included returns all arguments except population
    elif language:
        return f"{city}, {country}, {language}"
    #If neither population or language are included returns only city and country
    else:
        return f"{city}, {country}"

print(city_country("Indianapolis", "United States"))
print(city_country("Berlin", "Germany", "3432000"))
print(city_country("Tokyo", "Japan", "14180000", "Japanese"))