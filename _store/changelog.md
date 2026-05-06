---
aid: changelog
url: https://raw.githubusercontent.com/api-evangelist/changelog/refs/heads/main/apis.yml
name: Changelog
x-type: company
description: Changelog is a media company and podcast network for developers covering open source and software development. Founded by Adam Stacoviak and Jerod Santo, Changelog produces world-class developer podcasts including The Changelog, which features deep technical interviews and conversations with the people and teams driving open source software forward. Changelog also publishes a weekly developer news newsletter and operates an open source platform (changelog.com) built with Elixir and Phoenix.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer Community
  - Media
  - Open Source
  - Podcasts
access: 3rd-Party
apis:
  - aid: changelog:podcast-rss
    name: The Changelog Podcast RSS Feed
    description: The Changelog podcast RSS feed provides access to all episodes of The Changelog, a weekly podcast covering software development, open source, and the people and projects behind the code. The feed returns standard podcast RSS/Atom XML with episode metadata including titles, descriptions, audio URLs, and publish dates.
    humanURL: https://changelog.com/podcast
    baseURL: https://changelog.com
    tags:
      - Open Source
      - Podcast
      - RSS
      - Software Development
    properties:
      - type: RSSFeed
        url: https://changelog.com/podcast/feed
      - type: Documentation
        url: https://changelog.com/podcast
  - aid: changelog:master-feed-rss
    name: Changelog Master Feed RSS
    description: The Changelog Master Feed aggregates all Changelog podcast shows into a single RSS feed. This is the one-stop subscription for all developer-focused audio content produced by Changelog Media, including The Changelog podcast and any other active shows in the network.
    humanURL: https://changelog.com/master
    baseURL: https://changelog.com
    tags:
      - Aggregated
      - Master Feed
      - Podcast
      - RSS
    properties:
      - type: RSSFeed
        url: https://changelog.com/master/feed
      - type: Documentation
        url: https://changelog.com/master
  - aid: changelog:news-rss
    name: Changelog News RSS Feed
    description: The Changelog News RSS feed surfaces the latest developer news curated by the Changelog team. Changelog News is a weekly newsletter and short podcast covering what is happening in software development, open source, and the broader developer ecosystem.
    humanURL: https://changelog.com/news
    baseURL: https://changelog.com
    tags:
      - Developer News
      - News
      - Newsletter
      - RSS
    properties:
      - type: RSSFeed
        url: https://changelog.com/news/feed
      - type: Documentation
        url: https://changelog.com/news
  - aid: changelog:github-platform
    name: Changelog Open Source Platform (GitHub)
    description: The Changelog platform is an open source Elixir and Phoenix application that powers changelog.com. The source code is publicly available on GitHub and includes the full CMS, podcast management, episode metadata, and content delivery infrastructure. Developers can explore the codebase to understand how the platform works and contribute to the project.
    humanURL: https://github.com/thechangelog/changelog.com
    baseURL: https://github.com/thechangelog
    tags:
      - CMS
      - Elixir
      - Open Source
      - Phoenix
    properties:
      - type: Documentation
        url: https://github.com/thechangelog/changelog.com
      - type: Repository
        url: https://github.com/thechangelog/changelog.com
common:
  - url: https://changelog.com/
    name: Changelog Website
    type: Website
  - url: https://changelog.com/podcast
    name: The Changelog Podcast
    type: Podcast
  - url: https://changelog.com/master
    name: Changelog Master Feed
    type: Podcast
  - url: https://changelog.com/news
    name: Changelog News
    type: Newsletter
  - url: https://changelog.com/podcast/feed
    name: The Changelog RSS Feed
    type: RSSFeed
  - url: https://changelog.com/master/feed
    name: Changelog Master RSS Feed
    type: RSSFeed
  - url: https://changelog.com/news/feed
    name: Changelog News RSS Feed
    type: RSSFeed
  - url: https://changelog.com/sponsor
    name: Sponsor Changelog
    type: Sponsorship
  - url: https://changelog.com/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://github.com/thechangelog
    name: Changelog on GitHub
    type: GitHub
  - url: https://github.com/thechangelog/changelog.com
    name: Changelog Open Source Platform
    type: Repository
  - url: https://podcasts.apple.com/us/podcast/the-changelog-software-development-open-source/id341623264
    name: The Changelog on Apple Podcasts
    type: Podcast
  - url: https://open.spotify.com/show/5bBki72YeKSLUqyD94qsuJ
    name: The Changelog on Spotify
    type: Podcast
  - url: https://x.com/changelog
    name: Changelog on X
    type: X
  - name: Features
    type: Features
    data:
      - name: Developer Podcasts
      - name: Open Source Focus
      - name: Weekly Newsletter
      - name: Podcast Network
      - name: RSS Feeds
      - name: Master Feed
      - name: Developer Community
      - name: Episode Notes
      - name: Guest Interviews
      - name: Live Events
      - name: Open Source Platform
      - name: Elixir and Phoenix
      - name: Sponsorships
  - name: UseCases
    type: UseCases
    data:
      - name: Developer Education
      - name: Open Source Promotion
      - name: Podcast Distribution
      - name: Newsletter Aggregation
      - name: Developer News Consumption
      - name: Conference and Event Coverage
      - name: Sponsor Content Distribution
  - name: Shows
    type: Shows
    data:
      - name: The Changelog
      - name: Changelog News
      - name: Go Time
      - name: JS Party
      - name: Practical AI
      - name: Ship It!
      - name: Brain Science
  - name: Integrations
    type: Integrations
    data:
      - name: Apple Podcasts
      - name: Spotify
      - name: Overcast
      - name: Pocket Casts
      - name: RSS
      - name: GitHub
      - name: YouTube
      - name: Fireside
created: '2026-03-24'
modified: '2026-04-23'
specificationVersion: '0.19'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
