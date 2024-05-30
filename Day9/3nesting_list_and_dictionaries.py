
capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

# nesting dictionary in dictionary
travel_log1 = {
    "France":["Paris","Madrid","Dijon"],
    "Germany":["Berlin","Hamburg"]
}

travel_log2 = {
    "France":{"cities_visited":["Paris","Madrid","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["]Berlin","Hamburg"],"total_visited":5}
}

# Nesting dict in list
travel_log3 = {
    {"country":"France",
     "cities_visited":["Paris","Madrid","Dijon"],
     "total_visits":12},
    {"country":"Germany",
     "cities_visited":["]Berlin","Hamburg"],
     "total_visited":5}
}
