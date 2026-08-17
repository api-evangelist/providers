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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Live authenticated backend API for the Ajar Online property-management and rent-collection platform. The service root reports health but all resource endpoints require authentication; no public OpenAP
  name: Ajar Online API
  slug: ajar-online-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ajar-online-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ajar-online-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ajar.com.kw
created: '2026-07-17'
description: Ajar Online is a cloud-based property management and rent-collection platform headquartered in Kuwait and founded in 2015. It lets landlords, real-estate agencies, and property managers digitize rent collection and property administration, sending payment requests to tenants over SMS and email and accepting payment via credit and debit cards, KNET, and Sadad so tenants can pay in under a minute from anywhere. The platform adds portfolio dashboards, tenant and contract management, and analytics for data-driven property decisions, and has expanded across the GCC into the UAE and Saudi Arabia. The company operates a live, authenticated API backend at api.joinajar.com; there is no public API documentation, OpenAPI definition, or SDK published at this time, so this profile captures verifiable identity and domain-security signals pending a public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ajar-online.png
layout: provider
modified: '2026-07-17'
name: Ajar Online
nav: Providers
network: true
overview: Ajar Online publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, PropTech, Property Management, and Rent Payments.
random_paper: 61
score:
  band: minimal
  composite: 7.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Ajar Online Domain Security
  slug: ajar-online-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ajar-online
tags:
- Company
- Real Estate
- PropTech
- Property Management
- Rent Payments
- Payments
- Kuwait
- MENA
website: https://ajar.com.kw
---
