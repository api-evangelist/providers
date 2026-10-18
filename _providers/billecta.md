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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 16
apis:
- description: Main API documented at Billecta Docs reference page.
  name: Billecta API
  slug: billecta-api-2
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Accounting API from Billecta — 3 operation(s) for accounting.
  name: Billecta Accounting API
  slug: billecta-accounting-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Accountingdimensions API from Billecta — 3 operation(s) for accountingdimensions.
  name: Billecta Accountingdimensions API
  slug: billecta-accountingdimensions-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Action API from Billecta — 1 operation(s) for action.
  name: Billecta Action API
  slug: billecta-action-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Authentication API from Billecta — 2 operation(s) for authentication.
  name: Billecta Authentication API
  slug: billecta-authentication-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Bankaccount API from Billecta — 2 operation(s) for bankaccount.
  name: Billecta Bankaccount API
  slug: billecta-bankaccount-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Bankid API from Billecta — 2 operation(s) for bankid.
  name: Billecta Bankid API
  slug: billecta-bankid-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Common API from Billecta — 1 operation(s) for common.
  name: Billecta Common API
  slug: billecta-common-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Contractinvoice API from Billecta — 2 operation(s) for contractinvoice.
  name: Billecta Contractinvoice API
  slug: billecta-contractinvoice-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Creditors API from Billecta — 2 operation(s) for creditors.
  name: Billecta Creditors API
  slug: billecta-creditors-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Debtors API from Billecta — 1 operation(s) for debtors.
  name: Billecta Debtors API
  slug: billecta-debtors-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Invoice API from Billecta — 1 operation(s) for invoice.
  name: Billecta Invoice API
  slug: billecta-invoice-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Products API from Billecta — 1 operation(s) for products.
  name: Billecta Products API
  slug: billecta-products-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Search API from Billecta — 1 operation(s) for search.
  name: Billecta Search API
  slug: billecta-search-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Add Ons API from Billecta — 2 operation(s) for add ons.
  name: Billecta Add Ons API
  slug: billecta-add-ons-api
- baseURL: https://api.billecta.com
  baseurl_source: declared
  description: The Cost Centers API from Billecta — 2 operation(s) for cost centers.
  name: Billecta Cost Centers API
  slug: billecta-cost-centers-api
artifact_total: 25
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/rules/billecta-rules.yml
  title: ''
  type: Spectral
  url: rules/billecta-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/json-ld/billecta-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billecta-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/vocabulary/billecta-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billecta-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/data-model/billecta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billecta-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/conformance/billecta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billecta-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/hosts/billecta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billecta-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/vendors/billecta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billecta-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billecta.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.billecta.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billecta.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billecta/refs/heads/main/security/billecta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billecta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billecta.com/
coverage:
  checked: '2026-10-15'
  detail: API documentation provides HTML pages but no OpenAPI, GraphQL schema, or other machine‑readable contract (openapi.json 404, GraphQL endpoint 401).
  evidence:
  - status: 404
    url: https://api.billecta.com/openapi.json
  - status: 401
    url: https://api.billecta.com/v1/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Billecta provides a cloud‑based invoicing and payment automation platform for businesses in Sweden and beyond. Their solution automates the full invoicing flow, from invoice creation and delivery to payment collection and bookkeeping. Features include automated reminders, credit‑control, integration with accounting systems, and support for direct payments and auto‑giro. The service is offered as a SaaS product with a free trial and is designed for companies of all sizes, from startups to large enterprises. Billecta emphasizes ease of use, speed, and compliance with Swedish financial regulations.
json_schemas:
- name: PostV1AccountingAccountingidRequest
  property_count: 1
  slug: billecta-post-v1-accounting-accountingid-request
- name: PostV1BankaccountInitiateretrievalRequest
  property_count: 2
  slug: billecta-post-v1-bankaccount-initiateretrieval-request
- name: PostV1BankaccountInitiateretrievalRequest2
  property_count: 1
  slug: billecta-post-v1-bankaccount-initiateretrieval-request2
- name: PostV1BankidPhoneauthenticationRequest
  property_count: 1
  slug: billecta-post-v1-bankid-phoneauthentication-request
- name: PutV1AccountingAccountingidRequest
  property_count: 1
  slug: billecta-put-v1-accounting-accountingid-request
- name: PutV1BankidBankididRequest
  property_count: 1
  slug: billecta-put-v1-bankid-bankidid-request
jsonld:
- class_count: 37
  name: Billecta Context
  property_count: 26
  slug: billecta-context
layout: provider
modified: '2026-10-15'
name: Billecta
nav: Providers
network: true
overview: 'Billecta is listed with 16 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Accountingdimensions API, Action API, and 13 more. Tagged areas include Fintech, Invoicing, Payments, Software-as-a-Service, and Sweden.


  The Billecta catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Billecta''s developer surface includes API reference, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Billecta API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: billecta-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: domain-security
  name: Billecta Domain Security
  slug: billecta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: billecta
tags:
- Fintech
- Invoicing
- Payments
- Software-as-a-Service
- Sweden
- BusinessAutomation
website: https://billecta.com/
---
