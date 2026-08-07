---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: 'API-driven Interac e-Transfer for Canadian money movement, supporting Send Money, Request Money, Receive AutoDeposit, and Receive Question-and-Answer flows so program managers and fintech clients can '
  name: Peoples Group Interac e-Transfer API
  slug: peoples-group-interac-etransfer-api
- description: Electronic Funds Transfer API for pre-authorized debits and credits to and from Canadian-domiciled accounts in CAD and USD, used for disbursements, remittances, payroll, and loading prepaid cards, wit
  name: Peoples Group EFT API
  slug: peoples-group-eft-api
- description: Bill payment API that processes payments to more than 12,000 billers across Canada, with support for individual, batch, and recurring payments. Access is provided to Peoples Group clients; no public O
  name: Peoples Group Bill Pay API
  slug: peoples-group-bill-pay-api
- description: Real-time push-to-card disbursements via Visa Direct and Mastercard Send, letting clients pay out funds directly to eligible Visa and Mastercard cards for B2B and B2C use cases. Built on the card netw
  name: Peoples Group Push-to-Card API (Visa Direct & Mastercard Send)
  slug: peoples-group-push-to-card-api
- description: 'Prepaid and credit card issuing through Visa and Mastercard BIN sponsorship for fintech program managers in Canada, with the integration technology and APIs to launch and manage card programs. Access '
  name: Peoples Group Card Issuing
  slug: peoples-group-card-issuing
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peoples-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peoplesgroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.peoplesgroup.com/fintech/solutions/payments
- group: docs
  title: ''
  type: Documentation
  url: https://www.peoplesgroup.com/fintech
- group: operate
  title: ''
  type: Support
  url: https://www.peoplesgroup.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://www.peoplesgroup.com/personal/portal-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peoplesgroup.com/about-us/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peoplesgroup.com/about-us/legal/privacy-security/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.peoplesgroup.com/about-us/legal/privacy-security
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/peoples-group-of-companies
- group: company
  title: ''
  type: Blog
  url: https://www.peoplesgroup.com/about-us/news-insights/press-releases
- group: design
  title: ''
  type: Conformance
  url: conformance/peoples-group-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peoples-group-llms.txt
created: '2026-07-24'
description: 'Peoples Group is the operating name of Peoples Trust Company, a Vancouver-based Canadian trust company and chartered-bank group founded in 1985 and owned by the Triple Five Group. Alongside its mortgage, deposit, and commercial-lending businesses, Peoples Group runs a fintech and payments arm that provides embedded banking-as-a-service to program managers, fintechs, brokers, and merchants across Canada: prepaid and credit card issuing under Visa and Mastercard BIN sponsorship, merchant acquiring, trust account services, and API-driven money movement including Interac e-Transfer (send, request money, and autodeposit), Electronic Funds Transfer (EFT) for CAD and USD debits and credits, bill payment to more than 12,000 Canadian billers, and push-to-card payouts via Visa Direct and Mastercard Send. In February 2026 Peoples Group partnered with Fiserv to build a next-generation, always-on payments platform carrying rich ISO 20022 data over direct connections to Canada''s payment
  systems, positioning it for Payments Canada''s Real-Time Rail. Its APIs are real and in production, but access is partnership- and sales-gated: there is no public self-serve developer portal, no downloadable OpenAPI/Swagger specification, and no public Postman workspace. Integration is arranged through a client relationship and the product documentation lives on the corporate fintech site.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Peoples Group
nav: Providers
network: true
overview: 'Peoples Group publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Canada, Banking-as-a-Service, Card Issuing, and Money Movement.


  Peoples Group''s developer surface includes documentation, support, engineering blog, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 23.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Peoples Group Domain Security
  slug: peoples-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: peoples-group
tags:
- Payments
- Canada
- Banking-as-a-Service
- Card Issuing
- Money Movement
- Interac e-Transfer
- EFT
- Bill Payment
- Merchant Acquiring
- Real-Time Payments
- ISO 20022
- BIN Sponsorship
website: https://www.peoplesgroup.com/
---
