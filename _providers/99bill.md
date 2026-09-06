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
  url: https://www.99bill.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.99bill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.99bill.com/menu!access.do
- group: operate
  title: ''
  type: Support
  url: https://help.99bill.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/99bill-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/99bill-llms.txt
created: '2026-07-17'
description: 99Bill Corporation (快钱, Kuaiqian) is one of China's leading independent third-party electronic payment service providers, offering a comprehensive suite of online payment, mobile payment, and settlement solutions for merchants and enterprises. Its Kuaiqian Merchant Open Platform (open.99bill.com) exposes standardized payment interfaces over common internet protocols, covering protocol/agreement (card-free) payments, online banking (B2C and B2B) payments, and WeChat Official Account and Mini-Program payments, with SDKs and demo code published for Java, PHP, and .NET. Developers select a product in the Product Center, build against a sandbox using provided demos, then contact 99Bill business staff to activate a production merchant account (issued MerchantAcctID and product keys) before going live. 99Bill was surfaced as a portfolio company of DCM Ventures and is profiled here in the API Evangelist network. No public OpenAPI, AsyncAPI, or package-registry SDK was found during enrichment;
  developer resources are distributed through the authenticated open platform and help center.
image: https://www.99bill.com/favicon.ico
layout: provider
modified: '2026-07-17'
name: 99Bill
nav: Providers
network: true
overview: '99Bill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Processing, and Online Payment.


  99Bill''s developer surface includes documentation, support, and 4 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/99bill/refs/heads/main/screenshots/99bill-2026-07-25T181251.png
security:
- kind: domain-security
  name: 99Bill Domain Security
  slug: 99bill-domain-security
  summary_line: TLSv1.2 · HSTS
slug: 99bill
tags:
- Company
- Fintech
- Payments
- Payment Processing
- Online Payment
- Mobile Payment
- China
- Merchant Services
website: https://www.99bill.com/
---
