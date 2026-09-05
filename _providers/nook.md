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
  url: security/nook-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nook.io
- group: start
  title: ''
  type: Login
  url: https://app.modulrfinance.com
created: '2026-07-17'
description: Nook is an accounts payable (AP) automation platform for businesses, combining invoice management with automated payment workflows to reduce manual data entry, cut errors, and give finance teams clearer visibility over outgoings. Founded in the UK and backed by Speedinvest as an early investor, Nook was acquired by payments infrastructure provider Modulr; its product now operates as "Modulr AP" and its former standalone site at nook.io presents the combined Modulr AP offering. Nook does not publish an independent public developer platform, API reference, or SDKs — the payment rails are provided through Modulr's platform — so this profile is maintained as a company record rather than an API-bearing provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nook.png
layout: provider
modified: '2026-07-20'
name: Nook
nav: Providers
network: true
overview: Nook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Accounts Payable, Payments, and Invoice Automation.
random_paper: 19
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nook/refs/heads/main/screenshots/nook-2026-08-07T185453.png
security:
- kind: domain-security
  name: Nook Domain Security
  slug: nook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nook
tags:
- Company
- Fintech
- Accounts Payable
- Payments
- Invoice Automation
- Spend Management
- B2B
- Financial Operations
website: https://nook.io
---
