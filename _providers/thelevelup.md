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
  url: security/thelevelup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thelevelup.com/
created: '2026-07-17'
description: LevelUp (thelevelup.com) was a mobile payments and loyalty platform that let consumers pay and earn rewards at local restaurants and businesses via a QR-code / mobile-order-ahead app, and gave merchants a way to increase engagement and loyalty. It launched in March 2011 as a spinoff of SCVNGR and historically ran a developer API for payments, ordering, and loyalty at developer.thelevelup.com. LevelUp was acquired by Grubhub in 2018 for $390 million; as of this enrichment pass the entire thelevelup.com domain 302-redirects to grubhub.com and the former developer.thelevelup.com and api.thelevelup.com subdomains no longer resolve, so there is no independent live API surface remaining to catalog. This profile is retained as a historical network record of an acquired company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thelevelup.png
layout: provider
modified: '2026-07-21'
name: LevelUp
nav: Providers
network: true
overview: LevelUp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Mobile Payments, Loyalty, and Rewards.
random_paper: 15
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 1
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
  name: Thelevelup Domain Security
  slug: thelevelup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thelevelup
tags:
- Company
- Payments
- Mobile Payments
- Loyalty
- Rewards
- Restaurant
- Ordering
- Acquired
website: https://www.thelevelup.com/
---
