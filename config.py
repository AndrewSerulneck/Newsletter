"""
Configuration module for the newsletter generator.
Loads environment variables and provides configuration settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for newsletter settings."""
    
    # News API Configuration
    NEWS_API_KEY = os.getenv('NEWS_API_KEY', '')
    NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
    
    # Newsletter Settings
    NEWSLETTER_TITLE = os.getenv('NEWSLETTER_TITLE', 'Daily Tech Newsletter')
    NEWS_CATEGORY = os.getenv('NEWS_CATEGORY', 'technology')
    NEWS_COUNTRY = os.getenv('NEWS_COUNTRY', 'us')
    MAX_ARTICLES = int(os.getenv('MAX_ARTICLES', '10'))
    
    @classmethod
    def validate(cls):
        """Validate required configuration."""
        # Re-load in case environment changed
        api_key = os.getenv('NEWS_API_KEY', '')
        if not api_key:
            raise ValueError(
                "NEWS_API_KEY is required. "
                "Please set it in .env file or environment variable."
            )
        return True
