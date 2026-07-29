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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Submit checkout and sale events to Signifyd's Commerce Protection Platform for real-time fraud and chargeback risk evaluation. The Checkout flow supports pre-authorization screening, while the Sale fl
  name: Signifyd Sale (Checkout) API
  slug: signifyd-sale-api
- description: Submit finalized order and payment transaction details after authorization. Enables Signifyd to reconcile the pre-auth Checkout decision with the captured transaction, evaluate any post-auth risk sign
  name: Signifyd Transaction API
  slug: signifyd-transaction-api
- description: Programmatically retrieve guarantee decisions, case details, and policy results for orders submitted to Signifyd. Surfaces the checkpointAction (ACCEPT/HOLD/REJECT), checkpointActionReason, matched po
  name: Signifyd Decisions API
  slug: signifyd-decisions-api
- description: 'Report observed user outcomes back to Signifyd to close the loop between real-time decisions and production reality. Feedback drives model improvement, business customization, and rules optimization. '
  name: Signifyd Feedback API
  slug: signifyd-feedback-api
- description: Submit return events for evaluation by Signifyd's Return Insights and Return Abuse Prevention models. Helps merchants identify abusive returners, automate refund decisions, and power the Instant Refun
  name: Signifyd Returns API
  slug: signifyd-returns-api
- description: Calculate and remit US sales tax across jurisdictions using Signifyd's Sales Tax product. Provides nexus-aware rate lookup, tax calculation at checkout, and the data feeds required for filing and remi
  name: Signifyd Sales Tax API
  slug: signifyd-sales-tax-api
- description: Score and protect non-purchase customer journeys — Account Opening, Login, and Modification events — against account takeover, synthetic identity, and bonus abuse. Pairs with dedicated Feedback endpoi
  name: Signifyd Account Protection API
  slug: signifyd-account-protection-api
- description: Receive asynchronous decision notifications from Signifyd. The primary topic is ORDER_CHECKPOINT_ACTION_UPDATE, covering CHECKOUT, SALE, TRANSACTION, REROUTE, MERCHANT_REVIEW, and SIGNIFYD_REVIEW chec
  name: Signifyd Webhooks API
  slug: signifyd-webhooks-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signifyd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signifyd-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.signifyd.com
- group: start
  title: ''
  type: Portal
  url: https://developer.signifyd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signifyd.com/main/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signifyd.com/main/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signifyd.com/main/v3.0/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signifyd.com/main/v2.0/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.signifyd.com/main/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.signifyd.com/main/docs/authenticating
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signifyd.com/main/docs/configuring-webhooks
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signifyd.com/pricing/
- group: company
  title: ''
  type: AboutUs
  url: https://www.signifyd.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.signifyd.com/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.signifyd.com/customers/
- group: build
  title: ''
  type: Library
  url: https://www.signifyd.com/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signifyd.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signifyd.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.signifyd.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signifyd
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/signifyd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Signifyd
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signifyd
- group: build
  title: ''
  type: SDKs
  url: https://github.com/signifyd/php
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/signifyd/docs
created: '2026-05-25'
description: Signifyd is an ecommerce fraud prevention, chargeback protection, and revenue optimization platform. Its Commerce Protection Platform applies machine learning, elastic linking, and the merchant consortium network (covering ~98% of US online shoppers) to make real-time guarantee decisions on orders. Merchants integrate via the Checkout, Sale, Transaction, Decisions, Returns, Sales Tax, and Feedback APIs (v2 and v3) with synchronous responses or asynchronous webhooks, plus device-fingerprinting scripts and Android/iOS SDKs. Signifyd financially guarantees approved orders against chargebacks and offers Account Protection, Payments Optimization, and Return Abuse Prevention as adjacent products.
features:
- Commerce Protection Platform — real-time guarantee decisions on every order
- 100% financial guarantee against fraudulent chargebacks on approved orders
- Merchant consortium network covering ~98% of US online shoppers for elastic linking
- Synchronous decision API responses typically returned in hundreds of milliseconds
- Asynchronous webhook delivery (ORDER_CHECKPOINT_ACTION_UPDATE) with HMAC-SHA256 signatures
- Checkout API for pre-authorization fraud screening
- Sale and Transaction APIs for post-authorization order submission
- Decisions API to retrieve checkpointAction, policies, and score
- Account Protection for Account Opening, Login, and Modification checkpoints
- Feedback API to close the loop between decisions and observed outcomes
- Returns API powering Return Insights, Return Abuse Prevention, and Instant Refunds
- Sales Tax API for nexus-aware US tax calculation, filing, and remittance
- Payments Optimization / Fearless Payments for authorization rate uplift and 3DS routing
- Device profiling JavaScript snippet and Android/iOS SDKs
- Native integrations with Shopify, BigCommerce, Magento/Adobe Commerce, Salesforce Commerce Cloud, SAP Commerce, commercetools, Stripe, Adyen, Braintree, and major marketplaces
- Open-source PHP library plus Magento 1, Magento 2, and SFCC cartridges on GitHub
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signifyd.png
layout: provider
modified: '2026-05-25'
name: Signifyd
nav: Providers
network: true
overview: 'Signifyd publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud, Fraud Prevention, Chargebacks, Ecommerce, and Payments.


  Signifyd''s developer surface includes developer portal, documentation, getting-started guide, authentication, pricing, engineering blog, support, and 18 more developer resources.'
random_paper: 71
score:
  band: emerging
  composite: 26.4
  delta: -4.3
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signifyd/refs/heads/main/screenshots/signifyd-2026-06-20T193910.png
security:
- kind: domain-security
  name: Signifyd Domain Security
  slug: signifyd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Signifyd Vulnerability Disclosure
  slug: signifyd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: signifyd
tags:
- Fraud
- Fraud Prevention
- Chargebacks
- Ecommerce
- Payments
- Risk
- Machine Learning
- Commerce Protection
- Account Protection
- Returns
website: https://www.signifyd.com
---
