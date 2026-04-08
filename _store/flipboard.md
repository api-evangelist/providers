---
aid: flipboard
url: https://raw.githubusercontent.com/api-evangelist/flipboard/refs/heads/main/apis.yml
apis:
- aid: flipboard:rss-feeds
  name: Flipboard RSS Feeds
  description: Flipboard supports RSS feeds as the primary integration mechanism for publishers and content creators. Publishers can submit RSS feeds to be featured as Flipboard Magazines, enabling content distribution to Flipboard's audience. Feeds must meet Flipboard's RSS guidelines, including full article body content, images of at least 400px wide, at least 30 items, and updates pushed via PubSubHubbub.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://about.flipboard.com/rss-guidelines/
  baseURL: https://flipboard.com
  tags:
  - Content Syndication
  - News
  - Publishers
  - RSS
  properties:
  - url: https://about.flipboard.com/rss-guidelines/
    type: Documentation
  - url: https://about.flipboard.com/forpublishers/
    type: GettingStarted
  - url: https://feedvalidator.flipboard.com/
    type: Validator
  - url: https://flipboard.helpshift.com/hc/en/1-flipboard/faq/1024-submit-a-publisher-application/
    type: GettingStarted
- aid: flipboard:activitypub
  name: Flipboard ActivityPub
  description: Flipboard has implemented the ActivityPub protocol, making its content available to the broader Fediverse. Starting in 2023, Flipboard began federating its magazines and curators via ActivityPub, allowing users on Mastodon, Threads, Pixelfed, and other ActivityPub-compatible platforms to follow and interact with Flipboard content. Flipboard's full architecture is built around ActivityPub.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://about.flipboard.com/inside-flipboard/flipboard-begins-to-federate/
  baseURL: https://flipboard.com
  tags:
  - ActivityPub
  - Decentralized
  - Fediverse
  - Mastodon
  - Open Social Web
  properties:
  - url: https://github.com/Flipboard/activitypub
    type: GitHubRepository
  - url: https://about.flipboard.com/inside-flipboard/flipboard-begins-to-federate/
    type: Announcement
  - url: https://about.flipboard.com/business/publisher-federation-flipboard/
    type: Guide
name: Flipboard
tags:
- ActivityPub
- Content Curation
- Digital Publishing
- Fediverse
- News
- RSS
- Social Media
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Flipboard is a content curation and social magazine platform that aggregates articles, videos, and social media posts into personalized, magazine-style feeds. Founded in 2010, Flipboard allows users to curate content into magazines around topics of interest and follow curators and publishers. Flipboard has embraced open web standards, implementing ActivityPub to federate with the Fediverse and supporting RSS for publisher content distribution.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

