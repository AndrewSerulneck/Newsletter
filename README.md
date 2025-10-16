# Tech Newsletter Generator

A Python application that automatically scans the news and generates a daily tech newsletter in a consistent format. The app fetches the latest technology headlines and formats them into professional newsletters in multiple formats (text, HTML, and Markdown).

## Features

- 🚀 **Fast & Automated**: Quickly fetches and formats tech news
- 📰 **Multiple Sources**: Aggregates news from various tech sources via News API
- 🎨 **Multiple Formats**: Generates newsletters in text, HTML, and Markdown
- ⚙️ **Configurable**: Easily customize newsletter settings
- 📅 **Consistent Format**: Same professional format every day
- 💾 **Automatic Saving**: Saves newsletters with timestamped filenames

## Prerequisites

- Python 3.7 or higher
- News API key (free at [newsapi.org](https://newsapi.org/))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/AndrewSerulneck/Newsletter.git
cd Newsletter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API key:
```bash
cp .env.example .env
```

4. Edit `.env` and add your News API key:
```
NEWS_API_KEY=your_actual_api_key_here
```

## Usage

Run the newsletter generator:

```bash
python newsletter_generator.py
```

The script will:
1. Fetch the latest tech headlines from News API
2. Format them into newsletters
3. Save them in the `newsletters/` directory in three formats:
   - `newsletter_YYYYMMDD.txt` - Plain text format
   - `newsletter_YYYYMMDD.html` - HTML format (can be viewed in browser)
   - `newsletter_YYYYMMDD.md` - Markdown format

## Configuration

You can customize the newsletter by editing the `.env` file:

```env
# News API Key - Get yours at https://newsapi.org/
NEWS_API_KEY=your_api_key_here

# Newsletter settings
NEWSLETTER_TITLE=Daily Tech Newsletter
NEWS_CATEGORY=technology
NEWS_COUNTRY=us
MAX_ARTICLES=10
```

### Configuration Options

- `NEWS_API_KEY`: Your News API key (required)
- `NEWSLETTER_TITLE`: Title of your newsletter (default: "Daily Tech Newsletter")
- `NEWS_CATEGORY`: News category to fetch (default: "technology")
  - Options: technology, business, entertainment, general, health, science, sports
- `NEWS_COUNTRY`: Country code for news sources (default: "us")
  - Options: us, gb, ca, au, etc.
- `MAX_ARTICLES`: Maximum number of articles to include (default: 10)

## Example Output

### Text Format
```
======================================================================
                        Daily Tech Newsletter                         
                          October 16, 2025                           
======================================================================

1. Latest AI Breakthrough Announced
   Source: TechCrunch

   Researchers have unveiled a new AI model that...

   Read more: https://example.com/article

----------------------------------------------------------------------
```

### HTML Format
Opens in browser with professional styling, featuring:
- Clean, responsive design
- Article cards with hover effects
- Easy-to-read typography
- Click-through links to full articles

### Markdown Format
Perfect for GitHub, documentation sites, or markdown-based platforms.

## Automation

To generate newsletters automatically every day, you can set up a cron job (Linux/Mac) or Task Scheduler (Windows).

### Linux/Mac Cron Example:

```bash
# Run daily at 8 AM
0 8 * * * cd /path/to/Newsletter && python newsletter_generator.py
```

### GitHub Actions Example:

Create `.github/workflows/daily-newsletter.yml`:

```yaml
name: Daily Newsletter
on:
  schedule:
    - cron: '0 8 * * *'  # Run at 8 AM UTC daily
  workflow_dispatch:      # Allow manual trigger

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: python newsletter_generator.py
        env:
          NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
      - uses: actions/upload-artifact@v2
        with:
          name: newsletter
          path: newsletters/
```

## Project Structure

```
Newsletter/
├── newsletter_generator.py   # Main script
├── config.py                 # Configuration management
├── news_fetcher.py          # News API integration
├── newsletter_formatter.py   # Newsletter formatting
├── requirements.txt          # Python dependencies
├── .env.example             # Example configuration
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Troubleshooting

### "NEWS_API_KEY is required" error
Make sure you've created a `.env` file and added your API key.

### "Failed to fetch news" error
- Check your internet connection
- Verify your API key is valid
- Check if you've exceeded your API rate limit (free tier: 100 requests/day)

### No articles found
- Try changing the `NEWS_CATEGORY` or `NEWS_COUNTRY` in `.env`
- Some categories may have fewer articles for certain countries

## API Rate Limits

The free News API tier allows:
- 100 requests per day
- Articles from the last 24 hours only

For higher limits and more features, consider upgrading at [newsapi.org/pricing](https://newsapi.org/pricing).

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Acknowledgments

- News data provided by [News API](https://newsapi.org/)
- Built with Python and ❤️