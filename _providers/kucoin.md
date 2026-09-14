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
- description: Cryptocurrency Trading Platform
  name: KuCoin
  slug: kucoin
artifact_total: 4
asyncapis:
- description: 'AsyncAPI 2.6 description of KuCoin''s public WebSocket streaming API for the Classic (Spot/Margin) account. ## Obtaining the connection endpoint The WebSocket endpoint and a short-lived bearer token ar'
  name: KuCoin Public WebSocket API
  slug: kucoin-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kucoin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.kucoin.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.kucoin.com/blog
created: '2026-05-28'
description: Cryptocurrency Trading Platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kucoin.png
layout: provider
modified: '2026-05-29'
name: KuCoin
nav: Providers
network: true
overview: 'KuCoin publishes 1 API on the [APIs.io](https://apis.io/) network: KuCoin. Tagged areas include Cryptocurrency and Public APIs.


  The KuCoin catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  KuCoin''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: KuCoin API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: kucoin-asyncapi-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/kucoin/refs/heads/main/screenshots/kucoin-2026-06-20T184213.png
security:
- kind: domain-security
  name: Kucoin Domain Security
  slug: kucoin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kucoin
tags:
- Cryptocurrency
- Public APIs
website: https://docs.kucoin.com/
---
