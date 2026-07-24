---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Public HTTP API for Antpool, Bitmain's Bitcoin mining pool. Account operators can read account balance, account and worker hashrate, worker lists, payment history, and pool statistics. All private int
  name: Antpool API
  slug: antpool-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://bitmain.com
- group: operate
  title: ''
  type: Support
  url: https://support.bitmain.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitmaintech
- group: docs
  title: ''
  type: Documentation
  url: https://www.antpool.com/userApiGuide
- group: docs
  title: ''
  type: APIReference
  url: https://www.antpool.com/userApiGuide
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitmain-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitmain-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitmain-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitmain-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitmain-llms.txt
created: '2026-07-17'
description: Bitmain Technologies is a Beijing-based designer and manufacturer of ASIC cryptocurrency-mining hardware, best known for its Antminer line of Bitcoin (SHA-256) and other proof-of-work miners. Bitmain also operates Antpool, one of the world's largest Bitcoin mining pools, which exposes a public HTTP API that lets account operators programmatically read account balances, account and worker hashrate, worker lists, payment history, and pool-wide statistics. The Antpool API authenticates each request with an HMAC-SHA256 signature computed from the operator's user id, API key, and an incrementing nonce, and rate-limits clients to 600 requests per 10 minutes per IP. This company was surfaced as a portfolio company of Hongshan and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitmain.png
layout: provider
modified: '2026-07-18'
name: Bitmain
nav: Providers
network: true
overview: 'Bitmain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Cryptocurrency, Bitcoin, and Mining.


  Bitmain''s developer surface includes support, documentation, API reference, authentication, and 6 more developer resources.'
random_paper: 26
rate_limits:
- limit_count: 1
  name: Bitmain Rate Limits
  slug: bitmain-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Bitmain Authentication
  slug: bitmain-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitmain Domain Security
  slug: bitmain-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitmain
tags:
- Company
- Technology
- Cryptocurrency
- Bitcoin
- Mining
- Mining Pool
- Hardware
- Blockchain
website: https://bitmain.com
---
