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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brickschain/refs/heads/main/hosts/brickschain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brickschain-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brickschain.tech/Terms-and-Condition.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brickschain.tech/Privacy-Policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brickschain/refs/heads/main/security/brickschain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brickschain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brickschain.tech
coverage:
  checked: '2026-10-03'
  detail: OpenAPI endpoint returned HTML page instead of a machine‑readable spec, indicating the docs are rendered via JavaScript.
  evidence:
  - status: 200
    url: https://www.brickschain.tech/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Brickschain provides a blockchain-based fractional ownership platform for real estate in India, enabling investors to buy and trade shares of property assets with regulatory backing. The platform offers a transparent, secure ledger for property transactions, targeting high returns and democratizing access to real estate investments.
layout: provider
modified: '2026-10-03'
name: Brickschain
nav: Providers
network: true
overview: Brickschain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Blockchain, Fractional Ownership, Investment, and India.
random_paper: 9
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brickschain Domain Security
  slug: brickschain-domain-security
  summary_line: TLSv1.3
slug: brickschain
tags:
- Real Estate
- Blockchain
- Fractional Ownership
- Investment
- India
website: https://www.brickschain.tech
---
