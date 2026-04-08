---
aid: software-engineering-daily
url: https://raw.githubusercontent.com/api-evangelist/software-engineering-daily/refs/heads/main/apis.yml
apis:
- aid: software-engineering-daily:podcast-rss-feed
  name: Software Engineering Daily Podcast RSS Feed
  description: Software Engineering Daily provides RSS podcast feeds for its main episode stream as well as topic-specific feeds. These standard podcast RSS feeds are compatible with all major podcast clients including Apple Podcasts, Spotify, Overcast, and Podcast Addict, and can be consumed programmatically using any feed parsing library to access episode metadata, audio file URLs, descriptions, and publication dates.
  humanURL: https://softwareengineeringdaily.com/
  baseURL: https://softwareengineeringdaily.com
  tags:
  - Feed
  - Podcasts
  - RSS
  - Syndication
  properties:
  - type: Documentation
    url: https://softwareengineeringdaily.com/2017/07/05/new-topic-feeds/
  - type: RSSFeed
    url: https://softwareengineeringdaily.com/feed/podcast/
- aid: software-engineering-daily:backend-api
  name: Software Engineering Daily Backend API
  description: The Software Engineering Daily Backend API is an open-source REST API that powers the platform's web, iOS, and Android front ends. Built with Node.js, MongoDB, and Redis, it provides endpoints for accessing podcast episodes, user accounts, bookmarks, playback tracking, upvotes, comments, and search. API documentation is available in Swagger format at the /api/docs path. The codebase is MIT-licensed and available on GitHub.
  humanURL: https://github.com/SoftwareEngineeringDaily/software-engineering-daily-api
  baseURL: https://softwareengineeringdaily.com
  tags:
  - Episodes
  - Open Source
  - Podcasts
  - REST
  properties:
  - type: Documentation
    url: https://softwareengineeringdaily.github.io/Backend/gettingstarted/
  - type: GitHubRepository
    url: https://github.com/SoftwareEngineeringDaily/software-engineering-daily-api
name: Software Engineering Daily
tags:
- Media
- Podcasts
- Software Engineering
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Software Engineering Daily is a podcast and media platform dedicated to covering software engineering topics through daily technical interviews and discussions. Founded by Jeff Meyerson in 2015, the platform publishes episodes five days a week featuring conversations with software engineers, startup founders, and technology leaders on topics ranging from distributed systems, cloud computing, databases, and programming languages to AI, machine learning, and the business of software.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

