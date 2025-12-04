# 🌤️ Rain Reminder + Motivation SMS Bot

A simple Python automation script that sends you a motivational quote plus a rain warning (if applicable) via Twilio SMS.
The bot checks your weather for the next 12 hours using OpenWeather One Call API 3.0, and sends:
- ✅ A motivational quote
- ✅ A random emoji
- ☂️ A friendly reminder if it’s going to rain
- 📩 Delivered right to your phone via Twilio

## Features
- Pulls a random motivational quote from quotes_bank.json
- Pulls a random emoji from emoji_bank.json
- Uses OpenWeather API to determine if rain is expected in the next 12 hours
- Sends SMS through Twilio with:
- Quote of the day
- Emoji of the day
- Optional rain alert
- Customizable latitude/longitude, phone numbers, and API keys


## Tech Stack
- Python 3-
- Twilio REST API
- OpenWeather API (One Call 3.0)
- JSON for quote/emoji storage


## 🔧 Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```

2. Install dependencies
```bash
pip install requests twilio
```
3. Create my_params.py
```python
MY_LAT = 00.0000            # Your latitude
MY_LONG = 00.0000           # Your longitude

MY_TWILIO_NUM = "+1234567890"
RECIPIENT_NUM = "+1234567890"
```
4. Set your environment variables

You must export the following:
- OWM_API_KEY — OpenWeather One Call API key
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN

## How It Works
1.	Loads quotes + emojis from JSON files
2.	Randomly selects one of each
3.	Fetches hourly forecast for 12 hours from OpenWeather
4.	Checks if any weather ID < 700
5.	Adds a rain warning if needed
6.	Sends a composed SMS using Twilio

## Important Notes
- Do NOT store API keys directly in the script.
- Make sure to keep environment variables private.
- Twilio trial accounts can only text verified phone numbers.

## 🤝 Contributing

Feel free to open issues or submit pull requests for:
- Better quote sources
- Adding a scheduler (cron, GitHub Actions)
- Expanding the weather conditions

## 📜 License

This project is open-source and available under the MIT License.
