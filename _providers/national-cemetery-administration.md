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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-cemetery-administration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-cemetery-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-cemetery-administration
- group: company
  title: ''
  type: Website
  url: https://www.cem.va.gov/
- group: other
  title: ''
  type: GravesiteLocator
  url: https://gravelocator.cem.va.gov/
- group: other
  title: ''
  type: OpenData
  url: https://www.data.va.gov/
- group: other
  title: ''
  type: ParentAgency
  url: https://www.va.gov/
created: '2024-12-25'
description: The National Cemetery Administration (NCA) is an agency of the U.S. Department of Veterans Affairs that provides burial and memorial benefits to veterans and their eligible family members. NCA does not currently expose a documented public REST API; access is via web tools such as the Nationwide Gravesite Locator and Cemetery Finder, with broader data available through VA Open Data.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-cemetery-administration.png
layout: provider
modified: '2026-04-28'
name: National Cemetery Administration
nav: Providers
network: true
overview: National Cemetery Administration is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cemetery, Federal-Government, Veterans, and Burial.
random_paper: 19
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 93.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-cemetery-administration/refs/heads/main/screenshots/national-cemetery-administration-2026-06-20T190008.png
security:
- kind: domain-security
  name: National Cemetery Administration Domain Security
  slug: national-cemetery-administration-domain-security
  summary_line: DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: National Cemetery Administration Vulnerability Disclosure
  slug: national-cemetery-administration-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: national-cemetery-administration
tags:
- Cemetery
- Federal-Government
- Veterans
- Burial
website: https://www.cem.va.gov/
---
