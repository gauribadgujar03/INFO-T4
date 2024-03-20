import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from urllib import request

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        
        self.location_label = ttk.Label(master, text="Enter Location:")
        self.location_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.location_entry = ttk.Entry(master, width=30)
        self.location_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.search_button = ttk.Button(master, text="Search", command=self.search_weather)
        self.search_button.grid(row=0, column=2, padx=10, pady=5)
        
        self.weather_frame = ttk.LabelFrame(master, text="Weather Details")
        self.weather_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W+tk.E)
        
        self.weather_label = ttk.Label(self.weather_frame, text="")
        self.weather_label.pack()
        
    def search_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showwarning("Warning", "Please enter a location.")
            return
        
        api_key = "630c2a6ca11cdcea058a14d06946b293"  # Replace with your OpenWeatherMap API key
     
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        
        try:
            with request.urlopen(url) as response:
                data = json.loads(response.read())
                if data["cod"] == 200:
                    weather_description = data["weather"][0]["description"]
                    temperature = data["main"]["temp"]
                    humidity = data["main"]["humidity"]
                    wind_speed = data["wind"]["speed"]
                    
                    weather_info = f"Weather: {weather_description.capitalize()}\n"
                    weather_info += f"Temperature: {temperature}°C\n"
                    weather_info += f"Humidity: {humidity}%\n"
                    weather_info += f"Wind Speed: {wind_speed} m/s"
                    
                    self.weather_label.config(text=weather_info)
                else:
                    messagebox.showerror("Error", "Location not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()