---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The NPP API Framework defines the mandatory technical approach and data attributes for APIs built on the New Payments Platform, aligned to the ISO 20022 messaging standard. NPP Australia does not itse
  name: NPP API Framework
  slug: npp-api-framework
- description: PayTo is NPP's real-time, digital mandated-debit overlay service. It lets businesses initiate real-time payments from a customer's bank account under a pre-authorised agreement, giving consumers visib
  name: PayTo
  slug: payto
- description: 'PayID is NPP''s addressing service, allowing payments to be directed using a simple identifier such as a mobile number, email address, ABN or organisation ID instead of a BSB and account number. It is '
  name: PayID
  slug: payid
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/npp-australia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/npp-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auspayplus.com.au/solutions/npp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developers.auspayplus.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auspayplus.com.au/solutions/npp-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.developers.auspayplus.com.au/apis/
- group: start
  title: ''
  type: Sandbox
  url: https://nppa-developer.swift.com/user/register
- group: start
  title: ''
  type: SignUp
  url: https://www.developers.auspayplus.com.au/api/auth/signup/
- group: start
  title: ''
  type: Login
  url: https://www.developers.auspayplus.com.au/api/auth/login/
- group: company
  title: ''
  type: Blog
  url: https://www.auspayplus.com.au/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auspayplus/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auspayplus.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auspayplus.com.au/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.developers.auspayplus.com.au/go-live/
- group: operate
  title: ''
  type: Support
  url: https://www.developers.auspayplus.com.au/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auspayplus
- group: agent
  title: ''
  type: WellKnown
  url: well-known/npp-australia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/npp-australia-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/npp-australia-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/npp-australia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/npp-australia-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.auspayplus.com.au/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/npp-australia-llms.txt
created: '2026-07-24'
description: 'NPP Australia is the operator of the New Payments Platform (NPP), Australia''s national real-time, data-rich, account-to-account payments infrastructure that settles 24 hours a day, 365 days a year across more than 100 connected banks, credit unions, fintechs and government agencies. Since 2021 NPP Australia has been a wholly owned subsidiary of Australian Payments Plus (AP+), the entity formed by amalgamating NPP Australia, BPAY Group and eftpos. On top of the core clearing-and-settlement rail, NPP operates two overlay services: PayID, an addressing service that maps a mobile number, email, ABN or organisation ID to a bank account, and PayTo, a real-time mandated-debit capability that gives consumers visibility and control over recurring and one-off account debits. Its home market is Australia, and it sits alongside the Consumer Data Right as the country''s payments spine. Its API posture is that of a scheme and rail operator rather than a self-serve PSP: NPP Australia itself
  does not sell a public API, but it publishes the ISO 20022-aligned NPP API Framework that defines the mandatory technical approach and data attributes NPP Participants implement, and AP+ runs a (registration-gated) developer portal plus a SWIFT-hosted API sandbox. The consumable APIs are offered by NPP Participants, not by NPP Australia.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: NPP Australia (AP+)
nav: Providers
network: true
overview: 'NPP Australia (AP+) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and ISO 20022.


  NPP Australia (AP+)''s developer surface includes documentation, API reference, sandbox, signup flow, engineering blog, getting-started guide, support, and 16 more developer resources.'
random_paper: 36
score:
  band: thin
  composite: 31.8
  delta: -3.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 35.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Npp Australia Authentication
  slug: npp-australia-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Npp Australia Domain Security
  slug: npp-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Npp Australia Vulnerability Disclosure
  slug: npp-australia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: npp-australia
tags:
- Payments
- Australia
- Real-Time Payments
- Account-to-Account
- ISO 20022
- Payment Scheme
- Rails
- PayTo
- PayID
- Open Banking
website: https://www.auspayplus.com.au/solutions/npp
---
