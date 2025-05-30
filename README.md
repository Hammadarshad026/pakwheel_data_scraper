# 🚗 PakWheels Data Scraper

A simple yet powerful web scraper that collects used car listings data from PakWheels.com - Pakistan's #1 automotive marketplace.

![Car Data](https://img.shields.io/badge/Car%20Data-Collection-blue)
![Python](https://img.shields.io/badge/Python-100%25-brightgreen)

## 📋 What This Project Does

This tool automatically visits PakWheels.com and collects detailed information about used cars listed across different regions of Pakistan. It saves all data neatly into a CSV file for easy analysis.

## 🌟 Features

- **Regional Coverage**: Scrapes car listings from Punjab, Sindh, KPK, Balochistan, and Azad Kashmir
- **Detailed Information**: Collects 12 important data points for each car listing
- **Efficient**: Navigates through multiple pages of listings
- **Easy Output**: Saves everything in a clean CSV format

## 🚙 Data Collected

For each car listing, the scraper collects:
- Model Name
- Manufacturer
- Registration Location
- Model Year
- Fuel Type
- Transmission Type
- Color
- Body Type
- Engine Displacement
- Mileage
- Price
- Original Listing URL

## 🛠️ Setup Instructions

### Requirements
- Python 3.6 or newer
- Internet connection

### Installation

1. Clone this repository:
```
git clone https://github.com/Hammadarshad026/pakwheel_data_scraper.git
cd pakwheel_data_scraper
```

2. Install required packages:
```
pip install -r requirements.txt
```

3. Run the scraper:
```
python scraper.py
```

## 📊 Output

The data is saved to a file named `vichle_data.csv` in the same directory. You can open this file with Microsoft Excel, Google Sheets, or any spreadsheet software.

## ⚠️ Important Notes

- Please use this tool responsibly
- Excessive scraping might be against PakWheels' terms of service
- Consider adding delays between requests to reduce server load

## 📈 Use Cases

- Market research on used car prices
- Analyzing trends in the Pakistani automotive market
- Finding the best deals across different regions
- Comparing car specifications and prices

## 🤝 Contributing

Feel free to fork this repository and make improvements! Pull requests are welcome.

## 📝 License

This project is available for open use. Please provide attribution if you use this code.

---

Made with ❤️ by [Hammad Arshad](https://github.com/Hammadarshad026)
