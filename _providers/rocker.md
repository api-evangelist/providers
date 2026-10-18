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
  href: https://raw.githubusercontent.com/api-evangelist/rocker/refs/heads/main/hosts/rocker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rocker-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rocker/refs/heads/main/security/rocker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rocker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rocker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rocker.com/portal/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rocker.com/portal/
- group: start
  title: ''
  type: GettingStarted
  url: https://rocker.com/pay/
- group: operate
  title: ''
  type: Support
  url: https://rocker.com/hjalp/
- group: company
  title: ''
  type: Blog
  url: https://rocker.com/var-story/
- group: commercial
  title: ''
  type: Pricing
  url: https://rocker.com/lan/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rocker.com/allmanna-villkor/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rocker.com/personuppgiftspolicy/
coverage:
  checked: '2026-10-15'
  detail: No machine‑readable API specification was found on rocker.com or its subdomains despite probing common spec locations.
  evidence:
  - status: 200
    url: https://rocker.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Rocker is a Swedish fintech company offering a peer‑to‑peer marketplace for buying and selling second‑hand goods, backed by a robust payment solution. The platform provides users with secure transactions, real‑time updates, and integrated banking features such as savings accounts and personal loans. Rocker aims to improve financial health by simplifying payments and offering tools for budgeting and financial planning, serving over 400 000 users across Scandinavia.
image: http://rocker.com/images/og-image.jpg
layout: provider
modified: '2026-10-15'
name: Rocker
nav: Providers
network: true
overview: 'Rocker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Marketplace, Peer-to-Peer, Payments, and Sweden.


  Rocker''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
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
  name: Rocker Domain Security
  slug: rocker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rocker
tags:
- Fintech
- Marketplace
- Peer-to-Peer
- Payments
- Sweden
website: https://rocker.com/
---
