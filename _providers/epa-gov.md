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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epa-gov-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USEPA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-epa
- group: company
  title: ''
  type: Website
  url: https://www.epa.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.epa.gov/enviro/envirofacts-data-service-api
- group: other
  title: ''
  type: Canonical
  url: https://raw.githubusercontent.com/api-evangelist/environmental-protection-agency/refs/heads/main/apis.yml
created: '2024-07-02'
description: EPA.gov is an alias for the Environmental Protection Agency entry. The canonical APIs.json index for U.S. EPA APIs and data services is maintained in the environmental-protection-agency repository, which catalogs EPA's Envirofacts Data Service, Air Quality System (AQS), UV Index, and ECHO Compliance and Enforcement APIs. Refer to the canonical record for current API listings, properties, and metadata.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epa-gov.png
layout: provider
modified: '2026-04-28'
name: EPA.gov
nav: Providers
network: true
overview: 'EPA.gov is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Alias, Environment, Federal Government, and Open Data.


  EPA.gov''s developer surface includes developer portal and 5 more developer resources.'
random_paper: 91
score:
  band: minimal
  composite: 5.5
  delta: -2.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epa-gov/refs/heads/main/screenshots/epa-gov-2026-06-20T180750.png
security:
- kind: domain-security
  name: Epa Gov Domain Security
  slug: epa-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: epa-gov
tags:
- Alias
- Environment
- Federal Government
- Open Data
website: https://www.epa.gov/
---
