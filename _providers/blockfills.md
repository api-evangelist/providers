---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API connectivity for BlockFills trading platforms
  name: BlockFills API
  slug: blockfills-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/blockfills/hosts/blockfills-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockfills-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockfills.com/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://www.blockfills.com/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.blockfills.com/blog/
- group: auth
  href: https://artifacts.apis.io/blockfills/security/blockfills-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockfills-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockfills.com/
coverage:
  checked: '2026-09-29'
  detail: The developer portal page https://www.blockfills.com/open/ contains no machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://www.blockfills.com/open/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: BlockFills provides crypto trading solutions and financial technology services, offering liquidity solutions, OTC trading, crypto options, SaaS platforms, FIX API, REST API and more. The company focuses on end‑to‑end digital asset technology for institutional and retail clients, delivering bespoke trading infrastructure and market access.
layout: provider
modified: '2026-09-29'
name: BlockFills
nav: Providers
network: true
overview: 'BlockFills is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, and Fintech.


  BlockFills'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 5.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blockfills/blockfills-2026-11-03T122001.png
security:
- kind: domain-security
  name: Blockfills Domain Security
  slug: blockfills-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockfills
tags:
- Company
- Cryptocurrency
- Trading
- Fintech
website: https://www.blockfills.com/
---
