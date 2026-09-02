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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapiens-medicus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://esculap.io
created: '2026-07-17'
description: Sapiens Medicus operates Esculap.io, a consumer digital-health platform offering AI-powered doctor consultations delivered instantly through a web application. Marketed as "Your AI Doctor - Instant Medical Care Anytime," the service promises AI doctor consultations with medical specialist-level accuracy and high diagnostic confidence, with no appointments and no waiting times. Surfaced in the API Evangelist network as a 500 Global portfolio company, it is a consumer-facing React single-page application; as of this enrichment pass no public API, developer portal, SDK, machine-readable OpenAPI/AsyncAPI specification, MCP server, or /.well-known discovery surface is published on the esculap.io domain.
image: https://esculap.io/social.jpeg
layout: provider
modified: '2026-07-21'
name: Sapiens Medicus
nav: Providers
network: true
overview: Sapiens Medicus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health, Artificial Intelligence, and Medical.
random_paper: 13
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sapiens Medicus Domain Security
  slug: sapiens-medicus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sapiens-medicus
tags:
- Company
- Healthcare
- Health
- Artificial Intelligence
- Medical
- Telehealth
- Consumer Health
- Diagnostics
website: https://esculap.io
---
