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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/finn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/finn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.finn.com/
- group: company
  title: ''
  type: Blog
  url: https://www.finn.com/en-DE/blog
- group: company
  title: ''
  type: About
  url: https://www.finn.com/de-DE/about-us
- group: operate
  title: ''
  type: Support
  url: https://support.finn.com/hc/de-de
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.finn.com/de-DE/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.finn.com/de-DE/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finn-auto
- group: agent
  title: ''
  type: WellKnown
  url: well-known/finn-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/finn-security.txt
created: '2026-07-17'
description: FINN (finn.com) is a Munich-based consumer car-subscription service that lets individuals and businesses lease a car on a flexible monthly subscription, with insurance, maintenance, registration, taxes, and roadside assistance bundled into one all-inclusive price. Subscribers pick from more than twenty vehicle brands on terms from six to twenty-four months, and the company also runs a fleet/business offering. Backed by HV Capital, FINN operates in Germany, the United States, and other European markets. FINN is a consumer, direct-to-customer business with no public developer API or partner API program surfaced at this time; this profile captures its public web, security, and legal surface for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finn.png
layout: provider
modified: '2026-07-19'
name: Finn
nav: Providers
network: true
overview: 'Finn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Automotive, Car Subscription, and Mobility.


  Finn''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 88
score:
  band: emerging
  composite: 13.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finn/refs/heads/main/screenshots/finn-2026-07-25T214536.png
security:
- kind: domain-security
  name: Finn Domain Security
  slug: finn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Finn Vulnerability Disclosure
  slug: finn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: finn
tags:
- Company
- Consumer
- Automotive
- Car Subscription
- Mobility
- Leasing
- Fleet
website: https://www.finn.com/
---
