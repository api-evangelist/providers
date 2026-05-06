---
aid: podbean-api
name: Podbean API
description: This is for third-party apps to connect to Podbean in order to manage a user's podcast. To manage your own podcast via API, please use Client Credentials and Get Multiple Podcasts Tokens. The Podbean API supports OAuth 2.0 authentication and provides programmatic access to podcasts, episodes, analytics, and account management resources.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Podcasts
  - Podcasting
  - Audio
  - Media
  - OAuth
  - Episodes
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/podbean-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: podbean-api:podbean-api
    name: Podbean API
    description: This is for third-party apps to connect to Podbean in order to manage a user's podcast. To manage your own podcast via API, please use Client Credentials and Get Multiple Podcasts Tokens. Provides OAuth 2.0 authenticated access to manage podcasts and episodes.
    humanURL: https://developers.podbean.com/podbean-api-docs/
    baseURL: https://api.podbean.com/v1
    tags:
      - Podcasts
      - Audio
      - OAuth
    properties:
      - type: Documentation
        url: https://developers.podbean.com/podbean-api-docs/
      - type: Authentication
        url: https://developers.podbean.com/podbean-api-docs/#api-Authentication
common:
  - type: Website
    url: https://www.podbean.com
  - type: Documentation
    url: https://developers.podbean.com/podbean-api-docs/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
