def get_data(day: int = 12, toy: bool = True) -> list[list[str]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        lines = csv_file.readlines()
        rows = [row.strip("\n") for row in lines]
        return [row.split("-") for row in rows]
