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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Teachers Mutual Bank Banking Account Balances API
  slug: teachers-mutual-bank-banking-account-balances-api
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Teachers Mutual Bank Banking Account Direct Debits API
  slug: teachers-mutual-bank-banking-account-direct-debits-api
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Teachers Mutual Bank Banking Account Scheduled Payments API
  slug: teachers-mutual-bank-banking-account-scheduled-payments-api
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Teachers Mutual Bank Banking Account Transactions API
  slug: teachers-mutual-bank-banking-account-transactions-api
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Teachers Mutual Bank Banking Accounts API
  slug: teachers-mutual-bank-banking-accounts-api
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Teachers Mutual Bank Banking Payees API
  slug: teachers-mutual-bank-banking-payees-api
- baseURL: https://ob.tmbl.com.au/tmbank/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Teachers Mutual Bank Banking Products API
  slug: teachers-mutual-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-teachers-mutual-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-teachers-mutual-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-teachers-mutual-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-teachers-mutual-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-teachers-mutual-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-teachers-mutual-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-teachers-mutual-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/teachers-mutual-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teachers-mutual-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teachers-mutual-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teachers-mutual-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teachers-mutual-bank-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teachers-mutual-bank-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teachers-mutual-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/teachers-mutual-bank-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/teachers-mutual-bank-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teachers-mutual-bank-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/teachers-mutual-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teachers-mutual-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/teachers-mutual-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#banking-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tmbank.com.au/open-banking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tmbank.com.au/important-information
- group: company
  title: ''
  type: Website
  url: https://www.tmbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tmbank.com.au/open-banking
- group: docs
  title: ''
  type: Documentation
  url: https://www.tmbank.com.au/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teachers-mutual-bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tmbank.com.au/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.tmbank.com.au/security
- group: operate
  title: ''
  type: Support
  url: https://www.tmbank.com.au/contact
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.tmbl.com.au/
created: '2026-07-20'
description: Teachers Mutual Bank is an Australian customer-owned mutual bank and a brand of Teachers Mutual Bank Limited (TMBL), an authorised deposit-taking institution (ADI) regulated by APRA that also operates UniBank, Firefighters Mutual Bank, Health Professionals Bank and Hiver. As a member-owned bank it returns value to members rather than external shareholders and serves teachers, education staff and the wider community. Under Australia's Consumer Data Right (CDR / Open Banking), Teachers Mutual Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, letting anyone retrieve its banking product catalogue. Consumer (account and transaction) data sharing is available to accredited data recipients through the authenticated CDR channel using the OAuth2 / OpenID Connect FAPI security profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teachers-mutual-bank.png
layout: provider
modified: '2026-07-21'
name: Teachers Mutual Bank
nav: Providers
network: true
overview: 'Teachers Mutual Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Teachers Mutual Bank''s developer surface includes authentication, API reference, getting-started guide, documentation, support, and 21 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 2
  name: Teachers Mutual Bank Rate Limits
  slug: teachers-mutual-bank-rate-limits
scopes:
- name: Teachers Mutual Bank Scopes
  scope_count: 5
  slug: teachers-mutual-bank-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 44.5
  provenance:
    conformance: derived
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
    score: 53.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teachers-mutual-bank/refs/heads/main/screenshots/teachers-mutual-bank-2026-07-21T114753.png
security:
- kind: authentication
  name: Teachers Mutual Bank Authentication
  slug: teachers-mutual-bank-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Teachers Mutual Bank Domain Security
  slug: teachers-mutual-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: teachers-mutual-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.tmbank.com.au/
---
