#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])







def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        print("Status Code: 200")
        posts = response.json()
        cleaned_posts = [
            {
                "id": post["id"],
                "tittle": post["tittle"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv","w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "tittle", "body"])
            writer.writeheader()
            writer.writerows(cleaned_posts)
