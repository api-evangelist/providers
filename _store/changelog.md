---
aid: changelog
url: https://raw.githubusercontent.com/api-evangelist/changelog/refs/heads/main/apis.yml
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
name: Changelog
tags:
- Developer Community
- Media
- Open Source
- Podcasts
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Changelog is a media company and podcast network for developers covering open source and software development. Founded by Adam Stacoviak and Jerod Santo, Changelog produces world-class developer podcasts including The Changelog, which features deep technical interviews and conversations with the people and teams driving open source software forward. Changelog also publishes a weekly developer news newsletter and operates an open source platform (changelog.com) built with Elixir and Phoenix.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

