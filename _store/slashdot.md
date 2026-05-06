---
aid: slashdot
url: https://raw.githubusercontent.com/api-evangelist/slashdot/refs/heads/main/apis.yml
name: Slashdot
tags:
  - Media
  - Open Source
  - Technology News
  - RSS
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-24'
modified: '2026-05-02'
position: Consumer
segments:
  - Media
  - Technology News
description: Slashdot is a technology news aggregation and community discussion site founded in 1997, focused on open source software, Linux, science, and technology topics. Known by its tagline "News for nerds, stuff that matters," Slashdot allows readers to submit and vote on stories, comment on articles, and follow developments across the technology landscape. The site offers RSS and Atom feeds for programmatic access to its content across multiple topic sections including developers, Linux, games, science, Apple, and more. Feed requests are rate-limited to one per 30 minutes.
apis:
  - aid: slashdot:rss-feeds
    name: Slashdot RSS/Atom Feeds
    tags:
      - RSS
      - Atom
      - News
      - Technology News
      - Open Source
      - Media
    humanURL: https://slashdot.org/faq/feeds.shtml
    properties:
      - url: https://rss.slashdot.org/Slashdot/slashdotMain
        type: RSS
      - url: https://rss.slashdot.org/Slashdot/slashdotDevelopers
        type: RSS
      - url: https://rss.slashdot.org/Slashdot/slashdotApple
        type: RSS
      - url: https://rss.slashdot.org/Slashdot/slashdotLinux
        type: RSS
      - url: https://rss.slashdot.org/Slashdot/slashdotGames
        type: RSS
      - url: https://rss.slashdot.org/Slashdot/slashdotScience
        type: RSS
      - url: https://rss.slashdot.org/Slashdot/slashdotYourRightsOnline
        type: RSS
      - url: openapi/slashdot-rss-openapi.yml
        type: OpenAPI
      - url: json-ld/slashdot-context.jsonld
        type: JSON-LD
      - url: vocabulary/slashdot-vocabulary.yml
        type: Vocabulary
    description: Slashdot provides RSS 1.0 and Atom 1.0 feeds for programmatic access to technology news across multiple topic sections. Feeds are rate-limited to one request per 30 minutes per feed URL. Section feeds are available by substituting section names in the base RSS URL pattern. Subscriber feeds support a log token parameter for personalized content.
common:
  - type: Website
    url: https://slashdot.org/
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotMain
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotDevelopers
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotApple
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotLinux
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotGames
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotScience
  - type: RSS
    url: https://rss.slashdot.org/Slashdot/slashdotYourRightsOnline
  - type: About
    url: https://slashdot.org/faq/slashmeta.shtml
  - type: FAQ
    url: https://slashdot.org/faq/index.shtml
  - type: FAQ-Feeds
    url: https://slashdot.org/faq/feeds.shtml
  - type: Firehose
    url: https://slashdot.org/faq/firehose.shtml
  - type: Privacy Policy
    url: https://slashdot.org/privacy
  - type: OpenAPI
    url: openapi/slashdot-rss-openapi.yml
  - type: JSON-LD
    url: json-ld/slashdot-context.jsonld
  - type: Vocabulary
    url: vocabulary/slashdot-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
