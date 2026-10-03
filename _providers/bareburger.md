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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bareburger/refs/heads/main/hosts/bareburger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bareburger-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bareburger/refs/heads/main/vendors/bareburger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bareburger-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bareburger/refs/heads/main/security/bareburger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bareburger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bareburger.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bareburger
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Bareburger is a fast‑casual restaurant chain offering a variety of globally inspired, all‑natural burgers, salads, and sides. Founded in 2002, the brand emphasizes fresh, responsibly sourced ingredients, customizable menu options, and a commitment to sustainability. The company operates locations across the United States and internationally, providing dine‑in, takeout, and delivery services through its website and partner platforms. This profile captures Bareburger’s public-facing presence and prepares for further API documentation enrichment.
image: https://bareburger.com/wp-content/uploads/2024/02/Organic-Spicy-Sustainable-New-York-Bareburger-copy.webp
layout: provider
modified: '2026-09-27'
name: Bareburger
nav: Providers
network: true
overview: Bareburger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Fast Casual, Food, and Sustainability.
random_paper: 1
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bareburger Domain Security
  slug: bareburger-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bareburger
tags:
- Company
- Restaurant
- Fast Casual
- Food
- Sustainability
website: https://bareburger.com
---
