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
api_count: 1
apis:
- description: API endpoints for Betidigitalservices platform
  name: Betidigitalservices API
  slug: betidigitalservices-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/betidigitalservices/refs/heads/main/llms/betidigitalservices-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betidigitalservices-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betidigitalservices/refs/heads/main/hosts/betidigitalservices-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betidigitalservices-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://betadigital.in/partners/registered-partner-of-amazon/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betadigital.in/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betidigitalservices/refs/heads/main/security/betidigitalservices-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betidigitalservices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betadigital.in
coverage:
  checked: '2026-09-28'
  detail: OpenAPI JSON not found at https://api.betadigital.in/openapi.json (404)
  evidence:
  - status: 404
    url: https://api.betadigital.in/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Beta Digital Services is a technology and digital marketing firm based in India, offering a wide range of services including marketplace management, e‑commerce marketing, social media advertising, web development, and AI‑powered digital solutions. Founded in 2018, the company serves brands across major Indian marketplaces such as Amazon, Flipkart, and Myntra, helping them grow through product onboarding, catalog management, advertising, and analytics. The team combines strategy, creativity, and technology to deliver scalable solutions for businesses seeking to expand their online presence.
image: https://betadigital.in/wp-content/uploads/2026/03/cropped-beta_logo_4__1_-removebg-preview.png
layout: provider
modified: '2026-09-28'
name: Betidigitalservices
nav: Providers
network: true
overview: 'Betidigitalservices publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Marketing, E-Commerce, Marketplace Services, and Web Development.


  Betidigitalservices'' developer surface includes signup flow and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betidigitalservices Domain Security
  slug: betidigitalservices-domain-security
  summary_line: TLSv1.3 · DMARC
slug: betidigitalservices
tags:
- Company
- Digital Marketing
- E-Commerce
- Marketplace Services
- Web Development
- AI Solutions
website: https://betadigital.in
---
