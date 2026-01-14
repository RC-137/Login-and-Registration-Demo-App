import webview
import csv
import random
import os

class RegisterAPI:
    def register(self, name, username, custom, length):
        if not name or not username:
            return {"success": False, "message": "Name and Username are required"}

        try:
            passlength = int(length)
        except ValueError:
            return {"success": False, "message": "Password length must be a number"}

        chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&()"
        password = "".join(random.choice(chars) for _ in range(passlength))

        # Ensure store.csv exists
        file_exists = os.path.exists("store.csv")
        with open("store.csv", 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                # Optional: write headers
                writer.writerow(["username", "password", "name", "custom"])
            writer.writerow([username, password, name, custom])

        return {
            "success": True,
            "message": f"Registration Successful!\nUsername: {username}\nPassword: {password}"
        }

if __name__ == "__main__":
    webview.create_window(
        "User Registration - Storytelling RC",
        "register.html",
        width=400,
        height=500,
        js_api=RegisterAPI()
    )
    webview.start()
