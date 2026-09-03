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
api_count: 1
apis:
- description: URL shortener service
  name: Cutt.ly
  slug: cuttly
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cutt-ly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cutt.ly/api-documentation/cuttly-links-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: URL shortener service
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cutt-ly.png
layout: provider
modified: '2026-05-28'
name: Cutt.ly
nav: Providers
network: true
overview: Cutt.ly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include URL Shorteners and Public APIs.
random_paper: 8
score:
  band: minimal
  composite: 7.6
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
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cutt-ly/refs/heads/main/screenshots/cutt-ly-2026-06-20T175357.png
security:
- kind: domain-security
  name: Cutt Ly Domain Security
  slug: cutt-ly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cutt-ly
tags:
- URL Shorteners
- Public APIs
website: https://cutt.ly/api-documentation/cuttly-links-api
---
