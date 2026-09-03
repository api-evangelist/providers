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
  url: security/reshop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reshop.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reshop.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reshop.com/terms-of-service
created: '2026-07-17'
description: Reshop (Reshop US, Inc.) is a fintech company that provides instant refunds for e-commerce returns. When a shopper initiates a return at a partner retailer, Reshop pays out the refund immediately rather than making the customer wait for the item to ship back and be processed, delivering funds to the original payment method, a debit card, or a bank account. Reshop partners with clothing and lifestyle brands such as Volcom, RVCA, Vince Camuto, and Roxy, operates in the United States, and offers iOS and Android mobile apps. The company is backed by Matrix Partners. This profile was added to the API Evangelist network as a portfolio lead; Reshop publishes no public developer or API surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reshop.png
layout: provider
modified: '2026-07-20'
name: Reshop
nav: Providers
network: true
overview: Reshop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Refunds, and E-Commerce.
random_paper: 6
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reshop/refs/heads/main/screenshots/reshop-2026-09-02T153533.png
security:
- kind: domain-security
  name: Reshop Domain Security
  slug: reshop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reshop
tags:
- Company
- Fintech
- Payments
- Refunds
- E-Commerce
- Returns
website: https://reshop.com
---
