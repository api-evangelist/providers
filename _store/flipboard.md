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
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://flipboard.com/
    name: Flipboard Website
    type: Website
  - url: https://about.flipboard.com/
    name: About Flipboard
    type: About
  - url: https://about.flipboard.com/forpublishers/
    name: For Publishers
    type: Portal
  - url: https://about.flipboard.com/rss-guidelines/
    name: RSS Guidelines
    type: Documentation
  - url: https://feedvalidator.flipboard.com/
    name: Feed Validator
    type: Validator
  - url: https://engineering.flipboard.com/
    name: Flipboard Engineering Blog
    type: Blog
  - url: https://github.com/Flipboard
    name: Flipboard on GitHub
    type: GitHubOrganization
  - url: https://github.com/Flipboard/activitypub
    name: ActivityPub Implementation
    type: GitHubRepository
  - url: https://flipboard.helpshift.com/hc/en/
    name: Help Center
    type: Support
  - url: https://flipboard.helpshift.com/hc/en/1-flipboard/contact-us/
    name: Contact Us
    type: Contact
  - url: https://about.flipboard.com/terms-of-service/
    name: Terms of Service
    type: TermsOfService
  - url: https://about.flipboard.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://about.flipboard.com/cookie-policy/
    name: Cookie Policy
    type: CookiePolicy
  - url: https://about.flipboard.com/community-guidelines/
    name: Community Guidelines
    type: CommunityGuidelines
  - url: https://x.com/flipboard
    name: X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/flipboard
    name: LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/flipboard
    name: Facebook
    type: Facebook
description: Flipboard is a content curation and social magazine platform that aggregates articles, videos, and social media posts into personalized, magazine-style feeds. Founded in 2010, Flipboard allows users to curate content into magazines around topics of interest and follow curators and publishers. Flipboard has embraced open web standards, implementing ActivityPub to federate with the Fediverse and supporting RSS for publisher content distribution.
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
---
