---
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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Aduna's aggregated implementation of the CAMARA Number Verification API (v2.1), confirming possession of a mobile phone number in real time by verifying it directly against the carrier network with mi
  name: Aduna Number Verification API
  slug: aduna-number-verification-api
- description: Aduna's aggregated implementation of the CAMARA SIM Swap API, returning real-time information about recent SIM card changes associated with a mobile phone number so an application can detect account-t
  name: Aduna SIM Swap API
  slug: aduna-sim-swap-api
- description: Aduna's aggregated implementation of the CAMARA KYC Match API, comparing customer-supplied identity attributes — name, phone number, birthdate, address, email — against the verified KYC data held by t
  name: Aduna KYC Match API
  slug: aduna-kyc-match-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/aduna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aduna-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aduna-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aduna-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aduna-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aduna-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aduna-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aduna-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/aduna-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aduna-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aduna-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aduna-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aduna-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aduna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/adunaglobal
- group: company
  title: ''
  type: Website
  url: https://adunaglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adunaglobal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.adunaglobal.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adunaglobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adunaglobal/
- group: company
  title: ''
  type: Blog
  url: https://adunaglobal.com/resources/
- group: operate
  title: ''
  type: PressReleases
  url: https://adunaglobal.com/resources/?contentType=Newsroom
- group: operate
  title: ''
  type: Contact
  url: https://adunaglobal.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://adunaglobal.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://portal.adunaglobal.com/login
- group: operate
  title: ''
  type: Roadmap
  url: https://adunaglobal.com/work-with-us/availability/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/adunaglobal/nv2-asp-server-java-aduna-sdk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adunaglobal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adunaglobal.com/privacy-notice/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://adunaglobal.com/code-of-conduct/
- group: other
  title: ''
  type: Availability
  url: https://adunaglobal.com/work-with-us/availability/
created: '2026-07-25'
description: 'Aduna is the Ericsson-led network API joint venture — a 50:50 company owned half by Ericsson (Stockholm, Sweden) and half by twelve global communications service providers including AT&T, Bharti Airtel, Deutsche Telekom, KDDI, Orange, Reliance Jio, Singtel, Telefonica, Telstra, T-Mobile, Verizon and Vodafone, with e& added later as an equity partner. Announced from Stockholm and incorporated as Aduna Global, LLC, it exists to aggregate CAMARA-standardised mobile network APIs from many carriers into one commercial channel so that developers do not have to negotiate operator by operator. Aduna sits in the exposure layer of the telecom value chain: it does not own spectrum and it does not sell to developers directly at scale — it aggregates operator capability and reaches the market through partner platforms (Google Cloud, Infobip, Sinch, Vonage, Microsoft Azure and the Azure Marketplace, Comviva on AWS, Bridge Alliance). Its API posture is honestly partner-gated. The public website
  documents an API catalogue in prose but publishes no OpenAPI, no sandbox and no self-serve signup; the developer documentation at docs.adunaglobal.com redirects every path to an Auth0 login wall at portal.adunaglobal.com, and the SDK onboarding instruction is to contact Aduna Global. The one genuinely open surface is a small set of source-available first-party SDK repositories on GitHub for CAMARA Number Verification v2, which are the only place Aduna''s real endpoints, OAuth scopes and CIBA flow are publicly visible.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Aduna
nav: Providers
network: true
overview: 'Aduna publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Sweden, Network APIs, CAMARA, and Open Gateway.


  Aduna''s developer surface includes authentication, changelog, documentation, engineering blog, support, and 26 more developer resources.'
random_paper: 35
scopes:
- name: Aduna Scopes
  scope_count: 4
  slug: aduna-scopes
  summary_line: 4 scopes · authorizationCode/urn:ietf:params:oauth:grant-type:jwt-bearer/ciba
score:
  band: thin
  composite: 36.5
  delta: 7.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 28.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Aduna Authentication
  slug: aduna-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Aduna Domain Security
  slug: aduna-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aduna Vulnerability Disclosure
  slug: aduna-vulnerability-disclosure
  summary_line: Hackerone
slug: aduna
tags:
- Telecommunications
- Sweden
- Network APIs
- CAMARA
- Open Gateway
- API Aggregator
- Identity Verification
- SIM Swap
- Number Verification
- Fraud Prevention
- Quality on Demand
- Device Location
- Ericsson
website: https://adunaglobal.com/
---
