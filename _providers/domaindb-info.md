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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Domain name search to find all domains containing particular words/phrases/etc
  name: DomainDb Info
  slug: domaindb-info
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domaindb-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.domainsdb.info/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Domain name search to find all domains containing particular words/phrases/etc
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domaindb-info.png
layout: provider
modified: '2026-05-28'
name: DomainDb Info
nav: Providers
network: true
overview: DomainDb Info publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Development and Public APIs.
random_paper: 60
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domaindb-info/refs/heads/main/screenshots/domaindb-info-2026-06-20T180137.png
security:
- kind: domain-security
  name: Domaindb Info Domain Security
  slug: domaindb-info-domain-security
  summary_line: TLSv1.3 · HSTS
slug: domaindb-info
tags:
- Development
- Public APIs
website: https://api.domainsdb.info/
---
