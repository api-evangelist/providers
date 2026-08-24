---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The Braiins Mining Insights Public API provides access to Bitcoin mining network statistics, hashrate data, and mining pool performance metrics. Used for research, analysis, and integration with minin
  name: Braiins Mining Insights Public API
  slug: mining-insights-api
- description: API access for Braiins Pool (formerly Slush Pool), the world's first Bitcoin mining pool. Provides miner statistics, payout data, worker management, and pool hashrate information.
  name: Braiins Pool API
  slug: braiins-pool-api
- description: Braiins OS+ is custom mining firmware for Bitcoin ASICs (Antminer series) featuring autotuning, dynamic performance scaling, and thermal management. Supports remote batch configuration via Braiins Too
  name: Braiins OS+ Firmware API
  slug: braiins-os-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/braiins-academy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braiins
- group: company
  title: ''
  type: Website
  url: https://braiins.com
- group: learn
  title: ''
  type: Academy
  url: https://academy.braiins.com
- group: other
  title: ''
  type: Pool
  url: https://braiins.com/pool
- group: other
  title: ''
  type: Firmware
  url: https://braiins.com/os/plus
- group: other
  title: ''
  type: StratumV2
  url: https://braiins.com/stratum-v2
- group: docs
  title: ''
  type: Documentation
  url: https://academy.braiins.com/os/plus-en/
- group: company
  title: ''
  type: Blog
  url: https://braiins.com/blog
created: '2025-03-01'
description: Braiins is a Bitcoin mining technology company operating the world's longest-running Bitcoin mining pool (Slush Pool, now Braiins Pool), developing Braiins OS+ mining firmware, and pioneering the Stratum V2 next-generation mining protocol. Braiins Academy provides educational resources on Bitcoin mining, and the company publishes a public Mining Insights API with network statistics. Stratum V2 increases mining security, bandwidth efficiency, and miner autonomy through decentralized transaction selection.
finops:
- name: Braiins Academy Finops
  service_category: API
  slug: braiins-academy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/braiins-academy.png
layout: provider
modified: '2026-04-21'
name: Braiins
nav: Providers
network: true
overview: 'Braiins publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bitcoin Mining, Cryptocurrency, Mining Pool, Mining Firmware, and Blockchain.


  Braiins'' developer surface includes academy / training, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Braiins Academy Plans Pricing
  plan_count: 3
  slug: braiins-academy-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Braiins Academy Rate Limits
  slug: braiins-academy-rate-limits
score:
  band: emerging
  composite: 11.5
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/braiins-academy/refs/heads/main/screenshots/braiins-academy-2026-06-20T173627.png
security:
- kind: domain-security
  name: Braiins Academy Domain Security
  slug: braiins-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: braiins-academy
tags:
- Bitcoin Mining
- Cryptocurrency
- Mining Pool
- Mining Firmware
- Blockchain
- Stratum V2
website: https://braiins.com
---
