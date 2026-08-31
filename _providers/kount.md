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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The Payments Fraud API is the core REST endpoint of the Kount 360 platform for AI-driven digital fraud prevention. Merchants submit order, payment, customer, and device session data, and receive a rea
  name: Kount Payments Fraud API
  slug: kount-payments-fraud-api
- description: The Risk Inquiry Service (RIS) is Kount's legacy RESTful API for transaction risk evaluation. RIS joins device data from the JavaScript Data Collector with merchant-supplied order data, scores each tr
  name: Kount Risk Inquiry Service (RIS) API
  slug: kount-risk-inquiry-service-api
- description: 'The Kount Data Collector is a client-side JavaScript and mobile SDK component that gathers device fingerprinting and behavioral session data — including device characteristics, browser attributes, IP '
  name: Kount Data Collector
  slug: kount-data-collector
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kount-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kount.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.kount.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.kount.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kount.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kount.com/hc/en-us/sections/4410851086356-Integration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kount
- group: operate
  title: ''
  type: Support
  url: https://support.kount.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kount
- group: other
  title: Equifax (Parent Company)
  type: ParentCompany
  url: https://www.equifax.com/business/identity-fraud/
- group: build
  title: RIS Java SDK
  type: SDKs
  url: https://github.com/Kount/kount-ris-java-sdk
- group: build
  title: RIS PHP SDK
  type: SDKs
  url: https://github.com/Kount/kount-ris-php-sdk
- group: build
  title: RIS Python SDK
  type: SDKs
  url: https://github.com/Kount/kount-ris-python-sdk
- group: build
  title: RIS .NET SDK
  type: SDKs
  url: https://github.com/Kount/kount-ris-dotnet-sdk
- group: build
  title: Android Data Collector SDK
  type: SDKs
  url: https://github.com/Kount/kount-android-sdk
- group: build
  title: iOS Data Collector SDK (Objective-C)
  type: SDKs
  url: https://github.com/Kount/kount-ios-sdk
- group: build
  title: iOS Data Collector SDK (Swift)
  type: SDKs
  url: https://github.com/Kount/kount-swift-ios-sdk
- group: build
  title: Web (JavaScript) Data Collector SDK
  type: SDKs
  url: https://github.com/Kount/kount-web-sdk
- group: build
  title: Sample E-Commerce Web App
  type: Sample
  url: https://github.com/Kount/kount-sample-web-app
created: '2026-05-25'
description: Kount is a Boise, Idaho-based fraud prevention and chargeback management platform, now operating as part of Equifax. Kount combines AI-driven risk scoring, device fingerprinting, identity intelligence, and a multi-tenant global data network to help merchants, payment processors, and digital businesses stop payment fraud, account takeover, and chargebacks while reducing false positives. The Kount 360 platform offers Payments Fraud, Account Takeover Protection, Chargeback Management, and Identity Trust services exposed through REST APIs, mobile SDKs, a JavaScript Data Collector, and e-commerce platform plugins.
features:
- description: Machine learning models score each transaction in real time and return Approve, Decline, or Review decisions with reason codes.
  name: AI-Driven Risk Scoring
- description: JavaScript and mobile Data Collectors capture device, browser, network, and behavioral signals tied to a session identifier.
  name: Device Fingerprinting
- description: A multi-tenant global data network correlates personas across merchants to identify trusted customers and known fraudsters.
  name: Identity Trust Network
- description: Refund/Chargeback (RFCB) reporting plus dispute response workflows reduce chargeback losses and recover revenue.
  name: Chargeback Management
- description: Login and account-change risk scoring detects credential stuffing, session hijacking, and synthetic account creation.
  name: Account Takeover Protection
- description: Merchant-managed allow/deny lists for cards, emails, devices, addresses, payment instruments, gift cards, and custom UDFs.
  name: VIP Lists
- description: 3DS transaction tagging API supports step-up authentication for stronger customer authentication where required.
  name: 3-D Secure Orchestration
- description: Merchants can layer business rules on top of the model score via the Agent Web Console.
  name: Custom Decisioning Rules
- description: Native Android and iOS SDKs (Objective-C and Swift) for in-app device data collection.
  name: Mobile SDKs
- description: Out-of-the-box integrations for Magento 2, Shopify, Salesforce Commerce Cloud, and Miva.
  name: E-Commerce Platform Plugins
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kount.png
integrations:
- description: Official Magento 2 plugin for the Kount 360 platform.
  name: Magento 2
- description: Shopify app integration for Kount risk decisioning.
  name: Shopify
- description: SFCC Link cartridge for Kount integration.
  name: Salesforce Commerce Cloud
- description: Miva e-commerce platform integration documented in Miva developer docs.
  name: Miva
- description: Parent-company integration with Equifax identity and credit data services.
  name: Equifax
layout: provider
modified: '2026-05-25'
name: Kount
nav: Providers
network: true
overview: 'Kount publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Prevention, Fraud Detection, Chargebacks, Payments, and Identity.


  Kount''s developer surface includes developer portal, documentation, getting-started guide, support, and 15 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kount/refs/heads/main/screenshots/kount-2026-06-20T184141.png
security:
- kind: domain-security
  name: Kount Domain Security
  slug: kount-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kount
solutions:
- description: Unified fraud prevention platform combining Payments Fraud, Account Takeover, and Chargeback Management on a single AI model.
  name: Kount 360
- description: Real-time CNP transaction screening for merchants and payment processors.
  name: Payments Fraud
- description: Login and account-event risk scoring to block credential abuse.
  name: Account Takeover Protection
- description: Pre-transaction prevention plus post-transaction dispute response workflows.
  name: Chargeback Management
- description: Cross-merchant persona data network underlying all Kount decisions.
  name: Identity Trust Global Network
tags:
- Fraud Prevention
- Fraud Detection
- Chargebacks
- Payments
- Identity
- Risk Scoring
- Device Intelligence
- Account Takeover
use_cases:
- description: Score e-commerce CNP transactions for stolen-card and BIN-attack fraud before authorization.
  name: Card-Not-Present Payment Fraud
- description: Pre-authorization screening and post-transaction chargeback tagging to reduce chargeback ratios.
  name: Chargeback Reduction
- description: Score login and password-reset events to block credential-stuffing and ATO attempts.
  name: Account Takeover Defense
- description: Screen account-creation events for synthetic identities and bot signups.
  name: New Account Fraud
- description: High-velocity digital goods and gift-card flows benefit from device + persona network signals.
  name: Digital Goods and Gift Card Fraud
- description: Two-sided marketplaces use Kount to vet both buyers and sellers.
  name: Marketplace Trust
- description: Detect coupon stacking, refund abuse, and other policy-abuse patterns via custom rules and UDFs.
  name: Promo Abuse and Policy Abuse
website: https://kount.com/
---
