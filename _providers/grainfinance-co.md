---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Grainfinance Co Agentic Access
  operation_count: 36
  slug: grainfinance-co-agentic-access
  summary_line: 36 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: Conversion objects represent currency conversions executed for immediate or near-term settlement.
  name: Grain Conversions API
  slug: grainfinance-co-conversions-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: Customer objects represent your end customers on the Grain platform. A customer must be created before a hedge or conversion can be initiated.
  name: Grain Customers API
  slug: grainfinance-co-customers-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: A dual hedge mitigates FX risk by automatically generating two linked hedge legs - a customer leg and a supplier leg - both routed through the customer's functional currency. This structure reduces ex
  name: Grain Dual Hedges API
  slug: grainfinance-co-dual-hedges-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: The Grain API API from Grain — 0 operation(s) for grain api.
  name: Grain Grain API
  slug: grainfinance-co-grain-api-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: Hedge objects represent transactions that lock exchange rates for future dates. A single hedge locks an exchange rate for a future transaction between two currencies.
  name: Grain Hedges API
  slug: grainfinance-co-hedges-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: The Payouts API from Grain — 3 operation(s) for payouts.
  name: Grain Payouts API
  slug: grainfinance-co-payouts-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: Pricing endpoints provide access to FX rates for currency pairs that are not being hedged. These endpoints can be used for live rate display or bulk retrieval to support high-volume quoting workflows.
  name: Grain Pricing API
  slug: grainfinance-co-pricing-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: Vendor objects represent payees that payouts can be sent to. A vendor holds contact details and one or more payout methods — the bank accounts payouts are sent to.
  name: Grain Vendors API
  slug: grainfinance-co-vendors-api
- baseURL: https://api.grainfinance.co/v1
  baseurl_source: declared
  description: Endpoints to view balances, manage funding, and perform transfers.
  name: Grain Wallets API
  slug: grainfinance-co-wallets-api
artifact_total: 25
asyncapis:
- description: ''
  name: Grainfinance Co Webhooks
  slug: grainfinance-co-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/grainfinance-co/agentic-access/grainfinance-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/grainfinance-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/grainfinance-co/rules/grainfinance-co-rules.yml
  title: ''
  type: Spectral
  url: rules/grainfinance-co-rules.yml
- group: design
  href: https://artifacts.apis.io/grainfinance-co/json-ld/grainfinance-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/grainfinance-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/grainfinance-co/vocabulary/grainfinance-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/grainfinance-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/grainfinance-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/grainfinance-co/asyncapi/grainfinance-co-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/grainfinance-co-webhooks.yml
- group: design
  href: https://artifacts.apis.io/grainfinance-co/data-model/grainfinance-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/grainfinance-co-data-model.yml
- group: auth
  href: https://artifacts.apis.io/grainfinance-co/authentication/grainfinance-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grainfinance-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/grainfinance-co/errors/grainfinance-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grainfinance-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/grainfinance-co/conformance/grainfinance-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grainfinance-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/grainfinance-co/llms/grainfinance-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grainfinance-co-llms.txt
- group: other
  href: https://artifacts.apis.io/grainfinance-co/a2a/grainfinance-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/grainfinance-co-a2a.yml
- group: other
  href: https://artifacts.apis.io/grainfinance-co/hosts/grainfinance-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grainfinance-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/grainfinance-co/vendors/grainfinance-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grainfinance-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.grainfinance.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grainfinance.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.grainfinance.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.grainfinance.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.grainfinance.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.grainfinance.co/get-started/setup-your-configuration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.grainfinance.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.grainfinance.co/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grainfinance
- group: auth
  href: https://artifacts.apis.io/grainfinance-co/security/grainfinance-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grainfinance-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.grainfinance.com/
created: '2026-10-25'
description: Grain provides an embedded FX hedging solution for platforms and marketplaces, offering AI‑driven cross‑currency protection via a flexible API. It helps businesses eliminate foreign‑exchange risk, reduce hedging costs, and increase sales by guaranteeing rates and handling transactions in multiple currencies. Backed by Bain Capital Ventures, Grain serves travel, payment providers, marketplaces, and supply‑chain platforms.
image: https://static.wixstatic.com/media/4bced4_d1b65cdb19844fb29253bf3235765250~mv2.png/v1/fill/w_1200,h_628,al_c/4bced4_d1b65cdb19844fb29253bf3235765250~mv2.png
json_schemas:
- name: AcceptOfflineDualHedgeProposalRequestBody
  property_count: 10
  slug: grainfinance-co-accept-offline-dual-hedge-proposal-request-body
- name: AcceptOfflineHedgeProposalRequestBody
  property_count: 8
  slug: grainfinance-co-accept-offline-hedge-proposal-request-body
- name: CreatedCustomerHedgeProposalResponseBody
  property_count: 13
  slug: grainfinance-co-created-customer-hedge-proposal-response-body
- name: DrawdownProposalResponse
  property_count: 12
  slug: grainfinance-co-drawdown-proposal-response
- name: DrawdownResponse
  property_count: 13
  slug: grainfinance-co-drawdown-response
- name: GetDualHedgeResponseBody
  property_count: 8
  slug: grainfinance-co-get-dual-hedge-response-body
jsonld:
- class_count: 76
  name: Grainfinance Co Context
  property_count: 151
  slug: grainfinance-co-context
layout: provider
modified: '2026-10-25'
name: Grain
nav: Providers
network: true
overview: 'Grain publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversions API, Customers API, Dual Hedges API, and 6 more. Tagged areas include Fintech, Payments, Currency, API, and Embedded.


  The Grain catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Grain''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 20 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Grain API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: grainfinance-co-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 74.0
    developer_ergonomics: 44.6
    discoverability: 67.9
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Grainfinance Co Authentication
  slug: grainfinance-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Grainfinance Co Domain Security
  slug: grainfinance-co-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: grainfinance-co-conversion-workflow
  slug: grainfinance-co-conversion-workflow
- name: grainfinance-co-create-customer
  slug: grainfinance-co-create-customer
- name: grainfinance-co-payout-review-and-submit
  slug: grainfinance-co-payout-review-and-submit
- name: grainfinance-co-withdraw-funds
  slug: grainfinance-co-withdraw-funds
slug: grainfinance-co
tags:
- Fintech
- Payments
- Currency
- API
- Embedded
website: https://www.grainfinance.com/
---
