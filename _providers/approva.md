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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/approva-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/approva-llms.txt
- group: company
  title: ''
  type: Website
  url: https://approva.co/
created: '2026-07-17'
description: 'Approva is an all-in-one marketplace where mortgage brokers and lenders interact with each other to create and fund deals, streamlining loan origination and refinancing by connecting brokers with alternative and traditional lenders in one place. Surfaced as a portfolio company of sierra-ventures and added to the API Evangelist network for enrichment. Sector: fintech. At the time of profiling, Approva operates a web marketplace at approva.co and does not publish a public API, developer portal, or SDKs; this profile captures its identity and probed domain-security posture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/approva.png
layout: provider
modified: '2026-07-17'
name: Approva
nav: Providers
network: true
overview: Approva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Mortgage, Lending, and Marketplace.
random_paper: 65
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/approva/refs/heads/main/screenshots/approva-2026-07-25T200840.png
security:
- kind: domain-security
  name: Approva Domain Security
  slug: approva-domain-security
  summary_line: TLSv1.3
slug: approva
tags:
- Company
- Fintech
- Mortgage
- Lending
- Marketplace
- Loans
- Brokers
website: https://approva.co/
---
