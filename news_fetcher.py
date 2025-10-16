"""
News fetcher module.
Handles fetching news from News API.
"""
import requests
from typing import List, Dict, Optional
from config import Config


class NewsFetcher:
    """Fetches news articles from News API."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize the news fetcher.
        
        Args:
            api_key: News API key. If not provided, uses Config.NEWS_API_KEY
        """
        self.api_key = api_key or Config.NEWS_API_KEY
        self.api_url = Config.NEWS_API_URL
        
    def fetch_top_headlines(
        self,
        category: str = None,
        country: str = None,
        max_articles: int = None
    ) -> List[Dict]:
        """
        Fetch top headlines from News API.
        
        Args:
            category: News category (e.g., 'technology', 'business')
            country: Country code (e.g., 'us', 'gb')
            max_articles: Maximum number of articles to fetch
            
        Returns:
            List of article dictionaries
        """
        category = category or Config.NEWS_CATEGORY
        country = country or Config.NEWS_COUNTRY
        max_articles = max_articles or Config.MAX_ARTICLES
        
        params = {
            'apiKey': self.api_key,
            'category': category,
            'country': country,
            'pageSize': max_articles
        }
        
        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') == 'ok':
                return data.get('articles', [])
            else:
                error_msg = data.get('message', 'Unknown error')
                raise Exception(f"API error: {error_msg}")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch news: {str(e)}")
    
    def parse_article(self, article: Dict) -> Dict:
        """
        Parse and extract relevant information from an article.
        
        Args:
            article: Raw article dictionary from API
            
        Returns:
            Parsed article dictionary
        """
        return {
            'title': article.get('title', 'No Title'),
            'description': article.get('description', 'No description available.'),
            'url': article.get('url', ''),
            'source': article.get('source', {}).get('name', 'Unknown Source'),
            'published_at': article.get('publishedAt', ''),
            'author': article.get('author', 'Unknown Author'),
            'image_url': article.get('urlToImage', '')
        }
