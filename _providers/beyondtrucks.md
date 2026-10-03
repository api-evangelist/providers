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
  href: https://raw.githubusercontent.com/api-evangelist/beyondtrucks/refs/heads/main/hosts/beyondtrucks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyondtrucks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beyondtrucks/refs/heads/main/vendors/beyondtrucks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beyondtrucks-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.beyondtrucks.com/press/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beyondtrucks/refs/heads/main/security/beyondtrucks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyondtrucks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beyondtrucks.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://go.beyondtrucks.com
- group: docs
  title: ''
  type: Documentation
  url: https://go.beyondtrucks.com
- group: operate
  title: ''
  type: Support
  url: https://www.beyondtrucks.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.beyondtrucks.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beyondtrucks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beyondtrucks.com/privacy
coverage:
  checked: '2026-09-28'
  detail: Developer portal at https://go.beyondtrucks.com returns HTML shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://go.beyondtrucks.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BeyondTrucks provides AI‑powered transportation management software for mission‑critical fleets. Their platform automates order ingestion, dispatch planning, finance, and analytics, leveraging generative AI to create dynamic rate logic and real‑time optimization. Serving industries from petroleum to food‑and‑beverage, BeyondTrucks helps fleets reduce manual errors, improve utilization, and accelerate order processing with intelligent automation and predictive notifications.
image: https://framerusercontent.com/assets/vntdfcQnIVZRLCmoBy5AwddI.png
layout: provider
modified: '2026-09-28'
name: BeyondTrucks
nav: Providers
network: true
overview: 'BeyondTrucks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Artificial Intelligence, Logistics, and Fleet Management.


  BeyondTrucks'' developer surface includes documentation, support, engineering blog, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.0
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
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beyondtrucks Domain Security
  slug: beyondtrucks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beyondtrucks
tags:
- Company
- Transportation
- Artificial Intelligence
- Logistics
- Fleet Management
website: https://www.beyondtrucks.com
---
