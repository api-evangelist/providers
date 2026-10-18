---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossover-markets/refs/heads/main/hosts/crossover-markets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crossover-markets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crossover-markets/refs/heads/main/vendors/crossover-markets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crossover-markets-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crossovermarkets.com/terms-of-use/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crossover-markets/refs/heads/main/security/crossover-markets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossover-markets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crossovermarkets.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://crossovermarkets.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Crossover Markets operates CROSSx, an execution‑only digital‑asset electronic communication network (ECN) that provides institutions with ultra‑low‑latency trade execution and custom dark and lit liquidity pools. The platform does not offer custody or brokerage services and connects participants via FIX API or a GUI, trading 24/7 with sub‑20 µs matching engine latency. Fees start at 0.01% and decrease with volume, with commissions waived for certain stablecoin pairs.
image: https://crossovermarkets.com/wp-content/uploads/2023/04/CVR_Master_URLPreview_2023-04-17.jpg
layout: provider
modified: '2026-10-11'
name: Crossover Markets
nav: Providers
network: true
overview: Crossover Markets is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Asset ECN, Institutional Trading, Execution‑Only Exchange, Low‑Latency Matching, and Liquidity Pools.
random_paper: 20
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crossover Markets Domain Security
  slug: crossover-markets-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crossover-markets
tags:
- Digital Asset ECN
- Institutional Trading
- Execution‑Only Exchange
- Low‑Latency Matching
- Liquidity Pools
website: https://crossovermarkets.com/
---
