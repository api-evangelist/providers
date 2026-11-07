---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: St George Bank Agentic Access
  operation_count: 19
  slug: st-george-bank-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: St.George Bank Banking Account Balances API
  slug: st-george-bank-banking-account-balances-api
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: St.George Bank Banking Account Direct Debits API
  slug: st-george-bank-banking-account-direct-debits-api
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: St.George Bank Banking Account Scheduled Payments API
  slug: st-george-bank-banking-account-scheduled-payments-api
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: St.George Bank Banking Account Transactions API
  slug: st-george-bank-banking-account-transactions-api
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: St.George Bank Banking Accounts API
  slug: st-george-bank-banking-accounts-api
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: St.George Bank Banking Payees API
  slug: st-george-bank-banking-payees-api
- baseURL: https://digital-api.stgeorge.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: St.George Bank Banking Products API
  slug: st-george-bank-banking-products-api
artifact_total: 25
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-st-george-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-st-george-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-st-george-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-st-george-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-st-george-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-st-george-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-st-george-bank-banking-products-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stgeorge.com.au/business/payment-solutions/eftpos-fees
- group: commercial
  href: https://artifacts.apis.io/st-george-bank/plans/st-george-bank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/st-george-bank-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/st-george-bank/capabilities/st-george-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/st-george-bank-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/st-george-bank/agentic-access/st-george-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/st-george-bank-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/st-george-bank/security/st-george-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/st-george-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stgeorge.com.au/
- group: start
  title: ''
  type: Portal
  url: https://www.stgeorge.com.au/online-services/open-banking
- group: docs
  title: ''
  type: Documentation
  url: https://www.stgeorge.com.au/online-services/open-banking/error-mapping
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stgeorge.com.au/privacy/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stgeorge.com.au/help/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.stgeorge.com.au/online-services/security-centre
- group: other
  href: https://artifacts.apis.io/st-george-bank/overlays/st-george-bank-cds-banking-products-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/st-george-bank-cds-banking-products-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/st-george-bank/authentication/st-george-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/st-george-bank-authentication.yml
- group: auth
  href: https://artifacts.apis.io/st-george-bank/scopes/st-george-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/st-george-bank-scopes.yml
- group: design
  href: https://artifacts.apis.io/st-george-bank/conventions/st-george-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/st-george-bank-conventions.yml
- group: design
  href: https://artifacts.apis.io/st-george-bank/errors/st-george-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/st-george-bank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/st-george-bank/conformance/st-george-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/st-george-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.stgeorge.com.au/content/dam/public/wbc/documents/pdf/aw/WBC_CDR_Policy.pdf
- group: design
  href: https://artifacts.apis.io/st-george-bank/lifecycle/st-george-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/st-george-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  href: https://artifacts.apis.io/st-george-bank/data-model/st-george-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/st-george-bank-data-model.yml
- group: agent
  href: https://artifacts.apis.io/st-george-bank/mcp/st-george-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/st-george-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/st-george-bank/llms/st-george-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/st-george-bank-llms.txt
- group: auth
  href: https://artifacts.apis.io/st-george-bank/security/st-george-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/st-george-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.westpac.com.au/security/how-to-report/responsible-disclosure/
- group: agent
  href: https://artifacts.apis.io/st-george-bank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: St.George Bank is one of Australia's largest retail and business banks and a division of Westpac Banking Corporation (ASX:WBC), one of the country's "Big Four" banks. Originally a New South Wales building society that grew into an independent ADI, St.George merged into the Westpac Group in 2008 and today operates as a Westpac brand alongside BankSA, Bank of Melbourne and RAMS. As an authorised deposit-taking institution it is a designated Data Holder under Australia's Consumer Data Right (CDR / Open Banking), and therefore exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, alongside the consented, ADR-gated CDR data-sharing APIs. St.George does not operate a broad public developer portal beyond its CDR Open Banking surface.
finops:
- has_sources: true
  method: derived
  name: St George Bank Finops
  primary_unit: terminal
  service_category: ''
  slug: st-george-bank-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/st-george-bank.png
layout: provider
modified: '2026-07-21'
name: St.George Bank
nav: Providers
network: true
overview: 'St.George Bank publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  The St.George Bank catalog on APIs.io includes 1 Spectral governance ruleset.


  St.George Bank''s developer surface includes pricing, developer portal, documentation, support, authentication, and 21 more developer resources.'
plans:
- name: St George Bank Plans Pricing
  plan_count: 5
  slug: st-george-bank-plans-pricing
- name: St George Bank Price Estimates
  plan_count: 0
  slug: st-george-bank-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: St.George Bank API Rules
  rule_count: 68
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 5
  slug: st-george-bank-rules
scopes:
- name: St George Bank Scopes
  scope_count: 9
  slug: st-george-bank-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 73.7
    contract_governance: 31.8
    contract_quality: 44.7
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 53.6
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
    score: 52.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/st-george-bank/st-george-bank-2026-07-21T114749.png
security:
- kind: authentication
  name: St George Bank Authentication
  slug: st-george-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: St George Bank Domain Security
  slug: st-george-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: St George Bank Vulnerability Disclosure
  slug: st-george-bank-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 2
skills:
- name: Read consented accounts, balances and transactions (CDR ADR)
  slug: st-george-bank-accounts-and-transactions
- name: Browse St.George banking products (public CDR PRD)
  slug: st-george-bank-product-reference-data
slug: st-george-bank
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- Westpac Group
website: https://www.stgeorge.com.au/
---
