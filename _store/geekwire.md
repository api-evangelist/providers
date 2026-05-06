---
aid: geekwire
name: GeekWire
description: GeekWire is a leading technology news site covering startups, innovation, and the Pacific Northwest tech scene. Founded in Seattle, GeekWire delivers breaking news, analysis, and commentary on technology, business, and entrepreneurship, with a particular focus on companies like Amazon, Microsoft, and the broader Seattle and Pacific Northwest startup ecosystem. GeekWire also operates GeekWork, a technology job board, and produces popular podcasts and weekly radio programming.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Media
  - Startups
  - Technology News
url: https://raw.githubusercontent.com/api-evangelist/geekwire/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
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
common:
  - url: https://www.geekwire.com/
    name: GeekWire
    type: Website
    description: 'null'
  - url: https://www.geekwire.com/about-geekwire/
    name: About GeekWire
    type: About
    description: 'null'
  - url: https://www.geekwire.com/contact-us/
    name: Contact GeekWire
    type: Contact
    description: 'null'
  - url: https://www.geekwire.com/rss-feeds/
    name: GeekWire RSS Feeds
    type: RSSFeeds
    description: 'null'
  - url: https://www.geekwire.com/feed/
    name: GeekWire Main RSS Feed
    type: RSSFeed
    description: 'null'
  - url: https://www.geekwire.com/newsletter/
    name: GeekWire Newsletter
    type: Newsletter
    description: 'null'
  - url: https://www.geekwire.com/jobs/
    name: GeekWork Job Board
    type: JobBoard
    description: 'null'
  - url: https://www.geekwire.com/advertise/
    name: Advertise on GeekWire
    type: Advertising
    description: 'null'
  - url: https://www.geekwire.com/privacy/
    name: Privacy Policy for GeekWire
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.geekwire.com/termsofuse/
    name: Terms of Use for GeekWire
    type: TermsOfService
    description: 'null'
  - url: https://podcasts.apple.com/us/podcast/geekwire/id427374434
    name: GeekWire Podcast on Apple Podcasts
    type: Podcast
    description: 'null'
  - url: https://open.spotify.com/show/2PPEGel5l0v3XxlD8fVxAh
    name: GeekWire Podcast on Spotify
    type: Podcast
    description: 'null'
  - url: https://www.linkedin.com/company/geekwire
    name: GeekWire on LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://x.com/geekwire
    name: GeekWire on X
    type: X
    description: 'null'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
