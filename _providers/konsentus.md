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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 49.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Konsentus Agentic Access
  operation_count: 1
  slug: konsentus-agentic-access
  summary_line: 1 operation
api_count: 3
apis:
- description: 'Managed service that maintains the up-to-date eIDAS certificate trust chain required to secure PSD2 Open Banking API traffic. Removes the burden of tracking EU trusted list updates, QTSP changes, and '
  name: Konsentus Certificate Chain Service API
  slug: konsentus-certificate-chain-service-api
- description: End-to-end platform used by central banks and market operators to build, manage, and maintain national or regional open finance trust frameworks. Covers participant onboarding, directory services, cer
  name: Konsentus Open Trust Platform
  slug: konsentus-open-trust-platform
- description: Third-Party Provider identity and regulatory validation
  name: Konsentus PSP Checking Service API
  slug: konsentus-psp-checking-service-api
artifact_total: 20
collections:
- collection_type: open
  name: Konsentus Verify API
  slug: open-konsentus-verify-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/konsentus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/konsentus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/konsentus-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.konsentus.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.konsentus.com/api-reference/introduction.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.psd.konsentus.com/
- group: docs
  title: ''
  type: Swagger
  url: https://swagger.konsentus.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.konsentus.com/api-reference/getting-started.html
- group: auth
  title: ''
  type: Authentication
  url: https://developers.konsentus.com/api-reference/fi-authentication.html
- group: design
  title: ''
  type: Versioning
  url: https://developers.konsentus.com/api-reference/endpoint-versioning.html
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.konsentus.com/api-reference/error-codes.html
- group: other
  title: ''
  type: Glossary
  url: https://developers.konsentus.com/api-reference/glossary.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.konsentus.com/api-reference/release-notes.html
- group: operate
  title: ''
  type: Support
  url: https://developers.konsentus.com/api-reference/support.html
- group: operate
  title: ''
  type: FAQ
  url: https://developers.konsentus.com/api-reference/faqs.html
- group: start
  title: ''
  type: Sandbox
  url: https://www.konsentus.com/first-psd2-open-banking-tpp-sandbox/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.konsentus.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.konsentus.com/terms-conditions
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.konsentus.com/acceptable-use-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.konsentus.com/cookie-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.konsentus.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.konsentus.com/content-hub
- group: operate
  title: ''
  type: PressReleases
  url: https://www.konsentus.com/press-releases
- group: other
  title: ''
  type: Events
  url: https://www.konsentus.com/events
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/konsentus/
- group: other
  title: ''
  type: X
  url: https://twitter.com/konsentus/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/konsentus
created: '2026-05-25'
description: Konsentus is a UK-headquartered specialist provider of identity verification and trust services for open banking and open finance ecosystems. Its flagship Konsentus Verify SaaS API gives Financial Institutions (ASPSPs) real-time PSD2 Third-Party Provider (TPP) identity and regulatory checking against National Competent Authority registers across the EEA, validating eIDAS, OBIE, and OBHD certificates with the issuing Qualified Trust Service Provider. The Konsentus Certificate Chain Service keeps the eIDAS trust chain current, and the Konsentus Open Trust Platform plus advisory practice helps central banks and market operators stand up national open finance trust frameworks under PSD2, PSD3, and FiDA. Trusted by 250+ financial institutions globally.
features:
- Real-time Third-Party Provider (TPP) identity verification via eIDAS certificates
- Real-time TPP regulatory status checking against National Competent Authority (NCA) registers on a pan-EEA basis
- Support for eIDAS, OBIE, and OBHD certificate test scenarios
- Certificate Chain Service tracking EU trusted list, QTSP changes, and root/intermediate rotation
- Immutable audit log of every identity and regulatory check
- Access token issuance, validation, and lifecycle management on behalf of the ASPSP (OAuth 2.0)
- Directory of 5,000+ regulated PISPs, AISPs, and ASPSPs
- Deployment as SaaS API, customer portal, or on-premise
- Customisable data feed frequency to match business requirements
- Pay-only-for-what-you-consume commercial model
- Konsentus Open Trust Platform for central banks and market operators building open finance frameworks
- Advisory and training services for PSD2, PSD3, and FiDA market participants
- 250+ financial institutions on the platform with claimed 100% uptime
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/konsentus.png
layout: provider
modified: '2026-05-25'
name: Konsentus
nav: Providers
network: true
overview: 'Konsentus publishes 1 API on the [APIs.io](https://apis.io/) network: PSP Checking Service API. Tagged areas include Open Banking, Open Finance, PSD2, PSD3, and FiDA.


  Konsentus'' developer surface includes authentication, developer portal, documentation, getting-started guide, release notes, support, FAQ, and 20 more developer resources.'
random_paper: 33
score:
  band: thin
  composite: 40.2
  delta: 0.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.9
    developer_ergonomics: 52.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.6
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/konsentus/refs/heads/main/screenshots/konsentus-2026-06-20T184135.png
security:
- kind: authentication
  name: Konsentus Authentication
  slug: konsentus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Konsentus Domain Security
  slug: konsentus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: konsentus
tags:
- Open Banking
- Open Finance
- PSD2
- PSD3
- FiDA
- TPP Verification
- Identity
- eIDAS
- Trust Services
- Regulatory Checking
- Financial Services
website: https://www.konsentus.com
---
