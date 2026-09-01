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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Post to and update maintenance and incidents on your status page through an HTTP REST API
  name: Instatus
  slug: instatus
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instatus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instatus.com/help/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://instatus.com/blog
created: '2026-05-28'
description: Post to and update maintenance and incidents on your status page through an HTTP REST API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instatus.png
layout: provider
modified: '2026-05-30'
name: Instatus
nav: Providers
network: true
overview: 'Instatus publishes 1 API on the [APIs.io](https://apis.io/) network: Instatus. Tagged areas include Business and Public APIs.


  Instatus'' developer surface includes engineering blog and 3 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 43.6
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instatus/refs/heads/main/screenshots/instatus-2026-06-20T183418.png
security:
- kind: domain-security
  name: Instatus Domain Security
  slug: instatus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: instatus
tags:
- Business
- Public APIs
website: https://instatus.com/help/api
---
