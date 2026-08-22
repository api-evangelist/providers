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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'The primary Santiment GraphQL API giving developers programmatic access to on-chain metrics, social sentiment, developer activity, and price data for 2,800+ crypto assets. Supports timeseries queries '
  name: SanAPI
  slug: sanapi
- description: A Google Sheets plugin that exposes Santiment metric data directly inside spreadsheets using simple sheet functions. Requires a Santiment API key and a Sanbase subscription. Ideal for analysts who pre
  name: Sansheets
  slug: sansheets
artifact_total: 5
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/santiment/sanpy/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santiment-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://academy.santiment.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://app.santiment.net/pricing
- group: operate
  title: ''
  type: Status
  url: https://status.santiment.net/
- group: company
  title: ''
  type: Blog
  url: https://insights.santiment.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/santiment
- group: commercial
  title: ''
  type: Plans
  url: https://academy.santiment.net/products-and-plans/sanapi-plans/
- group: operate
  title: ''
  type: RateLimits
  url: https://academy.santiment.net/sanapi/rate-limits/
- group: auth
  title: ''
  type: Authentication
  url: https://academy.santiment.net/products-and-plans/create-an-api-key/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://santiment.net/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://santiment.net/privacy/
created: '2026-06-14'
description: Santiment is a crypto market intelligence platform providing REST and GraphQL APIs for accessing on-chain metrics, social sentiment data, developer activity, and blockchain analytics signals. SanAPI covers 2,800+ crypto assets across 14 blockchain networks and offers more than 1,000 metrics including daily active addresses, MVRV ratio, social sentiment scores, Twitter follower counts, trending topics, developer commit activity, and labeled address intelligence spanning 75+ million Ethereum addresses and 65+ million Bitcoin addresses. Data is available via a GraphQL endpoint, a Python SDK (sanpy), S3 parquet exports, and a Google Sheets plugin.
graphqls:
- description: Santiment exposes its full platform through a single GraphQL endpoint at `https://api.santiment.net/graphql`. The API provides programmatic access to on-chain metrics, social sentiment data, developer
  name: Santiment GraphQL API
  slug: santiment-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/santiment.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-14'
name: Santiment
nav: Providers
network: true
overview: 'Santiment publishes 1 API on the [APIs.io](https://apis.io/) network: SanAPI. Tagged areas include Crypto, Blockchain, Market Intelligence, On-Chain Metrics, and Social Sentiment.


  The Santiment catalog on APIs.io includes 1 JSON-LD context.


  Santiment''s developer surface includes developer portal, pricing, status page, engineering blog, authentication, and 7 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 27.3
  delta: -3.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 44.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/santiment/refs/heads/main/screenshots/santiment-2026-06-20T193411.png
security:
- kind: domain-security
  name: Santiment Domain Security
  slug: santiment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: santiment
tags:
- Crypto
- Blockchain
- Market Intelligence
- On-Chain Metrics
- Social Sentiment
- Developer Activity
- Analytics
- GraphQL
website: https://academy.santiment.net/
---
