---
aid: the-new-stack
url: https://raw.githubusercontent.com/api-evangelist/the-new-stack/refs/heads/main/apis.yml
apis:
- aid: the-new-stack:rss
  name: The New Stack RSS Feed
  description: RSS feed providing the latest articles and news from The New Stack covering cloud native, DevOps, and open source technologies.
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
- aid: the-new-stack:podcast-rss
  name: The New Stack Podcast Feed
  description: RSS feed for The New Stack podcast, featuring discussions with developers, engineers, and operations professionals building at-scale architectures.
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
name: The New Stack
tags:
- Cloud Native
- DevOps
- Media
- Technology News
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The New Stack is a tech media platform covering cloud native, DevOps, and open source technologies, providing news, analysis, podcasts, webinars, and ebooks for developers, software engineers, and operations professionals.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

