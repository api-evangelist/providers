---
aid: the-new-stack
url: https://raw.githubusercontent.com/api-evangelist/the-new-stack/refs/heads/main/apis.yml
apis:
  - aid: the-new-stack:rss
    name: The New Stack RSS Feed
    description: RSS feed providing the latest articles and news from The New Stack covering cloud native, DevOps, AI, and open source technologies. Feed follows RSS 2.0 with Dublin Core and WordPress content extensions.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://thenewstack.io/rss-feeds/
    baseURL: https://thenewstack.io
    tags:
      - Cloud Native
      - DevOps
      - News Feed
      - RSS
    properties:
      - url: https://thenewstack.io/feed/
        type: RSS
      - url: https://thenewstack.io/rss-feeds/
        type: Documentation
    features:
      - RSS 2.0 Feed
      - Category Filtering
      - Full Article Content
      - Author Attribution
      - Publication Timestamps
    useCases:
      - News Aggregation
      - Content Monitoring
      - Tech News Alert Feeds
      - Developer Tool Discovery
  - aid: the-new-stack:podcast-rss
    name: The New Stack Podcast Feed
    description: RSS feed for The New Stack podcast, featuring discussions with developers, engineers, and operations professionals building at-scale architectures. Hosted on Simplecast.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://thenewstack.io/podcasts/
    baseURL: https://thenewstack.simplecast.com
    tags:
      - Cloud Native
      - DevOps
      - Podcast
      - RSS
    properties:
      - url: https://thenewstack.simplecast.com/episodes
        type: RSS
      - url: https://thenewstack.io/podcasts/
        type: HumanURL
    features:
      - Podcast RSS Feed
      - Episode Audio Downloads
      - Show Notes
      - Guest Information
    useCases:
      - Podcast Aggregation
      - Developer Podcast Discovery
      - Tech Interview Content
name: The New Stack
tags:
  - Cloud Native
  - DevOps
  - Media
  - Technology News
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://thenewstack.io/
    name: The New Stack Website
    type: Website
  - url: https://thenewstack.io/about-and-contact-info/
    name: About
    type: About
  - url: https://thenewstack.io/rss-feeds/
    name: RSS Feeds
    type: RSS
  - url: https://thenewstack.io/feed/
    name: Main RSS Feed
    type: RSS
  - url: https://thenewstack.io/newsletter/
    name: Newsletter
    type: Newsletter
  - url: https://thenewstack.io/podcasts/
    name: Podcasts
    type: Podcast
  - url: https://thenewstack.simplecast.com/
    name: Podcast on Simplecast
    type: Podcast
  - url: https://open.spotify.com/show/2nj1mpDb9jxHxi9vjZvDdk
    name: Podcast on Spotify
    type: Podcast
  - url: https://thenewstack.io/contributions/
    name: Contribute
    type: Contribute
  - url: https://thenewstack.io/sponsorship/
    name: Sponsorship
    type: Sponsorship
  - url: https://thenewstack.io/events/
    name: Events
    type: Events
  - url: https://thenewstack.io/webinars/
    name: Webinars
    type: Webinars
  - url: https://thenewstack.io/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://x.com/thenewstack
    name: X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/the-new-stack
    name: LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/thenewstack/
    name: Facebook
    type: Facebook
  - url: https://www.youtube.com/thenewstack
    name: YouTube
    type: YouTube
description: The New Stack is a tech media platform covering cloud native, DevOps, AI, and open source technologies, providing news, analysis, podcasts, webinars, and ebooks for developers, software engineers, and operations professionals. Public data access is available via RSS feeds for articles and podcasts.
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
