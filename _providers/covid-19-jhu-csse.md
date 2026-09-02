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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Open-source API for exploring Covid19 cases based on JHU CSSE
  name: Covid-19 JHU CSSE
  slug: covid-19-jhu-csse
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covid-19-jhu-csse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuttaphat.com/covid19-api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Open-source API for exploring Covid19 cases based on JHU CSSE
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covid-19-jhu-csse.png
layout: provider
modified: '2026-05-28'
name: Covid-19 JHU CSSE
nav: Providers
network: true
overview: Covid-19 JHU CSSE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 19
score:
  band: minimal
  composite: 6.0
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
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/covid-19-jhu-csse/refs/heads/main/screenshots/covid-19-jhu-csse-2026-06-20T175134.png
security:
- kind: domain-security
  name: Covid 19 Jhu Csse Domain Security
  slug: covid-19-jhu-csse-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: covid-19-jhu-csse
tags:
- Health
- Public APIs
website: https://nuttaphat.com/covid19-api/
---
