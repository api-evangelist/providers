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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The AI API from Zocomputer — 3 operation(s) for ai.
  name: Zocomputer AI API
  slug: zocomputer-ai-api
- description: The Personas API from Zocomputer — 1 operation(s) for personas.
  name: Zocomputer Personas API
  slug: zocomputer-personas-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zocomputer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zocomputer-domain-security.yml
created: '2026-07-17'
description: Zocomputer is a company surfaced as a portfolio company of lightspeed-venture-partners and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zocomputer.png
layout: provider
modified: '2026-07-17'
name: Zocomputer
nav: Providers
network: true
overview: 'Zocomputer publishes 2 APIs on the [APIs.io](https://apis.io/) network: AI API and Personas API. Tagged areas include Company.'
random_paper: 24
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.1
    developer_ergonomics: 0.0
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Zocomputer Domain Security
  slug: zocomputer-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zocomputer Vulnerability Disclosure
  slug: zocomputer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zocomputer
tags:
- Company
---
