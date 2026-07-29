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
  url: security/distributional-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/distributional-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/distributional-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distributional.com
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/distributional-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/distributional-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/distributional-llms.txt
created: '2026-07-17'
description: 'Distributional is an a16z-backed company (security contact Scott Clark) tracked in the API Evangelist network. As of July 2026 distributional.com serves a pre-launch holding page ("Something new is coming") with no public API, backend, or authentication surface. The site does publish machine-readable discovery surfaces, however: an RFC 9116 security.txt at /.well-known/security.txt and an llms.txt with plain-markdown page twins for direct LLM ingestion. This profile captures those published surfaces and probed domain-security posture, and will be enriched further once the company launches a developer or API offering.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/distributional.png
layout: provider
modified: '2026-07-18'
name: Distributional
nav: Providers
network: true
overview: Distributional is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, AI Testing, and Reliability.
random_paper: 59
score:
  band: minimal
  composite: 8.2
  delta: 0.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/distributional/refs/heads/main/screenshots/distributional-2026-07-25T212114.png
security:
- kind: domain-security
  name: Distributional Domain Security
  slug: distributional-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Distributional Vulnerability Disclosure
  slug: distributional-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: distributional
tags:
- Company
- Artificial Intelligence
- Machine Learning
- AI Testing
- Reliability
- MLOps
website: https://distributional.com
---
