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
- description: Live authenticated application backend for Examedi's consumer apps (Django REST Framework). Requires authorization; no public developer documentation or OpenAPI definition is published. Discovered via
  name: Examedi Application API
  slug: examedi-application-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/examedi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/examedi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://examedi.com
created: '2026-07-17'
description: Examedi is a Latin American healthtech company providing at-home medical and laboratory testing. Patients book online and a healthcare professional visits their home to collect samples (blood, urine, PCR and more), with results delivered digitally through the company's app and website. Examedi operates in Chile (examedi.cl) and Mexico (examedi.mx) and runs a live authenticated application backend at api.examedi.com. The company is backed by General Catalyst. No public developer program, API documentation, or OpenAPI definition is published at this time; this profile records the company's identity and discovered surfaces for the API Evangelist network.
image: https://examedi.com/images/apple-touch-icon.png
layout: provider
modified: '2026-07-19'
name: Examedi
nav: Providers
network: true
overview: Examedi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, HealthTech, and Diagnostics.
random_paper: 53
score:
  band: minimal
  composite: 9.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/examedi/refs/heads/main/screenshots/examedi-2026-07-25T213839.png
security:
- kind: domain-security
  name: Examedi Domain Security
  slug: examedi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: examedi
tags:
- Company
- Health
- Healthcare
- HealthTech
- Diagnostics
- Laboratory
- Medical Testing
- At-Home Care
- Latin America
website: https://examedi.com
---
