---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Highline Fi Agentic Access
  operation_count: 27
  slug: highline-fi-agentic-access
  summary_line: 27 operations · 11 acting
api_count: 10
apis:
- description: The Highline API lets billers, lenders, and platforms verify consumer eligibility for paycheck-deduction payments, present the Highline Link flow to authorize a connection, submit and manage payment r
  name: Highline Pay by Paycheck API
  slug: pay-by-paycheck-api
- description: The Auth API from Highline — 2 operation(s) for auth.
  name: Highline Auth API
  slug: highline-fi-auth-api
- description: The Companies API from Highline — 1 operation(s) for companies.
  name: Highline Companies API
  slug: highline-fi-companies-api
- description: The Connections API from Highline — 2 operation(s) for connections.
  name: Highline Connections API
  slug: highline-fi-connections-api
- description: The Employments API from Highline — 1 operation(s) for employments.
  name: Highline Employments API
  slug: highline-fi-employments-api
- description: The Payment Requests API from Highline — 4 operation(s) for payment requests.
  name: Highline Payment Requests API
  slug: highline-fi-payment-requests-api
- description: The Payments API from Highline — 3 operation(s) for payments.
  name: Highline Payments API
  slug: highline-fi-payments-api
- description: The Products API from Highline — 4 operation(s) for products.
  name: Highline Products API
  slug: highline-fi-products-api
- description: The Settlements API from Highline — 3 operation(s) for settlements.
  name: Highline Settlements API
  slug: highline-fi-settlements-api
- description: The Users API from Highline — 4 operation(s) for users.
  name: Highline Users API
  slug: highline-fi-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Highline API
  slug: open-highline-fi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/highline-fi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highline-fi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/highline-fi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://highline.co/
- group: other
  title: ''
  type: Payroll
  url: https://highline.co/payroll/
- group: other
  title: ''
  type: PayrollAndHR
  url: https://highline.co/for-payroll-and-hr-providers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.highline.co/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.highline.co/llms.txt
- group: company
  title: ''
  type: About
  url: https://highline.co/about/
- group: company
  title: ''
  type: Careers
  url: https://highline.co/careers/
- group: operate
  title: ''
  type: Contact
  url: https://highline.co/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highlineco/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/HighlineCo
- group: company
  title: ''
  type: Blog
  url: https://highline.co/feed/
created: '2026-05-23'
description: Highline is an embedded payment infrastructure company whose Pay by Paycheck product captures funds from a consumer's payroll before they reach the checking account and routes them to billers and lenders. The platform pairs with payroll providers to create a split direct deposit at payroll run time, so designated bills are paid on time and in full, and the remainder is deposited to the consumer's bank as normal. Highline ships an API-first developer experience with hosted documentation at docs.highline.co, a Highline Link client widget, webhook-based notifications, sandbox simulations, daily ACH settlements, and an llms.txt for AI agents. The company is sometimes referenced as highline.fi but operates today at highline.co.
finops:
- name: Highline Fi Finops
  service_category: API
  slug: highline-fi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highline-fi.png
layout: provider
modified: '2026-05-23'
name: Highline
nav: Providers
network: true
overview: 'Highline publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Companies API, Connections API, and 6 more. Tagged areas include Embedded Finance, Payroll, Payments, ACH, and Bill Pay.


  Highline''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Highline Fi Plans Pricing
  plan_count: 1
  slug: highline-fi-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Highline Fi Rate Limits
  slug: highline-fi-rate-limits
score:
  band: thin
  composite: 30.9
  delta: -0.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 48.6
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highline-fi/refs/heads/main/screenshots/highline-fi-2026-06-20T182729.png
security:
- kind: authentication
  name: Highline Fi Authentication
  slug: highline-fi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Highline Fi Domain Security
  slug: highline-fi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: highline-fi
tags:
- Embedded Finance
- Payroll
- Payments
- ACH
- Bill Pay
- Lending
- Direct Deposit
- API-First
- Webhooks
- Pay by Paycheck
website: https://highline.co/
---
