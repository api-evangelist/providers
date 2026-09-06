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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://precium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.precium.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/precium-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://precium.com/magazine
- group: operate
  title: ''
  type: StatusPage
  url: https://precium.com/status
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/precium-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/precium-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://precium.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://precium.com/legal-docs/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://precium.com/legal-docs/privacy-policy
created: '2026-07-17'
description: Precium is a South African fintech that provides local payment infrastructure for global merchants expanding into Africa. Its enterprise-grade platform handles payment processing across cards, instant EFT, mobile wallets and debit orders, plus intelligent smart routing, network tokenization, automated reconciliation, cross-border settlement, and payment recovery through retries and mandates. Precium exposes a public API and a mandates API (per its status dashboard) and integrates via server-to-server, redirect, and orchestrator paths with webhook status updates, though it does not publish a public API reference or OpenAPI. Backed by Partech, QED Investors, and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/precium.png
layout: provider
modified: '2026-07-20'
name: Precium
nav: Providers
network: true
overview: 'Precium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Payments, Payment Processing, and Payment Infrastructure.


  Precium''s developer surface includes documentation, engineering blog, support, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 13.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/precium/refs/heads/main/screenshots/precium-2026-09-02T151912.png
security:
- kind: domain-security
  name: Precium Domain Security
  slug: precium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: precium
tags:
- Company
- Financial-Services
- Payments
- Payment Processing
- Payment Infrastructure
- Fintech
- South Africa
website: https://precium.com/
---
