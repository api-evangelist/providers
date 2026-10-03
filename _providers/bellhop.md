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
- description: API for Bellhop moving service platform, documented via the Help Center.
  name: Bellhop API
  slug: bellhop-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/well-known/bellhop-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bellhop-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/well-known/bellhop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bellhop-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/llms/bellhop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bellhop-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/hosts/bellhop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bellhop-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/vendors/bellhop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bellhop-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.getbellhops.com/about/press/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.getbellhops.com/hc/en-us/sections/13327290453019-Getting-Started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/security/bellhop-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bellhop-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bellhop/refs/heads/main/security/bellhop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bellhop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getbellhops.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.getbellhops.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://help.getbellhops.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.getbellhops.com/hc/en-us/articles/13252993088283-What-size-are-your-trucks
- group: company
  title: ''
  type: Blog
  url: https://www.getbellhops.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getbellhops.com/moving-cost-calculator/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbellhops.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbellhops.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.getbellhops.com/hc/en-us
coverage:
  checked: '2026-09-27'
  detail: Help Center pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 0
    url: https://api.getbellhops.com/openapi.json
  - status: 0
    url: https://api.getbellhops.com/swagger.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Bellhop provides on-demand moving services, allowing customers to book professional movers online with transparent pricing and flexible options. Their platform streamlines the moving experience through a user-friendly website and mobile app, offering local, long-distance, labor-only, and packing services. Bellhop emphasizes customer satisfaction, safety, and reliability, supported by a network of vetted movers across the United States.
image: https://us-east-1.graphassets.com/AFtSkJF2sQZy1WJRTVW2Qz/0yE8QFruQT2aB6HPLTqK
layout: provider
modified: '2026-09-27'
name: Bellhop
nav: Providers
network: true
overview: 'Bellhop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Moving, On-Demand, Logistics, Transportation, and Customer Experience.


  Bellhop''s developer surface includes getting-started guide, documentation, API reference, engineering blog, pricing, support, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bellhop Domain Security
  slug: bellhop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bellhop Vulnerability Disclosure
  slug: bellhop-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bellhop
tags:
- Moving
- On-Demand
- Logistics
- Transportation
- Customer Experience
- Company
website: https://www.getbellhops.com/
---
