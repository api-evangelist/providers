---
aid: bloomberg-media-platforms
name: Bloomberg Media Platforms
description: Bloomberg Media Platforms encompass Bloomberg's digital news and content distribution channels including Bloomberg.com, Bloomberg Businessweek, Bloomberg Markets, Bloomberg Technology, Bloomberg Opinion, and Bloomberg Quicktake. Bloomberg provides news APIs for distributing financial news, market data updates, and editorial content to institutional clients and media partners.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-media-platforms/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Media
  - News
  - Financial News
  - Digital Media
  - Bloomberg.com
  - Bloomberg Businessweek
  - Bloomberg
apis:
  - aid: bloomberg-media-platforms:bloomberg-news-api
    name: Bloomberg News API
    description: Access Bloomberg's real-time financial news, market reports, and editorial content through Bloomberg's news data feeds. Available to Bloomberg Terminal subscribers and enterprise data license clients.
    humanURL: https://www.bloomberg.com/professional/solution/news/
    baseURL: blpapi://localhost:8194
    tags:
      - News
      - Financial News
      - Real-Time News
      - Content Feed
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/news/
  - aid: bloomberg-media-platforms:bloomberg-media-api
    name: Bloomberg Media API
    description: Content distribution API for Bloomberg's editorial content including articles, video clips, and multimedia from Bloomberg.com, Bloomberg Businessweek, and other Bloomberg media properties.
    humanURL: https://www.bloomberg.com/professional/
    baseURL: https://api.bloomberg.com/media
    tags:
      - Media Content
      - Articles
      - Video
      - Editorial
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/professional/solution/news/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Real-Time News
        description: Real-time financial news and market updates from Bloomberg's newsroom.
      - name: News Search
        description: Search and filter Bloomberg news archives by company, topic, and date.
      - name: Exclusive Reporting
        description: Original reporting and investigative journalism from Bloomberg journalists.
      - name: Bloomberg Opinion
        description: Columnist opinions and editorial analysis on financial and economic topics.
      - name: Bloomberg Quicktake
        description: Digital video and multimedia content for financial news consumption.
      - name: Bloomberg Markets Magazine
        description: In-depth analysis of global financial markets and investment trends.
  - type: UseCases
    data:
      - name: News Monitoring
        description: Monitor breaking financial news and market-moving events in real time.
      - name: Sentiment Analysis
        description: Apply NLP to Bloomberg news for financial sentiment analysis.
      - name: Research Integration
        description: Integrate Bloomberg news into research and analytics platforms.
      - name: Content Licensing
        description: License Bloomberg content for distribution on third-party platforms.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
