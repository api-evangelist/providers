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
- description: GraphQL API for Anyplace services
  name: Anyplace GraphQL API
  slug: anyplace-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anyplace/refs/heads/main/llms/anyplace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anyplace-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anyplace.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.anyplace.com/anyplace-support-knowledge
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anyplace.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.anyplace.com/press
- group: company
  title: ''
  type: Blog
  url: https://blog.anyplace.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.anyplace.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anyplace/refs/heads/main/hosts/anyplace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anyplace-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anyplace/refs/heads/main/vendors/anyplace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anyplace-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anyplace/refs/heads/main/security/anyplace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anyplace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anyplace.com
coverage:
  checked: 2026-09-25
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://dev.anyplace.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Anyplace provides flexible‑term, fully furnished apartments designed for remote workers, corporate teams, and digital nomads. Founded in 2017, the platform offers move‑in ready rentals with dedicated workspaces, high‑speed internet, utilities, and all‑inclusive amenities. Users can book month‑to‑month leases in major cities worldwide, enjoying premium furnishings, private high‑speed internet, and 24/7 support. The service simplifies housing by handling utilities, internet, and furniture, allowing professionals to focus on work and travel. Anyplace also offers corporate housing solutions, partner networks for property owners, and a seamless online booking experience with transparent pricing and flexible terms.
image: https://www.anyplace.com/home/thumbnail.webp
layout: provider
modified: '2026-09-25'
name: Anyplace
nav: Providers
network: true
overview: 'Anyplace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Housing, Remote Work, FlexibleLease, and Apartments.


  Anyplace''s developer surface includes support, engineering blog, documentation, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.0
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anyplace Domain Security
  slug: anyplace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anyplace
tags:
- Company
- Housing
- Remote Work
- FlexibleLease
- Apartments
website: https://www.anyplace.com
---
