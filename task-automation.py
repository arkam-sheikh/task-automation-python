import smtplib
import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

# Function to send an email
def send_email(subject, body, to_email):
    from_email = input("Enter your email address: ")
    password = getpass("Enter your email password: ")

    try:
        # Create message object
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Create server object
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email successfully sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to rename files in a directory
def rename_files_in_directory(directory, prefix):
    try:
        if not os.path.isdir(directory):
            print("Invalid directory path.")
            return

        for count, filename in enumerate(os.listdir(directory)):
            file_extension = os.path.splitext(filename)[1]
            new_filename = f"{prefix}_{count}{file_extension}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

    except Exception as e:
        print(f"Error renaming files: {e}")

# Function to fetch and print weather information
def fetch_weather(city):
    api_key = input("Enter your OpenWeatherMap API key: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key

    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_description = weather["description"]

            print(f"Temperature: {temperature:.2f}°C")
            print(f"Atmospheric Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_description.capitalize()}")
        else:
            print("City not found.")

    except Exception as e:
        print(f"Error fetching weather data: {e}")

# Main function to run the tasks
def main():
    while True:
        print("\nTask Automation Script")
        print("1. Send an Email")
        print("2. Rename Files in a Directory")
        print("3. Fetch Weather Information")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter the email subject: ")
            body = input("Enter the email body: ")
            to_email = input("Enter the recipient email: ")
            send_email(subject, body, to_email)
        elif choice == '2':
            directory = input("Enter the directory path: ")
            prefix = input("Enter the prefix for renaming files: ")
            rename_files_in_directory(directory, prefix)
        elif choice == '3':
            city = input("Enter the city name: ")
            fetch_weather(city)
        elif choice == '4':
            print("Exiting the script.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
