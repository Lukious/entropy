import bisect

HOURS_IN_DAYS = 24
SECONDS_IN_ONE_DAY = 3600

time_to_object_map = {
    86400: "You could have written the song Yesterday",
    2419200: "A house fly lives and dies",
    126227808: "You could have painted the Mona Lisa",
    1209600: "You could have built Facebook",
    630720000: "You could have built the Taj Mahal",
    259200: "You could have reached the moon",
    518400: "You could have written the The Strange Case of Docotor Jekyll and Mr Hyde",
    216000: "You could have written the The Boy in Striped Pajamas",
    1814400: "You could have written A Christmas Carol",
}


def get_message(wasted_days):
    days_in_seconds = wasted_days * HOURS_IN_DAYS * SECONDS_IN_ONE_DAY
    ordered_keys = sorted(time_to_object_map.keys())
    list_of_tuples = [(x, time_to_object_map[x]) for x in ordered_keys]
    first, second = zip(*list_of_tuples)
    index = bisect.bisect_left(first, days_in_seconds)
    return second[index]


if __name__ == "__main__":
    print(get_message(1))
