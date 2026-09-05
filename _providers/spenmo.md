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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spenmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spenmo.com/
created: '2026-07-17'
description: Spenmo was a Singapore-based spend management platform for businesses, offering corporate Visa debit cards (physical and virtual), bill and invoice management with smart scanning, employee reimbursements and claims, and accounting integrations with Xero, NetSuite, QuickBooks and Jurnal. Operated by Digital Services SG Five Pte Ltd, it worked with MAS-licensed payment partners rather than providing regulated payment services directly. The company ceased operations on 14 August 2025 and permanently disabled customer access. No public API or developer program was ever published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spenmo.png
layout: provider
modified: '2026-07-21'
name: Spenmo
nav: Providers
network: true
overview: Spenmo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spend Management, Expense Management, Corporate Cards, and Fintech.
random_paper: 7
score:
  band: minimal
  composite: 1.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spenmo/refs/heads/main/screenshots/spenmo-2026-09-02T160410.png
security:
- kind: domain-security
  name: Spenmo Domain Security
  slug: spenmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spenmo
tags:
- Company
- Spend Management
- Expense Management
- Corporate Cards
- Fintech
- Payments
- Accounting
- Singapore
- Defunct
website: https://spenmo.com/
---
