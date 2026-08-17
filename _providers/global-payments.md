---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Global Payments Agentic Access
  operation_count: 6
  slug: global-payments-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 5
apis:
- description: The Global Payments Integrated API provides ISVs and software partners with payment integration capabilities including credit card processing, ACH payments, and reporting. The platform supports semi-i
  name: Global Payments Integrated API
  slug: integrated-api
- description: Manage chargebacks and disputes.
  name: Global Payments Disputes API
  slug: global-payments-disputes-api
- description: Manage stored payment methods and tokenization.
  name: Global Payments Payment Methods API
  slug: global-payments-payment-methods-api
- description: Access settlement and funding information.
  name: Global Payments Settlements API
  slug: global-payments-settlements-api
- description: Process and manage payment transactions.
  name: Global Payments Transactions API
  slug: global-payments-transactions-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Global Payments Unified Payments Disputes API
  slug: open-global-payments-disputes-api
- collection_type: open
  name: Global Payments Unified Payments Disputes Payment Methods API
  slug: open-global-payments-payment-methods-api
- collection_type: open
  name: Global Payments Unified Payments Disputes Settlements API
  slug: open-global-payments-settlements-api
- collection_type: open
  name: Global Payments Unified Payments Disputes Transactions API
  slug: open-global-payments-transactions-api
- collection_type: open
  name: Global Payments Unified Payments API
  slug: open-global-payments-unified-payments-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/global-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/global-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/global-payments-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/global-payments-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globalpayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/global-payments
- group: start
  title: ''
  type: Portal
  url: https://developer.globalpayments.com/
- group: company
  title: ''
  type: Website
  url: https://www.globalpayments.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.globalpayments.com/llms.txt
created: '2026-03-21'
description: Global Payments is a leading worldwide provider of payment technology and software solutions delivering innovative services to customers globally. The company operates developer portals at developer.globalpayments.com and developer.globalpaymentsintegrated.com, offering a unified cloud-powered REST API for payment facilitation, card issuing, and multi-currency processing, along with integrated payment solutions for ISVs and software partners.
finops:
- name: Global Payments Finops
  service_category: Payments
  slug: global-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/global-payments.png
layout: provider
modified: '2026-05-19'
name: Global Payments
nav: Providers
network: true
overview: 'Global Payments publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Disputes API, Payment Methods API, Settlements API, and 1 more. Tagged areas include eCommerce, Payment Processing, Payment Technology, Payments, and POS.


  Global Payments'' developer surface includes authentication, developer portal, and 7 more developer resources.'
plans:
- name: Global Payments Plans Pricing
  plan_count: 2
  slug: global-payments-plans-pricing
press:
- date: '2026-05-25'
  title: Global Payments Inc. (@GlobalPaymentsInc)
  url: https://www.facebook.com/GlobalPaymentsInc/
- date: '2026-05-25'
  title: AI's vital role in payments and commerce
  url: https://www.globalpayments.com/insights/ai-in-payments-and-commerce
- date: '2026-05-25'
  title: BofA's New GenAI Assistant Transforms Global Payments ...
  url: https://www.prnewswire.com/news-releases/bofas-new-genai-assistant-transforms-global-payments-solutions-302570314.html
- date: '2026-05-25'
  title: Global Payments Unveils AI-First Genius Handheld Built for ...
  url: https://www.businesswire.com/news/home/20260512297137/en/Global-Payments-Unveils-AI-First-Genius-Handheld-Built-for-the-Future-of-Commerce
- date: '2026-05-25'
  title: Global Payments Joins Forces with AWS to Deliver ...
  url: https://investors.globalpayments.com/news-events/press-releases/detail/49/global-payments-joins-forces-with-aws-to-deliver-the-future
random_paper: 61
rate_limits:
- limit_count: 2
  name: Global Payments Rate Limits
  slug: global-payments-rate-limits
scopes:
- name: Global Payments Scopes
  scope_count: 4
  slug: global-payments-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 54.5
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/screenshots/global-payments-2026-06-20T181917.png
security:
- kind: authentication
  name: Global Payments Authentication
  slug: global-payments-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Global Payments Domain Security
  slug: global-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: global-payments
tags:
- eCommerce
- Payment Processing
- Payment Technology
- Payments
- POS
- Fortune 1000
website: https://www.globalpayments.com/
---
