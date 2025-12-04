#!/usr/bin/python3

import requests
import csv

fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        print("Status Code: 200")
        posts = response.json()
        cleaned_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv","w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "tittle", "body"])
            writer.writeheader()
            write.writerows(cleaned_posts)
