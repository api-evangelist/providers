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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-17'
api_count: 17
apis:
- description: Payer provides a modern B2B payments platform with APIs for payment initiation, invoice management, and reporting.
  name: Payer API
  slug: payer-api-2
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The All API from Payer — 1 operation(s) for all.
  name: Payer All API
  slug: payer-all-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Audit API from Payer — 1 operation(s) for audit.
  name: Payer Audit API
  slug: payer-audit-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Changelog API from Payer — 1 operation(s) for changelog.
  name: Payer Changelog API
  slug: payer-changelog-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Documentation API from Payer — 1 operation(s) for documentation.
  name: Payer Documentation API
  slug: payer-documentation-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Events API from Payer — 1 operation(s) for events.
  name: Payer Events API
  slug: payer-events-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Export API from Payer — 1 operation(s) for export.
  name: Payer Export API
  slug: payer-export-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Invoices API from Payer — 1 operation(s) for invoices.
  name: Payer Invoices API
  slug: payer-invoices-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Oauth2 API from Payer — 1 operation(s) for oauth2.
  name: Payer Oauth2 API
  slug: payer-oauth2-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Orders API from Payer — 4 operation(s) for orders.
  name: Payer Orders API
  slug: payer-orders-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Page API from Payer — 4 operation(s) for page.
  name: Payer Page API
  slug: payer-page-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Payer API API from Payer — 1 operation(s) for payer api.
  name: Payer Payer API
  slug: payer-payer-api-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Reader Access API from Payer — 1 operation(s) for reader access.
  name: Payer Reader Access API
  slug: payer-reader-access-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Reference API from Payer — 2 operation(s) for reference.
  name: Payer Reference API
  slug: payer-reference-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Search API from Payer — 1 operation(s) for search.
  name: Payer Search API
  slug: payer-search-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Users API from Payer — 1 operation(s) for users.
  name: Payer Users API
  slug: payer-users-api
- baseURL: https://b2b.payer.se
  baseurl_source: declared
  description: The Version API from Payer — 5 operation(s) for version.
  name: Payer Version API
  slug: payer-version-api
artifact_total: 28
asyncapis:
- description: ''
  name: Payer Webhooks
  slug: payer-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/rules/payer-rules.yml
  title: ''
  type: Spectral
  url: rules/payer-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/json-ld/payer-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/payer-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/vocabulary/payer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/payer-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/asyncapi/payer-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/payer-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/data-model/payer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/payer-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/authentication/payer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/payer-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/errors/payer-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/payer-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/conformance/payer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payer-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/hosts/payer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payer-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developerhub.io/support-center/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payer/refs/heads/main/security/payer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payer.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://payerdocs.developerhub.io/
- group: docs
  title: ''
  type: Documentation
  url: https://payerdocs.developerhub.io/
- group: docs
  title: ''
  type: APIReference
  url: https://payerdocs.developerhub.io/
- group: company
  title: ''
  type: Blog
  url: https://payer.eu/blogg-artiklar/
- group: commercial
  title: ''
  type: Pricing
  url: https://payer.eu/priser/
- group: operate
  title: ''
  type: Support
  url: https://payer.eu/kontakt-landningssida/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://payer.eu/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://payer.eu/om-payer/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://payer.eu/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Payer provides a modern B2B payments platform that automates order-to-cash processes, offering flexible payment methods, invoicing, and reconciliation. Their solution helps financial, commercial, and technical leaders accelerate cash flow, reduce manual effort, and enable new business models. The platform includes APIs for payment initiation, invoice management, and reporting, aiming to streamline payments for enterprises.
image: https://payer.eu/wp-content/uploads/2021/10/Others.png
json_schemas:
- name: GetApiV2OrdersInvoicesInvoiceidResponse
  property_count: 1
  slug: payer-get-api-v2-orders-invoices-invoiceid-response
- name: PostApiV2OrdersInvoicesCreditCreditidRequest
  property_count: 6
  slug: payer-post-api-v2-orders-invoices-credit-creditid-request
- name: PostApiV2OrdersInvoicesCreditCreditidResponse
  property_count: 1
  slug: payer-post-api-v2-orders-invoices-credit-creditid-response
- name: PostApiV2OrdersInvoicesInvoiceidRequest
  property_count: 4
  slug: payer-post-api-v2-orders-invoices-invoiceid-request
- name: PostOauth2TokenResponse
  property_count: 4
  slug: payer-post-oauth2-token-response
- name: PutApiV2OrdersInvoicesSendRequest
  property_count: 7
  slug: payer-put-api-v2-orders-invoices-send-request
jsonld:
- class_count: 9
  name: Payer Context
  property_count: 19
  slug: payer-context
layout: provider
modified: '2026-10-15'
name: Payer
nav: Providers
network: true
overview: 'Payer is listed with 17 APIs on the [APIs.io](https://apis.io/) network, including All API, Audit API, Changelog API, and 14 more. Tagged areas include Company, Payments, B2B, Fintech, and Automation.


  The Payer catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Payer''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, pricing, support, and 13 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Payer API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: payer-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 33.3
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 17
      marker_coverage: 100.0
      total: 17
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Payer Authentication
  slug: payer-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Payer Domain Security
  slug: payer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: payer
tags:
- Company
- Payments
- B2B
- Fintech
- Automation
website: https://payer.eu/
---
