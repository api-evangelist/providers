---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Konsentus Agentic Access
  operation_count: 1
  slug: konsentus-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'Managed service that maintains the up-to-date eIDAS certificate trust chain required to secure PSD2 Open Banking API traffic. Removes the burden of tracking EU trusted list updates, QTSP changes, and '
  name: Konsentus Certificate Chain Service API
  slug: konsentus-certificate-chain-service-api
- description: End-to-end platform used by central banks and market operators to build, manage, and maintain national or regional open finance trust frameworks. Covers participant onboarding, directory services, cer
  name: Konsentus Open Trust Platform
  slug: konsentus-open-trust-platform
- baseURL: https://api.konsentus.com
  baseurl_source: declared
  description: Third-Party Provider identity and regulatory validation
  name: Konsentus PSP Checking Service API
  slug: konsentus-psp-checking-service-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Konsentus Verify PSP Checking Service API
  slug: open-konsentus-psp-checking-service-api
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
random_paper: 15
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 54.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Financial-Services
website: https://www.konsentus.com
---
