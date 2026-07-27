---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 26.9
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The credits API from World Labs — 1 operation(s) for credits.
  name: World Labs credits API
  slug: world-labs-credits-api
- description: The Marble API from World Labs — 8 operation(s) for marble.
  name: World Labs Marble API
  slug: world-labs-marble-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/world-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/world-labs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://worldlabs.ai
created: '2026-07-17'
description: 'World Labs is a company surfaced as a portfolio company of sv-angel and added to the API Evangelist network as a stub for enrichment. Sector: ai. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-labs.png
layout: provider
modified: '2026-07-17'
name: World Labs
nav: Providers
network: true
overview: 'World Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: credits API and Marble API. Tagged areas include Company and Ai.


  World Labs'' developer surface includes authentication and 3 more developer resources.'
random_paper: 63
score:
  band: emerging
  composite: 21.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.1
    developer_ergonomics: 10.9
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: World Labs Authentication
  slug: world-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: World Labs Domain Security
  slug: world-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: World Labs Vulnerability Disclosure
  slug: world-labs-vulnerability-disclosure
  summary_line: disclosure policy published
slug: world-labs
tags:
- Company
- Ai
website: https://worldlabs.ai
---
