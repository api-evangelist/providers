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
  type: DomainSecurity
  url: security/dusk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dusk.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dusk.app
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dusk-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dusk-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dusk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.notion.so/Responsible-Disclosure-Policy-5f18bb6b86804eaf989c006131778b9c
created: '2026-07-17'
description: Dusk (dusk.app), tagline "Make the night," is a consumer mobile app backed by 500 Global. It publishes product documentation on a Notion-hosted docs site (docs.dusk.app) and maintains an RFC 9116 security.txt pointing to a public Responsible Disclosure Policy. Dusk was surfaced as a 500 Global portfolio company and added to the API Evangelist network; it exposes no public developer API, OpenAPI, or SDK surface at this time, so this profile captures its verifiable web, documentation, and security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dusk.png
layout: provider
modified: '2026-07-18'
name: Dusk
nav: Providers
network: true
overview: 'Dusk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Mobile App, Social, and Nightlife.


  Dusk''s developer surface includes documentation and 6 more developer resources.'
random_paper: 29
score:
  band: minimal
  composite: 9.2
  delta: -0.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dusk/refs/heads/main/screenshots/dusk-2026-07-25T212517.png
security:
- kind: domain-security
  name: Dusk Domain Security
  slug: dusk-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dusk Vulnerability Disclosure
  slug: dusk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dusk
tags:
- Company
- Consumer
- Mobile App
- Social
- Nightlife
website: https://dusk.app
---
