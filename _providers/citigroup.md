---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 11
apis:
- description: The Citi Accounts and Transactions API provides authorized third-party access to retail customer accounts, current and available balances, and transaction histories, enabling account-aggregation and p
  name: Citi Accounts and Transactions API
  slug: citi-accounts-transactions-api
- description: The Citi Money Movement API enables authorized payment initiation from Citi retail accounts, including domestic ACH, wire, and internal book transfers, on behalf of a consenting customer. It is one of
  name: Citi Money Movement API
  slug: citi-money-movement-api
- description: The Citi Authorize API handles the OAuth 2.0 authorization-code and customer-consent flows required for third-party applications to gain scoped access to a customer's Citi account data and to initiate
  name: Citi Authorize API
  slug: citi-authorize-api
- description: The Citi Customers API provides authorized access to retail customer profile information, including contact details and demographic data, for use in onboarding, personalization, and Know-Your-Customer
  name: Citi Customers API
  slug: citi-customers-api
- description: The Citi Onboarding API enables digital account opening, document submission, and KYC-driven origination workflows for onboarding new retail customers onto Citi products. It is one of the seven core p
  name: Citi Onboarding API
  slug: citi-onboarding-api
- description: The Citi Pay with Points API enables Citi cardholders to redeem ThankYou points and other rewards balances for purchases at merchant checkouts and inside partner applications. It is part of the Citi D
  name: Citi Pay with Points API
  slug: citi-pay-with-points-api
- description: The Citi Utilities API provides supporting reference data such as foreign-exchange rates, branch and ATM locators, and cut-off times used to support transactional workflows across Citi's retail and co
  name: Citi Utilities API
  slug: citi-utilities-api
- description: CitiConnect is the corporate treasury and trade integration channel within Citi's Treasury and Trade Solutions (TTS) business, exposing APIs for real-time payment initiation, payment status reporting,
  name: CitiConnect API
  slug: citiconnect-api
- description: The CitiConnect WorldLink Payment Services API delivers cross-border, multi-currency payment capabilities within the CitiConnect suite, including FX rate enquiry, FX deal booking, and cross-border pay
  name: CitiConnect WorldLink Payment Services API
  slug: citiconnect-worldlink-api
- description: The CitiConnect FX API provides real-time foreign-exchange information and execution for corporate treasury clients, supporting FX rate requests and the booking of FX contracts directly from ERP and T
  name: CitiConnect FX (Real-Time FX) API
  slug: citiconnect-fx-api
- description: The CitiConnect Statements and Reporting API delivers self-service reports, account statements, intraday and prior-day balance and transaction reporting, cut-off times, and proof-of-payment confirmati
  name: CitiConnect Statements and Reporting API
  slug: citiconnect-statements-reporting-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.citigroup.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.citi.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://partner.citi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner.citi.com/developers
- group: other
  title: ''
  type: APICatalog
  url: https://sandbox.developerhub.citi.com/api-catalog-list
- group: other
  title: ''
  type: CitiConnect
  url: https://www.citigroup.com/global/insights/citiconnect-api-portal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/citigroup
- group: company
  title: ''
  type: Blog
  url: https://www.citigroup.com/global/news
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.citigroup.com/global/investors
- group: commercial
  title: ''
  type: TermsOfService
  url: https://online.citi.com/US/JRS/pands/detail.do?ID=Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://online.citi.com/US/JRS/pands/detail.do?ID=PrivacyTerms
- group: operate
  title: ''
  type: Support
  url: https://online.citi.com/US/contactus.htm
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citigroup-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/citigroup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/citigroup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/citigroup-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citigroup-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/citigroup-rules.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/citigroup-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/citigroup-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/citigroup-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/citigroup-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/citigroup-llms.txt
created: '2026-03-23'
description: 'Citigroup (Citi) is a global, diversified money-center financial services holding company headquartered in New York City, serving consumers, corporations, governments, and institutions across roughly 90 countries. Citi exposes public API access through two distinct, voluntary developer surfaces. The retail Citi Developer Hub (developer.citi.com, now consolidated into the Citi Partner Portal at partner.citi.com) was one of the earliest bank open-banking programs, launched in 2016, and documents seven core API product families: Accounts, Authorize, Customers, Money Movement, Utilities, Onboarding, and Pay with Points, secured with OAuth 2.0 authorization-code and consent flows against a developer sandbox. The corporate surface is CitiConnect, part of Treasury and Trade Solutions (TTS), which has processed more than one billion API calls since 2017 and exposes real-time payments, cross-border WorldLink FX, statements and reporting, request-to-pay, proof-of-payment, and account-balance
  APIs across the full TTS footprint, integrated through ERP and TMS systems with OAuth 2.0 and mutual TLS. As a US institution Citi participates in voluntary open finance rather than a single mandated contract: it is a co-owner of the Akoya data-access network and shares consumer-permissioned data under emerging FDX / CFPB Section 1033 norms. No public downloadable OpenAPI, Swagger, SDK, or Postman artifacts are published; documentation is HTML and partner-gated, so entries below are documented humanURL references without harvested machine-readable specs.'
finops:
- name: Citigroup Finops
  service_category: Banking
  slug: citigroup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citigroup.png
jsonld:
- class_count: 17
  name: Citigroup Context
  property_count: 0
  slug: citigroup-context
layout: provider
modified: '2026-07-23'
name: Citigroup
nav: Providers
network: true
overview: 'Citigroup publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, United States, Money Center Bank, and Open Banking.


  The Citigroup catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citigroup''s developer surface includes documentation, engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Citigroup Plans Pricing
  plan_count: 2
  slug: citigroup-plans-pricing
press:
- date: '2026-05-25'
  title: Introducing AI Agents
  url: https://www.citigroup.com/global/news/perspectives/2026/introducing-ai-agents-next-phase-citi-artificial-intelligence-journey
- date: '2026-05-25'
  title: How Citigroup Helps Employees Harness the Power of AI
  url: https://aimagazine.com/news/jane-fraser-on-how-citi-is-harnessing-ai
- date: '2026-05-25'
  title: Citi Wealth Unveils “Citi Sky” – An AI-Powered Member of ...
  url: https://www.citigroup.com/global/news/press-release/2026/citi-wealth-unveils-citi-sky-ai-powered-member-google-cloud-deepmind-technologies
- date: '2026-05-25'
  title: Citi is leveling up its AI game, according to a new memo ...
  url: https://www.facebook.com/techinsider/posts/citi-is-leveling-up-its-ai-game-according-to-a-new-memo-sent-wednesday-and-viewe/1093504075982401/
- date: '2026-05-25'
  title: Citi eyes AI productivity gains as it consolidates data systems
  url: https://www.ciodive.com/news/citigroup-data-compliance-modernization-generative-ai/745683/
random_paper: 34
rate_limits:
- limit_count: 2
  name: Citigroup Rate Limits
  slug: citigroup-rate-limits
rules:
- name: Citigroup API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: citigroup-rules
score:
  band: thin
  composite: 37.8
  delta: -1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 34.8
    discoverability: 83.3
    governance: 33.3
    operational_transparency: 26.3
  previous_composite: 38.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citigroup/refs/heads/main/screenshots/citigroup-2026-06-20T174411.png
security:
- kind: authentication
  name: Citigroup Authentication
  slug: citigroup-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Citigroup Domain Security
  slug: citigroup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citigroup
tags:
- Banking
- Financial Services
- United States
- Money Center Bank
- Open Banking
- Open Finance
- Treasury and Trade Solutions
- CitiConnect
- Payments
- FX
- Corporate Banking
- Fortune 100
website: https://www.citigroup.com
---
