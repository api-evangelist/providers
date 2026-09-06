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
  url: https://xsquare.biz
- group: commercial
  title: ''
  type: Pricing
  url: https://xsquare.biz/pricing
- group: design
  title: ''
  type: Conformance
  url: conformance/xsquire-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://xsquare.biz/pricing
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xsquire-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xsquire-domain-security.yml
created: '2026-07-17'
description: XSquare (listed as XSquire in the 500 Global portfolio) is a Dubai-based B2B financial operations platform for the GCC, live across the UAE and Qatar. It unifies e-invoicing, receivables collection via embedded payment links and QR codes (card, Apple Pay, Google Pay, bank), supplier payables on corporate card, and automatic invoice-to-payment reconciliation on a single ledger, with native ERP integrations (Zoho, Xero, Wafeq, Odoo) and a PSP network (Tess, Telr, Geidea). PCI DSS Level 1 v4 certified, UAE FTA e-invoicing ready (PEPPOL, structured XML), and non-custodial by design through licensed PSP partners regulated by CBUAE and QCB. Founded in 2023 by Tanvir Shah and Ashwin Shenoy; operates as XSquare Payment Services LLC (Dubai) and XSquare LLC (Doha). No public developer API, docs, or SDKs are published as of July 2026.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xsquire.png
layout: provider
modified: '2026-07-21'
name: XSquare
nav: Providers
network: true
overview: 'XSquare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Invoicing, and Reconciliation.


  XSquare''s developer surface includes pricing and 5 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 12.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xsquire/refs/heads/main/screenshots/xsquire-2026-09-02T171158.png
security:
- kind: domain-security
  name: Xsquire Domain Security
  slug: xsquire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xsquire
tags:
- Company
- Fintech
- Payments
- Invoicing
- Reconciliation
- B2B
- Accounts Payable
- Accounts Receivable
- E-Invoicing
- United Arab Emirates
- Qatar
website: https://xsquare.biz
---
