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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ing Australia Agentic Access
  operation_count: 19
  slug: ing-australia-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: ING Australia Banking Account Balances API
  slug: ing-australia-banking-account-balances-api
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: ING Australia Banking Account Direct Debits API
  slug: ing-australia-banking-account-direct-debits-api
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: ING Australia Banking Account Scheduled Payments API
  slug: ing-australia-banking-account-scheduled-payments-api
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: ING Australia Banking Account Transactions API
  slug: ing-australia-banking-account-transactions-api
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: ING Australia Banking Accounts API
  slug: ing-australia-banking-accounts-api
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: ING Australia Banking Payees API
  slug: ing-australia-banking-payees-api
- baseURL: https://id.ob.ing.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: ING Australia Banking Products API
  slug: ing-australia-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-ing-australia-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-ing-australia-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-ing-australia-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-ing-australia-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-ing-australia-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-ing-australia-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-ing-australia-banking-products-api
common:
- group: other
  href: https://artifacts.apis.io/ing-australia/capabilities/ing-australia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ing-australia-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ing-australia/agentic-access/ing-australia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ing-australia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ing-australia/security/ing-australia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ing-australia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ing-australia/authentication/ing-australia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ing-australia-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ing-australia/scopes/ing-australia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ing-australia-scopes.yml
- group: agent
  href: https://artifacts.apis.io/ing-australia/well-known/ing-australia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ing-australia-well-known.yml
- group: design
  href: https://artifacts.apis.io/ing-australia/conformance/ing-australia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ing-australia-conformance.yml
- group: design
  href: https://artifacts.apis.io/ing-australia/errors/ing-australia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ing-australia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ing-australia/conventions/ing-australia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ing-australia-conventions.yml
- group: design
  href: https://artifacts.apis.io/ing-australia/lifecycle/ing-australia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ing-australia-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
- group: design
  href: https://artifacts.apis.io/ing-australia/data-model/ing-australia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ing-australia-data-model.yml
- group: agent
  href: https://artifacts.apis.io/ing-australia/mcp/ing-australia-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ing-australia-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ing-australia/llms/ing-australia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ing-australia-llms.txt
- group: other
  href: https://artifacts.apis.io/ing-australia/overlays/ing-australia-cds-banking-products-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ing-australia-cds-banking-products-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ing-australia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.ing.com.au/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ing.com.au/open-banking.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.ing.com.au/pdf/CDR-policy.pdf
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: operate
  title: ''
  type: Support
  url: mailto:cdrenquiry@ing.com.au
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ing.com.au/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ing.com.au/legal.html
created: '2026-07-20'
description: ING Australia is the retail banking division of ING Bank (Australia) Limited (ABN 24 000 893 292), a wholly owned subsidiary of the Dutch multinational ING Groep N.V. headquartered in Amsterdam. Launched in 1999 as ING Direct and rebranded to ING in 2017, it is a branchless, digital-first direct bank offering everyday transaction and savings accounts, home loans, superannuation, and insurance to Australian consumers. It is not a customer-owned mutual; it is a foreign-owned Authorised Deposit-taking Institution (ADI) regulated by APRA and ASIC. As an active ADI, ING is an accredited data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes the mandatory public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards (CDS). Authenticated consumer-data sharing follows the CDR ecosystem model (OAuth2 / OIDC FAPI profile via accredited data recipients); ING does not operate a broad, self-serve public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ing-australia.png
layout: provider
modified: '2026-07-21'
name: ING Australia
nav: Providers
network: true
overview: 'ING Australia publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  ING Australia''s developer surface includes authentication, getting-started guide, documentation, API reference, support, and 18 more developer resources.'
random_paper: 9
scopes:
- name: Ing Australia Scopes
  scope_count: 10
  slug: ing-australia-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 37.2
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
    score: 37.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ing-australia/ing-australia-2026-07-21T114732.png
security:
- kind: authentication
  name: Ing Australia Authentication
  slug: ing-australia-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Ing Australia Domain Security
  slug: ing-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Read ING Australia account data via CDR consumer data sharing
  slug: ing-australia-consumer-data-sharing
- name: List ING Australia banking products (public CDR PRD)
  slug: ing-australia-list-products
slug: ing-australia
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.ing.com.au/
---
