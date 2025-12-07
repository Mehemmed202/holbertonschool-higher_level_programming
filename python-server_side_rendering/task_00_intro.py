#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template is invalid input type.")
        return

    if not isinstance(attendees, dict):
        print("Attendees is invalid input type.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    output_dir = "invites"
    os.makedirs(output_dir, exist_ok=True)

    for index, attendee in enumerate(attendees, start=1):
        placeholder = ["name", "event_title", "event_date", "event_location"]

        for key in placeholder:
            value = attendees.get(key)
            if value is None:
                value = "N/A"

            content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open("filename", "w", encoding="utf-8") as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
