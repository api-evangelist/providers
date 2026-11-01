---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Two Agentic Access
  operation_count: 34
  slug: two-agentic-access
  summary_line: 34 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.two.inc
  baseurl_source: declared
  description: The API Key API from Two — 2 operation(s) for api key.
  name: Two API Key API
  slug: two-api-key-api
- baseURL: https://api.two.inc
  baseurl_source: declared
  description: The Invoice API from Two — 8 operation(s) for invoice.
  name: Two Invoice API
  slug: two-invoice-api
- baseURL: https://api.two.inc
  baseurl_source: declared
  description: The Order API from Two — 15 operation(s) for order.
  name: Two Order API
  slug: two-order-api
- baseURL: https://api.two.inc
  baseurl_source: declared
  description: The Order intent API from Two — 2 operation(s) for order intent.
  name: Two Order intent API
  slug: two-order-intent-api
- baseURL: https://api.two.inc
  baseurl_source: declared
  description: The Settlement report API from Two — 3 operation(s) for settlement report.
  name: Two Settlement report API
  slug: two-settlement-report-api
artifact_total: 25
asyncapis:
- description: ''
  name: Two Webhooks
  slug: two-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/two/agentic-access/two-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/two-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/two/rules/two-rules.yml
  title: ''
  type: Spectral
  url: rules/two-rules.yml
- group: design
  href: https://artifacts.apis.io/two/json-ld/two-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/two-context.jsonld
- group: design
  href: https://artifacts.apis.io/two/vocabulary/two-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/two-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/two/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/two/asyncapi/two-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/two-webhooks.yml
- group: design
  href: https://artifacts.apis.io/two/data-model/two-data-model.yml
  title: ''
  type: DataModel
  url: data-model/two-data-model.yml
- group: design
  href: https://artifacts.apis.io/two/conventions/two-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/two-conventions.yml
- group: design
  href: https://artifacts.apis.io/two/conventions/two-conventions.yml
  title: ''
  type: Conventions
  url: conventions/two-conventions.yml
- group: auth
  href: https://artifacts.apis.io/two/authentication/two-authentication.yml
  title: ''
  type: Authentication
  url: authentication/two-authentication.yml
- group: build
  href: https://artifacts.apis.io/two/errors/two-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/two-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/two/errors/two-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/two-problem-types.yml
- group: design
  href: https://artifacts.apis.io/two/conformance/two-conformance.yml
  title: ''
  type: Conformance
  url: conformance/two-conformance.yml
- group: agent
  href: https://artifacts.apis.io/two/llms/two-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/two-llms.txt
- group: auth
  href: https://artifacts.apis.io/two/well-known/two-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/two-www-security.txt
- group: agent
  href: https://artifacts.apis.io/two/well-known/two-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/two-well-known.yml
- group: other
  href: https://artifacts.apis.io/two/hosts/two-hosts.yml
  title: ''
  type: Hosts
  url: hosts/two-hosts.yml
- group: other
  href: https://artifacts.apis.io/two/vendors/two-vendors.yml
  title: ''
  type: Vendors
  url: vendors/two-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.two.inc/llms/guides/path-to-trade-account-onboarding.txt
- group: auth
  href: https://artifacts.apis.io/two/security/two-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/two-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.two.inc
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.two.inc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.two.inc
- group: docs
  title: ''
  type: APIReference
  url: https://docs.two.inc
- group: operate
  title: ''
  type: Support
  url: https://support.two.inc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.two.inc/company/legal/privacy-policy
- group: company
  title: ''
  type: Press
  url: https://www.two.inc/company/two-in-the-press
created: '2026-10-29'
description: Two is the global B2B payments leader for SMBs and enterprises, offering instant net‑terms to improve cash flow, average order value, and conversions. The platform provides a suite of APIs for checkout, trade accounts, billing, marketplace, and more, enabling businesses to embed financing directly into their payment flows. Backed by Sequoia Capital, Two serves thousands of merchants worldwide with a focus on seamless integration and robust security.
image: https://cdn.prod.website-files.com/67125812d0e0a2a3306a1206/68fb8312b3371671274c9163_Two%20Logo%20-%20navy_yellow%20(1).png
json_schemas:
- name: CreateOrderIntentRequestSchema
  property_count: 13
  slug: two-create-order-intent-request-schema
- name: CreateOrderRequestSchema
  property_count: 46
  slug: two-create-order-request-schema
- name: EditOrderRequestSchema
  property_count: 24
  slug: two-edit-order-request-schema
- name: InvoiceDetailsWithStatusSchema
  property_count: 28
  slug: two-invoice-details-with-status-schema
- name: OrderIntentResponseSchema
  property_count: 19
  slug: two-order-intent-response-schema
- name: OrderResponseSchema
  property_count: 77
  slug: two-order-response-schema
jsonld:
- class_count: 112
  name: Two Context
  property_count: 288
  slug: two-context
layout: provider
modified: '2026-10-29'
name: Two
nav: Providers
network: true
overview: 'Two publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Key API, Invoice API, Order API, and 2 more. Tagged areas include Company, B2B Payments, FinTech, API Platform, and Checkout.


  The Two catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Two''s developer surface includes authentication, getting-started guide, documentation, API reference, support, and 22 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Two API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: two-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 70.1
    developer_ergonomics: 56.5
    discoverability: 67.9
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Two Authentication
  slug: two-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Two Domain Security
  slug: two-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 8
skills:
- name: two-create-and-confirm-order
  slug: two-create-and-confirm-order
- name: two-create-and-get-order-intent
  slug: two-create-and-get-order-intent
- name: two-create-and-retrieve-invoice
  slug: two-create-and-retrieve-invoice
- name: two-create-order-intent
  slug: two-create-order-intent
- name: two-create-order
  slug: two-create-order
- name: two-download-invoice-pdf
  slug: two-download-invoice-pdf
- name: two-manage-api-keys
  slug: two-manage-api-keys
- name: two-revoke-merchant-api-key
  slug: two-revoke-merchant-api-key
slug: two
tags:
- Company
- B2B Payments
- FinTech
- API Platform
- Checkout
- Trade Accounts
website: https://www.two.inc
---
