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
  scored_at: '2026-09-01'
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
overview: Distributional is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, AI Testing, and Reliability.
random_paper: 5
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 7.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Machine-Learning
- AI Testing
- Reliability
- MLOps
website: https://distributional.com
---
