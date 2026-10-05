def sort_by_ratings(items: list):
    def order_by_rating(item: object):
        return item["rating"]

    return sorted(items, key=order_by_rating, reverse=True)
