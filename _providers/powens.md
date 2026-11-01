---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://payment-links.powens.com
  baseurl_source: declared
  description: 'Powens API as documented publicly: 44 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Powens API
  slug: powens-api
artifact_total: 12
asyncapis:
- description: ''
  name: Powens Webhooks
  slug: powens-webhooks
common:
- group: design
  href: https://artifacts.apis.io/powens/rules/powens-rules.yml
  title: ''
  type: Spectral
  url: rules/powens-rules.yml
- group: design
  href: https://artifacts.apis.io/powens/json-ld/powens-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/powens-context.jsonld
- group: design
  href: https://artifacts.apis.io/powens/vocabulary/powens-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/powens-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/powens/asyncapi/powens-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/powens-webhooks.yml
- group: design
  href: https://artifacts.apis.io/powens/data-model/powens-data-model.yml
  title: ''
  type: DataModel
  url: data-model/powens-data-model.yml
- group: auth
  href: https://artifacts.apis.io/powens/authentication/powens-authentication.yml
  title: ''
  type: Authentication
  url: authentication/powens-authentication.yml
- group: design
  href: https://artifacts.apis.io/powens/conformance/powens-conformance.yml
  title: ''
  type: Conformance
  url: conformance/powens-conformance.yml
- group: agent
  href: https://artifacts.apis.io/powens/llms/powens-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/powens-llms.txt
- group: agent
  href: https://artifacts.apis.io/powens/well-known/powens-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/powens-well-known.yml
- group: other
  href: https://artifacts.apis.io/powens/hosts/powens-hosts.yml
  title: ''
  type: Hosts
  url: hosts/powens-hosts.yml
- group: other
  href: https://artifacts.apis.io/powens/vendors/powens-vendors.yml
  title: ''
  type: Vendors
  url: vendors/powens-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.powens.com/media
- group: auth
  href: https://artifacts.apis.io/powens/security/powens-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powens.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.powens.com/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.powens.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.powens.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.powens.com/documentation/integration-guides/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.powens.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.powens.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://console.powens.com/auth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.powens.com/documentation/legal-notice
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/powens/workspace
created: '2026-10-21'
description: Powens provides an Open Finance Platform delivering API solutions for financial data aggregation, transactions, wealth management, identity verification, and payment services. Their suite enables banks, fintechs, and enterprises to integrate real‑time financial data, automate accounting, and offer embedded banking experiences through robust APIs and developer tools.
image: https://www.powens.com/wp-content/uploads/powens_thumbnail.webp
json_schemas:
- name: GetUsersMeAccountsAccountidAmortizationsResponse
  property_count: 18
  slug: powens-get-users-me-accounts-accountid-amortizations-response
- name: GetUsersMeAmortizationsResponse
  property_count: 18
  slug: powens-get-users-me-amortizations-response
- name: GetUsersMeConnectionsConnectionidAmortizationsResponse
  property_count: 18
  slug: powens-get-users-me-connections-connectionid-amortizations-response
- name: GetUsersMeMarketordersResponse
  property_count: 24
  slug: powens-get-users-me-marketorders-response
- name: PostApiPaymentLinksRequest
  property_count: 13
  slug: powens-post-api-payment-links-request
- name: PostPaymentsRequest
  property_count: 7
  slug: powens-post-payments-request
jsonld:
- class_count: 19
  name: Powens Context
  property_count: 37
  slug: powens-context
layout: provider
modified: '2026-10-21'
name: Powens
nav: Providers
network: true
overview: 'Powens is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, OpenFinance, APIs, and Payments.


  The Powens catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Powens'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Powens API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: powens-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 61.9
    discoverability: 67.9
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
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
  name: Powens Authentication
  slug: powens-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Powens Domain Security
  slug: powens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: powens
tags:
- Company
- FinTech
- OpenFinance
- APIs
- Payments
website: https://powens.com/
---
