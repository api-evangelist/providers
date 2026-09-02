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
- description: Basic candidate data and live electoral vote counts for top two parties in US presidential election
  name: US Presidential Election Data by TogaTech
  slug: us-presidential-election-data-by-togatech
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-presidential-election-data-by-togatech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uselection.togatech.org/api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Basic candidate data and live electoral vote counts for top two parties in US presidential election
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-presidential-election-data-by-togatech.png
layout: provider
modified: '2026-05-28'
name: US Presidential Election Data by TogaTech
nav: Providers
network: true
overview: US Presidential Election Data by TogaTech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 15
score:
  band: minimal
  composite: 4.2
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
  previous_composite: 4.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-presidential-election-data-by-togatech/refs/heads/main/screenshots/us-presidential-election-data-by-togatech-2026-06-20T200629.png
security:
- kind: domain-security
  name: Us Presidential Election Data By Togatech Domain Security
  slug: us-presidential-election-data-by-togatech-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: us-presidential-election-data-by-togatech
tags:
- Government
- Public APIs
website: https://uselection.togatech.org/api/
---
