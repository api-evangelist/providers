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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
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
random_paper: 49
score:
  band: emerging
  composite: 17.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.4
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 43.5
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Financial Services
- Consumer
- Germany
- Mobile App
website: https://www.clark.de
---
