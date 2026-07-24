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
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Gigya / SAP Customer Data Cloud REST API for accounts, identity, social login, consent, and profile data. Endpoints are data-center scoped under {service}.{dc}.gigya.com (e.g. accounts.us1.gigya.com) '
  name: Gigya REST API (SAP Customer Data Cloud)
  slug: gigya-rest-api-sap-customer-data-cloud
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gigya-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sap.com/report-a-vulnerability
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_CUSTOMER_DATA_CLOUD
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gigya.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sap.com/about/trust-center.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gigya-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gigya-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/gigya-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gigya-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gigya-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gigya-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gigya-llms.txt
created: '2026-07-17'
description: Gigya is a customer identity and access management (CIAM) platform, acquired by SAP in 2017 and now delivered as SAP Customer Data Cloud. It provides Registration-as-a-Service (RaaS), social and passwordless login, progressive profiling, consent and preference management, and a unified customer profile store, exposed through a data-center-scoped REST API (accounts, socialize, ds, and related services under accounts.{dc}.gigya.com). Developers integrate via first-party SDKs for Web, iOS/Swift, Android, Flutter, React Native, and server-side Java, PHP, Python, and .NET, authenticating with a site API key plus signed application/user secrets or OAuth 2.0 client-credentials tokens. Originally a Mayfield-backed venture, Gigya's technology now underpins SAP's customer data and identity offering.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gigya.png
layout: provider
modified: '2026-07-19'
name: Gigya
nav: Providers
network: true
overview: 'Gigya publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Authentication, CIAM, and Customer Identity.


  Gigya''s developer surface includes documentation, authentication, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.8
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gigya Authentication
  slug: gigya-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Gigya Domain Security
  slug: gigya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gigya Vulnerability Disclosure
  slug: gigya-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gigya
tags:
- Company
- Identity
- Authentication
- CIAM
- Customer Identity
- OAuth
- Single Sign-On
- Consent Management
- SAP
website: https://developers.gigya.com/
---
