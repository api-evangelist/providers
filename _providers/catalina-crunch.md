---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: GraphQL API providing access to Catalina Crunch e‑commerce data such as products, collections, and checkout.
  name: Catalina Crunch GraphQL API
  slug: catalina-crunch-graphql-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/well-known/catalina-crunch-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/catalina-crunch-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/llms/catalina-crunch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catalina-crunch-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/well-known/catalina-crunch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/catalina-crunch-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/hosts/catalina-crunch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catalina-crunch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/vendors/catalina-crunch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catalina-crunch-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://us.catalinacrunch.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://us.catalinacrunch.com/account/login
- group: docs
  title: ''
  type: Documentation
  url: https://us.catalinacrunch.com/pages/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.catalinacrunch.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.catalinacrunch.com/pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://us.catalinacrunch.com/pages/contact
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/security/catalina-crunch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/catalina-crunch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/catalina-crunch/refs/heads/main/security/catalina-crunch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalina-crunch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://us.catalinacrunch.com/
created: '2026-10-07'
description: Catalina Crunch creates high‑protein, low‑sugar snacks and cereals, founded by a Type 1 diabetic to fill a market gap for nutritious, low‑sugar options. The brand now offers a broad portfolio of snacks, cereals, granola, and chocolate bars, emphasizing protein and fiber while minimizing sugar, and provides online shopping, subscriptions, and retail locations across the US.
image: http://us.catalinacrunch.com/cdn/shop/files/new-logo_800x_33d4ec95-65a9-4007-af0b-23015fa35f11.png?v=1742205920&width=1200
layout: provider
modified: '2026-10-07'
name: Catalina Crunch
nav: Providers
network: true
overview: 'Catalina Crunch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Snacks, Food, Health, and E-Commerce.


  Catalina Crunch''s developer surface includes documentation, support, and 13 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catalina Crunch Domain Security
  slug: catalina-crunch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Catalina Crunch Vulnerability Disclosure
  slug: catalina-crunch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: catalina-crunch
tags:
- Company
- Snacks
- Food
- Health
- E-Commerce
- Nutrition
website: https://us.catalinacrunch.com/
---
