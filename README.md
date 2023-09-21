# Introduction
This project is provides a Web Interface and an API endpoint which gives you 
recommendations based on a country and the season.

# Instructions
## Deployment
- Copy .env.example to .env and fill in the API key
- Make sure docker and docker compose is installed and configured properly
- Run docker compose up --build
- Open http://localhost:3000

### API 
The API endpoint is available at http://localhost:3000/recommend
and it accepts 2 arguments in the form of a JSON object e.g.
```json
{
  "country": "United Kingdom",
  "season": "Summer"
}
```

It will return a JSON with the country and the season values from the request,
and an additional list with 3 suggested activities returned by OpenAI

---
