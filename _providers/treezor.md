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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-17'
api_count: 14
apis:
- description: Treezor API provides banking-as-a-service endpoints for accounts, virtual IBANs, cards, payments and compliance.
  name: Treezor API
  slug: treezor-api-2
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Beneficiaries API from Treezor — 2 operation(s) for beneficiaries.
  name: Treezor Beneficiaries API
  slug: treezor-beneficiaries-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Cardimages API from Treezor — 1 operation(s) for cardimages.
  name: Treezor Cardimages API
  slug: treezor-cardimages-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Cards API from Treezor — 5 operation(s) for cards.
  name: Treezor Cards API
  slug: treezor-cards-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Core Connect API from Treezor — 5 operation(s) for core connect.
  name: Treezor Core Connect API
  slug: treezor-core-connect-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Customization API from Treezor — 1 operation(s) for customization.
  name: Treezor Customization API
  slug: treezor-customization-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The [...] API from Treezor — 1 operation(s) for [...].
  name: Treezor [...] API
  slug: treezor-default-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Documents API from Treezor — 1 operation(s) for documents.
  name: Treezor Documents API
  slug: treezor-documents-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Oauth API from Treezor — 1 operation(s) for oauth.
  name: Treezor OAuth API
  slug: treezor-oauth-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Retry API from Treezor — 2 operation(s) for retry.
  name: Treezor Retry API
  slug: treezor-retry-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Simulation API from Treezor — 1 operation(s) for simulation.
  name: Treezor Simulation API
  slug: treezor-simulation-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Treezor API API from Treezor — 1 operation(s) for treezor api.
  name: Treezor Treezor API
  slug: treezor-treezor-api-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Users API from Treezor — 1 operation(s) for users.
  name: Treezor Users API
  slug: treezor-users-api
- baseURL: https://api.treezor.com
  baseurl_source: declared
  description: The Wallets API from Treezor — 1 operation(s) for wallets.
  name: Treezor Wallets API
  slug: treezor-wallets-api
artifact_total: 26
asyncapis:
- description: ''
  name: Treezor Webhooks
  slug: treezor-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/well-known/treezor-treezor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/treezor-treezor-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/rules/treezor-rules.yml
  title: ''
  type: Spectral
  url: rules/treezor-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/json-ld/treezor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/treezor-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/vocabulary/treezor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/treezor-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/asyncapi/treezor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/treezor-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/data-model/treezor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/treezor-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/conventions/treezor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/treezor-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.treezor.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/authentication/treezor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/treezor-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/lifecycle/treezor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/treezor-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/conformance/treezor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/treezor-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/llms/treezor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/treezor-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/well-known/treezor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/treezor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/hosts/treezor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/treezor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/vendors/treezor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/treezor-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://treezor.statuspage.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.treezor.com/guide/overview/getting-started.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/security/treezor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/treezor-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/treezor/refs/heads/main/security/treezor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/treezor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.treezor.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.treezor.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.treezor.com/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.treezor.com/api-documentation/
- group: operate
  title: ''
  type: Support
  url: https://www.treezor.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.treezor.com/insights/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.treezor.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treezor.com/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.treezor.com/pricing/
coverage:
  checked: '2026-10-14'
  detail: API reference page renders an interactive OpenAPI UI but the raw spec is not directly accessible.
  evidence:
  - status: 200
    url: https://docs.treezor.com/api-reference/api-endpoints.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Treezor provides a comprehensive Banking-as-a-Service platform, offering payment processing, card issuing, SEPA transfers, KYC compliance, and embedded finance solutions for fintechs and regulated institutions across Europe. Their API enables developers to integrate accounts, virtual IBANs, card programs, and real‑time transaction monitoring, supporting both B2B and B2C use cases.
image: https://www.treezor.com/app/uploads/2022/06/treezor_featured.jpg
json_schemas:
- name: GetCoreConnectScaScawalletsScawalletidResponse
  property_count: 22
  slug: treezor-get-core-connect-sca-scawallets-scawalletid-response
- name: GetResponse
  property_count: 22
  slug: treezor-get-response
- name: PostCardsRequest
  property_count: 11
  slug: treezor-post-cards-request
- name: PostCoreConnectCardBulkRequest
  property_count: 14
  slug: treezor-post-core-connect-card-bulk-request
- name: PostCoreConnectScaScaoperationsRequest
  property_count: 4
  slug: treezor-post-core-connect-sca-scaoperations-request
- name: PostCoreConnectScaScaoperationsResponse
  property_count: 10
  slug: treezor-post-core-connect-sca-scaoperations-response
jsonld:
- class_count: 27
  name: Treezor Context
  property_count: 78
  slug: treezor-context
layout: provider
modified: '2026-10-14'
name: Treezor
nav: Providers
network: true
overview: 'Treezor is listed with 14 APIs on the [APIs.io](https://apis.io/) network, including Beneficiaries API, Cardimages API, Cards API, and 11 more. Tagged areas include Fintech, Payments, Banking as a Service, and Europe.


  The Treezor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Treezor''s developer surface includes authentication, getting-started guide, documentation, API reference, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Treezor API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: treezor-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 33.4
    developer_ergonomics: 57.1
    discoverability: 69.6
    operational_transparency: 23.7
  provenance:
    conformance: first-party
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
    score: 33.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Treezor Authentication
  slug: treezor-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Treezor Domain Security
  slug: treezor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Treezor Trust Center
  slug: treezor-trust-center
  summary_line: ISO 27001, PCI DSS
slug: treezor
tags:
- Fintech
- Payments
- Banking as a Service
- Europe
website: https://www.treezor.com
---
