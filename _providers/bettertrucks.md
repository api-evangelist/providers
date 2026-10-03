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
api_count: 1
apis:
- description: Better Trucks provides a delivery platform API (no public machine‑readable contract found).
  name: Better Trucks API
  slug: better-trucks-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bettertrucks/refs/heads/main/hosts/bettertrucks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bettertrucks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bettertrucks/refs/heads/main/vendors/bettertrucks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bettertrucks-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bettertrucks.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bettertrucks/refs/heads/main/security/bettertrucks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettertrucks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bettertrucks.com
- group: company
  title: ''
  type: Blog
  url: https://www.bettertrucks.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.bettertrucks.com/resource-center
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bettertrucks.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.bettertrucks.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.bettertrucks.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bettertrucks.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bettertrucks.com/terms-conditions/
coverage:
  detail: Docs are served as JavaScript‑rendered pages, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.bettertrucks.com/resource-center
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Better Trucks is a regional, last‑mile delivery platform that provides rapid residential parcel delivery for shippers, carriers, freight operators and drivers. The company leverages technology to minimize stops, improve efficiency, and offer same‑day, next‑day, two‑day, and two‑hour delivery options. Founded in 2019, Better Trucks serves retailers seeking to meet rising consumer expectations for fast, reliable shipping across the United States.
layout: provider
modified: '2026-09-28'
name: Bettertrucks
nav: Providers
network: true
overview: 'Bettertrucks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Delivery, Transportation, Technology, and Company.


  Bettertrucks'' developer surface includes engineering blog, documentation, getting-started guide, support, and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bettertrucks Domain Security
  slug: bettertrucks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bettertrucks
tags:
- Logistics
- Delivery
- Transportation
- Technology
- Company
website: https://www.bettertrucks.com
---
