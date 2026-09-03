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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airside-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airsidemobile.com/
created: '2026-07-17'
description: 'Airside (formerly Airside Mobile) is a digital identity and mobile credential product whose website airsidemobile.com now permanently redirects (HTTP 301) to Entrust''s Airside app page, indicating the product and its assets were acquired by Entrust. As of this enrichment pass no public API, OpenAPI specification, SDK, developer portal, or developer documentation surface could be discovered: developer/api/docs subdomains do not resolve and the root domain and /.well-known/security.txt both redirect off-site to Entrust. The company was originally surfaced as a bain-capital-ventures portfolio lead (sector ai-apps) and remains a stub pending any first-party developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airside.png
layout: provider
modified: '2026-07-17'
name: Airside
nav: Providers
network: true
overview: Airside is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Digital Identity, Mobile Credentials, and Identity Verification.
random_paper: 2
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airside/refs/heads/main/screenshots/airside-2026-07-25T195435.png
security:
- kind: domain-security
  name: Airside Domain Security
  slug: airside-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airside
tags:
- Company
- Ai Apps
- Digital Identity
- Mobile Credentials
- Identity Verification
- Acquired
- Entrust
website: https://airsidemobile.com/
---
