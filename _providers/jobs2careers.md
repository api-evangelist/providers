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
- description: Job aggregator
  name: Jobs2Careers
  slug: jobs2careers
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobs2careers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://api.jobs2careers.com/api/spec.pdf
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Job aggregator
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jobs2careers.png
layout: provider
modified: '2026-05-28'
name: Jobs2Careers
nav: Providers
network: true
overview: Jobs2Careers publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Jobs and Public APIs.
random_paper: 29
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jobs2careers/refs/heads/main/screenshots/jobs2careers-2026-06-20T183744.png
security:
- kind: domain-security
  name: Jobs2Careers Domain Security
  slug: jobs2careers-domain-security
  summary_line: TLSv1.2 · DMARC
slug: jobs2careers
tags:
- Jobs
- Public APIs
website: http://api.jobs2careers.com/api/spec.pdf
---
