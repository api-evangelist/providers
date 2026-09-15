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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-14'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agraga/refs/heads/main/security/agraga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agraga-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agraga/refs/heads/main/llms/agraga-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agraga-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agraga/refs/heads/main/plans/agraga-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agraga-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agraga/refs/heads/main/rate-limits/agraga-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agraga-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.agraga.com/
- group: company
  title: ''
  type: About
  url: https://www.agraga.com/about
- group: other
  title: ''
  type: Services
  url: https://www.agraga.com/products
- group: operate
  title: ''
  type: Support
  url: https://www.agraga.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://booking.agraga.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agraga.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agraga.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agraga
coverage:
  checked: '2026-09-12'
  detail: 'Agraga sells freight, not software: its marketing site is a seven-route React SPA whose bundle never once contains the string "API", there is no GitHub organization (api.github.com/orgs/agraga returns 404) and no package in any registry, and the only API hosts that exist - api.agraga.com and pricing.agraga.com, both found in Agraga''s own booking-app bundle - are private backends that answer every anonymous path, well-known namespace included, with 401 {"error":"Invalid Token"}.'
  evidence:
  - status: 401
    url: https://api.agraga.com/openapi.json
  - status: 401
    url: https://api.agraga.com/.well-known/agent-card.json
  - status: 401
    url: https://pricing.agraga.com/
  - status: 404
    url: https://api.github.com/orgs/agraga
  - status: 404
    url: https://notify.agraga.com/.well-known/api-catalog
  - status: 401
    url: https://api.agraga.com/api-docs
  - status: 404
    url: https://files.agraga.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Agraga (operated by Virya Logistics Technologies Private Limited) is a Chennai, India based digital cross-border logistics platform founded in 2021 by Anoop Raghavan and Venkatesh Narayanaswamy. It positions itself as a single operator for every leg of a shipment, bringing ocean freight, air freight, domestic transport, customs broking, warehousing, e-commerce fulfilment and embedded trade finance onto one booking and tracking platform aimed at underserved Indian MSME exporters and importers. It reports 700+ customers and 1,000+ vendors across 40-plus markets, and raised INR 100 crore in a pre-Series B round led by Bajaj Finserv with IvyCap Ventures. As of this profile Agraga publishes no public developer program, API documentation, SDK or machine-readable API contract; its platform backends are private and answer every anonymous request with an authentication error.
image: https://www.agraga.com/assets/agraga-logo-BtkIvqFd.png
layout: provider
modified: '2026-09-12'
name: Agraga
nav: Providers
network: true
overview: 'Agraga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight, Freight Forwarding, Supply Chain, and Shipping.


  Agraga''s developer surface includes support, signup flow, and 10 more developer resources.'
plans:
- name: Agraga Plans Pricing
  plan_count: 0
  slug: agraga-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Agraga Rate Limits
  slug: agraga-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 5.0
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agraga Domain Security
  slug: agraga-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agraga
tags:
- Logistics
- Freight
- Freight Forwarding
- Supply Chain
- Shipping
- Customs
- Warehousing
- Embedded Finance
- Trade
- India
- Company
website: https://www.agraga.com/
---
