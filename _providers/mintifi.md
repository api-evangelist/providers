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
  url: security/mintifi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mintifi.com
created: '2026-07-17'
description: Mintifi is an Indian supply-chain financing platform that provides inventory and working-capital financing to SMEs, distributors, and dealers across manufacturer distribution networks. Its products include checkout and inventory financing, an Electronic Invoice Presentment and Payment (EIPP) solution for ERP-integrated invoice settlement and reconciliation, WhatsApp-based inventory financing, and Mintifi Collect for payment collection with Tally integration. The company exposes ERP-integration APIs to partners and is backed by Norwest Venture Partners. No public developer portal, OpenAPI, or self-serve API documentation is currently published; the docs host is access-gated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mintifi.png
layout: provider
modified: '2026-07-20'
name: Mintifi
nav: Providers
network: true
overview: Mintifi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Lending, Supply Chain Finance, and Fintech.
random_paper: 7
score:
  band: minimal
  composite: 1.5
  delta: -4.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mintifi/refs/heads/main/screenshots/mintifi-2026-08-07T183654.png
security:
- kind: domain-security
  name: Mintifi Domain Security
  slug: mintifi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mintifi
tags:
- Company
- Financial Services
- Lending
- Supply Chain Finance
- Fintech
- SME
- Payments
- India
website: https://mintifi.com
---
