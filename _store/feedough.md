---
aid: feedough
url: https://raw.githubusercontent.com/api-evangelist/feedough/refs/heads/main/apis.yml
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
name: Feedough
tags:
- Business Models
- Entrepreneurship
- Media
- Startups
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Feedough is a media platform and entrepreneurship resource covering startup ideas, business models, and entrepreneurship. Founded in December 2013 by Aashish Pahwa to bridge the information gap in the startup industry, Feedough explains startup concepts in plain language without the fluff. The platform is ranked among the top twenty startup websites globally and is cited as a resource by institutions including Harvard Business School and the University of Washington.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

