---
access_model:
  confidence: medium
  label: Partner onboarding / OBIE Dynamic Client Registration
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Algbra Agentic Access
  operation_count: 8
  slug: algbra-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 4
apis:
- description: Algbra's UK Open Banking Account & Transaction Information (AIS) dedicated interface, conformant to the OBIE Read/Write Standard v3.1, enabling authorised AISP Third Party Providers to create account-
  name: Algbra Account and Transaction Information API (AIS)
  slug: algbra-account-transaction-api
- description: Algbra's UK Open Banking Payment Initiation (PIS) dedicated interface under the OBIE Read/Write Standard v3.1.8, allowing authorised PISP Third Party Providers to initiate payments on a customer's beh
  name: Algbra Payment Initiation API (PIS)
  slug: algbra-payment-initiation-api
- description: Algbra's UK Open Banking Confirmation of Funds (CBPII) dedicated interface under the OBIE Read/Write Standard v3.1.8, allowing authorised CBPII Third Party Providers to confirm the availability of fun
  name: Algbra Confirmation of Funds API (CBPII)
  slug: algbra-confirmation-of-funds-api
- description: Algbra Labs' first-party Partner Banking (Banking-as-a-Service) API for B2B partners, covering customer onboarding and compliance checks, primary and virtual accounts, card issuing, internal/inbound/o
  name: Algbra Partner Banking API
  slug: algbra-partner-banking-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create an OBIE account-access consent, confirm it is authorised, then read the customer's accounts, balances and transactions through Algbra's UK Open Banking (AIS) dedicated interface. All operationI
  name: Algbra OBIE account-access and read
  slug: algbra-account-access-flow
artifact_total: 12
asyncapis:
- description: ''
  name: Algbra Partner Banking Webhooks
  slug: algbra-partner-banking-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/algbra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/algbra-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/algbra-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/algbra-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/algbra-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/algbra-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/algbra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/algbra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/algbra-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/algbra-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/algbra-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/algbra-account-transaction-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/algbra-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/algbra-account-access-flow.yml
- group: auth
  title: ''
  type: Security
  url: https://www.algbra.com/responsible-disclosure/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.algbralabs.com/partner-banking/getting-started
- group: company
  title: ''
  type: Website
  url: https://www.algbra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.algbralabs.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://developer.algbralabs.com/open-banking-uk/introduction
- group: start
  title: ''
  type: SignUp
  url: https://developer.algbralabs.com/partner-banking/getting-started/partner-onboarding
- group: company
  title: ''
  type: Blog
  url: https://www.algbra.com/news/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.algbra.com/fees-and-charges/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.algbra.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.algbra.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.algbra.com/help/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.algbra.com/responsible-disclosure/
- group: company
  title: ''
  type: LinkedIn
  url: https://algbra.com/socials/linkedin
created: '2026-07-23'
description: Algbra is a UK values-based, sustainability-focused fintech operated by Algbra FS UK Limited (company number 12629086), an electronic money institution authorised by the Financial Conduct Authority under the Electronic Money Regulations 2011 (FRN 952360); its parent, Algbra Group Limited, is a certified B Corporation. Rather than a licensed clearing bank or building society, Algbra is a challenger provider of ethical multi-currency accounts, cards, savings and Banking-as-a-Service infrastructure. Through the Algbra Labs developer platform it exposes two API surfaces - a first-party Partner Banking (BaaS) API for onboarding, accounts, cards, payments and transactions, and a UK Open Banking dedicated interface conformant to the Open Banking Implementation Entity (OBIE) Read/Write Standard v3.1.8 covering Account & Transaction Information (AIS), Payment Initiation (PIS) and Confirmation of Funds (CBPII), delivered via the Tell Money (Tell Connect) platform. As a non-CMA9 ASPSP
  it meets PSD2 access-to-account obligations, securing the interface with FAPI-grade OAuth2/OIDC, mutual-TLS using OBIE OBWAC/OBSEAL eIDAS certificates, PS256 request-object signing, Dynamic Client Registration (DCR v3.2) and PSD2 strong customer authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Algbra
nav: Providers
network: true
overview: 'Algbra publishes 1 API on the [APIs.io](https://apis.io/) network: Account and Transaction Information API (AIS). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  The Algbra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Algbra''s developer surface includes authentication, sandbox, getting-started guide, documentation, signup flow, engineering blog, pricing, and 21 more developer resources.'
random_paper: 64
scopes:
- name: Algbra Scopes
  scope_count: 4
  slug: algbra-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 49.7
  delta: -3.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 78.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/algbra/refs/heads/main/screenshots/algbra-2026-07-25T195604.png
security:
- kind: authentication
  name: Algbra Authentication
  slug: algbra-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Algbra Domain Security
  slug: algbra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Algbra Vulnerability Disclosure
  slug: algbra-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: algbra
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Fintech
- Ethical Finance
- Banking as a Service
website: https://www.algbra.com/
---
