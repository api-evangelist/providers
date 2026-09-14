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
- baseURL: https://bybit-exchange.github.io/docs/linear/#t-introduction
  baseurl_source: declared
  description: Cryptocurrency data feed and algorithmic trading
  name: Bybit
  slug: bybit
artifact_total: 3
asyncapis:
- description: 'AsyncAPI definition for the Bybit V5 WebSocket API. Bybit exposes five public WebSocket endpoints split by product (spot, linear, inverse, option, spread) plus a single authenticated private endpoint '
  name: Bybit V5 WebSocket API
  slug: bybit-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://bybit-exchange.github.io/docs/linear/#t-introduction
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency data feed and algorithmic trading
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bybit.png
layout: provider
modified: '2026-05-29'
name: Bybit
nav: Providers
network: true
overview: 'Bybit publishes 1 API on the [APIs.io](https://apis.io/) network: Bybit. Tagged areas include Cryptocurrency and Public APIs.


  The Bybit catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 13
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Bybit API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: bybit-asyncapi-spectral-rules
slug: bybit
tags:
- Cryptocurrency
- Public APIs
website: https://bybit-exchange.github.io/docs/linear/#t-introduction
---
