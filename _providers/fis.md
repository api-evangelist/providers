---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Fis Agentic Access
  operation_count: 8
  slug: fis-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: FIS (Fidelity National Information Services) provides core banking platforms including the Systematics suite. APIs bridge mainframe-based account processing, transaction management, and loan servicing
  name: FIS Core Banking API
  slug: fis-core-banking-api
- description: FIS wealth management APIs enable integration with portfolio management, account aggregation, trading, and advisory systems for wealth management platforms and financial advisors.
  name: FIS Wealth Management API
  slug: fis-wealth-management-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Account information and balance inquiries
  name: FIS Global Accounts API
  slug: fis-accounts-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: ACH (Automated Clearing House) payment operations
  name: FIS Global ACH API
  slug: fis-ach-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Initiate and manage payment transactions
  name: FIS Global Payments API
  slug: fis-payments-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Transaction history and status
  name: FIS Global Transactions API
  slug: fis-transactions-api
- baseURL: https://api.fisglobal.com
  baseurl_source: declared
  description: Domestic and international wire transfer operations
  name: FIS Global Wire Transfers API
  slug: fis-wire-transfers-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FIS Payments Accounts API
  slug: open-fis-accounts-api
- collection_type: open
  name: FIS Payments Accounts ACH API
  slug: open-fis-ach-api
- collection_type: open
  name: FIS Accounts Payments API
  slug: open-fis-payments-api
- collection_type: open
  name: FIS Payments API
  slug: open-fis-payments
- collection_type: open
  name: FIS Payments Accounts Transactions API
  slug: open-fis-transactions-api
- collection_type: open
  name: FIS Payments Accounts Wire Transfers API
  slug: open-fis-wire-transfers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fis-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fis-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FISGlobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fis
description: FIS (Fidelity National Information Services) is a global leader in financial technology providing APIs for core banking, payments, wealth management, and capital markets through the CodeConnect API marketplace. APIs connect financial institutions, fintechs, and enterprises to FIS banking and payment infrastructure.
finops:
- name: Fis Finops
  service_category: Financial Services Software
  slug: fis-finops
json_schemas:
- name: FIS Payment
  property_count: 15
  slug: fis-payment
jsonld:
- class_count: 12
  name: Fis Context
  property_count: 10
  slug: fis-context
layout: provider
modified: '2026-04-28'
name: FIS Global
nav: Providers
network: true
overview: 'FIS Global publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ACH API, Payments API, and 2 more. Tagged areas include Banking, Core Banking, Financial-Services, Payments, and Fintech.


  The FIS Global catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FIS Global''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Fis Plans Pricing
  plan_count: 3
  slug: fis-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Fis Rate Limits
  slug: fis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FIS Global API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fis-jsonschema-spectral-rules
scopes:
- name: Fis Scopes
  scope_count: 3
  slug: fis-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 61.1
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/screenshots/fis-2026-06-20T181251.png
security:
- kind: authentication
  name: Fis Authentication
  slug: fis-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fis Domain Security
  slug: fis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fis
tags:
- Banking
- Core Banking
- Financial-Services
- Payments
- Fintech
---
