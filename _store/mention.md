---
aid: mention
name: Mention
description: Mention is a media monitoring and social listening platform that monitors over one billion sources in real-time across 42 languages. Its JSON-based RESTful API gives developers programmatic access to alerts, mentions, streaming data, and account management features.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Alerts
  - Brand Monitoring
  - Media Monitoring
  - Social Listening
url: https://raw.githubusercontent.com/api-evangelist/mention/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mention:mention-api
    name: Mention API
    description: The Mention API is a JSON-based RESTful API that gives developers access to Mention's media monitoring features. It supports managing alerts, listing and streaming mentions, and integrating monitoring data into custom workflows.
    humanURL: https://api.mention.com/
    baseURL: https://api.mention.com/api
    tags:
      - Alerts
      - Media Monitoring
      - Social Listening
    properties:
      - type: Documentation
        url: https://api.mention.com/
      - type: Getting Started
        url: https://en.support.mention.com/en/articles/1904644-api-access-explained
common:
  - type: Portal
    url: https://mention.com/en/media-monitoring-api/
  - type: Website
    url: https://mention.com/
  - type: Sign Up
    url: https://mention.com/en/pricing/
  - type: Login
    url: https://app.mention.com/login
  - type: Pricing
    url: https://mention.com/en/pricing/
  - type: Support
    url: https://en.support.mention.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
