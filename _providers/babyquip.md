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
  href: https://raw.githubusercontent.com/api-evangelist/babyquip/refs/heads/main/hosts/babyquip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/babyquip-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/babyquip/refs/heads/main/vendors/babyquip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/babyquip-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.babyquip.com/press
- group: start
  title: ''
  type: Login
  url: https://www.babyquip.com/customers/login
- group: other
  title: ''
  type: Leadership
  url: https://www.babyquip.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/babyquip/refs/heads/main/security/babyquip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babyquip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.babyquip.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.babyquip.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://www.babyquip.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.babyquip.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.babyquip.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.babyquip.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.babyquip.com/privacypolicy
coverage:
  checked: '2026-09-27'
  detail: API reference page returns 404 and no machine‑readable spec is available.
  evidence:
  - status: 404
    url: https://www.babyquip.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: 'BabyQuip is the #1 baby equipment rental service and marketplace, offering thousands of baby gear items in over 5,000+ cities across the US, Canada, Mexico, Caribbean, Australia & New Zealand. Founded in 2016 by traveling parents, it provides clean, safe, insured rentals of cribs, strollers, car seats, toys, and more, improving family travel experiences. Over 500,000 reservations have been completed, with 62% of parents saying renting saved their vacation.'
image: https://d28w2s5u3j4b6n.cloudfront.net/img/BQ_PrimaryCentered_RGB.jpg
layout: provider
modified: '2026-09-27'
name: BabyQuip
nav: Providers
network: true
overview: 'BabyQuip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include BabyGear, Rentals, Marketplace, Travel, and Family.


  BabyQuip''s developer surface includes documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Babyquip Domain Security
  slug: babyquip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: babyquip
tags:
- BabyGear
- Rentals
- Marketplace
- Travel
- Family
website: https://www.babyquip.com
---
