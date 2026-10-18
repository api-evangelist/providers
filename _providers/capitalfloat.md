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
  href: https://raw.githubusercontent.com/api-evangelist/capitalfloat/refs/heads/main/hosts/capitalfloat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capitalfloat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capitalfloat/refs/heads/main/vendors/capitalfloat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capitalfloat-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.axio.co.in/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capitalfloat/refs/heads/main/security/capitalfloat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capitalfloat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axio.co.in
- group: company
  title: ''
  type: Blog
  url: https://www.axio.co.in/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axio.co.in/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axio.co.in/privacy-policy
coverage:
  checked: '2026-10-07'
  detail: API reference page returns 404, suggesting access requires partner login.
  evidence:
  - status: 404
    url: https://www.axio.co.in/api
  reason: partner-login
  state: gated
created: '2026-10-06'
description: Capitalfloat, now operating as Axio, is an Indian consumer finance platform offering pay‑later, credit, and personal finance management solutions. Founded to provide flexible financing for online shoppers and small businesses, Axio has expanded into a unified financial services ecosystem, serving millions of customers across India with digital loans, budgeting tools, and merchant partnerships. The company focuses on transparent, technology‑driven credit products and aims to make credit worthy for all.
image: https://cdn.prod.website-files.com/67efed6ce5cf32249dadb268/6821d3ee49d9bd2e8a7dd446_1.png
layout: provider
modified: '2026-10-06'
name: Capitalfloat
nav: Providers
network: true
overview: 'Capitalfloat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Fintech, ConsumerFinance, and India.


  Capitalfloat''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capitalfloat Domain Security
  slug: capitalfloat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capitalfloat
tags:
- Company
- Finance
- Fintech
- ConsumerFinance
- India
- Payments
website: https://www.axio.co.in
---
