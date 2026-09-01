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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utopia-labs-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/utopia-labs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/utopia-labs-llms.txt
- group: company
  title: ''
  type: Website
  url: https://utopialabs.com
created: '2026-07-17'
description: Utopia Labs was a stablecoin payments and finance-operations platform for crypto-native teams and DAOs, covering payments, payroll, invoicing, and approval workflows, backed by Paradigm. Coinbase acquired Utopia Labs Corp. on November 13, 2024, and the team joined Base to build onchain payments into Coinbase Wallet. The company no longer operates independently and publishes no public API surface — utopialabs.com returns 404 and its former docs, api, and app subdomains no longer resolve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/utopia-labs.png
layout: provider
modified: '2026-07-21'
name: Utopia Labs
nav: Providers
network: true
overview: Utopia Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Fintech, Stablecoins, Payments, and DAO.
random_paper: 8
score:
  band: minimal
  composite: 1.5
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Utopia Labs Domain Security
  slug: utopia-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: utopia-labs
tags:
- Company
- Crypto Fintech
- Stablecoins
- Payments
- DAO
- Payroll
- Acquired
website: https://utopialabs.com
---
