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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
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
  composite: 7.3
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
