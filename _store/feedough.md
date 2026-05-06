---
aid: feedough
name: Feedough
description: Feedough is a media platform and entrepreneurship resource covering startup ideas, business models, and entrepreneurship. Founded in December 2013 by Aashish Pahwa to bridge the information gap in the startup industry, Feedough explains startup concepts in plain language without the fluff. The platform is ranked among the top twenty startup websites globally and is cited as a resource by institutions including Harvard Business School and the University of Washington.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Business Models
  - Entrepreneurship
  - Media
  - Startups
url: https://raw.githubusercontent.com/api-evangelist/feedough/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: feedough:rss-feed
    name: Feedough RSS Feed
    description: Feedough provides an RSS feed for its main content stream, allowing developers and readers to consume articles on startup ideas, business models, and entrepreneurship programmatically using standard feed parsing libraries and tools.
    humanURL: https://www.feedough.com/feed/
    baseURL: https://www.feedough.com
    tags:
      - Feed
      - News
      - RSS
      - Syndication
    properties:
      - type: RSSFeed
        url: https://www.feedough.com/feed/
  - aid: feedough:wordpress-rest-api
    name: Feedough WordPress REST API
    description: Feedough is built on WordPress and exposes the standard WordPress REST API, providing JSON endpoints for accessing posts, categories, tags, authors, and other content types. The API is available at the /wp-json/wp/v2/ base path and supports filtering, pagination, and searching across all Feedough content.
    humanURL: https://developer.wordpress.org/rest-api/
    baseURL: https://www.feedough.com/wp-json/wp/v2
    tags:
      - Content
      - JSON
      - REST
      - WordPress
    properties:
      - type: Documentation
        url: https://developer.wordpress.org/rest-api/
      - type: OpenAPI
        url: https://www.feedough.com/wp-json/
common:
  - url: https://www.feedough.com/
    name: Feedough
    type: Website
    description: 'null'
  - url: https://www.feedough.com/about-us/
    name: About Feedough
    type: About
    description: 'null'
  - url: https://www.feedough.com/subscribe/
    name: Subscribe to Feedough
    type: Newsletter
    description: 'null'
  - url: https://www.feedough.com/partner-with-feedough/
    name: Partner with Feedough
    type: Advertising
    description: 'null'
  - url: https://www.feedough.com/feed/
    name: Feedough RSS Feed
    type: RSSFeed
    description: 'null'
  - url: https://www.feedough.com/startup-resources/
    name: Feedough Startup Resources
    type: Portal
    description: 'null'
  - url: https://www.feedough.com/daily/
    name: Feedough Startup Daily
    type: Blog
    description: 'null'
  - url: https://www.feedough.com/legal/privacy-policy/
    name: Privacy Policy for Feedough
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.feedough.com/legal/terms/
    name: Terms of Service for Feedough
    type: TermsOfService
    description: 'null'
  - url: https://www.feedough.com/legal/cookie-policy/
    name: Cookie Policy for Feedough
    type: CookiePolicy
    description: 'null'
  - url: https://www.feedough.com/disclaimer/
    name: Disclaimer for Feedough
    type: Disclaimer
    description: 'null'
  - url: https://www.linkedin.com/company/feedough
    name: Feedough on LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://x.com/FeedoughCom
    name: Feedough on X
    type: X
    description: 'null'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
