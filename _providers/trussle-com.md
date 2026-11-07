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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Trussle provides a GraphQL API at https://api.trussle.com/v1/graphql (authentication required).
  name: Trussle GraphQL API
  slug: trussle-graphql-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/trussle-com/hosts/trussle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trussle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trussle-com/vendors/trussle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trussle-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/trussle-com/packages/trussle-com-packages.yml
  title: ''
  type: SDKs
  url: packages/trussle-com-packages.yml
- group: build
  href: https://artifacts.apis.io/trussle-com/packages/trussle-com-packages.yml
  title: ''
  type: Packages
  url: packages/trussle-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://better.co.uk/terms
- group: start
  title: ''
  type: SignUp
  url: https://better.co.uk/account/signup?application=eyJwcm9wZXJ0eURldGFpbHMiOnsib2ZmZXJBY2NlcHRlZCI6dHJ1ZX0sInB1cmNoYXNpbmdQdXJwb3NlIjoiUFVSQ0hBU0UiLCJwdXJjaGFzaW5nSW50ZW50Ijp7Im9mZmVyTWFkZSI6dHJ1ZSwib2ZmZXJTdGF0dXMiOiJBQ0NFUFRFRCJ9fQ==
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://better.co.uk/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://better.co.uk/press
- group: start
  title: ''
  type: GettingStarted
  url: https://better.co.uk/get-started/remaining-term
- group: company
  title: ''
  type: Website
  url: http://trussle.com
- group: auth
  href: https://artifacts.apis.io/trussle-com/security/trussle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trussle-com-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: The GraphQL endpoint https://api.trussle.com/v1/graphql returns 401 Unauthorized, indicating authentication is required.
  evidence:
  - status: 401
    url: https://api.trussle.com/v1/graphql
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Trussle was a UK‑based digital mortgage broker that helped homeowners find and manage mortgage products online. Founded in 2015, Trussle offered a streamlined, technology‑driven approach to mortgage advice and application. The company was later acquired and rebranded by Better.com, after which the original trussle.com domain redirects to Better.com’s UK site. While the original brand is no longer active, its legacy persists in the mortgage‑tech ecosystem, and this entry records the historic company information for reference.
image: https://better.co.uk/images/stacked-social.png
layout: provider
modified: '2026-10-28'
name: Trussle
nav: Providers
network: true
overview: 'Trussle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mortgage, Fintech, United Kingdom, Brokerage, and Digital.


  Trussle''s developer surface includes signup flow, getting-started guide, and 9 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 67.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trussle-com/trussle-com-2026-11-03T145116.png
security:
- kind: domain-security
  name: Trussle Com Domain Security
  slug: trussle-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: trussle-com
tags:
- Mortgage
- Fintech
- United Kingdom
- Brokerage
- Digital
website: http://trussle.com
---
