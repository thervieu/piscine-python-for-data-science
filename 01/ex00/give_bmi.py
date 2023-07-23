def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    return [float(w) / (float(h)*float(h)) for w, h in zip(weight, height)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [elt > limit for elt in bmi]
