#!/usr/bin/env python3
"""
Demo script to show newsletter generator functionality without API key.
Uses sample data to demonstrate the output formats.
"""
from datetime import datetime
from newsletter_formatter import NewsletterFormatter


# Sample articles for demonstration
SAMPLE_ARTICLES = [
    {
        'title': 'Revolutionary AI Model Breaks Language Barriers',
        'description': 'A new artificial intelligence model has achieved unprecedented accuracy in real-time translation across 100+ languages, making global communication more accessible than ever.',
        'url': 'https://example.com/ai-translation',
        'source': 'TechCrunch',
        'published_at': '2025-10-16T10:30:00Z',
        'author': 'Sarah Johnson',
        'image_url': 'https://example.com/images/ai.jpg'
    },
    {
        'title': 'Quantum Computing Breakthrough Announced by Tech Giant',
        'description': 'Major technology company unveils new quantum processor with 1000+ qubits, potentially revolutionizing drug discovery and cryptography applications.',
        'url': 'https://example.com/quantum-computing',
        'source': 'Wired',
        'published_at': '2025-10-16T09:15:00Z',
        'author': 'Michael Chen',
        'image_url': 'https://example.com/images/quantum.jpg'
    },
    {
        'title': 'Electric Vehicle Startup Raises $500M in Series C',
        'description': 'Promising EV manufacturer secures massive funding round to expand production of affordable electric vehicles with 500-mile range.',
        'url': 'https://example.com/ev-funding',
        'source': 'Bloomberg',
        'published_at': '2025-10-16T08:45:00Z',
        'author': 'Jennifer Martinez',
        'image_url': 'https://example.com/images/ev.jpg'
    },
    {
        'title': 'New Cybersecurity Framework Protects IoT Devices',
        'description': 'Industry coalition releases open-source security framework designed to protect billions of Internet of Things devices from emerging threats.',
        'url': 'https://example.com/iot-security',
        'source': 'The Verge',
        'published_at': '2025-10-16T07:30:00Z',
        'author': 'David Park',
        'image_url': 'https://example.com/images/security.jpg'
    },
    {
        'title': 'Social Media Platform Launches Creator Fund Initiative',
        'description': 'Popular social network announces $100M fund to support content creators, offering grants and resources for innovative digital content.',
        'url': 'https://example.com/creator-fund',
        'source': 'TechCrunch',
        'published_at': '2025-10-16T06:00:00Z',
        'author': 'Emma Wilson',
        'image_url': 'https://example.com/images/social.jpg'
    }
]


def main():
    """Generate demo newsletter with sample data."""
    print("=" * 70)
    print("Tech Newsletter Generator - DEMO MODE".center(70))
    print("=" * 70)
    print()
    print("This demo shows what the newsletter output looks like.")
    print("To use real news data, set up your API key following the README.")
    print()
    
    # Format newsletter
    formatter = NewsletterFormatter(title="Daily Tech Newsletter (Demo)")
    
    # Generate text format
    print("📝 Generating text format...")
    text_content = formatter.format_text(SAMPLE_ARTICLES)
    
    # Print to console
    print()
    print(text_content)
    print()
    
    # Save demo files
    print("💾 Saving demo files...")
    
    with open('demo_newsletter.txt', 'w', encoding='utf-8') as f:
        f.write(text_content)
    print("   ✅ Saved: demo_newsletter.txt")
    
    html_content = formatter.format_html(SAMPLE_ARTICLES)
    with open('demo_newsletter.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("   ✅ Saved: demo_newsletter.html")
    
    md_content = formatter.format_markdown(SAMPLE_ARTICLES)
    with open('demo_newsletter.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print("   ✅ Saved: demo_newsletter.md")
    
    print()
    print("=" * 70)
    print("✨ Demo complete!".center(70))
    print("=" * 70)
    print()
    print("Open demo_newsletter.html in your browser to see the HTML version!")
    print()


if __name__ == "__main__":
    main()
