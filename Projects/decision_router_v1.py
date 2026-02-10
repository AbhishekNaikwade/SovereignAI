from datetime import datetime
def get_user_input():
    text = input("Enter a message: ").strip()
    return text
def validate_input(text):
    if len(text) == 0:
        return False, "Empty"
    if len(text) > 200:
        return False, "TOO_LONG"
    return True, "OK"
def guardrail_check(text):
    letters = sum(c.isalpha() for c in text)
    if letters == 0:
        return False, "NO_LETTERS"
    ratio = letters / len(text)
    if ratio < 0.3:
        return False, "LOW_SIGNAL"
    banned_patterns = ["rm -rf", "drop table", "<script>"]
    t = text.lower()
    for p in banned_patterns:
        if p in t:
            return False, "BANNED_PATTERN"
    return True, "OK"
def classify_input(text):
    t = text.lower().strip()
    if t.startswith(("run","execute","start")):
        return "COMMAND"
    if text.endswith("?") and any(c.isalpha() for c in t):
        return "QUESTION"
    return "UNKNOWN"
def handle_question(text):
    return f"[QUESTION_HANDLER] You asked: {text}"
def handle_command(text):
    return f"[COMMAND_HANDLER] Command detected: {text}"
def handle_unknown(text):
    return f"[UNKNOWN_HANDLER] Could not classify: {text}"
def route(text, category):
    if category == "QUESTION":
        return handle_question(text)
    elif category == "COMMAND":
        return handle_command(text)
    else:
        return handle_unknown(text)
def log_result(text, category, result, status):
    length = len(text)

    line = (
        f"{datetime.now()} | "
        f"status={status} | "
        f"category={category} | "
        f"len={length} | "
        f"text={text} | "
        f"result={result}\n"
    )

    with open("logs/router_log.txt", "a") as f:
        f.write(line)
def main():
    text = get_user_input()
    valid, status = validate_input(text)
    if not valid:
        print(f"Validation failed: {status}")
        log_result(text, "INVALID", "", status)
        return
    safe, gstatus = guardrail_check(text)
    if not safe:
        print(f"Gaurdrail blocked input: {gstatus}")
        log_result(text, "BLOCKED", "", gstatus)
        return
    category = classify_input(text)
    result = route(text, category)
    print(result)
    log_result(text, category, result, "OK")
if __name__ == "__main__":
    main()