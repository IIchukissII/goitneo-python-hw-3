import datetime


def get_birthdays_per_week(data):
    current_date = datetime.date.today()
    people_with_birthday_next_week = []
    people_with_birthday_next_week_dict = {}
    message = f'Today is {current_date.strftime("%A %d %B %Y")}\n'
    message += "The following people have their birthdays next week:\n"

    for person in data:
        person_birthday = person["birthday"]
        birthday_this_year = person_birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = person_birthday.replace(year=current_date.year + 1)

        delta_weeks = (birthday_this_year - current_date).days // 7

        if delta_weeks == 0 and (birthday_this_year.weekday() in (5, 6)):
            people_with_birthday_next_week.append(["Monday", person["name"]])
        elif delta_weeks == 1 and not (birthday_this_year.weekday() in (5, 6)):
            people_with_birthday_next_week.append(
                [birthday_this_year.strftime("%A"), person["name"]]
            )

    for people in people_with_birthday_next_week:
        day = people[0]
        if day not in people_with_birthday_next_week_dict:
            people_with_birthday_next_week_dict[day] = []
        people_with_birthday_next_week_dict[day].append(people[1])

    #    message += "{:>15}: {:<}\n".format('Day of week', 'Name')
    for key, value in people_with_birthday_next_week_dict.items():
        message += "{:<15}: {:<}\n".format(key, ", ".join(value))

    return message


if __name__ == "__main__":
    import json
    from faker import Faker

    fake = Faker()

    def get_fake_users(amount):
        users_list = []
        for i in range(amount):
            mock = {
                "name": fake.name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "birthday": fake.date_object().strftime("%d.%m.%Y"),
            }
            users_list.append(mock)

        # Serializing json
        json_object = json.dumps(users_list, indent=4)

        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
        return users_list

    data = get_fake_users(200)
    print(get_birthdays_per_week(data))
