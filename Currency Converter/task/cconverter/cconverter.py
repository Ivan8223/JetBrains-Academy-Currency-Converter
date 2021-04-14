import requests

SOURCE_URL = 'http://www.floatrates.com/daily/'
cached_currency_rates = {}


def get_all_rates_by_currency(currency):
    r = requests.get(f"{SOURCE_URL}{currency}.json")

    if r:
        return r.json()


def add_currency_rate_to_cache(currency_name, currency_info):
    cached_currency_rates.update({currency_name: currency_info['rate']})


def get_currency_rate_from_cache(currency_name):
    return cached_currency_rates[currency_name]


def is_in_cache(currency):
    print("Checking the cache...")

    if currency in cached_currency_rates:
        print("Oh! It is in the cache!")
        return True

    print("Sorry, but it is not in the cache!")
    return False


def print_exchange_currency_result(amount_of_money,
                                   rate_for_exchange,
                                   currency_to_exchange):
    print(f"You received "
          f"{round(amount_of_money * rate_for_exchange, 2)} "
          f"{currency_to_exchange}.")


def main():
    target_currency = input()
    all_currency_rates = get_all_rates_by_currency(target_currency)

    if target_currency != 'usd':
        add_currency_rate_to_cache('usd', all_currency_rates['usd'])

    if target_currency != 'eur':
        add_currency_rate_to_cache('eur', all_currency_rates['eur'])

    while True:
        currency_to_exchange = input()
        if not currency_to_exchange:
            break

        amount_of_money = input()
        if not amount_of_money:
            break

        if not is_in_cache(currency_to_exchange):
            add_currency_rate_to_cache(
                currency_to_exchange,
                get_all_rates_by_currency(
                    target_currency)
                [currency_to_exchange]
            )

        currency_rate_from_cache = get_currency_rate_from_cache(
                currency_to_exchange
        )

        print_exchange_currency_result(
            int(amount_of_money),
            currency_rate_from_cache,
            currency_to_exchange
        )


if __name__ == '__main__':
    main()
