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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/womply-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/womply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://womply.com
created: '2026-07-17'
description: Womply (legally Oto Analytics, Inc.) was a small-business software company founded in 2011 by Toby Scammell that spent a decade building marketing, reputation, and payments software for roughly 500,000 Main Street businesses, and during the Paycheck Protection Program built the application-intake and identity-screening technology its lender partners used to process loans for sole proprietors and the smallest businesses. The company sold in 2021 for approximately $1.1 billion and is no longer operating; womply.com today is a primary-source documentary record of Womply's PPP role, sourced to court rulings, the JAMS arbitration award, SBA data, and the company's own production files. No public developer/API surface remains — this profile captures the company's identity and the record site's published artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/womply.png
layout: provider
modified: '2026-07-21'
name: Womply
nav: Providers
network: true
overview: Womply is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Small Business, Fintech, Payments, and Lending.
random_paper: 8
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 3
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
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/womply/refs/heads/main/screenshots/womply-2026-09-02T170905.png
security:
- kind: domain-security
  name: Womply Domain Security
  slug: womply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: womply
tags:
- Company
- Small Business
- Fintech
- Payments
- Lending
- PPP
- Software
- Historical Record
website: https://womply.com
---
