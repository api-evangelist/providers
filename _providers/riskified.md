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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Riskified Agentic Access
  operation_count: 20
  slug: riskified-agentic-access
  summary_line: 20 operations · 20 acting · 1 human-in-the-loop
api_count: 10
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
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Operations for managing order lifecycle (cancel, refund, fulfill, chargeback)
  name: Riskified Automation Endpoints API
  slug: riskified-automation-endpoints-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Operations related to customer activity, including login, password resets, customer verification attempts, and customer-merchant contact events.
  name: Riskified Customer Actions API
  slug: riskified-customer-actions-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Operations related to account management, including customer creation and updates.
  name: Riskified Customer Management API
  slug: riskified-customer-management-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Riskified's PSD2 Optimization product, which is complementary to our Chargeback Guarantee product, is designed to minimize the friction associated with SCA and maximize conversions - all while meeting
  name: Riskified Order Pre-Auth Review and PSD2/3DS/CVV Recommendations API
  slug: riskified-order-pre-auth-review-and-psd2-3ds-cvv-recommendations-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Operations for initiating and verifying one-time password recovery requests.
  name: Riskified OTP Recover (Sync flow) API
  slug: riskified-otp-recover-sync-flow-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Operations that allow you to send orders to Riskified for fraud review after payment authorization
  name: Riskified Post-Authorization Flow API
  slug: riskified-post-authorization-flow-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: Operations that allow you to send orders to Riskified for fraud review before payment authorization
  name: Riskified Pre-Authorization Flow API
  slug: riskified-pre-authorization-flow-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: The Refunds API from Riskified — 2 operation(s) for refunds.
  name: Riskified Refunds API
  slug: riskified-refunds-api
- baseURL: https://wh.riskified.com/
  baseurl_source: declared
  description: The Returns API from Riskified — 1 operation(s) for returns.
  name: Riskified Returns API
  slug: riskified-returns-api
artifact_total: 88
asyncapis:
- description: ''
  name: Riskified Webhooks
  slug: riskified-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/agentic-access/riskified-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/riskified-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/rules/riskified-rules.yml
  title: ''
  type: Spectral
  url: rules/riskified-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/json-ld/riskified-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/riskified-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/vocabulary/riskified-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/riskified-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/asyncapi/riskified-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/riskified-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/data-model/riskified-data-model.yml
  title: ''
  type: DataModel
  url: data-model/riskified-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.riskified.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/errors/riskified-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/riskified-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/conformance/riskified-conformance.yml
  title: ''
  type: Conformance
  url: conformance/riskified-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/llms/riskified-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/riskified-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/well-known/riskified-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/riskified-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/well-known/riskified-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riskified-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/hosts/riskified-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riskified-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/integrations/riskified-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/riskified-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/vendors/riskified-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riskified-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.riskified.com/hc/en-us?_gl=1*h5db4w*_gcl_au*NTY1ODg5MDI2LjE3ODEyNzE2ODkuLS4tLjE3ODQzMTI0MzAuNjY5OTE5ODU0LjE3ODQ3NDQ4MTAuMTc4NDc1MDQ4MQ..*_ga*MTM0Mzk3ODAyNy4xNzgxMjcxNjkz*_ga_L8RV3KLX8W*czE3ODQ3Mzg2NTQkbzc4JGcxJHQxNzg0NzUzMTM1JGo0MyRsMCRoMTM2NzU4NzA1Ng..
- group: start
  title: ''
  type: Login
  url: https://app.riskified.com/login
- group: company
  title: ''
  type: Website
  url: https://www.riskified.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/security/riskified-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/riskified-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riskified/refs/heads/main/security/riskified-domain-security.yml
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
  type: Examples
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
json_schemas:
- name: adaptive_checkout_3ds_declined
  property_count: 1
  slug: riskified-adaptive-checkout-3ds-declined
- name: adaptive_checkout_psd2_approved
  property_count: 1
  slug: riskified-adaptive-checkout-psd2-approved
- name: advise_3ds_response
  property_count: 1
  slug: riskified-advise-3ds-response
- name: advise_cvv_response
  property_count: 1
  slug: riskified-advise-cvv-response
- name: advise_psd2_response
  property_count: 1
  slug: riskified-advise-psd2-response
- name: Cancel_Response
  property_count: 1
  slug: riskified-cancel-response
- name: chargeback_response
  property_count: 1
  slug: riskified-chargeback-response
- name: Claim_Create_Response_Approve
  property_count: 2
  slug: riskified-claim-create-response-approve
- name: Claim_Create_Response_Captured
  property_count: 2
  slug: riskified-claim-create-response-captured
- name: Claim_Create_Response_Decline
  property_count: 2
  slug: riskified-claim-create-response-decline
- name: Claim_Create_Response_Excluded
  property_count: 2
  slug: riskified-claim-create-response-excluded
- name: Claim_Create_Response_Review
  property_count: 2
  slug: riskified-claim-create-response-review
- name: ClaimDecisionRequest
  property_count: 1
  slug: riskified-claim-decision-request
- name: customer_create_response
  property_count: 3
  slug: riskified-customer-create-response
- name: customer_create
  property_count: 9
  slug: riskified-customer-create
- name: customer_update
  property_count: 10
  slug: riskified-customer-update
- name: decide_response_approve
  property_count: 1
  slug: riskified-decide-response-approve
- name: decide_response_decline
  property_count: 1
  slug: riskified-decide-response-decline
- name: login_action_response
  property_count: 2
  slug: riskified-login-action-response
- name: login_action
  property_count: 14
  slug: riskified-login-action
- name: OtpInitiateRequest
  property_count: 5
  slug: riskified-otp-initiate-request
- name: OtpInitiateResponse
  property_count: 1
  slug: riskified-otp-initiate-response
- name: refund_response
  property_count: 1
  slug: riskified-refund-response
- name: reset_password_action
  property_count: 7
  slug: riskified-reset-password-action
- name: submit_response_submitted
  property_count: 1
  slug: riskified-submit-response-submitted
jsonld:
- class_count: 113
  name: Riskified Context
  property_count: 264
  slug: riskified-context
layout: provider
modified: '2026-05-25'
name: Riskified
nav: Providers
network: true
overview: 'Riskified publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Automation Endpoints API, Customer Actions API, Customer Management API, and 13 more. Tagged areas include Fraud Prevention, Chargebacks, E-Commerce, Payments, and Risk Management.


  The Riskified catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Riskified''s developer surface includes support, developer portal, API reference, getting-started guide, authentication, documentation, engineering blog, and 59 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Riskified API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: riskified-rules
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 26.1
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 73.0
    developer_ergonomics: 73.8
    discoverability: 71.4
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 22.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
- Fraud Prevention
- Chargebacks
- E-Commerce
- Payments
- Risk Management
- Machine Learning
- Account Takeover
- Policy Abuse
- 3D
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
website: https://www.riskified.com/
---
