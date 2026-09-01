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
  url: security/lucidact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lucidact.com
created: '2026-07-17'
description: LucidAct (Lucidact Health) is an AI-powered care management platform operating in the healthcare technology and digital health vertical. The company builds software that streamlines patient care coordination and clinical workflows, using artificial intelligence to automate administrative tasks, support clinical decision-making, and improve patient engagement and population-health outcomes for healthcare organizations. LucidAct was surfaced as a portfolio company of 500 Global and added to the API Evangelist network for enrichment. As of this enrichment pass no public developer portal, API documentation, OpenAPI definition, SDKs, or /.well-known discovery surface could be found — the marketing site (www.lucidact.com) returns 403 on developer and well-known paths — so this profile currently carries only the provider's probed domain security posture alongside its identity.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidact.png
layout: provider
modified: '2026-07-20'
name: LucidAct
nav: Providers
network: true
overview: LucidAct is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Care Management, and Artificial Intelligence.
random_paper: 1
score:
  band: minimal
  composite: 3.3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucidact/refs/heads/main/screenshots/lucidact-2026-07-25T225637.png
security:
- kind: domain-security
  name: Lucidact Domain Security
  slug: lucidact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lucidact
tags:
- Company
- Healthcare
- Digital Health
- Care Management
- Artificial Intelligence
- Clinical Workflow
website: https://lucidact.com
---
