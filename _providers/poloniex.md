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
- baseURL: https://docs.poloniex.com
  baseurl_source: declared
  description: US based digital asset exchange
  name: Poloniex
  slug: poloniex
artifact_total: 4
asyncapis:
- description: AsyncAPI 2.6 description of the Poloniex public, private (spot) and futures (v3) WebSocket interfaces. All channels and message field names are derived from Poloniex's official Java and Python SDKs pu
  name: Poloniex WebSocket API
  slug: poloniex-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poloniex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.poloniex.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: US based digital asset exchange
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poloniex.png
layout: provider
modified: '2026-05-29'
name: Poloniex
nav: Providers
network: true
overview: 'Poloniex publishes 1 API on the [APIs.io](https://apis.io/) network: Poloniex. Tagged areas include Cryptocurrency and Public APIs.


  The Poloniex catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Poloniex API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: poloniex-asyncapi-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/poloniex/refs/heads/main/screenshots/poloniex-2026-06-20T191855.png
security:
- kind: domain-security
  name: Poloniex Domain Security
  slug: poloniex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: poloniex
tags:
- Cryptocurrency
- Public APIs
website: https://docs.poloniex.com
---
