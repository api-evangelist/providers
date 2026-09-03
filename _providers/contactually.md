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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contactually-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contactually.com
created: '2026-07-17'
description: Contactually was a cloud-based CRM (customer relationship management) platform focused on helping real estate agents, brokers, and other relationship-driven professionals nurture their networks through follow-up reminders, contact bucketing, pipelines, and automated outreach. Founded around 2011, it was acquired by real estate brokerage Compass on February 27, 2019, and had already been powering Compass's own CRM. Contactually permanently ceased operations on March 31, 2022. It historically exposed a v2 REST API (api.contactually.com) documented at developers.contactually.com for contacts, buckets, notes, tasks, and webhooks, but that developer surface, the API hosts, and all SDKs are now offline. This API Evangelist profile is retained as a historical record of a defunct provider; no live API, documentation, SDK, or event surface remains to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contactually.png
layout: provider
modified: '2026-07-18'
name: Contactually
nav: Providers
network: true
overview: Contactually is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Real-Estate, Contact Management, and Relationships.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contactually/refs/heads/main/screenshots/contactually-2026-07-25T210315.png
security:
- kind: domain-security
  name: Contactually Domain Security
  slug: contactually-domain-security
  summary_line: no transport/DNS hardening detected
slug: contactually
tags:
- Company
- CRM
- Real-Estate
- Contact Management
- Relationships
- Sales
- Defunct
website: https://contactually.com
---
