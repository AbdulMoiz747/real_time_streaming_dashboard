import csv, random, datetime

pages = ["/home", "/products", "/about", "/contact", "/cart"]

with open("logs.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "user_id", "page", "duration"])
    for _ in range(500):
        time = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 86400))
        writer.writerow([
            time.isoformat(),
            random.randint(1, 100),
            random.choice(pages),
            random.randint(5, 300)
        ])

print("✅ Log data generated as logs.csv")