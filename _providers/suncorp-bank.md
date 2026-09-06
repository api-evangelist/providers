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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Suncorp Bank Agentic Access
  operation_count: 19
  slug: suncorp-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- description: Suncorp Bank's merchant payment gateway, a Suncorp-branded instance of Mastercard Payment Gateway Services (MPGS). It offers merchants a REST/JSON (and NVP) API plus hosted checkout, hosted batch, and
  name: Suncorp Bank Gateway (Mastercard) Payments API
  slug: suncorp-bank-gateway-payments-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Suncorp Bank Banking Account Balances API
  slug: suncorp-bank-banking-account-balances-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Suncorp Bank Banking Account Direct Debits API
  slug: suncorp-bank-banking-account-direct-debits-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Suncorp Bank Banking Account Scheduled Payments API
  slug: suncorp-bank-banking-account-scheduled-payments-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Suncorp Bank Banking Account Transactions API
  slug: suncorp-bank-banking-account-transactions-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Suncorp Bank Banking Accounts API
  slug: suncorp-bank-banking-accounts-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Suncorp Bank Banking Payees API
  slug: suncorp-bank-banking-payees-api
- baseURL: https://id-ob.suncorpbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Suncorp Bank Banking Products API
  slug: suncorp-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-suncorp-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-suncorp-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-suncorp-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-suncorp-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-suncorp-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-suncorp-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-suncorp-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/suncorp-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suncorp-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suncorp-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/suncorp-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/suncorp-bank-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/suncorp-bank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/suncorp-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cdr.gov.au/find-a-provider
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/suncorp-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/suncorp-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cdr.gov.au/performance
- group: operate
  title: ''
  type: Deprecation
  url: https://www.suncorpbank.com.au/variation
- group: design
  title: ''
  type: Conventions
  url: conventions/suncorp-bank-conventions.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/suncorp-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/suncorp-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/suncorp-bank-cds-banking-products-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/suncorp-bank-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/suncorp-bank-product-reference-data.md
- group: company
  title: ''
  type: Website
  url: https://www.suncorpbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.suncorpbank.com.au/help-support/open-banking.html
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/suncorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suncorp/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suncorpbank.com.au/about-us/legal/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suncorpbank.com.au/about-us/legal.html
- group: operate
  title: ''
  type: Support
  url: https://www.suncorpbank.com.au/help-support/open-banking.html
created: '2026-07-20'
description: Suncorp Bank is an Australian retail and business bank headquartered in Brisbane, Queensland, offering transaction and savings accounts, home and personal lending, credit cards, and business banking. Formerly the banking arm of Suncorp Group, it was acquired by Australia and New Zealand Banking Group (ANZ) on 31 July 2024 and now operates as a division of ANZ while retaining the Suncorp Bank brand under a multi-year transition. As an authorised deposit-taking institution (ADI) it is a data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards, powered by the Frollo PRD portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suncorp-bank.png
layout: provider
modified: '2026-07-21'
name: Suncorp Bank
nav: Providers
network: true
overview: 'Suncorp Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Suncorp Bank''s developer surface includes authentication, documentation, support, and 23 more developer resources.'
random_paper: 17
scopes:
- name: Suncorp Bank Scopes
  scope_count: 10
  slug: suncorp-bank-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 74.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suncorp-bank/refs/heads/main/screenshots/suncorp-bank-2026-07-21T114752.png
security:
- kind: authentication
  name: Suncorp Bank Authentication
  slug: suncorp-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Suncorp Bank Domain Security
  slug: suncorp-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: suncorp-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- Consumer Data Right
website: https://www.suncorpbank.com.au/
---
