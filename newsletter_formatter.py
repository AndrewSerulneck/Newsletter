"""
Newsletter formatter module.
Formats articles into a consistent newsletter format.
"""
from datetime import datetime
from typing import List, Dict
from config import Config


class NewsletterFormatter:
    """Formats news articles into a newsletter."""
    
    def __init__(self, title: str = None):
        """
        Initialize the formatter.
        
        Args:
            title: Newsletter title
        """
        self.title = title or Config.NEWSLETTER_TITLE
    
    def format_text(self, articles: List[Dict]) -> str:
        """
        Format articles as plain text newsletter.
        
        Args:
            articles: List of parsed article dictionaries
            
        Returns:
            Formatted newsletter as plain text
        """
        lines = []
        lines.append("=" * 70)
        lines.append(f"{self.title}".center(70))
        lines.append(f"{datetime.now().strftime('%B %d, %Y')}".center(70))
        lines.append("=" * 70)
        lines.append("")
        
        for i, article in enumerate(articles, 1):
            lines.append(f"{i}. {article['title']}")
            lines.append(f"   Source: {article['source']}")
            lines.append("")
            lines.append(f"   {article['description']}")
            lines.append("")
            lines.append(f"   Read more: {article['url']}")
            lines.append("")
            lines.append("-" * 70)
            lines.append("")
        
        lines.append("=" * 70)
        lines.append("End of Newsletter".center(70))
        lines.append("=" * 70)
        
        return "\n".join(lines)
    
    def format_html(self, articles: List[Dict]) -> str:
        """
        Format articles as HTML newsletter.
        
        Args:
            articles: List of parsed article dictionaries
            
        Returns:
            Formatted newsletter as HTML
        """
        html = []
        html.append("<!DOCTYPE html>")
        html.append("<html>")
        html.append("<head>")
        html.append("    <meta charset='UTF-8'>")
        html.append("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
        html.append(f"    <title>{self.title}</title>")
        html.append("    <style>")
        html.append("        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f5f5f5; }")
        html.append("        .header { background-color: #2c3e50; color: white; padding: 30px; text-align: center; border-radius: 5px; }")
        html.append("        .header h1 { margin: 0; }")
        html.append("        .header .date { margin-top: 10px; font-size: 14px; opacity: 0.9; }")
        html.append("        .article { background-color: white; margin: 20px 0; padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }")
        html.append("        .article h2 { color: #2c3e50; margin-top: 0; }")
        html.append("        .article .meta { color: #7f8c8d; font-size: 14px; margin: 10px 0; }")
        html.append("        .article .description { line-height: 1.6; color: #34495e; margin: 15px 0; }")
        html.append("        .article .read-more { display: inline-block; background-color: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 3px; margin-top: 10px; }")
        html.append("        .article .read-more:hover { background-color: #2980b9; }")
        html.append("        .footer { text-align: center; margin-top: 30px; padding: 20px; color: #7f8c8d; }")
        html.append("    </style>")
        html.append("</head>")
        html.append("<body>")
        html.append("    <div class='header'>")
        html.append(f"        <h1>{self.title}</h1>")
        html.append(f"        <div class='date'>{datetime.now().strftime('%B %d, %Y')}</div>")
        html.append("    </div>")
        
        for i, article in enumerate(articles, 1):
            html.append("    <div class='article'>")
            html.append(f"        <h2>{i}. {article['title']}</h2>")
            html.append(f"        <div class='meta'>Source: {article['source']}</div>")
            html.append(f"        <div class='description'>{article['description']}</div>")
            html.append(f"        <a href='{article['url']}' class='read-more'>Read Full Article</a>")
            html.append("    </div>")
        
        html.append("    <div class='footer'>")
        html.append("        <p>End of Newsletter</p>")
        html.append("    </div>")
        html.append("</body>")
        html.append("</html>")
        
        return "\n".join(html)
    
    def format_markdown(self, articles: List[Dict]) -> str:
        """
        Format articles as Markdown newsletter.
        
        Args:
            articles: List of parsed article dictionaries
            
        Returns:
            Formatted newsletter as Markdown
        """
        lines = []
        lines.append(f"# {self.title}")
        lines.append(f"*{datetime.now().strftime('%B %d, %Y')}*")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        for i, article in enumerate(articles, 1):
            lines.append(f"## {i}. {article['title']}")
            lines.append(f"**Source:** {article['source']}")
            lines.append("")
            lines.append(article['description'])
            lines.append("")
            lines.append(f"[Read Full Article]({article['url']})")
            lines.append("")
            lines.append("---")
            lines.append("")
        
        lines.append("*End of Newsletter*")
        
        return "\n".join(lines)
