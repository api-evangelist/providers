---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  - '{''url'': ''https://www.tietoevry.com/en/'', ''status'': 301, ''note'': ''declared website redirects to https://www.tieto.com/en/ — a different registrable domain (tietoevry.com -> tieto.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-03'
api_count: 24
apis:
- baseURL: https://openbanking.api.tietoevry.com
  baseurl_source: declared
  description: PSD2-compliant Access to Account (XS2A) APIs implementing the Berlin Group NextGenPSD2 framework, plus Tietoevry premium extensions beyond the PSD2 mandate. Covers account information (AIS), payment i
  name: Tietoevry Open Banking XS2A APIs
  slug: tietoevry-openbanking-xs2a
- baseURL: https://aggregation.api.tieto.com
  baseurl_source: declared
  description: A single-integration aggregation layer over Nordic and Baltic banks, exposing provider discovery, end-user management and aggregated XS2A operations (accounts, balances, transactions, consents, confir
  name: Tietoevry Financial API Aggregation
  slug: tietoevry-financial-api-aggregation
- baseURL: https://payments.api.tieto.com/live/v1/sepadd
  baseurl_source: declared
  description: 'A SEPA Direct Debit gateway for Creditor and Debtor roles, allowing creditors to initiate payments, cancel (reverse) them and issue refunds, and debtors to reject payments and raise chargebacks, with '
  name: Tietoevry SEPA Direct Debits
  slug: tietoevry-sepa-direct-debits
- description: A credit platform used by banks and financial institutions in 20+ countries to manage virtually any type of credit, organised around loan origination, loan life cycle and collection. The developer por
  name: Tietoevry Credit Cloud
  slug: tietoevry-credit-cloud
artifact_total: 9
asyncapis:
- description: ''
  name: Tietoevry Sepa Direct Debit Webhooks
  slug: tietoevry-sepa-direct-debit-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tietoevry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tietoevry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tietoevry.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tietoevry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://openbanking.api.tietoevry.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://openbanking.api.tietoevry.com/documentation/xs2a
- group: start
  title: ''
  type: GettingStarted
  url: https://openbanking.api.tietoevry.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://openbanking.api.tietoevry.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://openbanking.api.tietoevry.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://openbanking.api.tietoevry.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://openbanking.api.tietoevry.com/faq
- group: other
  title: ''
  type: Glossary
  url: https://openbanking.api.tietoevry.com/documentation/glossary
- group: company
  title: ''
  type: Blog
  url: https://www.tieto.com/en/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tietoevry
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tietoevry.com/en/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tietoevry.com/en/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tietoevry
- group: build
  title: ''
  type: Packages
  url: packages/tietoevry-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tietoevry-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tietoevry-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tietoevry-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/tietoevry-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tietoevry-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tietoevry-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tietoevry-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tietoevry-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tietoevry-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tietoevry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tietoevry-rate-limits.yml
created: '2026-09-02'
description: 'TietoEVRY (Tietoevry Corporation, listed as TIETO on Nasdaq Helsinki and Stockholm, rebranded to "Tieto" in 2026) is a Nordic software and technology company of roughly 14,000 people operating in 20+ countries, serving banking, healthcare, public sector and industry. Its public API surface is published by the banking business (Tieto Banktech / Tietoevry Banking) through the Tietoevry Banking API Hub at api.tietoevry.com, which fronts three developer portals: an Open Banking PSD2/XS2A platform built on the Berlin Group NextGenPSD2 framework with a free self-service sandbox, a Financial API Aggregation service offering one integration to Nordic and Baltic banks, and a Credit Cloud platform for loan origination and loan life-cycle management. 24 machine-readable Swagger 2.0 / OpenAPI 3.0 contracts covering 211 operations are published unauthenticated from the Open Banking and Aggregation portals, including account information, payment initiation, confirmation of funds, bulk and
  periodic payments, payment recall, request-to-pay, signing baskets, virtual account management, card account information and a SEPA Direct Debits gateway with a webhook event-notification surface.'
image: https://www.tieto.com/images/tieto-logo.svg
layout: provider
modified: '2026-09-02'
name: TietoEVRY
nav: Providers
network: true
overview: 'TietoEVRY publishes 3 APIs on the [APIs.io](https://apis.io/) network: Open Banking XS2A APIs, Financial API Aggregation, and SEPA Direct Debits. Tagged areas include Company, Banking, Open Banking, PSD2, and XS2A.


  The TietoEVRY catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TietoEVRY''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 23 more developer resources.'
plans:
- name: Tietoevry Plans Pricing
  plan_count: 0
  slug: tietoevry-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Tietoevry Rate Limits
  slug: tietoevry-rate-limits
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 59.0
    developer_ergonomics: 66.1
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 52.1
  provenance:
    conformance: first-party
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Tietoevry Authentication
  slug: tietoevry-authentication
  summary_line: apiKey/openIdConnect/mutualTLS · 7 schemes
- kind: domain-security
  name: Tietoevry Domain Security
  slug: tietoevry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tietoevry
tags:
- Company
- Banking
- Open Banking
- PSD2
- XS2A
- Berlin Group
- Payments
- SEPA
- Account Information
- Financial Services
- Aggregation
- Credit
- Fintech
- Nordic
- Finland
website: https://www.tietoevry.com/en/
---
