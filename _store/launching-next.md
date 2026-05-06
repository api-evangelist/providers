---
aid: launching-next
name: Launching Next
description: Launching Next is a startup discovery and submission platform that publishes daily listings of new and trending tech startups and side projects worldwide. Founded as a long-running startup directory, the platform has featured over 45,000 startups and side projects, making it a go-to resource for founders, investors, and early adopters looking to discover what is being built next. Entrepreneurs can submit their startups for free, with an optional paid fast-track review.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Discovery
  - Product Launch
  - Startups
url: https://raw.githubusercontent.com/api-evangelist/launching-next/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: launching-next:rss-feed
    name: Launching Next RSS Feed
    description: Launching Next provides an RSS feed for the latest startup listings published on the platform. The feed allows developers, aggregators, and readers to programmatically consume new startup entries as they are published, enabling integration with feed readers, monitoring tools, and custom startup discovery workflows.
    humanURL: https://www.launchingnext.com/
    baseURL: https://www.launchingnext.com
    tags:
      - Feed
      - RSS
      - Startups
      - Syndication
    properties:
      - type: Documentation
        url: https://www.launchingnext.com/
      - type: RSSFeed
        url: https://www.launchingnext.com/feed/
common:
  - url: https://www.launchingnext.com/
    name: Launching Next Website
    type: Website
  - url: https://www.launchingnext.com/submit/
    name: Submit a Startup
    type: Portal
  - url: https://www.launchingnext.com/feed/
    name: Launching Next RSS Feed
    type: RSSFeed
  - url: https://x.com/LaunchingNext
    name: Launching Next on X
    type: X
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
