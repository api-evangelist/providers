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
- group: other
  href: https://artifacts.apis.io/rugslayer-com/hosts/rugslayer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rugslayer-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/rugslayer-com/security/rugslayer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rugslayer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rugslayer.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rugslayer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rugslayer.com/privacy
coverage:
  checked: '2026-10-29'
  detail: The service was shut down on October 29, 2026, and all API endpoints now return HTTP 410 Gone.
  evidence:
  - status: 410
    url: https://rugslayer.com/openapi.json
  reason: defunct
  state: none
created: '2026-10-29'
description: RugSlayer was a Solana token risk scanning service operated by MeltingPixels LLC. It provided developers and investors with tools to detect malicious token contracts, rug pulls, and other on‑chain threats on the Solana blockchain. The platform offered an API for automated risk assessment, a web dashboard, and documentation for integration. RugSlayer announced its shutdown on October 29, 2026, and the website now displays a closure notice. Although the service is no longer active, the company’s historical focus was on enhancing security and transparency in the Solana ecosystem.
image: https://rugslayer.com/_tomb/icon.svg
layout: provider
modified: '2026-10-29'
name: rugslayer-com
nav: Providers
network: true
overview: rugslayer-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solana, Security, Cryptocurrency, and Risk-Scanner.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rugslayer-com/rugslayer-com-2026-11-03T142521.png
security:
- kind: domain-security
  name: Rugslayer Com Domain Security
  slug: rugslayer-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rugslayer-com
tags:
- Company
- Solana
- Security
- Cryptocurrency
- Risk-Scanner
website: https://rugslayer.com/
---
