# API Examples - Free Public APIs

This repository contains simple examples of using free public APIs with Python. No authentication or API keys required!

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/singh-odyssey/api-into.git
cd api-into
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Examples

#### Simple Example (Beginner-Friendly)
```bash
python3 simple_api_example.py
```
This fetches a random dog image URL from the Dog CEO API.

#### All Examples
```bash
python3 api_example.py
```
This runs multiple examples showcasing different free APIs.

## 📚 API Examples Included

### 1. **Dog CEO API** 🐕
- **URL:** https://dog.ceo/api/breeds/image/random
- **What it does:** Returns a random dog image URL
- **No authentication needed**

### 2. **Nager.Date Public Holidays API** 📅
- **URL:** https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}
- **What it does:** Get public holidays for any country
- **Example:** USA holidays for 2025

### 3. **Random User Generator API** 👤
- **URL:** https://randomuser.me/api/
- **What it does:** Generates random user data (name, email, location, etc.)
- **Great for testing**

### 4. **Bored API** 🎯
- **URL:** https://www.boredapi.com/api/activity
- **What it does:** Suggests random activities when you're bored
- **Returns activity type and participant count**

### 5. **Cat Facts API** 🐱
- **URL:** https://catfact.ninja/fact
- **What it does:** Returns random cat facts
- **Fun for cat lovers!**

## 📖 Code Structure

```
api-into/
├── simple_api_example.py   # Simplest example (10 lines)
├── api_example.py           # Multiple API examples
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔧 How It Works

All examples follow the same pattern:

1. **Make a request** using `requests.get(url)`
2. **Parse JSON response** with `response.json()`
3. **Extract and display data** from the response

### Basic Example:
```python
import requests

# Make GET request
response = requests.get("https://dog.ceo/api/breeds/image/random")

# Parse JSON
data = response.json()

# Use the data
print(data['message'])
```

## 🌟 Features

- ✅ No API keys required
- ✅ Simple and easy to understand
- ✅ Error handling included
- ✅ Multiple real-world examples
- ✅ Well-commented code
- ✅ Ready to run

## 📦 Dependencies

- **requests** (2.31.0) - For making HTTP requests

## 🤝 Contributing

Feel free to add more free public API examples! Some suggestions:
- OpenWeatherMap (with free tier)
- JSONPlaceholder (fake REST API)
- REST Countries API
- Open Trivia Database
- Pokemon API

## 📝 License

See LICENSE file for details.

## 🔗 Useful Resources

- [Public APIs GitHub Repository](https://github.com/public-apis/public-apis) - A huge list of free APIs
- [Requests Documentation](https://requests.readthedocs.io/) - Learn more about the requests library

## 💡 Tips

- Always check the API's rate limits
- Handle errors gracefully
- Some APIs may be temporarily unavailable
- Read the API documentation before using

---

**Happy Coding! 🎉**
