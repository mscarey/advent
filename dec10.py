def get_data(day: int = 10, toy: bool = True) -> list[list[int]]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        lines = csv_file.readlines()
        rows = [row.strip("\n") for row in lines]
        return rows


MATCHES = {")": "(", "}": "{", "]": "[", ">": "<"}
REVERSE_MATCHES = {v: k for k, v in MATCHES.items()}

SCORING = {")": 3, "}": 1197, "]": 57, ">": 25137, "": 0}


def check_corrupted(text: str) -> str:
    stack = []
    for c in text:
        if c in (")]>}"):
            if MATCHES[c] != stack.pop():
                return c
        else:
            stack.append(c)
    return ""


def get_score(text: str) -> int:
    return SCORING[check_corrupted(text)]


AUTOCOMPLETE_SCORING = {")": 1, "]": 2, "}": 3, ">": 4}


def score_completion_string(text: str) -> int:
    score = 0
    for c in text:
        score *= 5
        score += AUTOCOMPLETE_SCORING[c]
    return score


def filter_corrupted(data: list[str]) -> list[str]:
    return [row for row in data if not check_corrupted(row)]


def get_autocomplete(text: str) -> str:
    stack = []
    for c in text:
        if c in (")]>}"):
            stack.pop()
        else:
            stack.append(c)
    answer = ""
    while stack:
        c = stack.pop()
        answer += REVERSE_MATCHES[c]
    return answer


def get_autocomplete_scores(data: list[str]) -> list[int]:
    to_complete = filter_corrupted(data)
    autocompletes = [get_autocomplete(row) for row in to_complete]
    return [score_completion_string(row) for row in autocompletes]


def get_middle_score(data: list[str]) -> int:
    scores = sorted(get_autocomplete_scores(data))
    return scores[len(scores) // 2]
