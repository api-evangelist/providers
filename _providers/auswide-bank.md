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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Auswide Bank Banking Account Balances API
  slug: auswide-bank-banking-account-balances-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Auswide Bank Banking Account Direct Debits API
  slug: auswide-bank-banking-account-direct-debits-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Auswide Bank Banking Account Scheduled Payments API
  slug: auswide-bank-banking-account-scheduled-payments-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Auswide Bank Banking Account Transactions API
  slug: auswide-bank-banking-account-transactions-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: Auswide Bank Banking Accounts API
  slug: auswide-bank-banking-accounts-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Auswide Bank Banking Payees API
  slug: auswide-bank-banking-payees-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Auswide Bank Banking Products API
  slug: auswide-bank-banking-products-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-auswide-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-auswide-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-auswide-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-auswide-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-auswide-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-auswide-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-auswide-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/auswide-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/auswide-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/auswide-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/auswide-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/auswide-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/auswide-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/auswide-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/auswide-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/auswide-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/auswide-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/auswide-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/auswide-bank-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/auswide-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/auswide-bank-product-lookup.md
- group: company
  title: ''
  type: Website
  url: https://www.auswidebank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auswidebank.com.au/help/banking-support/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auswide-bank-ltd/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auswidebank.com.au/about/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auswidebank.com.au/about/website-terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.auswidebank.com.au/about/contact-us/
created: '2026-07-20'
description: Auswide Bank Ltd is an Australian authorised deposit-taking institution (ADI) headquartered in Bundaberg, Queensland, offering home loans, savings and transaction accounts, term deposits, credit cards, and personal and business banking. Formerly Wide Bay Australia and previously ASX-listed (ABA), Auswide is now a division of MyState Bank Limited, a wholly owned subsidiary of the ASX-listed MyState Limited (ASX MYS) following the 2025 merger. As an active CDR data holder under Australia's Consumer Data Right (Open Banking), Auswide exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, alongside the accredited-data-recipient consumer data sharing channels required of every Australian bank.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/auswide-bank.png
layout: provider
modified: '2026-07-21'
name: Auswide Bank
nav: Providers
network: true
overview: 'Auswide Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Auswide Bank''s developer surface includes authentication, documentation, support, and 17 more developer resources.'
random_paper: 14
scopes:
- name: Auswide Bank Scopes
  scope_count: 5
  slug: auswide-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 37.3
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
    score: 60.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/auswide-bank/refs/heads/main/screenshots/auswide-bank-2026-07-21T114702.png
security:
- kind: authentication
  name: Auswide Bank Authentication
  slug: auswide-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Auswide Bank Domain Security
  slug: auswide-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: auswide-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.auswidebank.com.au/
---
