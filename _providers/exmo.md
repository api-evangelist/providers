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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Cryptocurrencies exchange based in UK
  name: EXMO
  slug: exmo
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exmo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://documenter.getpostman.com/view/10287440/SzYXWKPi
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://exmo.com/blog/en/news/
created: '2026-05-28'
description: Cryptocurrencies exchange based in UK
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exmo.png
layout: provider
modified: '2026-05-28'
name: EXMO
nav: Providers
network: true
overview: 'EXMO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.


  EXMO''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.1
  delta: 1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exmo/refs/heads/main/screenshots/exmo-2026-06-20T180931.png
security:
- kind: domain-security
  name: Exmo Domain Security
  slug: exmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exmo Vulnerability Disclosure
  slug: exmo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: exmo
tags:
- Cryptocurrency
- Public APIs
website: https://documenter.getpostman.com/view/10287440/SzYXWKPi
---
