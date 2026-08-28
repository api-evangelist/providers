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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silversheet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://silversheet.com
created: '2026-07-17'
description: silversheet was a healthcare credentialing and provider-workforce technology company added to the API Evangelist network as a stub from venture-portfolio sourcing. As of this enrichment pass its domain silversheet.com no longer serves an independent product or developer surface — it redirects to AMN Healthcare's workforce technology platform (amnhealthcare.com/technology/workforce/), indicating the Silversheet brand has been absorbed into AMN Healthcare. No api/developer/docs subdomains resolve, no OpenAPI or developer portal was found, and no first-party API surface exists to enrich. The domain is still administratively live (SPF and DMARC configured, Proofpoint MX), so a domain-security probe was recorded, but there is no independent API to profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silversheet.png
layout: provider
modified: '2026-07-21'
name: silversheet
nav: Providers
network: true
overview: silversheet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Credentialing, Workforce, and Medical.
random_paper: 1
score:
  band: minimal
  composite: 3.3
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Silversheet Domain Security
  slug: silversheet-domain-security
  summary_line: DMARC
slug: silversheet
tags:
- Company
- Healthcare
- Credentialing
- Workforce
- Medical
- Acquired
website: https://silversheet.com
---
