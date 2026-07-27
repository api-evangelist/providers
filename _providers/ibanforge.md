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
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: IBAN validation and BIC/SWIFT lookup for 75+ countries with 121K+ bank entries
  name: IBANforge
  slug: ibanforge
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibanforge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibanforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.ibanforge.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://ibanforge.com/en/blog
created: '2026-05-28'
description: IBAN validation and BIC/SWIFT lookup for 75+ countries with 121K+ bank entries
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibanforge.png
layout: provider
modified: '2026-05-28'
name: IBANforge
nav: Providers
network: true
overview: 'IBANforge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.


  IBANforge''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 57
score:
  band: minimal
  composite: 7.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibanforge/refs/heads/main/screenshots/ibanforge-2026-06-20T183111.png
security:
- kind: domain-security
  name: Ibanforge Domain Security
  slug: ibanforge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ibanforge Vulnerability Disclosure
  slug: ibanforge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ibanforge
tags:
- Finance
- Public APIs
website: https://api.ibanforge.com
---
