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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/corgi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://corgi.insure/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corgi-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corgi-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/corgi-security.txt
- group: company
  title: ''
  type: Website
  url: https://corgi.insure/
- group: company
  title: ''
  type: Blog
  url: https://corgi.insure/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.corgi.insure/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.corgi.insure
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corgi.insure/docs/Corgi%20Terms%20of%20Service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corgi.insure/docs/Corgi%20Privacy%20Policy.pdf
created: '2026-07-17'
description: Corgi is an AI-native, full-stack business insurance platform for startups, offering modular coverage (Commercial General Liability, Directors & Officers, Tech Errors & Omissions, Cyber, EPLI, and fiduciary) quoted in minutes. Founded in 2024 and based in San Francisco, Corgi is a licensed insurance carrier rather than a broker, underwriting and issuing policies directly with pricing tailored to a startup's stage (pre-seed, Series A, growth). Backed by Kindred Ventures and TCV, the company was reported as an AI insurance unicorn in 2026. This API Evangelist profile was seeded from Kindred Ventures' portfolio; Corgi does not currently publish a public API or developer portal.
image: https://www.corgi.insure/api/og?title=Startup+Insurance%2C+Quoted+in+Minutes&type=page
layout: provider
modified: '2026-07-18'
name: Corgi
nav: Providers
network: true
overview: 'Corgi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Business Insurance, and Startups.


  Corgi''s developer surface includes engineering blog, signup flow, and 9 more developer resources.'
random_paper: 40
score:
  band: emerging
  composite: 17.1
  delta: -2.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corgi/refs/heads/main/screenshots/corgi-2026-07-25T210433.png
security:
- kind: domain-security
  name: Corgi Domain Security
  slug: corgi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Corgi Vulnerability Disclosure
  slug: corgi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: corgi
tags:
- Company
- Insurance
- Insurtech
- Business Insurance
- Startups
- Cyber Insurance
- Artificial Intelligence
- Financial Services
website: https://corgi.insure/
---
