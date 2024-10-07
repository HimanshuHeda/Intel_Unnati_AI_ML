# 1. You are developing a program to store geographical coordinates (latitude and longitude)
# of various cities. The coordinates should be immutable so that they don&#39;t get accidentally
# changed.
# Question: How would you use tuples to store the coordinates for five cities? Demonstrate how
# you would access the longitude of the third city in the list.

cities = [
    (40.7128, -74.0060),  # New York
    (34.0522, -118.2437),  # Los Angeles
    (37.7749, -122.4194),  # San Francisco
    (41.8781, -87.6298),  # Chicago
    (29.7604, -95.3698)   # Houston
]

third_city_longitude = cities[2][1]
print(third_city_longitude)  # Output: -122.4194

