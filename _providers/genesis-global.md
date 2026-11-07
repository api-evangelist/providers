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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/genesis-global/llms/genesis-global-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/genesis-global-llms.txt
- group: other
  href: https://artifacts.apis.io/genesis-global/hosts/genesis-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/genesis-global-hosts.yml
- group: other
  href: https://artifacts.apis.io/genesis-global/vendors/genesis-global-vendors.yml
  title: ''
  type: Vendors
  url: vendors/genesis-global-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genesis.global/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.genesis.global/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://genesis.global/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://genesis.global/about/newsroom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://genesis.global/platform/developer-portal/
- group: company
  title: ''
  type: Blog
  url: https://genesis.global/resources/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genesis.global/
- group: auth
  href: https://artifacts.apis.io/genesis-global/security/genesis-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genesis-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://genesis.global/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://support.genesis.global/mcp
  - status: 200
    url: https://genesis.global/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Genesis Global provides a platform that enables financial institutions to build high‑performance, resilient and secure applications for capital‑markets workflows. It combines preferred AI with reusable components to support single‑dealer platforms, institutional middle‑office, sales‑trader, primary‑markets trading, order and trade management, electronic trading venues and reporting/reconciliation. The platform offers developer resources, a launchpad and certification through its Genesis Academy.
image: https://genesis.global/wp-content/uploads/2025/05/Homepage.png
layout: provider
modified: '2026-10-25'
name: Genesis
nav: Providers
network: true
overview: 'Genesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Architecture, Capital Markets, Financial Institutions, Developer Portal, and Trading Platforms.


  Genesis'' developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/genesis-global/genesis-global-2026-11-03T132554.png
security:
- kind: domain-security
  name: Genesis Global Domain Security
  slug: genesis-global-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: genesis-global
tags:
- AI Architecture
- Capital Markets
- Financial Institutions
- Developer Portal
- Trading Platforms
- Middle Office
- Electronic Trading
website: https://genesis.global/
---
