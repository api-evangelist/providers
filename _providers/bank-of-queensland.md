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
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Of Queensland Agentic Access
  operation_count: 19
  slug: bank-of-queensland-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Bank of Queensland Banking Account Balances API
  slug: bank-of-queensland-banking-account-balances-api
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Bank of Queensland Banking Account Direct Debits API
  slug: bank-of-queensland-banking-account-direct-debits-api
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Bank of Queensland Banking Account Scheduled Payments API
  slug: bank-of-queensland-banking-account-scheduled-payments-api
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Bank of Queensland Banking Account Transactions API
  slug: bank-of-queensland-banking-account-transactions-api
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Bank of Queensland Banking Accounts API
  slug: bank-of-queensland-banking-accounts-api
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Bank of Queensland Banking Payees API
  slug: bank-of-queensland-banking-payees-api
- baseURL: https://secure.api.boq.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Bank of Queensland Banking Products API
  slug: bank-of-queensland-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-bank-of-queensland-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-bank-of-queensland-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-bank-of-queensland-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-bank-of-queensland-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-bank-of-queensland-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-bank-of-queensland-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-bank-of-queensland-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bank-of-queensland-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-queensland-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-queensland-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-queensland-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-queensland-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-queensland-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-queensland-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-queensland-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bank-of-queensland-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-queensland-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-queensland-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bank-of-queensland-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-queensland-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-queensland-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.boq.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.boq.com.au/personal/banking/openbanking/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.boq.com.au/personal/banking/openbanking/developers
- group: operate
  title: ''
  type: Support
  url: https://www.boq.com.au/help-and-support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boq.com.au/personal/help-and-support/forms-and-important-information/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boq.com.au/important-information/terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-queensland
created: '2026-07-20'
description: Bank of Queensland Limited (ASX code BOQ) is one of Australia's oldest banks, founded in Brisbane in 1874, and today an APRA-regulated authorised deposit-taking institution (ADI) and ASX-listed regional retail and commercial bank - a publicly listed company, not a customer-owned mutual. Its banking group includes the ME Bank, Virgin Money Australia and BOQ Specialist brands. As an accredited Consumer Data Right (CDR) data holder, BOQ exposes a public, unauthenticated Product Reference Data (PRD) API that conforms to the Australian Consumer Data Standards, while consumer data sharing runs through the regulated CDR / Accredited Data Recipient (ADR) model with OAuth2 / OIDC (FAPI) authorization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-queensland.png
layout: provider
modified: '2026-07-21T18:00:00Z'
name: Bank of Queensland
nav: Providers
network: true
overview: 'Bank of Queensland publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank of Queensland''s developer surface includes authentication, documentation, support, and 19 more developer resources.'
random_paper: 2
scopes:
- name: Bank Of Queensland Scopes
  scope_count: 9
  slug: bank-of-queensland-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 43.8
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
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 77.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-queensland/refs/heads/main/screenshots/bank-of-queensland-2026-07-21T114702.png
security:
- kind: authentication
  name: Bank Of Queensland Authentication
  slug: bank-of-queensland-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Bank Of Queensland Domain Security
  slug: bank-of-queensland-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: bank-of-queensland
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.boq.com.au/
---
