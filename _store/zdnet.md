---
aid: zdnet
url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/apis.yml
apis:
  - aid: zdnet:rss
    name: ZDNet RSS Feed
    description: RSS feeds providing the latest news, analysis, and reviews from ZDNet covering enterprise IT, security, cloud, hardware, software, artificial intelligence, and business technology for IT professionals.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.zdnet.com/news/rss.xml
    baseURL: https://www.zdnet.com
    tags:
      - Artificial Intelligence
      - Cloud
      - Enterprise IT
      - News Feed
      - RSS
      - Security
      - Technology News
    properties:
      - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/openapi/zdnet-rss.yml
        type: OpenAPI
      - url: https://www.zdnet.com/news/rss.xml
        type: RSS
        name: ZDNet News RSS Feed
      - url: https://www.zdnet.com/topic/security/rss.xml
        type: RSS
        name: ZDNet Security RSS Feed
      - url: https://www.zdnet.com/topic/cloud/rss.xml
        type: RSS
        name: ZDNet Cloud RSS Feed
      - url: https://www.zdnet.com/topic/artificial-intelligence/rss.xml
        type: RSS
        name: ZDNet AI RSS Feed
      - url: https://www.zdnet.com/topic/developer/rss.xml
        type: RSS
        name: ZDNet Developer RSS Feed
      - url: https://www.zdnet.com/topic/innovation/rss.xml
        type: RSS
        name: ZDNet Innovation RSS Feed
      - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/json-schema/
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/json-structure/
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/json-ld/zdnet-rss-context.jsonld
        type: JSON-LD
      - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/examples/
        type: Example
name: ZDNet
description: ZDNet is a business technology news website owned by Ziff Davis, covering enterprise IT, cybersecurity, cloud computing, hardware, software, and innovation for IT professionals and tech-savvy business leaders. ZDNet provides news, analysis, product reviews, and how-to guides. No public developer API is available; content is accessible via RSS feeds.
tags:
  - Enterprise IT
  - Media
  - Technology News
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.zdnet.com/
    name: ZDNet Website
    type: Website
  - url: https://www.zdnet.com/about-zdnet/
    name: About ZDNet
    type: About
  - url: https://www.zdnet.com/news/rss.xml
    name: News RSS Feed
    type: RSS
  - url: https://www.zdnet.com/topic/security/rss.xml
    name: Security RSS Feed
    type: RSS
  - url: https://www.zdnet.com/topic/cloud/rss.xml
    name: Cloud RSS Feed
    type: RSS
  - url: https://www.zdnet.com/topic/artificial-intelligence/rss.xml
    name: AI RSS Feed
    type: RSS
  - url: https://www.zdnet.com/topic/developer/rss.xml
    name: Developer RSS Feed
    type: RSS
  - url: https://www.zdnet.com/newsletters/
    name: Newsletters
    type: Newsletter
  - url: https://www.zdnet.com/meet-the-team/
    name: Editorial Team
    type: Team
  - url: https://www.zdnet.com/advertise/
    name: Advertise
    type: Advertising
  - url: https://www.zdnet.com/article/zdnet-editorial-guidelines/
    name: Editorial Guidelines
    type: EditorialGuidelines
  - url: https://www.zdnet.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.zdnet.com/terms-of-use/
    name: Terms of Use
    type: TermsOfService
  - url: https://x.com/ZDNet
    name: X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/zdnet-com
    name: LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/ZDNet
    name: Facebook
    type: Facebook
  - url: https://podcasts.apple.com/us/podcast/zdnet-video/id271364310
    name: ZDNet Video Podcast on Apple Podcasts
    type: Podcast
  - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/rules/zdnet-rules.yml
    name: ZDNet Spectral Ruleset
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/vocabulary/zdnet-vocabulary.yml
    name: ZDNet Vocabulary
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/zdnet/refs/heads/main/capabilities/zdnet-workflow.yaml
    name: ZDNet Workflow Capability
    type: NaftikoCapability
  - data:
      - name: RSS News Feed
        description: Latest enterprise IT news from ZDNet.
      - name: Topic-Specific Feeds
        description: Filtered RSS feeds for security, cloud, AI, developer, and innovation topics.
      - name: RSS 2.0 Format
        description: Standard XML RSS 2.0 format for syndication.
    name: Features
    type: Features
  - data:
      - name: News Aggregation
        description: Aggregate ZDNet articles into a news app or dashboard.
      - name: Topic Monitoring
        description: Monitor specific topic feeds (security, cloud, AI) for industry tracking.
    name: UseCases
    type: UseCases
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
