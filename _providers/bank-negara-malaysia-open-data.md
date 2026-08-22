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
- description: Malaysia Central Bank Open Data
  name: Bank Negara Malaysia Open Data
  slug: bank-negara-malaysia-open-data
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bank-negara-malaysia-open-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-negara-malaysia-open-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apikijangportal.bnm.gov.my/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Malaysia Central Bank Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-negara-malaysia-open-data.png
layout: provider
modified: '2026-05-28'
name: Bank Negara Malaysia Open Data
nav: Providers
network: true
overview: Bank Negara Malaysia Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 9
score:
  band: minimal
  composite: 5.8
  delta: -2.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-negara-malaysia-open-data/refs/heads/main/screenshots/bank-negara-malaysia-open-data-2026-06-20T172953.png
security:
- kind: domain-security
  name: Bank Negara Malaysia Open Data Domain Security
  slug: bank-negara-malaysia-open-data-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bank Negara Malaysia Open Data Vulnerability Disclosure
  slug: bank-negara-malaysia-open-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bank-negara-malaysia-open-data
tags:
- Government
- Public APIs
website: https://apikijangportal.bnm.gov.my/
---
