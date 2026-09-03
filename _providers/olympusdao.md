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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Olympusdao Agentic Access
  operation_count: 22
  slug: olympusdao-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: 'Serverless GCP Cloud Function that returns the current OHM circulating supply as a plain-text numeric string. Reads from a one-hour Firestore cache backed by the Olympus Protocol Metrics API. Used by '
  name: Olympus OHM Circulating Supply API
  slug: olympus-ohm-circulating-supply-api
- description: Serverless GCP Cloud Function that returns the current OHM total supply as a plain-text numeric string. Reads from a one-hour Firestore cache backed by the Olympus Protocol Metrics API. Used by CoinGe
  name: Olympus OHM Total Supply API
  slug: olympus-ohm-total-supply-api
- baseURL: https://treasury-subgraph-api.olympusdao.finance
  baseurl_source: declared
  description: API health and readiness endpoints.
  name: OlympusDAO Health API
  slug: olympusdao-health-api
- baseURL: https://treasury-subgraph-api.olympusdao.finance
  baseurl_source: declared
  description: Deprecated WunderGraph-compatible /operations routes.
  name: OlympusDAO Legacy API
  slug: olympusdao-legacy-api
- baseURL: https://treasury-subgraph-api.olympusdao.finance
  baseurl_source: declared
  description: Date bounds and indexer metadata.
  name: OlympusDAO Metadata API
  slug: olympusdao-metadata-api
- baseURL: https://treasury-subgraph-api.olympusdao.finance
  baseurl_source: declared
  description: Daily OHM supply attribution records.
  name: OlympusDAO OHM Supply API
  slug: olympusdao-ohm-supply-api
- baseURL: https://treasury-subgraph-api.olympusdao.finance
  baseurl_source: declared
  description: Daily cross-chain OHM protocol metrics.
  name: OlympusDAO Protocol Metrics API
  slug: olympusdao-protocol-metrics-api
- baseURL: https://treasury-subgraph-api.olympusdao.finance
  baseurl_source: declared
  description: Daily treasury asset holdings.
  name: OlympusDAO Treasury API
  slug: olympusdao-treasury-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Olympus Protocol Metrics Health API
  slug: open-olympusdao-health-api
- collection_type: open
  name: Olympus Protocol Metrics Health Legacy API
  slug: open-olympusdao-legacy-api
- collection_type: open
  name: Olympus Protocol Metrics Health Metadata API
  slug: open-olympusdao-metadata-api
- collection_type: open
  name: Olympus Protocol Metrics Health OHM Supply API
  slug: open-olympusdao-ohm-supply-api
- collection_type: open
  name: Olympus Health Protocol Metrics API
  slug: open-olympusdao-protocol-metrics-api
- collection_type: open
  name: Olympus Protocol Metrics Health Treasury API
  slug: open-olympusdao-treasury-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/OlympusDAO/coingecko-api/issues
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


  OlympusDAO''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OlympusDAO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: olympusdao-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.5
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 50.7
    developer_ergonomics: 11.9
    discoverability: 70.4
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
