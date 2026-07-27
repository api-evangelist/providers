---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 23.1
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: REST API for subscription management and recurring billing — accounts, subscriptions, campaigns, tokens/virtual currency, and payment operations.
  name: Vindicia Subscribe REST API
  slug: vindicia-subscribe-rest-api
- description: REST API for machine-learning-driven recovery of failed recurring payments.
  name: Vindicia Retain REST API
  slug: vindicia-retain-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Vindicia Webhooks
  slug: vindicia-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.vindicia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vindicia.com/category/developerhub
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vindicia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vindicia.com/bundle/b_Subscribe_REST_API_Guide/page/topics/Overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vindicia.com/bundle/b_restApiQuickStartGuide
- group: operate
  title: ''
  type: Support
  url: https://docs.vindicia.com/category/contactSupport
- group: start
  title: ''
  type: SignUp
  url: https://portal.vindicia.com/portal/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vindicia.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/vindicia-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vindicia-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vindicia-error-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vindicia-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vindicia-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vindicia-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/vindicia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vindicia-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vindicia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vindicia-llms.txt
created: '2026-07-17'
description: Vindicia (an Amdocs company) is a subscription-billing and payment-recovery platform for subscription businesses. Its flagship products are Vindicia Subscribe, a subscription-management and recurring-billing system, and Vindicia Retain, which uses payments intelligence and machine learning trained on billions of transactions to recover failed recurring payments and reduce involuntary churn. Vindicia Connect adds OAuth2/OpenID Connect identity for end-user authentication. The platform exposes REST APIs (Subscribe and Retain), a legacy CashBox SOAP API, documented webhooks, API-key and OAuth2 authentication, a React SDK, error-code references, dated per-product release notes, and an Atlassian status page. It integrates with major payment processors including Stripe, Adyen, Braintree, PayPal, Chase, CyberSource and ACI Worldwide.
image: https://vindicia.com/sites/default/files/vindicia-default-og-image.png
layout: provider
modified: '2026-07-21'
name: Vindicia
nav: Providers
network: true
overview: 'Vindicia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Subscription Billing, Recurring Payments, and Payment Recovery.


  The Vindicia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vindicia''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, changelog, and 11 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 22.6
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 32.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Vindicia Authentication
  slug: vindicia-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Vindicia Domain Security
  slug: vindicia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vindicia
tags:
- Company
- Fintech
- Subscription Billing
- Recurring Payments
- Payment Recovery
- Subscription Management
- Payments
- Churn
website: https://www.vindicia.com/
---
