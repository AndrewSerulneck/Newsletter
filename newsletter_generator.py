#!/usr/bin/env python3
"""
Newsletter Generator - Main Script
Generates a daily tech newsletter by fetching and formatting news articles.
"""
import os
import sys
from datetime import datetime
from config import Config
from news_fetcher import NewsFetcher
from newsletter_formatter import NewsletterFormatter


def create_output_directory():
    """Create output directory for newsletters if it doesn't exist."""
    output_dir = 'newsletters'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


def save_newsletter(content: str, format_type: str, output_dir: str):
    """
    Save newsletter to file.
    
    Args:
        content: Newsletter content
        format_type: Format type (text, html, markdown)
        output_dir: Output directory path
    """
    timestamp = datetime.now().strftime('%Y%m%d')
    filename = f"newsletter_{timestamp}.{format_type}"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main():
    """Main function to generate the newsletter."""
    print("=" * 70)
    print("Tech Newsletter Generator".center(70))
    print("=" * 70)
    print()
    
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print()
        print("Setup Instructions:")
        print("1. Copy .env.example to .env")
        print("2. Get a free API key from https://newsapi.org/")
        print("3. Add your API key to the .env file")
        sys.exit(1)
    
    # Create output directory
    output_dir = create_output_directory()
    print(f"📁 Output directory: {output_dir}")
    print()
    
    # Fetch news
    print("📰 Fetching top tech headlines...")
    try:
        fetcher = NewsFetcher()
        articles = fetcher.fetch_top_headlines()
        
        if not articles:
            print("⚠️  No articles found.")
            sys.exit(0)
        
        print(f"✅ Found {len(articles)} articles")
        print()
        
        # Parse articles
        parsed_articles = [fetcher.parse_article(article) for article in articles]
        
        # Format newsletter
        print("📝 Formatting newsletter...")
        formatter = NewsletterFormatter()
        
        # Generate in multiple formats
        formats = {
            'txt': formatter.format_text(parsed_articles),
            'html': formatter.format_html(parsed_articles),
            'md': formatter.format_markdown(parsed_articles)
        }
        
        # Save newsletters
        print()
        print("💾 Saving newsletters...")
        saved_files = []
        for format_type, content in formats.items():
            filepath = save_newsletter(content, format_type, output_dir)
            saved_files.append(filepath)
            print(f"   ✅ Saved: {filepath}")
        
        print()
        print("=" * 70)
        print("✨ Newsletter generation complete!".center(70))
        print("=" * 70)
        print()
        
        # Preview first few articles
        print("Preview of articles included:")
        print()
        for i, article in enumerate(parsed_articles[:3], 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']}")
            print()
        
        if len(parsed_articles) > 3:
            print(f"... and {len(parsed_articles) - 3} more articles")
            print()
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
