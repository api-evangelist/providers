---
access_model:
  confidence: low
  label: No public developer program identified
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Monument Bank Agentic Access
  operation_count: 86
  slug: monument-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: UK Open Banking Open Data API - the PUBLIC, unauthenticated reference-data surface defined by the OBIE Open Data Standard (product, ATM, branch, PCA, BCA, SME loan, and commercial credit card referenc
  name: Monument Bank Open Data API
  slug: monument-open-data-api
- description: UK Open Banking Read/Write Account & Transaction Information (AIS) API per the OBIE Read/Write API Standard - accounts, balances, transactions, beneficiaries, standing orders, direct debits, statement
  name: Monument Bank Account and Transaction Information API
  slug: monument-account-info-api
- description: UK Open Banking Read/Write Payment Initiation (PIS) API per the OBIE Read/Write API Standard - domestic, scheduled, standing-order, international, and file payment initiation for authorised PISP third
  name: Monument Bank Payment Initiation API
  slug: monument-payment-initiation-api
- description: UK Open Banking Read/Write Confirmation of Funds (CBPII) API per the OBIE Read/Write API Standard - confirms availability of funds on an account for authorised card-based payment instrument issuers. F
  name: Monument Bank Confirmation of Funds API
  slug: monument-confirmation-of-funds-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monument-bank-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monument-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monument-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monument-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monument-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/monument-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/monument-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monument-bank-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monument-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/monument-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monument-bank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.monument.co/
- group: company
  title: ''
  type: About
  url: https://www.monument.co/about
- group: company
  title: ''
  type: Blog
  url: https://www.monument.co/blog
- group: company
  title: ''
  type: News
  url: https://www.monument.co/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monument-bank/
- group: operate
  title: ''
  type: Support
  url: https://www.monument.co/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.monument.co/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monument.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monument.co/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://register.fca.org.uk/s/firm?id=0010X00004ksS6tQAE
created: '2026-07-23'
description: Monument Bank Limited is a UK challenger bank headquartered at 33 Cavendish Square, London, purpose-built for the "mass affluent" - professionals, entrepreneurs, and savers with substantial assets who have historically been underserved between mainstream retail banking and private banking. It received a full UK banking licence in November 2021, launched its first app-based savings products in early 2022, and in 2024 joined Tech Nation's Future Fifty cohort of leading pre-IPO companies. Monument is authorised by the Prudential Regulation Authority (PRA) and regulated by the Financial Conduct Authority (FCA) and PRA under FRN 849724, with eligible deposits protected by the FSCS. It is privately held (investors include Dubai Investments, which took a ~9% stake) and operates the technology it spun out as Monument Technology. Its current product suite is app-only savings - easy access accounts, cash ISAs, limited access savers, notice accounts, and fixed-term deposits - plus a planned
  move into buy-to-let and property lending. As a smaller, savings-and-lending-focused ASPSP it is NOT one of the CMA9 mandated banks and does not publish a public developer portal; where it participates in UK Open Banking it does so against the Open Banking Implementation Entity (OBIE) Open Data and Read/Write API Standards under the PSD2 / FCA framework, secured with FAPI-grade OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T10:00:00Z'
name: Monument Bank
nav: Providers
network: true
overview: 'Monument Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account and Transaction Information API, Payment Initiation API, and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Monument Bank''s developer surface includes authentication, engineering blog, product news, support, FAQ, and 16 more developer resources.'
random_paper: 31
scopes:
- name: Monument Bank Scopes
  scope_count: 3
  slug: monument-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 38.4
  delta: -2.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.6
    developer_ergonomics: 17.4
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 77.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Monument Bank Authentication
  slug: monument-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Monument Bank Domain Security
  slug: monument-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: monument-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Savings
- Challenger Bank
- Account Information
- Payments
website: https://www.monument.co/
---
