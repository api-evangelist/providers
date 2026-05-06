---
aid: software-engineering-daily
name: Software Engineering Daily
description: Software Engineering Daily is a podcast and media platform dedicated to covering software engineering topics through daily technical interviews and discussions. Founded by Jeff Meyerson in 2015, the platform publishes episodes five days a week featuring conversations with software engineers, startup founders, and technology leaders on topics ranging from distributed systems, cloud computing, databases, and programming languages to AI, machine learning, and the business of software. The platform also offers a membership program for premium content and provides open-source backend and mobile apps for community development.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Media
  - Podcasts
  - Software Engineering
  - Technical Content
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/software-engineering-daily/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-02'
specificationVersion: '0.19'
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
  - aid: software-engineering-daily:mobile-app
    name: Software Engineering Daily Mobile App
    description: The Software Engineering Daily mobile application is an open-source React Native app available on iOS and Android. It provides access to the full episode catalog, topic-specific feeds, bookmarking, and offline playback. The source code is publicly available on GitHub under the MIT license.
    humanURL: https://github.com/SoftwareEngineeringDaily/se-daily-iOS
    baseURL: https://softwareengineeringdaily.com
    tags:
      - Mobile
      - iOS
      - Android
      - React Native
      - Open Source
    properties:
      - type: GitHubRepository
        url: https://github.com/SoftwareEngineeringDaily/se-daily-iOS
      - type: GitHubRepository
        url: https://github.com/SoftwareEngineeringDaily/SE-Daily-Android
common:
  - url: https://softwareengineeringdaily.com/
    name: Software Engineering Daily Website
    type: Website
  - url: https://softwareengineeringdaily.com/about/
    name: About Software Engineering Daily
    type: About
  - url: https://softwareengineeringdaily.com/premium/
    name: Premium Membership
    type: Pricing
  - url: https://softwareengineeringdaily.com/feed/podcast/
    name: Main Podcast RSS Feed
    type: RSSFeed
  - url: https://softwareengineeringdaily.com/2017/07/05/new-topic-feeds/
    name: Topic RSS Feeds
    type: RSSFeeds
  - url: https://github.com/SoftwareEngineeringDaily/software-engineering-daily-api
    name: Backend API Repository
    type: GitHubRepository
  - url: https://softwareengineeringdaily.github.io/Backend/gettingstarted/
    name: API Getting Started Guide
    type: Documentation
  - url: https://podcasts.apple.com/podcast/software-engineering-daily/id1019576853
    name: Software Engineering Daily on Apple Podcasts
    type: Podcast
  - url: https://open.spotify.com/show/6UCtBYL29hwhw4YbTdX83N
    name: Software Engineering Daily on Spotify
    type: Podcast
  - url: https://twitter.com/software_daily
    name: Software Engineering Daily on X
    type: X
  - url: https://www.linkedin.com/company/software-engineering-daily
    name: Software Engineering Daily on LinkedIn
    type: LinkedIn
  - url: https://github.com/softwareengineeringdaily
    name: Software Engineering Daily on GitHub
    type: GitHubOrganization
  - url: https://softwareengineeringdaily.com/tos/
    name: Terms of Service
    type: TermsOfService
  - url: https://softwareengineeringdaily.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
