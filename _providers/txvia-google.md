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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/txvia-google-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/txvia-google-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.txvia.com
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://techcrunch.com/2012/04/02/google-buys-txvia-banking-on-better-payment-tech-and-100m-customers-for-google-wallet/
created: '2026-07-17'
description: 'TxVia was a New York-based payments technology company that provided an issuer-processing platform for prepaid and other emerging payment card programs, reported at the time of its exit to power programs covering roughly 100 million accounts. Backed by Bain Capital Ventures, TxVia was acquired by Google on April 2, 2012 and its technology and team were folded into Google Wallet (now Google Pay). The company no longer operates independently: txvia.com today serves a Google-hosted acquisition notice, and there is no public developer program, API surface, GitHub organization, or published packages. This profile is retained as an acquired-company lead in the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/txvia-google.png
layout: provider
modified: '2026-07-21'
name: TxVia (Google)
nav: Providers
network: true
overview: TxVia (Google) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Prepaid Cards, and Payment Processing.
random_paper: 20
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
screenshot: https://raw.githubusercontent.com/api-evangelist/txvia-google/refs/heads/main/screenshots/txvia-google-2026-09-02T164648.png
security:
- kind: domain-security
  name: Txvia Google Domain Security
  slug: txvia-google-domain-security
  summary_line: TLSv1.3 · DMARC
slug: txvia-google
tags:
- Company
- Fintech
- Payments
- Prepaid Cards
- Payment Processing
- Issuer Processing
- Acquired
website: https://www.txvia.com
---
