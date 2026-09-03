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
- description: Simple REST API that can scan submitted documents/files for the presence of threats
  name: Scanii
  slug: scanii
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/scanii-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scanii-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.scanii.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Simple REST API that can scan submitted documents/files for the presence of threats
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scanii.png
layout: provider
modified: '2026-05-28'
name: Scanii
nav: Providers
network: true
overview: Scanii publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti Malware and Public APIs.
random_paper: 1
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scanii/refs/heads/main/screenshots/scanii-2026-06-20T193508.png
security:
- kind: domain-security
  name: Scanii Domain Security
  slug: scanii-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scanii Trust Center
  slug: scanii-trust-center
  summary_line: GDPR
slug: scanii
tags:
- Anti Malware
- Public APIs
website: https://docs.scanii.com/
---
