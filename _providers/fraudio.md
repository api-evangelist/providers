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
  url: security/fraudio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fraudio.com
- group: company
  title: ''
  type: About
  url: https://www.fraudio.com/we-are-fraudio
- group: company
  title: ''
  type: Blog
  url: https://www.fraudio.com/blog
- group: operate
  title: ''
  type: ContactUs
  url: https://www.fraudio.com/contact-us
- group: other
  title: ''
  type: CardPaymentFraud
  url: https://www.fraudio.com/card-payment-fraud-detection
- group: other
  title: ''
  type: MerchantInitiatedFraud
  url: https://www.fraudio.com/merchant-initiated-fraud-detection
- group: other
  title: ''
  type: AntiMoneyLaundering
  url: https://www.fraudio.com/anti-money-laundering
- group: auth
  title: ''
  type: AuthorisedPushPaymentFraud
  url: https://www.fraudio.com/authorised-push-payment-fraud-detection
- group: other
  title: ''
  type: MoneyMuleDetection
  url: https://www.fraudio.com/money-mule-detection
- group: other
  title: ''
  type: CaseStudies
  url: https://www.fraudio.com/case-studies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fraudio
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/lifeatfraudio
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/lifeatfraudio
created: '2026-05-25'
description: Fraudio is an Amsterdam-based payments fraud detection and financial-crime scale-up founded in 2019 by João Moura (CEO), Nathan Trousdell (COO), and team, with additional offices in London, Lisbon, and Barcelona. Fraudio delivers AI- and machine-learning-driven fraud detection as a managed service to merchant acquirers, payment service providers, card issuers, and banks, with a product line that covers card payment fraud, merchant initiated fraud, anti-money laundering, authorised push payment (APP) fraud, and money mule detection. The company markets itself as "Generation 3" fraud detection, advancing past rule-based (Gen 1) and bespoke per-customer ML (Gen 2) approaches by training a single centralized "patent pending AI super brain" on the pooled transaction history of all of its customers, claiming network-effect performance gains versus single-tenant models. Fraudio integrates with customers through a plug-and-play real-time scoring API with sub-100ms response times, configurable
  risk-appetite thresholds, and no upfront integration or setup cost. Customers include Viva Wallet, Silverflow, Pismo, Bancontact, Fazz, PayTabs, IXOPAY, Bold.co, SaltPay, WiPay, ePayco, and LOQR. Fraudio is ISO 27001 certified, was selected for the Visa Innovation Program (2023), is co-financed by the EU Lisboa 2030 programme, has raised roughly $3.3M seed plus a Series A round (March 2025), and counts BigStar Ventures, BYND Venture Capital, Teya, Viva Wallet, Portugal Ventures, Iberis Capital, Shilling, and CTT among its investors. There is no public developer portal, no open API reference, no public OpenAPI spec, no SDK, and no GitHub organization — the fraud-scoring API is delivered as a gated B2B integration through a commercial sales process.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fraudio.png
layout: provider
modified: '2026-05-25'
name: Fraudio
nav: Providers
network: true
overview: 'Fraudio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Detection, Payment Fraud, Anti-Money Laundering, AML, and Financial Crime.


  Fraudio''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 2.0
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fraudio/refs/heads/main/screenshots/fraudio-2026-06-20T181510.png
security:
- kind: domain-security
  name: Fraudio Domain Security
  slug: fraudio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fraudio
tags:
- Fraud Detection
- Payment Fraud
- Anti-Money Laundering
- AML
- Financial Crime
- Payments
- Acquirers
- Payment Service Providers
- Card Issuers
- Banking
- Machine-Learning
- Artificial Intelligence
- Risk Scoring
- Netherlands
- Amsterdam
website: https://www.fraudio.com
---
