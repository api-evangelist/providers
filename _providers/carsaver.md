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
api_count: 1
apis:
- description: CarSaver provides a platform for buying, financing, and trading cars. Documentation is available but no machine‑readable contract was found.
  name: CarSaver API
  slug: carsaver-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carsaver/refs/heads/main/hosts/carsaver-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carsaver-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carsaver.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carsaver/refs/heads/main/security/carsaver-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carsaver-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carsaver.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carsaver.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carsaver.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.carsaver.ai/news
- group: company
  title: ''
  type: About
  url: https://www.carsaver.ai/about-carsaver
coverage:
  checked: '2026-10-07'
  detail: Main site renders via Wix and provides no machine‑readable API spec despite developer‑facing pages.
  evidence:
  - status: 200
    url: https://www.carsaver.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: CarSaver is an online platform that enables users to buy, finance, and trade cars with a lifetime warranty. Leveraging AI-powered search and a wide inventory, it offers tools for vehicle selection, price comparison, and trade‑in valuation. The service includes insurance protection, financing options, and a seamless checkout experience, aiming to simplify car ownership for consumers worldwide.
image: https://dr-theme.carsaver.com/carsaver.com/imgs/marketplace-landing-page/hero/xl/hero.webp
layout: provider
modified: '2026-10-07'
name: CarSaver
nav: Providers
network: true
overview: 'CarSaver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Automotive, Fintech, and Marketplace.


  CarSaver''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carsaver Domain Security
  slug: carsaver-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carsaver
tags:
- Company
- E-Commerce
- Automotive
- Fintech
- Marketplace
- car-buying
website: https://carsaver.com
---
