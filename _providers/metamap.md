---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 51
  human_in_the_loop: 6
  name: Metamap Agentic Access
  operation_count: 53
  slug: metamap-agentic-access
  summary_line: 53 operations · 51 acting · 6 human-in-the-loop
api_count: 10
apis:
- description: The Authentication API from MetaMap — 2 operation(s) for authentication.
  name: MetaMap Authentication API
  slug: metamap-authentication-api
- description: The Background Checks API from MetaMap — 2 operation(s) for background checks.
  name: MetaMap Background Checks API
  slug: metamap-background-checks-api
- description: The Credit Checks API from MetaMap — 1 operation(s) for credit checks.
  name: MetaMap Credit Checks API
  slug: metamap-credit-checks-api
- description: The Custom Watchlists API from MetaMap — 1 operation(s) for custom watchlists.
  name: MetaMap Custom Watchlists API
  slug: metamap-custom-watchlists-api
- description: The Email Checks API from MetaMap — 2 operation(s) for email checks.
  name: MetaMap Email Checks API
  slug: metamap-email-checks-api
- description: The GovChecks API from MetaMap — 34 operation(s) for govchecks.
  name: MetaMap GovChecks API
  slug: metamap-govchecks-api
- description: The Phone Checks API from MetaMap — 2 operation(s) for phone checks.
  name: MetaMap Phone Checks API
  slug: metamap-phone-checks-api
- description: The Verifications API from MetaMap — 7 operation(s) for verifications.
  name: MetaMap Verifications API
  slug: metamap-verifications-api
- description: The Watchlist Checks API from MetaMap — 1 operation(s) for watchlist checks.
  name: MetaMap Watchlist Checks API
  slug: metamap-watchlist-checks-api
- description: The Webhooks API from MetaMap — 1 operation(s) for webhooks.
  name: MetaMap Webhooks API
  slug: metamap-webhooks-api
artifact_total: 77
collections:
- collection_type: postman
  name: MetaMap Authentication API
  slug: postman-metamap-authentication-api
- collection_type: postman
  name: MetaMap Authentication Background Checks API
  slug: postman-metamap-background-checks-api
- collection_type: postman
  name: MetaMap Authentication Credit Checks API
  slug: postman-metamap-credit-checks-api
- collection_type: postman
  name: MetaMap Authentication Custom Watchlists API
  slug: postman-metamap-custom-watchlists-api
- collection_type: postman
  name: MetaMap Authentication Email Checks API
  slug: postman-metamap-email-checks-api
- collection_type: postman
  name: MetaMap Authentication GovChecks API
  slug: postman-metamap-govchecks-api
- collection_type: postman
  name: MetaMap Authentication Phone Checks API
  slug: postman-metamap-phone-checks-api
- collection_type: postman
  name: MetaMap Authentication Verifications API
  slug: postman-metamap-verifications-api
- collection_type: postman
  name: MetaMap Authentication Watchlist Checks API
  slug: postman-metamap-watchlist-checks-api
- collection_type: postman
  name: MetaMap Authentication Webhooks API
  slug: postman-metamap-webhooks-api
- collection_type: open
  name: MetaMap API
  slug: open-metamap
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/metamap/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metamap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metamap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metamap-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://metamap.com
- group: company
  title: ''
  type: AboutUs
  url: https://metamap.com/about-metamap
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/why-metamap
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/verification-tools-library
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/all-industries
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/kyc-solutions-aml-compliance/
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/banking-industry-kyc-solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/fintech-kyc-solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/lending-payments-kyc-solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/telecommunication-kyc-solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/transportation-kyc-solutions/
- group: operate
  title: ''
  type: Contact
  url: https://metamap.com/contact-metamap
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/careers
- group: company
  title: ''
  type: Press
  url: https://metamap.com/press-and-media/
- group: docs
  title: ''
  type: Documentation
  url: https://metamap.com/resources-home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metamap.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metamap.com
- group: start
  title: ''
  type: Signup
  url: https://dashboard.getmati.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.getmati.com/dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metamap.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/single-sign-on
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/metamaps
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/merits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/metamap-button
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/verification-results
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/custom-encryption
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/sdk-customization
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/document-verification
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/biometrics
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/govcheck
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/list-of-government-checks-by-country
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/location-intelligence
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/uam
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/facematch
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/email-check
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/phone-check
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/anti-money-laundering
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/custom-watchlists
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/e-signature
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/credit-check
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/tax-data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/background-check
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/video-agreement-1
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metamap.com/docs/on-demand-configuration-odc
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/webhook-specifications
- group: operate
  title: ''
  type: FAQ
  url: https://docs.metamap.com/docs/webhook-faq
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.metamap.com/docs/errors
- group: build
  title: ''
  type: SDKs
  url: https://docs.metamap.com/docs/sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metamap.com/docs/quick-start-6
- group: build
  title: ''
  type: SDKs
  url: https://docs.metamap.com/docs/android
- group: build
  title: ''
  type: SDKs
  url: https://docs.metamap.com/docs/ios
- group: build
  title: ''
  type: SDKs
  url: https://docs.metamap.com/docs/quick-start-1
- group: build
  title: ''
  type: SDKs
  url: https://docs.metamap.com/docs/quick-start-3
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.metamap.com/docs/android-changelog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.metamap.com/docs/ios-changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetMetaMap
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/metamap-android-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/metamap-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/metamap-flutter-plugin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/metamap-reactnative-plugin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/metamap-cordova-plugin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/metamap-capacitor-plugin
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/GetMetaMap/metamap-mobile-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/GetMetaMap/metamap-android-demo-kotlin
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/GetMetaMap/metamap-demo-web-apps
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/GetMetaMap/iOS_app_with_web_sdk_integration
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/GetMetaMap/android_app_with_web_sdk_integration
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/mati-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/mati_ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/GetMetaMap/mati-node
- group: commercial
  title: ''
  type: Pricing
  url: https://metamap.com/contact-metamap
- group: start
  title: ''
  type: Signup
  url: https://dashboard.getmati.com/
- group: start
  title: ''
  type: Sandbox
  url: https://dashboard.getmati.com/
- group: operate
  title: ''
  type: Forums
  url: https://docs.metamap.com/discuss
- group: commercial
  title: ''
  type: Plans
  url: plans/metamap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metamap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/metamap-finops.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/metamap/trust/home
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/biometric-verification-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/document-verification-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/location-intelligence-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/customer-access-management-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/custom-watchlist-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/email-check-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/phone-check-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/video-agreement-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://docs.metamap.com/docs/webhook-messages
- group: company
  title: ''
  type: Blog
  url: https://metamap.com/feed/
created: '2026-05-25'
description: MetaMap (formerly Mati) is an identity verification platform founded in 2017 in San Francisco and headquartered there, serving 600+ companies across 50+ countries with a focus on Latin America, Africa, and other emerging markets. The platform combines document verification, biometric liveness, facematch, watchlist screening, behavioral risk signals, and 40+ government-database "GovChecks" to power KYC, AML compliance, customer onboarding, authentication, and financial risk management workflows for banks, fintechs, lenders, telcos, and transportation providers. Developers integrate via a REST API on api.prod.metamap.com, configurable workflows ("metamaps"), webhooks, and native SDKs for Web, iOS, Android, Flutter, React Native, Cordova, and Capacitor. MetaMap joined Incode in 2024 to expand identity-verification coverage globally.
examples:
- key_count: 2
  name: Metamap Authentication Example
  slug: metamap-authentication-example
- key_count: 2
  name: Metamap Comply Advantage Example
  slug: metamap-comply-advantage-example
- key_count: 2
  name: Metamap Govcheck Mexico Curp Example
  slug: metamap-govcheck-mexico-curp-example
- key_count: 2
  name: Metamap Start Verification Example
  slug: metamap-start-verification-example
features:
- Customer onboarding with configurable verification workflows ("Metamaps")
- Document verification with reading, alteration detection, and validity scoring
- Biometric verification with liveness detection and selfie capture
- Facematch service for biometric comparison between document and selfie or two arbitrary faces
- 40+ Government Database Checks (GovChecks) across LatAm, Africa, and Asia
- GovChecks - Brazil (CPF, CPF-light, CNPJ extended validation)
- GovChecks - Chile (Registro Civil)
- GovChecks - Colombia (Civil Registry, Migration, RUES, PPT, Unified Legal Search)
- GovChecks - Costa Rica (TSE)
- GovChecks - Dominican Republic (RNC)
- GovChecks - Mexico (CURP, INE, RFC, RFC Status, PEP)
- GovChecks - Panama (TSE with optional facematch)
- GovChecks - Paraguay (RCP)
- GovChecks - Peru (GovCheck, Migration Institute, SUNAT)
- GovChecks - Uruguay (Registro Civil)
- GovChecks - Ghana (Ghana Card with optional facematch)
- GovChecks - Kenya (BRS, IPRS)
- GovChecks - Nigeria (NIN, VIN, Driver License, CAC, TIN, CAC Affiliates)
- GovChecks - Philippines (UMID / SSN)
- Watchlist screening via Comply Advantage (international sanctions, PEPs, adverse media)
- Custom Watchlist upload and check
- Email Check (ownership OTP and behavioral risk scoring)
- Phone Check (SMS OTP ownership and risk scoring)
- Credit Check (Brazil Serasa integration)
- Background Checks (Mexico and Brazil court records)
- Location Intelligence (geo-restriction and VPN detection)
- Customer Access Management (re-verification of existing biometric identities)
- E-Signature with identity authentication
- Video Agreement capture
- Tax Check against tax-agency records
- Custom Input and Custom Document templates
- Webhook delivery of all verification, step, and error events
- On-Demand Configuration (ODC) for runtime metamap selection
- SDK Cooldown to prevent duplicate verifications from a single origin
- Custom Encryption for verification payloads
- Web button and direct-link integration plus iOS, Android, Flutter, React Native, Cordova, and Capacitor SDKs
- PDF download of verification results
- Verification media (documents, photos, videos) retrieval via signed URLs
- Identity dashboard with verification review, audit logs, and SSO
finops:
- name: Metamap Finops
  service_category: Identity Verification and Compliance
  slug: metamap-finops
image: https://files.readme.io/8daff99-MetaMap_logo.svg
json_schemas:
- name: MetaMap GovCheck
  property_count: 4
  slug: metamap-govcheck
- name: MetaMap Verification
  property_count: 10
  slug: metamap-verification
- name: MetaMap Webhook Event
  property_count: 7
  slug: metamap-webhook
json_structures:
- name: Metamap Verification Structure
  property_count: 10
  slug: metamap-verification-structure
jsonld:
- class_count: 0
  name: Metamap Context
  property_count: 10
  slug: metamap-context
layout: provider
modified: '2026-05-25'
name: MetaMap
nav: Providers
network: true
overview: 'MetaMap publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Background Checks API, Credit Checks API, and 7 more. Tagged areas include Identity Verification, KYC, AML, Anti-Money Laundering, and Compliance.


  The MetaMap catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MetaMap''s developer surface includes authentication, developer portal, documentation, signup flow, getting-started guide, FAQ, changelog, and 88 more developer resources.'
plans:
- name: Metamap Plans Pricing
  plan_count: 2
  slug: metamap-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Metamap Rate Limits
  slug: metamap-rate-limits
rules:
- name: MetaMap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: metamap-jsonschema-spectral-rules
- name: MetaMap API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 4
  slug: metamap-rules
score:
  band: strong
  composite: 62.9
  delta: -3.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 70.4
    developer_ergonomics: 67.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metamap/refs/heads/main/screenshots/metamap-2026-06-20T185250.png
security:
- kind: authentication
  name: Metamap Authentication
  slug: metamap-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Metamap Domain Security
  slug: metamap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metamap
tags:
- Identity Verification
- KYC
- AML
- Anti-Money Laundering
- Compliance
- Biometrics
- Document Verification
- Facematch
- Liveness
- GovCheck
- Watchlist
- Background Check
- Credit Check
- Risk
- Fraud Prevention
- Onboarding
- LatAm
- Africa
- Mobile SDK
website: https://metamap.com
---
