---
aid: the-next-web
url: https://raw.githubusercontent.com/api-evangelist/the-next-web/refs/heads/main/apis.yml
name: The Next Web
description: The Next Web is a leading online media organization covering technology news, business, and culture. Founded in 2006, TNW reports on startups, innovation, artificial intelligence, digital culture, and the future of work. The primary programmatic access to TNW content is through its RSS 2.0 feed, which is updated hourly with the latest articles across all topic areas. Category-specific feeds are also available for Deep Tech, Plugged (consumer tech), and Sustainability. TNW also organizes the annual TNW Conference and operates a technology events business.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - Technology News
  - Innovation
  - Media
  - Events
  - Startups
  - Artificial Intelligence
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: the-next-web:the-next-web-rss-feed
    name: TNW RSS Feed
    description: The Next Web provides an RSS 2.0 feed updated hourly with the latest technology news, analysis, and articles published on thenextweb.com. The feed covers topics including artificial intelligence, startups, innovation, digital culture, and the future of work. Category-specific feeds are available for Deep Tech, Plugged (consumer tech), and Sustainability. Each article entry includes title, link, description, publication date, author, and category tags.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://thenextweb.com
    humanURL: https://thenextweb.com/feed/
    tags:
      - Articles
      - News
      - RSS
      - Technology
      - Innovation
    properties:
      - url: https://thenextweb.com/feed/
        type: RSS
      - url: https://thenextweb.com/deep-tech/feed/
        name: Deep Tech RSS Feed
        type: RSS
      - url: https://thenextweb.com/plugged/feed/
        name: Plugged RSS Feed
        type: RSS
      - url: https://thenextweb.com/sustainability/feed/
        name: Sustainability RSS Feed
        type: RSS
common:
  - url: https://thenextweb.com/
    name: TNW Website
    type: Website
  - url: https://thenextweb.com/feed/
    name: RSS Feed
    type: RSS
  - url: https://thenextweb.com/latest
    name: Latest News
    type: News
  - url: https://thenextweb.com/newsletters
    name: TNW Newsletters
    type: Newsletter
  - url: https://thenextweb.com/events
    name: TNW Events
    type: Events
  - url: https://thenextweb.com/conference
    name: TNW Conference
    type: Events
  - url: https://thenextweb.com/about
    name: About TNW
    type: About
  - url: https://thenextweb.com/advertise
    name: Advertise with TNW
    type: Advertising
  - url: https://deals.thenextweb.com/
    name: TNW Deals
    type: Marketplace
  - url: https://thenextweb.com/privacy-statement
    name: Privacy Statement
    type: PrivacyPolicy
  - url: https://thenextweb.com/terms-of-service
    name: Terms of Service
    type: TermsOfService
  - url: https://thenextweb.com/contact
    name: Contact TNW
    type: Contact
  - url: https://x.com/thenextweb
    name: TNW on X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/the-next-web
    name: TNW on LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/thenextweb/
    name: TNW on Facebook
    type: Facebook
  - url: https://github.com/thenextweb
    name: TNW on GitHub
    type: GitHub
  - url: json-schema/the-next-web-article-schema.json
    type: JSONSchema
  - url: json-ld/the-next-web-context.jsonld
    type: JSONLDContext
  - url: vocabulary/the-next-web-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
