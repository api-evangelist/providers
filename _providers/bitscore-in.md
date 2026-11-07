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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.bitscore.in/responsible-disclosure
- group: agent
  href: https://artifacts.apis.io/bitscore-in/llms/bitscore-in-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitscore-in-llms.txt
- group: auth
  href: https://artifacts.apis.io/bitscore-in/well-known/bitscore-in-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitscore-in-security.txt
- group: auth
  href: https://artifacts.apis.io/bitscore-in/well-known/bitscore-in-bitscore-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitscore-in-bitscore-security.txt
- group: agent
  href: https://artifacts.apis.io/bitscore-in/well-known/bitscore-in-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitscore-in-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitscore-in/hosts/bitscore-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitscore-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitscore-in/vendors/bitscore-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitscore-in-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitscore.in/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bitscore.in/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.bitscore.in/blog
- group: agent
  title: ''
  type: mcp
  url: https://www.bitscore.in/mcp
- group: auth
  href: https://artifacts.apis.io/bitscore-in/security/bitscore-in-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitscore-in-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bitscore-in/security/bitscore-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitscore-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitscore.in/
- group: agent
  title: ''
  type: mcp
  url: https://www.bitscore.in/mcp
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://www.bitscore.in/mcp
  - status: 200
    url: https://bitscore.in/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: BitScore Cybertech LLP is an authorised Bitsight partner delivering cyber risk intelligence, security ratings (250–900) and third-party risk management to enterprises worldwide. It provides objective ratings, free reports, and comprehensive risk insights for public and private entities, helping organizations assess and improve their security posture.
image: https://www.bitscore.in/assets/bitscore-og.png
layout: provider
modified: '2026-11-02'
name: BitScore
nav: Providers
network: true
overview: 'BitScore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Risk Management, Ratings, Enterprise, and India.


  BitScore''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitscore In Domain Security
  slug: bitscore-in-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitscore In Vulnerability Disclosure
  slug: bitscore-in-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bitscore-in
tags:
- Cybersecurity
- Risk Management
- Ratings
- Enterprise
- India
website: https://bitscore.in/
---
