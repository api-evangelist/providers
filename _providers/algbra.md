---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Algbra Agentic Access
  operation_count: 8
  slug: algbra-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: Algbra's UK Open Banking Payment Initiation (PIS) dedicated interface under the OBIE Read/Write Standard v3.1.8, allowing authorised PISP Third Party Providers to initiate payments on a customer's beh
  name: Algbra Payment Initiation API (PIS)
  slug: algbra-payment-initiation-api
- description: Algbra's UK Open Banking Confirmation of Funds (CBPII) dedicated interface under the OBIE Read/Write Standard v3.1.8, allowing authorised CBPII Third Party Providers to confirm the availability of fun
  name: Algbra Confirmation of Funds API (CBPII)
  slug: algbra-confirmation-of-funds-api
- description: Algbra Labs' first-party Partner Banking (Banking-as-a-Service) API for B2B partners, covering customer onboarding and compliance checks, primary and virtual accounts, card issuing, internal/inbound/o
  name: Algbra Partner Banking API
  slug: algbra-partner-banking-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Accounts API from Algbra — 2 operation(s) for accounts.
  name: Algbra Accounts API
  slug: algbra-accounts-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Transactions API from Algbra — 1 operation(s) for transactions.
  name: Algbra Transactions API
  slug: algbra-transactions-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Automated Payments API from Algbra — 4 operation(s) for automated payments.
  name: Algbra Automated Payments API
  slug: algbra-automated-payments-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Cards API from Algbra — 1 operation(s) for cards.
  name: Algbra Cards API
  slug: algbra-cards-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Compliance API from Algbra — 4 operation(s) for compliance.
  name: Algbra Compliance API
  slug: algbra-compliance-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Customers API from Algbra — 4 operation(s) for customers.
  name: Algbra Customers API
  slug: algbra-customers-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Investments API from Algbra — 5 operation(s) for investments.
  name: Algbra Investments API
  slug: algbra-investments-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Onboarding Prospects - Business API from Algbra — 3 operation(s) for onboarding prospects - business.
  name: Algbra Onboarding Prospects - Business API
  slug: algbra-onboarding-prospects-business-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Onboarding Prospects - Personal API from Algbra — 3 operation(s) for onboarding prospects - personal.
  name: Algbra Onboarding Prospects - Personal API
  slug: algbra-onboarding-prospects-personal-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Partner API from Algbra — 2 operation(s) for partner.
  name: Algbra Partner API
  slug: algbra-partner-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Partners API from Algbra — 2 operation(s) for partners.
  name: Algbra Partners API
  slug: algbra-partners-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Payment Simulations API from Algbra — 5 operation(s) for payment simulations.
  name: Algbra Payment Simulations API
  slug: algbra-payment-simulations-api
- baseURL: https://secure.tell.systems/algbra/open-banking/v3.1/pisp
  baseurl_source: declared
  description: The Payments API from Algbra — 12 operation(s) for payments.
  name: Algbra Payments API
  slug: algbra-payments-api
arazzos:
- description: Create an OBIE account-access consent, confirm it is authorised, then read the customer's accounts, balances and transactions through Algbra's UK Open Banking (AIS) dedicated interface. All operationI
  name: Algbra OBIE account-access and read
  slug: algbra-account-access-flow
artifact_total: 26
asyncapis:
- description: ''
  name: Algbra Partner Banking Webhooks
  slug: algbra-partner-banking-webhooks
collections:
- collection_type: open
  name: Account and Transaction API Specification
  slug: open-algbra-account-transaction-api
common:
- group: agent
  href: https://artifacts.apis.io/algbra/agentic-access/algbra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/algbra-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/algbra/security/algbra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algbra-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/algbra/scopes/algbra-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/algbra-scopes.yml
- group: auth
  href: https://artifacts.apis.io/algbra/authentication/algbra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algbra-authentication.yml
- group: design
  href: https://artifacts.apis.io/algbra/conventions/algbra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/algbra-conventions.yml
- group: design
  href: https://artifacts.apis.io/algbra/conventions/algbra-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/algbra-conventions.yml
- group: design
  href: https://artifacts.apis.io/algbra/conformance/algbra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algbra-conformance.yml
- group: design
  href: https://artifacts.apis.io/algbra/errors/algbra-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algbra-problem-types.yml
- group: design
  href: https://artifacts.apis.io/algbra/lifecycle/algbra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/algbra-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/algbra/data-model/algbra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algbra-data-model.yml
- group: start
  href: https://artifacts.apis.io/algbra/sandbox/algbra-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/algbra-sandbox.yml
- group: other
  href: https://artifacts.apis.io/algbra/overlays/algbra-account-transaction-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algbra-account-transaction-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/algbra/llms/algbra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algbra-llms.txt
- group: agent
  href: https://artifacts.apis.io/algbra/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/algbra/arazzo/algbra-account-access-flow.yml
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
overview: 'Algbra publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Transactions API, Automated Payments API, and 13 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  The Algbra catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Algbra''s developer surface includes authentication, sandbox, getting-started guide, documentation, signup flow, engineering blog, pricing, and 21 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Algbra API Rules
  rule_count: 43
  severity_counts:
    error: 34
    hint: 0
    info: 4
    warn: 5
  slug: algbra-rules
scopes:
- name: Algbra Scopes
  scope_count: 4
  slug: algbra-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 50.2
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 31.6
      derived: 0
      marker_coverage: 68.4
      total: 19
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/algbra/algbra-2026-07-25T195604.png
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
skill_count: 1
skills:
- name: Access Algbra account & transaction data (OBIE AIS)
  slug: algbra-account-access
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
