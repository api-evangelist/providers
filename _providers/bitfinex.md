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
- baseURL: https://docs.bitfinex.com/docs
  baseurl_source: declared
  description: Cryptocurrency Trading Platform
  name: Bitfinex
  slug: bitfinex
artifact_total: 4
asyncapis:
- description: AsyncAPI description of the Bitfinex public and authenticated WebSocket v2 API. The Bitfinex WebSocket API streams real-time market data and authenticated account information using a compact array-bas
  name: Bitfinex WebSocket API v2
  slug: bitfinex-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitfinex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.bitfinex.com/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://blog.bitfinex.com/feed/
created: '2026-05-28'
description: Cryptocurrency Trading Platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitfinex.png
layout: provider
modified: '2026-05-29'
name: Bitfinex
nav: Providers
network: true
overview: 'Bitfinex publishes 1 API on the [APIs.io](https://apis.io/) network: Bitfinex. Tagged areas include Cryptocurrency and Public APIs.


  The Bitfinex catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bitfinex''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 17
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Bitfinex API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: bitfinex-asyncapi-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/bitfinex/refs/heads/main/screenshots/bitfinex-2026-06-20T173307.png
security:
- kind: domain-security
  name: Bitfinex Domain Security
  slug: bitfinex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitfinex
tags:
- Cryptocurrency
- Public APIs
website: https://docs.bitfinex.com/docs
---
