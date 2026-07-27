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
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Submit orders to Riskified for fraud and chargeback risk evaluation, in either a pre-authorization (Decide / Decision) or post-authorization (Submit / Decide) flow. Returns an APPROVED, DECLINED, or S
  name: Riskified Chargeback Guarantee API
  slug: riskified-chargeback-guarantee-api
- description: Recommend the optimal authentication path at checkout — friction-free, CVV, 3DS, or PSD2 exemption — to maximize approval rates while remaining SCA-compliant. The Advise endpoint returns a recommendat
  name: Riskified Adaptive Checkout API
  slug: riskified-adaptive-checkout-api
- description: Protect non-purchase customer journeys against account takeover, synthetic identity, and credential abuse. Submit Login, Reset Password, Customer Create, and Customer Update events and receive a real-
  name: Riskified Account Secure API
  slug: riskified-account-secure-api
- description: 'Detect and prevent refund, return, and promotional abuse. Submit refund and return claims for adjudication (claim_create), retrieve Riskified''s decision (claim_decision), and update in-flight returns '
  name: Riskified Policy Protect API
  slug: riskified-policy-protect-api
- description: Initiate a one-time password challenge as a step-up verification mechanism for high-risk login, password reset, or account modification events. Pairs with the Account Secure API to mediate friction ad
  name: Riskified OTP API
  slug: riskified-otp-api
- description: Collect device, browser, and behavioral telemetry from the shopper's session and feed it into Riskified's risk models. The Beacon is delivered as a JavaScript snippet for web and as iOS, Android, Reac
  name: Riskified Beacon (Device Intelligence) SDK
  slug: riskified-beacon-sdk-api
- description: Connect Riskified directly to a payment gateway (Adyen, Braintree, PayPal, Shopify Payments, Stripe) so chargeback notifications and evidence flow into the Dispute Resolve product without merchant glu
  name: Riskified Chargeback Gateway Integration (CGI) API
  slug: riskified-chargeback-gateway-integration-api
artifact_total: 50
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/riskified-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riskified-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.riskified.com
- group: start
  title: ''
  type: Portal
  url: https://developers.riskified.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.riskified.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.riskified.com/docs/api-integration-guide
- group: auth
  title: ''
  type: Authentication
  url: https://developers.riskified.com/reference/api-authentication
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/reference/api-environments
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/reference/api-overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/reference/http-responses
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/reference/notifications
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/reference/retries
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/reference/integrated-platforms
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/docs/integration-hub-guide
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/docs/integration-timeline
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/docs/sso
- group: docs
  title: ''
  type: Documentation
  url: https://developers.riskified.com/llms.txt
- group: company
  title: ''
  type: AboutUs
  url: https://www.riskified.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.riskified.com/blog/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.riskified.com/press/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.riskified.com/customers/
- group: build
  title: ''
  type: Library
  url: https://www.riskified.com/resources/
- group: company
  title: ''
  type: Careers
  url: https://www.riskified.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.riskified.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.riskified.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.riskified.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riskified.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.riskified.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.riskified.com
- group: other
  title: ''
  type: ProductInformation
  url: https://www.riskified.com/adaptive-checkout/
- group: other
  title: ''
  type: ProductInformation
  url: https://www.riskified.com/chargeback-guarantee/
- group: other
  title: ''
  type: ProductInformation
  url: https://www.riskified.com/account-secure/
- group: other
  title: ''
  type: ProductInformation
  url: https://www.riskified.com/policy-protect/
- group: other
  title: ''
  type: ProductInformation
  url: https://www.riskified.com/chargeback-guarantee/dispute-resolve/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/riskified
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/RiskifiedInc
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/riskified/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Riskified
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Riskified/php_sdk
- group: build
  title: ''
  type: SDKs
  url: https://packagist.org/packages/riskified/php_sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Riskified/java_sdk
- group: build
  title: ''
  type: SDKs
  url: https://central.sonatype.com/artifact/com.riskified/riskified-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Riskified/sdk_net
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Riskified.SDK
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Riskified/riskified_ios_sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Riskified/riskified-ios-beacon
- group: build
  title: ''
  type: Samples
  url: https://github.com/Riskified/api_examples
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Riskified/apiref-changelog
created: '2026-05-25'
description: Riskified (NYSE RSKD) is an Israeli ecommerce risk-management platform that uses machine learning and a global merchant intelligence network to make sub-second decisions across the entire shopper journey. Its Chargeback Guarantee, Adaptive Checkout, Account Secure, Policy Protect, and Dispute Resolve products are exposed through a REST + webhook API surface at developers.riskified.com, covering pre-auth and post-auth order review, 3DS / PSD2 optimization, account integrity (login, password reset, customer create/update), claim adjudication for refund and return abuse, and an OTP service. Authentication is HMAC-SHA256 over the request body. Official SDKs ship for PHP, Java, and .NET, with iOS, Android, React Native, and Unity Beacon SDKs for device intelligence, plus first-party integrations for Shopify, Magento/Adobe Commerce, Salesforce Commerce Cloud, SAP Commerce / Hybris, commercetools, VTEX, Adyen, Braintree, PayPal, and Stripe.
features:
- Chargeback Guarantee — 100% financial guarantee on Riskified-approved orders against fraudulent chargebacks
- Adaptive Checkout — dynamic SCA, 3DS, and PSD2 routing tuned per order to maximize authorization rates
- Account Secure — pre-purchase identity protection at Login, Reset Password, Customer Create / Update events
- Policy Protect — refund and return abuse prevention with claim adjudication via claim_create / claim_decision / claim_update
- Dispute Resolve — automated chargeback representment and evidence assembly across major payment gateways
- HMAC-SHA256 authentication (X-RISKIFIED-HMAC-SHA256 + X-RISKIFIED-SHOP-DOMAIN headers) with versioned Accept header
- Sandbox and production environments per product (api.riskified.com, wh.riskified.com, otp.self-veri.com)
- Asynchronous webhook notifications with retry semantics
- Beacon device-intelligence JavaScript snippet plus iOS, Android, React Native, and Unity SDKs
- First-party PHP, Java, and .NET SDKs published to Packagist, Maven Central, and NuGet
- Chargeback Gateway Integration (CGI) connectors for Adyen, Braintree, PayPal, Shopify Payments, and Stripe
- Native ecommerce platform integrations for Shopify (incl. headless), Magento / Adobe Commerce, SAP Commerce / Hybris, Salesforce Commerce Cloud, commercetools, and VTEX
- SSO support for Riskified Control Center access
- LLMs.txt index of the developer portal for AI agent consumption
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riskified.png
integrations:
- Shopify and Shopify Payments (full storefront and headless)
- Magento / Adobe Commerce (Magento 1, Magento 2, and Deco replacement-flow)
- Salesforce Commerce Cloud
- SAP Commerce / Hybris
- commercetools
- VTEX
- PrestaShop
- Adyen (Chargeback Gateway Integration)
- Braintree (Chargeback Gateway Integration)
- PayPal (Chargeback Gateway Integration)
- Stripe (Chargeback Gateway Integration)
- Riskified Integration Hub for connector-based deployment
layout: provider
modified: '2026-05-25'
name: Riskified
nav: Providers
network: true
overview: 'Riskified publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud, Fraud Prevention, Chargebacks, Ecommerce, and Payments.


  Riskified''s developer surface includes developer portal, API reference, getting-started guide, authentication, documentation, engineering blog, pricing, and 41 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.1
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/screenshots/riskified-2026-06-20T193133.png
security:
- kind: domain-security
  name: Riskified Domain Security
  slug: riskified-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Riskified Trust Center
  slug: riskified-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: riskified
solutions:
- Chargeback Guarantee — guaranteed fraud chargeback protection
- Adaptive Checkout — checkout authentication and authorization optimization
- Account Secure — account takeover and identity abuse prevention
- Policy Protect — refund, return, and promotion abuse prevention
- Dispute Resolve — chargeback recovery and dispute representment
tags:
- Fraud
- Fraud Prevention
- Chargebacks
- Ecommerce
- Payments
- Risk
- Machine Learning
- Account Takeover
- Policy Abuse
- 3DS
- PSD2
- Returns
use_cases:
- Pre-authorization fraud screening at checkout with Riskified-guaranteed APPROVE / DECLINE decisions
- Post-authorization order review with asynchronous Submit and Decide flows
- PSD2 / SCA exemption optimization for European card payments
- 3DS step-up routing for non-regulated geographies based on risk score
- Account takeover prevention across login, password reset, and customer profile updates
- Refund and return abuse detection with claim-level adjudication
- Automated chargeback representment through CGI connectors to Adyen, Braintree, PayPal, Shopify Payments, and Stripe
- Promotion and reseller abuse detection through Policy Protect
- High-friction step-up via OTP for high-risk recovery events
- Cross-channel device intelligence on web, iOS, Android, React Native, and Unity surfaces
website: https://www.riskified.com
---
