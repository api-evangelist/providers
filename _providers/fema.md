---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fema Agentic Access
  operation_count: 9
  slug: fema-agentic-access
  summary_line: 9 operations
api_count: 7
apis:
- description: Self-describing metadata - dataset list and data dictionaries.
  name: OpenFEMA Catalog API
  slug: fema-catalog-api
- description: Federally declared disasters.
  name: OpenFEMA Disaster Declarations API
  slug: fema-disaster-declarations-api
- description: Hazard Mitigation Assistance (HMA) grant program data.
  name: OpenFEMA Hazard Mitigation API
  slug: fema-hazard-mitigation-api
- description: Integrated Public Alert and Warning System archived alerts.
  name: OpenFEMA IPAWS API
  slug: fema-ipaws-api
- description: National Flood Insurance Program redacted policy and claims data.
  name: OpenFEMA NFIP API
  slug: fema-nfip-api
- description: FEMA Public Assistance (PA) grant program data.
  name: OpenFEMA Public Assistance API
  slug: fema-public-assistance-api
- description: Per-disaster financial summary totals from NEMIS.
  name: OpenFEMA Web Disaster Summaries API
  slug: fema-web-disaster-summaries-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFEMA Catalog API
  slug: open-fema-catalog-api
- collection_type: open
  name: OpenFEMA Catalog Disaster Declarations API
  slug: open-fema-disaster-declarations-api
- collection_type: open
  name: OpenFEMA Catalog Hazard Mitigation API
  slug: open-fema-hazard-mitigation-api
- collection_type: open
  name: OpenFEMA Catalog IPAWS API
  slug: open-fema-ipaws-api
- collection_type: open
  name: OpenFEMA Catalog NFIP API
  slug: open-fema-nfip-api
- collection_type: open
  name: OpenFEMA Catalog Public Assistance API
  slug: open-fema-public-assistance-api
- collection_type: open
  name: OpenFEMA Catalog Web Disaster Summaries API
  slug: open-fema-web-disaster-summaries-api
- collection_type: open
  name: OpenFEMA API
  slug: open-fema
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fema-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fema-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fema.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fema.gov/about/openfema/api
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fema-rate-limits.yml
created: '2026-07-03'
description: OpenFEMA is FEMA's open data platform, publishing free, public, machine-readable datasets on disaster declarations, public assistance grants, hazard mitigation projects, the National Flood Insurance Program (NFIP), and emergency alerting through a read-only RESTful API. The API uses OData-style query string parameters ($filter, $select, $top, $skip, $orderby) over individually versioned dataset endpoints, requires no API key or subscription, and returns JSON, CSV, or Parquet.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fema.png
layout: provider
modified: '2026-07-03'
name: OpenFEMA
nav: Providers
network: true
overview: 'OpenFEMA publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Disaster Declarations API, Hazard Mitigation API, and 4 more. Tagged areas include Government, Open Data, Emergency Management, Disaster, and FEMA.


  OpenFEMA''s developer surface includes documentation and 4 more developer resources.'
random_paper: 111
rate_limits:
- limit_count: 5
  name: Fema Rate Limits
  slug: fema-rate-limits
score:
  band: emerging
  composite: 25.6
  delta: 0.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Fema Domain Security
  slug: fema-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fema
tags:
- Government
- Open Data
- Emergency Management
- Disaster
- FEMA
- Public Safety
website: https://www.fema.gov/
---
