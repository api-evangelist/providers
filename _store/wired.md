---
aid: wired
name: Wired
description: Wired (wired.com) is an American technology and culture magazine published by Condé Nast, covering how emerging technologies affect culture, the economy, and politics. Founded in 1993, Wired provides RSS feeds for programmatic content consumption across categories including Business, Science, Security, Politics, Gear, Ideas, Culture, and AI. The magazine also maintains a YouTube channel, newsletters, and social media presence.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Content
  - Innovation
  - Media
  - News
  - RSS
  - Science
  - Technology News
url: https://raw.githubusercontent.com/api-evangelist/wired/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wired:rss-feed
    name: Wired RSS Feed
    description: Wired provides standard RSS feeds for its main content stream and individual topic categories including Business, Science, Security, Politics, Gear, Ideas, Culture, and AI. These feeds allow developers and readers to consume Wired content programmatically using any feed parsing library or RSS reader tool.
    humanURL: https://www.wired.com/feed/rss
    baseURL: https://www.wired.com
    tags:
      - Feed
      - Media
      - News
      - RSS
      - Syndication
    properties:
      - type: Documentation
        url: https://www.wired.com/feed/rss
      - type: RSSFeed
        url: https://www.wired.com/feed/rss
      - type: RSSFeed
        url: https://www.wired.com/feed/category/business/latest/rss
      - type: RSSFeed
        url: https://www.wired.com/feed/category/science/latest/rss
      - type: RSSFeed
        url: https://www.wired.com/feed/category/security/latest/rss
      - type: RSSFeed
        url: https://www.wired.com/feed/category/gear/latest/rss
      - type: RSSFeed
        url: https://www.wired.com/feed/tag/ai/latest/rss
common:
  - url: https://www.wired.com/
    name: Wired
    type: Website
    description: Main website for Wired technology and culture magazine.
  - url: https://www.wired.com/about/
    name: About Wired
    type: About
    description: About page describing Wired's mission and history.
  - url: https://www.wired.com/feed/rss
    name: Wired Main RSS Feed
    type: RSSFeed
    description: Main RSS feed for all Wired content.
  - url: https://www.wired.com/feed/category/business/latest/rss
    name: Wired Business RSS Feed
    type: RSSFeed
    description: RSS feed for Wired Business category.
  - url: https://www.wired.com/feed/category/science/latest/rss
    name: Wired Science RSS Feed
    type: RSSFeed
    description: RSS feed for Wired Science category.
  - url: https://www.wired.com/feed/category/security/latest/rss
    name: Wired Security RSS Feed
    type: RSSFeed
    description: RSS feed for Wired Security category.
  - url: https://www.wired.com/feed/category/gear/latest/rss
    name: Wired Gear RSS Feed
    type: RSSFeed
    description: RSS feed for Wired Gear category.
  - url: https://www.wired.com/feed/tag/ai/latest/rss
    name: Wired AI RSS Feed
    type: RSSFeed
    description: RSS feed for Wired AI topic tag.
  - url: https://subscribe.wired.com/
    name: Wired Subscription
    type: Subscription
    description: Wired magazine subscription page.
  - url: https://www.wired.com/newsletter/
    name: Wired Newsletter
    type: Newsletter
    description: Wired newsletter signup and archive.
  - url: https://www.condenast.com/privacy-policy
    name: Privacy Policy
    type: PrivacyPolicy
    description: Condé Nast privacy policy.
  - url: https://www.condenast.com/user-agreement
    name: Terms of Service
    type: TermsOfService
    description: Condé Nast user agreement.
  - url: https://www.wired.com/about/advertising-info/
    name: Advertise with Wired
    type: Advertising
    description: Advertising information for Wired magazine.
  - url: https://www.condenast.com/careers/
    name: Careers at Condé Nast
    type: Careers
    description: Career opportunities at Condé Nast.
  - url: https://www.youtube.com/wired
    name: Wired on YouTube
    type: YouTube
    description: Official Wired YouTube channel.
  - url: https://x.com/wired
    name: Wired on X
    type: X
    description: Official Wired account on X (formerly Twitter).
  - url: https://www.linkedin.com/company/wired
    name: Wired on LinkedIn
    type: LinkedIn
    description: Official Wired company page on LinkedIn.
  - url: https://www.instagram.com/wired/
    name: Wired on Instagram
    type: Instagram
    description: Official Wired account on Instagram.
  - url: https://www.tiktok.com/@wired
    name: Wired on TikTok
    type: TikTok
    description: Official Wired account on TikTok.
  - url: https://raw.githubusercontent.com/api-evangelist/wired/refs/heads/main/json-ld/wired-context.jsonld
    name: Wired JSON-LD Context
    type: JSONLDContext
    description: JSON-LD context for Wired content domain vocabulary.
  - url: https://raw.githubusercontent.com/api-evangelist/wired/refs/heads/main/vocabulary/wired-vocabulary.yml
    name: Wired Vocabulary
    type: Vocabulary
    description: Domain vocabulary for Wired media content.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
