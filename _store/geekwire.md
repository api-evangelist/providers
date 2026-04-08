---
aid: geekwire
url: https://raw.githubusercontent.com/api-evangelist/geekwire/refs/heads/main/apis.yml
apis:
- aid: geekwire:rss-feed
  name: GeekWire RSS Feed
  description: GeekWire provides RSS feeds for its main news stream and individual topic categories including Microsoft, Space, Science, Real Estate, Games, Google, Mobile, GeekLife, Podcasts, and Apple. These Atom/RSS feeds allow developers and readers to consume GeekWire content programmatically using standard feed parsing libraries and tools.
  humanURL: https://www.geekwire.com/rss-feeds/
  baseURL: https://www.geekwire.com
  tags:
  - Feed
  - News
  - RSS
  - Syndication
  properties:
  - type: Documentation
    url: https://www.geekwire.com/rss-feeds/
  - type: RSSFeed
    url: https://www.geekwire.com/feed/
- aid: geekwire:wordpress-rest-api
  name: GeekWire WordPress REST API
  description: GeekWire is built on WordPress and exposes the standard WordPress REST API, providing JSON endpoints for accessing posts, categories, tags, authors, and other content types. The API is available at the /wp-json/wp/v2/ base path and supports filtering, pagination, and searching across all GeekWire content.
  humanURL: https://developer.wordpress.org/rest-api/
  baseURL: https://www.geekwire.com/wp-json/wp/v2
  tags:
  - Content
  - JSON
  - REST
  - WordPress
  properties:
  - type: Documentation
    url: https://developer.wordpress.org/rest-api/
  - type: OpenAPI
    url: https://www.geekwire.com/wp-json/
name: GeekWire
tags:
- Media
- Startups
- Technology News
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: GeekWire is a leading technology news site covering startups, innovation, and the Pacific Northwest tech scene. Founded in Seattle, GeekWire delivers breaking news, analysis, and commentary on technology, business, and entrepreneurship, with a particular focus on companies like Amazon, Microsoft, and the broader Seattle and Pacific Northwest startup ecosystem. GeekWire also operates GeekWork, a technology job board, and produces popular podcasts and weekly radio programming.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

