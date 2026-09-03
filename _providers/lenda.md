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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://lenda.com
created: '2026-07-17'
description: 'Lenda was surfaced as a 500 Global portfolio company and added to the API Evangelist network as a stub for enrichment. Enrichment on 2026-07-19 found no operating surface: lenda.com returns HTTP 200 but serves only a parked single-page notice offering the domain for sale via a contact form, hosted on AWS and registered through Amazon Registrar. Every developer-facing subdomain probed (api, developer, developers, docs, app, status, blog) is NXDOMAIN, the full /.well-known/ discovery surface plus /llms.txt, /openapi.json and /robots.txt all return 404, and there is no first-party package on npm or PyPI and no company GitHub organization. This company is treated as defunct with no API to catalog; no artifact pointers are wired because no artifacts genuinely exist.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lenda.png
layout: provider
modified: '2026-07-19'
name: Lenda
nav: Providers
network: true
overview: Lenda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Portfolio Lead, 500 Global, and No API Surface.
random_paper: 12
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
screenshot: https://raw.githubusercontent.com/api-evangelist/lenda/refs/heads/main/screenshots/lenda-2026-07-25T224853.png
slug: lenda
tags:
- Company
- Defunct
- Portfolio Lead
- 500 Global
- No API Surface
website: https://lenda.com
---
