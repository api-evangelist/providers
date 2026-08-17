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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Access to the laws of British Columbia
  name: BCLaws
  slug: bclaws
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bclaws-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bclaws.gov.bc.ca/civix/template/complete/api/index.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Access to the laws of British Columbia
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bclaws.png
layout: provider
modified: '2026-05-28'
name: BCLaws
nav: Providers
network: true
overview: BCLaws publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 40
score:
  band: minimal
  composite: 6.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bclaws/refs/heads/main/screenshots/bclaws-2026-06-20T173058.png
security:
- kind: domain-security
  name: Bclaws Domain Security
  slug: bclaws-domain-security
  summary_line: TLSv1.3
slug: bclaws
tags:
- Government
- Public APIs
website: https://www.bclaws.gov.bc.ca/civix/template/complete/api/index.html
---
