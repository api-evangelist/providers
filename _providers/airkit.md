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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airkit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.airkit.com
created: '2026-07-17'
description: AirKit (Airkit.ai) was a low-code platform for building customer-facing digital experiences and, later, AI-powered customer service agents, backed by Accel and Emergence Capital. The company was acquired by Salesforce (announced 2023) and its technology now underpins Salesforce Agentforce. As of this enrichment pass, www.airkit.com 301-redirects to salesforce.com/agentforce and the domain's CAA records point to salesforce.com, so AirKit no longer operates an independent developer surface, API, documentation, or portal of its own — all first-party discovery URLs resolve into Salesforce properties. This profile is retained as an acquired-company record; enrichment beyond domain-level DNS/TLS evidence is not applicable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airkit.png
layout: provider
modified: '2026-08-21'
name: AirKit
nav: Providers
network: true
overview: AirKit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Low-Code, Customer Experience, and Conversational AI.
random_paper: 14
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airkit/refs/heads/main/screenshots/airkit-2026-07-25T195425.png
security:
- kind: domain-security
  name: Airkit Domain Security
  slug: airkit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: airkit
tags:
- Company
- Automation
- Low-Code
- Customer Experience
- Conversational AI
- Acquired
- Salesforce
website: http://www.airkit.com
---
