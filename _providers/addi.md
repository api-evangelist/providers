---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API that lets e-commerce merchants create Addi buy-now-pay-later credit applications at checkout. Authentication is handled through Auth0 using the OAuth2 client-credentials flow (client_id + cli
  name: Addi Credit & Checkout API
  slug: addi-credit-checkout-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs-sandbox.addi.com/auth/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs-sandbox.addi.com/auth/
- group: company
  title: ''
  type: Website
  url: https://co.addi.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/addi-com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdelanteFinancialHoldings
- group: operate
  title: ''
  type: Support
  url: https://co.addi.com/preguntas-frecuentes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://co.addi.com/tyc-links-addi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://co.addi.com/pp
- group: start
  title: ''
  type: SignUp
  url: https://co.addi.com/
- group: build
  title: ''
  type: Packages
  url: packages/addi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/addi-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/addi-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/addi-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/addi-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/addi-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/addi-domain-security.yml
created: '2026-07-17'
description: Addi is a Colombian financial technology company founded in 2018 that provides buy-now-pay-later (BNPL) credit at the point of sale across Latin America. Consumers split purchases into installments using only a national ID — no credit card required — while merchants integrate Addi as a checkout payment method through first-party e-commerce plugins (VTEX IO, Magento 2, PrestaShop) and a REST API secured with Auth0 OAuth2 client-credentials. Addi serves more than two million customers and tens of thousands of merchants in Colombia and Brazil, and is regulated by the Superintendencia Financiera de Colombia.
image: https://framerusercontent.com/assets/8Hhy9sRJUr3NC5YbnftP6MrFAOQ.jpg
layout: provider
modified: '2026-07-17'
name: Addi
nav: Providers
network: true
overview: 'Addi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and Credit.


  Addi''s developer surface includes documentation, engineering blog, support, signup flow, authentication, sandbox, and 10 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 30.5
  delta: 4.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Addi Authentication
  slug: addi-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Addi Domain Security
  slug: addi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: addi
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- Credit
- Lending
- Checkout
- E-commerce
- Latin America
- Colombia
website: https://co.addi.com/
---
