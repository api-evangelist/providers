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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://ro.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ro.co/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ro.co/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://ro.co/contact-us/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ro-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ro-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ro-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/ro
created: '2026-07-17'
description: Ro (ro.co) is a direct-to-consumer telehealth company that connects patients with US-licensed healthcare providers entirely online, offering prescription treatment, provider visits, and pharmacy fulfillment across categories including men's and women's health, weight management (Ro Body), dermatology (Ro Derm), hair loss, fertility (Ro Fertility), and sexual health. Ro deliberately operates a "Zero-API" vertically integrated online-visit experience and does not publish a public developer API, SDKs, or a developer portal; its only public machine-readable surface is a security posture (RFC 9116 security.txt and a HackerOne vulnerability disclosure program). Ro is backed by Canaan Partners, General Catalyst, and Initialized Capital.
image: https://ro.co/rocostatic/images/og-image.jpg
layout: provider
modified: '2026-07-21'
name: Ro
nav: Providers
network: true
overview: 'Ro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telehealth, Healthcare, Digital Health, and Pharmacy.


  Ro''s developer surface includes support and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Ro Domain Security
  slug: ro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ro Vulnerability Disclosure
  slug: ro-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ro
tags:
- Company
- Telehealth
- Healthcare
- Digital Health
- Pharmacy
- Direct to Consumer
- Weight Management
- Fertility
website: https://ro.co
---
