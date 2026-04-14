# Country Population Projection

seconds_per_year = 60 * 60 * 24 * 365

births_per_year = seconds_per_year / 10
deaths_per_year = seconds_per_year / 20
immigrants_per_year = seconds_per_year / 30

curr_population = 50_000_000

net_change_per_year = births_per_year + immigrants_per_year - deaths_per_year

years = 5
new_population = curr_population + net_change_per_year * years

print(int(new_population))