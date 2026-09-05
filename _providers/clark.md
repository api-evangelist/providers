---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.clark.de/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clark.de
- group: company
  title: ''
  type: About
  url: https://www.clark.de/ueber-uns
- group: company
  title: ''
  type: Blog
  url: https://www.clark.de/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clark.de/datenschutz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clark.de/agb
- group: commercial
  title: ''
  type: Legal
  url: https://www.clark.de/impressum
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/clark-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clark-well-known.yml
created: '2026-07-17'
description: Clark ("Dein Versicherungsmanager") is a Germany-based digital insurance manager that lets consumers view, compare, optimize, and manage all of their insurance policies in one mobile app and web platform. Founded in Frankfurt in 2015, Clark pairs a licensed insurance brokerage with automated tariff comparison across more than 180 insurance providers and free expert consultation, covering health, liability, property, life, mobility, and retirement products. The company operates across Germany, Switzerland, France, and the UK, serves over 700,000 customers, and is backed by venture investors including Lightspeed Venture Partners. Clark exposes no public developer API or developer portal; it is a consumer-facing insurtech rather than an API producer.
image: https://www.clark.de/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Clark
nav: Providers
network: true
overview: 'Clark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Insurance Comparison, and Personal Finance.


  Clark''s developer surface includes engineering blog, legal docs, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Clark Domain Security
  slug: clark-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clark Vulnerability Disclosure
  slug: clark-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clark
tags:
- Company
- Insurance
- Insurtech
- Insurance Comparison
- Personal Finance
- Financial-Services
- Consumer
- Germany
- Mobile App
website: https://www.clark.de
---
