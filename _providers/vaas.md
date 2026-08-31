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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vaas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getvaas.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.getvaas.com/en/discover
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getvaas.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.getvaas.com/pqr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getvaas
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vaas-llms.txt
created: '2026-07-17'
description: Vaas is a Colombian fintech building debt infrastructure for Latin America, operating a platform that automates asset-backed debt facilities for originators, asset managers, and debt providers across industries. Vaas autonomously verifies asset documentation, reconciles cash flows end to end, and enforces collateral ownership in real time so assets cannot be pledged twice, bringing liquidity and transparency to private credit. Backed by Andreessen Horowitz (a16z). Vaas does not currently publish a public API or developer portal.
image: https://getvaas.com/logos/ImagenShare.png
layout: provider
modified: '2026-07-21'
name: Vaas
nav: Providers
network: true
overview: 'Vaas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Private Credit, Debt Infrastructure, and Asset-Backed Lending.


  Vaas'' developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Vaas Domain Security
  slug: vaas-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: vaas
tags:
- Company
- Fintech
- Private Credit
- Debt Infrastructure
- Asset-Backed Lending
- Verification
- Payment Reconciliation
- Capital Markets
- Latin America
- Colombia
website: https://www.getvaas.com/en/
---
