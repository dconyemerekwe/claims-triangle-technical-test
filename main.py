import csv

triangles = {}

with open("input.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # Skip header row
    
    for row in reader:
        product = row[0].strip()
        origin_year = int(row[1].strip())
        development_year = int(row[2].strip())
        incremental_value = float(row[3].strip())
        
        if product not in triangles:
            triangles[product] = {}
        
        if origin_year not in triangles[product]:
            triangles[product][origin_year] = {}
        
        triangles[product][origin_year][development_year] = incremental_value

min_origin_year = float("inf")
max_development_year = float("-inf")

for product in triangles:
    for origin_year in triangles[product]:
        # Update to minimum origin year
        if origin_year < min_origin_year:
            min_origin_year = origin_year
    
    for development_year in triangles[product][origin_year]:
        # Update to maximum development year
        if development_year > max_development_year:
            max_development_year = development_year

# Total number of development years calculation
total_development_years = max_development_year - min_origin_year + 1

# Filling missing zeros to complete triangle
for product in triangles:
    for origin_year in range(min_origin_year, max_development_year + 1):
        if origin_year not in triangles[product]:
            triangles[product][origin_year] = {}
        
        for development_year in range(origin_year, max_development_year + 1):
            if development_year not in triangles[product][origin_year]:
                triangles[product][origin_year][development_year] = 0.0

# Accumulating values
cumulative_triangles = {}

for product in triangles:
    cumulative_triangles[product] = {}

    for origin_year in triangles[product]:
        cumulative_triangles[product][origin_year] = {}
        running_total = 0 # Reset running total for each origin year

        for development_year in sorted(triangles[product][origin_year].keys()):
            running_total += triangles[product][origin_year][development_year]
            cumulative_triangles[product][origin_year][development_year] = running_total

# Write results to output.csv
with open("output.csv", "w") as file:
    file.write(f"{min_origin_year}, {total_development_years}\n")

    # One line per product 
    for product in sorted(cumulative_triangles.keys()):
        values = [product]

        # Triangle read column by column
        for development_year in range(min_origin_year, max_development_year + 1):
            for origin_year in range(min_origin_year, development_year + 1):
                if origin_year in cumulative_triangles[product]:
                    if development_year in cumulative_triangles[product][origin_year]:
                        value = cumulative_triangles[product][origin_year][development_year]
                        values.append(str(value))
                        
        file.write(", ".join(values) + "\n")

print("Output written to output.csv!")
print("\nCheck the output.csv file in your folder.")