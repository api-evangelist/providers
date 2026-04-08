---
aid: techcrunch
url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/apis.yml
apis:
- aid: techcrunch:wordpress-rest-api
  name: TechCrunch WordPress REST API
  description: TechCrunch is built on WordPress and exposes the standard WordPress REST API, providing JSON endpoints for accessing posts, categories, tags, authors, pages, and other content types. The API is available at the /wp-json/wp/v2/ base path and supports filtering, pagination, searching, and sorting across all TechCrunch content.
  humanURL: https://developer.wordpress.org/rest-api/
  baseURL: https://techcrunch.com/wp-json/wp/v2
  tags:
  - Content
  - JSON
  - REST
  - WordPress
  properties:
  - type: Documentation
    url: https://developer.wordpress.org/rest-api/
  - type: OpenAPI
    url: https://techcrunch.com/wp-json/
- aid: techcrunch:rss-feed
  name: TechCrunch RSS Feed
  description: TechCrunch provides RSS feeds covering its full range of technology news, startup coverage, and venture capital reporting. The main feed delivers all published articles, and category-specific feeds are available for topics including startups, venture capital, artificial intelligence, security, apps, gadgets, and more. These standard RSS/Atom feeds allow readers and developers to consume TechCrunch content programmatically using any standard feed reader or parsing library.
  humanURL: https://techcrunch.com/feed/
  baseURL: https://techcrunch.com
  tags:
  - Feed
  - News
  - RSS
  - Syndication
  properties:
  - type: Documentation
    url: https://techcrunch.com/feed/
  - type: RSSFeed
    url: https://techcrunch.com/feed/
name: TechCrunch
tags:
- Media
- Startups
- Technology News
- Venture Capital
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: TechCrunch (https://techcrunch.com/) is a leading technology media property dedicated to covering startups, venture capital, and innovation. Founded in 2005 and acquired by AOL in 2010 and later by Yahoo, TechCrunch delivers breaking news, in-depth analysis, and original reporting on the technology industry, emerging companies, funding rounds, and the people shaping the future of tech. The publication hosts flagship events including TechCrunch Disrupt and the Startup Battlefield competition.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

