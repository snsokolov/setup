import json

def completed_to_date(completed):
    return completed.split("T")[0]

entries = {}
with open("C:/Personal/tasks.json", encoding="utf8") as json_file:
    data = json.load(json_file)
    for list in data["items"]:
        for task in list["items"]:
            # Skip incomplete tasks.
            if task["status"] != "completed":
                continue

            completed_date = completed_to_date(task["completed"])
            if completed_date in entries:
                entries[completed_date].append(task["title"])
            else:
                entries[completed_date] = [task["title"]]

with open("C:/Personal/tasks_out.txt", "w", encoding="utf8") as out_file:
    for date in reversed(sorted(entries)):
        out_file.write("\n" + date + "\n")
        for task in entries[date]:
            out_file.write(task + "\n")

