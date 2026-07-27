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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Olympusdao Agentic Access
  operation_count: 22
  slug: olympusdao-agentic-access
  summary_line: 22 operations
api_count: 8
apis:
- description: 'Serverless GCP Cloud Function that returns the current OHM circulating supply as a plain-text numeric string. Reads from a one-hour Firestore cache backed by the Olympus Protocol Metrics API. Used by '
  name: Olympus OHM Circulating Supply API
  slug: olympus-ohm-circulating-supply-api
- description: Serverless GCP Cloud Function that returns the current OHM total supply as a plain-text numeric string. Reads from a one-hour Firestore cache backed by the Olympus Protocol Metrics API. Used by CoinGe
  name: Olympus OHM Total Supply API
  slug: olympus-ohm-total-supply-api
- description: API health and readiness endpoints.
  name: OlympusDAO Health API
  slug: olympusdao-health-api
- description: Deprecated WunderGraph-compatible /operations routes.
  name: OlympusDAO Legacy API
  slug: olympusdao-legacy-api
- description: Date bounds and indexer metadata.
  name: OlympusDAO Metadata API
  slug: olympusdao-metadata-api
- description: Daily OHM supply attribution records.
  name: OlympusDAO OHM Supply API
  slug: olympusdao-ohm-supply-api
- description: Daily cross-chain OHM protocol metrics.
  name: OlympusDAO Protocol Metrics API
  slug: olympusdao-protocol-metrics-api
- description: Daily treasury asset holdings.
  name: OlympusDAO Treasury API
  slug: olympusdao-treasury-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/olympusdao-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olympusdao-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://olympusdao.medium.com/feed
created: '2021-05-01'
description: OlympusDAO is a decentralized reserve currency protocol built on Ethereum that pioneered protocol-owned liquidity (POL). The Olympus protocol issues OHM, a crypto-native reserve currency backed by a diversified treasury of on-chain assets across Ethereum, Arbitrum, Base, Polygon, Fantom, and Berachain. OlympusDAO provides public REST APIs for querying daily OHM supply, treasury asset holdings, protocol metrics (price, APY, index), and bond market data — powering the Olympus Treasury Dashboard and third-party integrations such as CoinGecko.
examples:
- key_count: 4
  name: Daily Metrics Request
  slug: daily-metrics-request
- key_count: 2
  name: Daily Metrics Response
  slug: daily-metrics-response
- key_count: 2
  name: Ohm Supply Response
  slug: ohm-supply-response
- key_count: 2
  name: Treasury Assets Response
  slug: treasury-assets-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.olympusdao.finance/images/og-image.png
json_schemas:
- name: DailyMetric
  property_count: 14
  slug: daily-metric
- name: OhmSupplyRecord
  property_count: 6
  slug: ohm-supply-record
- name: TreasuryAsset
  property_count: 10
  slug: treasury-asset
jsonld:
- class_count: 0
  name: Olympusdao Context
  property_count: 0
  slug: olympusdao
layout: provider
modified: '2026-06-14'
name: OlympusDAO
nav: Providers
network: true
overview: 'OlympusDAO publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Health API, Legacy API, Metadata API, and 3 more. Tagged areas include DeFi, Protocol-Owned Liquidity, Reserve Currency, Treasury, and Staking.


  The OlympusDAO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OlympusDAO''s developer surface includes engineering blog and 2 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: OlympusDAO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: olympusdao-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 51.8
    developer_ergonomics: 2.2
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 33.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olympusdao/refs/heads/main/screenshots/olympusdao-2026-06-20T190659.png
security:
- kind: domain-security
  name: Olympusdao Domain Security
  slug: olympusdao-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: olympusdao
tags:
- DeFi
- Protocol-Owned Liquidity
- Reserve Currency
- Treasury
- Staking
- Bonds
- OHM
- Ethereum
- Web3
website: https://www.olympusdao.finance/
---
