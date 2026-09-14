---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: Seychelles based cryptocurrency exchange
  name: Huobi
  slug: huobi
artifact_total: 3
asyncapis:
- description: 'AsyncAPI 2.6 specification for Huobi (HTX) public WebSocket Market Data API and WebSocket v2 Asset & Order subscription API. ## Envelope conventions ### Market data (v1, /ws) - Subscribe: `{ "sub": "<'
  name: Huobi / HTX WebSocket API
  slug: huobi-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://huobiapi.github.io/docs/spot/v1/en/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Seychelles based cryptocurrency exchange
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huobi.png
layout: provider
modified: '2026-05-29'
name: Huobi
nav: Providers
network: true
overview: 'Huobi publishes 1 API on the [APIs.io](https://apis.io/) network: Huobi. Tagged areas include Cryptocurrency and Public APIs.


  The Huobi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 10
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Huobi API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: huobi-asyncapi-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/huobi/refs/heads/main/screenshots/huobi-2026-06-20T182957.png
slug: huobi
tags:
- Cryptocurrency
- Public APIs
website: https://huobiapi.github.io/docs/spot/v1/en/
---
