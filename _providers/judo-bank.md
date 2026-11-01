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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Judo Bank Agentic Access
  operation_count: 19
  slug: judo-bank-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Balance endpoints (authenticated CDR resource API; Judo Bank serves it on an mTLS data-holder host that is not published publicly - the DSB contract templates it as https://mtls.dh.exa
  name: Judo Bank Banking Account Balances API
  slug: judo-bank-banking-account-balances-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Direct Debit endpoints (authenticated CDR resource API; Judo Bank serves it on an mTLS data-holder host that is not published publicly - the DSB contract templates it as https://mtls.d
  name: Judo Bank Banking Account Direct Debits API
  slug: judo-bank-banking-account-direct-debits-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Scheduled Payment endpoints (authenticated CDR resource API; Judo Bank serves it on an mTLS data-holder host that is not published publicly - the DSB contract templates it as https://m
  name: Judo Bank Banking Account Scheduled Payments API
  slug: judo-bank-banking-account-scheduled-payments-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Transaction endpoints (authenticated CDR resource API; Judo Bank serves it on an mTLS data-holder host that is not published publicly - the DSB contract templates it as https://mtls.dh
  name: Judo Bank Banking Account Transactions API
  slug: judo-bank-banking-account-transactions-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account endpoints (authenticated CDR resource API; Judo Bank serves it on an mTLS data-holder host that is not published publicly - the DSB contract templates it as https://mtls.dh.example.com
  name: Judo Bank Banking Accounts API
  slug: judo-bank-banking-accounts-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Payee endpoints (authenticated CDR resource API; Judo Bank serves it on an mTLS data-holder host that is not published publicly - the DSB contract templates it as https://mtls.dh.example.com/c
  name: Judo Bank Banking Payees API
  slug: judo-bank-banking-payees-api
- baseURL: https://public.open.judo.bank/cds-au/v1
  baseurl_source: declared
  description: 'Banking Product endpoints (CDR Product Reference Data) - public, unauthenticated, served live by Judo Bank at public.open.judo.bank (the publicBaseUri registered for brand "Judo Bank" in the ACCC CDR '
  name: Judo Bank Banking Products API
  slug: judo-bank-banking-products-api
artifact_total: 36
collections:
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-judo-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-judo-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-judo-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-judo-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-judo-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-judo-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-judo-bank-banking-products-api
common:
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/maintenance.html
- group: operate
  href: https://artifacts.apis.io/judo-bank/rate-limits/judo-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/judo-bank-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/rules/judo-bank-rules.yml
  title: ''
  type: Spectral
  url: rules/judo-bank-rules.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/json-ld/judo-bank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/judo-bank-context.jsonld
- group: design
  href: https://artifacts.apis.io/judo-bank/vocabulary/judo-bank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/judo-bank-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/judo-bank/overlays/judo-bank-banking-account-balances-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/judo-bank-banking-account-balances-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/judo-bank/hosts/judo-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/judo-bank-hosts.yml
- group: build
  href: https://artifacts.apis.io/judo-bank/integrations/judo-bank-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/judo-bank-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/judo-bank/vendors/judo-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/judo-bank-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.judo.bank/feed/
- group: other
  href: https://artifacts.apis.io/judo-bank/capabilities/judo-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/judo-bank-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/judo-bank/agentic-access/judo-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/judo-bank-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/judo-bank/authentication/judo-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/judo-bank-authentication.yml
- group: auth
  href: https://artifacts.apis.io/judo-bank/security/judo-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/judo-bank-domain-security.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/conventions/judo-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/judo-bank-conventions.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/errors/judo-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/judo-bank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/conformance/judo-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/judo-bank-conformance.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/lifecycle/judo-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/judo-bank-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/judo-bank/data-model/judo-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/judo-bank-data-model.yml
- group: agent
  href: https://artifacts.apis.io/judo-bank/mcp/judo-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/judo-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/judo-bank/skills/judo-bank-product-lookup.md
  title: ''
  type: AgentSkill
  url: skills/judo-bank-product-lookup.md
- group: agent
  href: https://artifacts.apis.io/judo-bank/well-known/judo-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/judo-bank-well-known.yml
- group: agent
  href: https://artifacts.apis.io/judo-bank/llms/judo-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/judo-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.judo.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://www.judo.bank/open-banking/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.judo.bank/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/judobank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/judobank
created: '2026-07-20'
description: Judo Bank (Judo Capital Holdings Ltd) is an Australian challenger bank founded in 2016 and headquartered in Melbourne, purpose-built to serve small and medium-sized enterprises (SMEs) with relationship-led business lending alongside personal and business term deposits. It was the first new domestically-owned bank in decades to be granted a full, unrestricted authorised deposit-taking institution (ADI) licence by APRA, in April 2019, and has been publicly listed on the Australian Securities Exchange (ticker ASX JDO) since November 2021 - it is a for-profit, shareholder-owned bank, not a customer-owned mutual. As a designated ADI and data holder under Australia's Consumer Data Right (CDR / Open Banking) regime, Judo Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, while authenticated consumer-data sharing is governed by the accredited data recipient (ADR) model rather than an open self-serve
  developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/judo-bank.png
json_schemas:
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: judo-bank-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: judo-bank-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: judo-bank-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: judo-bank-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: judo-bank-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: judo-bank-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: judo-bank-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: judo-bank-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: judo-bank-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: judo-bank-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: judo-bank-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: judo-bank-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: judo-bank-response-banking-transaction-list-v2
jsonld:
- class_count: 95
  name: Judo Bank Context
  property_count: 280
  slug: judo-bank-context
layout: provider
modified: '2026-10-21'
name: Judo Bank
nav: Providers
network: true
overview: 'Judo Bank publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  The Judo Bank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Judo Bank''s developer surface includes authentication, documentation, and 26 more developer resources.'
plans:
- name: Judo Bank Plans Pricing
  plan_count: 0
  slug: judo-bank-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Judo Bank Rate Limits
  slug: judo-bank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Judo Bank API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: judo-bank-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 58.3
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 36.3
  provenance:
    agentic_access: derived
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
    score: 16.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/judo-bank/judo-bank-2026-07-21T114730.png
security:
- kind: authentication
  name: Judo Bank Authentication
  slug: judo-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Judo Bank Domain Security
  slug: judo-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: judo-bank-account-data-sharing
  slug: judo-bank-account-data-sharing
- name: judo-bank-product-lookup
  slug: judo-bank-product-lookup
slug: judo-bank
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- SME Lending
- Product Reference Data
website: https://www.judo.bank/
---
