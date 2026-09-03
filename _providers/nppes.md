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
api_count: 1
apis:
- description: National Plan & Provider Enumeration System, info on healthcare providers registered in US
  name: NPPES
  slug: nppes
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nppes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://npiregistry.cms.hhs.gov/registry/help-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: National Plan & Provider Enumeration System, info on healthcare providers registered in US
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nppes.png
layout: provider
modified: '2026-05-28'
name: NPPES
nav: Providers
network: true
overview: NPPES publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 4
score:
  band: minimal
  composite: 4.1
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nppes/refs/heads/main/screenshots/nppes-2026-06-20T190448.png
security:
- kind: domain-security
  name: Nppes Domain Security
  slug: nppes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nppes
tags:
- Health
- Public APIs
website: https://npiregistry.cms.hhs.gov/registry/help-api
---
