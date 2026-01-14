import webview
import csv
import os
import subprocess

class LoginAPI:
    def login(self, username, password):
        if not os.path.exists("store.csv"):
            return {"success": False, "message": "No user database found. Please register first."}

        with open("store.csv", "r") as file:                   
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2 and row[0] == username and row[1] == password or row[3] == password:
                    return {"success": True, "message": f"Welcome Back {row[2]}!"}

        return {"success": False, "message": "Invalid credentials"}

    def register(self):
        # This will run your separate cred.py script
        try:
            subprocess.Popen(["python", "cred.py"])
            return {"success": True, "message": "Registration window opened!"}
        except Exception as e:
            return {"success": False, "message": f"Error opening registration: {e}"}

if __name__ == "__main__":
    webview.create_window(
        "Login - Storytelling RC",
        "login.html",
        width=1200,
        height=700,
        js_api=LoginAPI()
    )
    webview.start()
