---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Billieio Agentic Access
  operation_count: 18
  slug: billieio-agentic-access
  summary_line: 18 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: API reference for Billie payment integration
  name: Billie API
  slug: billie-api
- baseURL: https://paella-sandbox.billie.io/api/v2
  baseurl_source: spec
  description: This API uses OAuth 2.0 for secure authentication. Different keys are used for the `sandbox` and `production` environments. Both systems operate completely independent, however both show largely the s
  name: Billieio Authentication API
  slug: billieio-authentication-api
- baseURL: https://paella-sandbox.billie.io/api/v2
  baseurl_source: spec
  description: The Back-end Order Creation API from Billieio — 2 operation(s) for back-end order creation.
  name: Billieio Back-end Order Creation API
  slug: billieio-back-end-order-creation-api
- baseURL: https://paella-sandbox.billie.io/api/v2
  baseurl_source: spec
  description: The Captures API from Billieio — 5 operation(s) for captures.
  name: Billieio Captures API
  slug: billieio-captures-api
- baseURL: https://paella-sandbox.billie.io/api/v2
  baseurl_source: spec
  description: '## To integrate the Billie checkout widget, the following steps are required: 1. Add the Billie checkout widget bundle to your checkout page 2. Provide config data _(with the `session_id` from the ser'
  name: Billieio Front-end Order Creation API
  slug: billieio-front-end-order-creation-api
- baseURL: https://paella-sandbox.billie.io/api/v2
  baseurl_source: spec
  description: The Order Management API from Billieio — 2 operation(s) for order management.
  name: Billieio Order Management API
  slug: billieio-order-management-api
artifact_total: 20
asyncapis:
- description: ''
  name: Billieio Webhooks
  slug: billieio-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/agentic-access/billieio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/billieio-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/rules/billieio-rules.yml
  title: ''
  type: Spectral
  url: rules/billieio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/json-ld/billieio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billieio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/vocabulary/billieio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billieio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/data-model/billieio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billieio-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/errors/billieio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/billieio-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/conformance/billieio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billieio-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/scopes/billieio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/billieio-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billieio-www-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/vendors/billieio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billieio-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/asyncapi/billieio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/billieio-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: https://billie.io/coordinated-vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/authentication/billieio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/billieio-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/llms/billieio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billieio-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billieio-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/billieio-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/well-known/billieio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billieio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/hosts/billieio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billieio-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.billie.io/s/?language=en_US
- group: operate
  title: ''
  type: StatusPage
  url: https://status.billie.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billie.io/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billie.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/security/billieio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/billieio-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/security/billieio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billieio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billie.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docs.billie.io/mcp
  - status: 401
    url: https://help.billie.io/mcp/v1
  - status: 403
    url: https://equityzen.com/company/billieio
  reason: partner-login
  state: gated
created: '2026-09-28'
description: Billie is a fintech platform that provides B2B payment solutions, enabling businesses to buy now and pay later, invoice financing, and flexible checkout options. It serves over 1.3 million buyers and 9,000 merchants across Europe, processing billions in transaction volume. The service includes integration via APIs for order creation, payment processing, and refunds, with support for multiple payment methods and partner integrations.
json_schemas:
- name: Order Creation Request
  property_count: 9
  slug: billieio-create-order-request
- name: Get Invoice Response
  property_count: 13
  slug: billieio-get-invoice-response
- name: Hpp Checkout Session Create Request
  property_count: 11
  slug: billieio-hpp-checkout-session-ecommerce
- name: Hpp Checkout Session Create Request
  property_count: 11
  slug: billieio-hpp-checkout-session-instore
- name: Hpp Checkout Session Create Request
  property_count: 11
  slug: billieio-hpp-checkout-session-telesales
- name: Order Entity
  property_count: 13
  slug: billieio-order
jsonld:
- class_count: 34
  name: Billieio Context
  property_count: 106
  slug: billieio-context
layout: provider
modified: '2026-09-28'
name: Billieio
nav: Providers
network: true
overview: 'Billieio publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Back-end Order Creation API, Captures API, and 3 more. Tagged areas include Fintech, Payments, B2B, and Europe.


  The Billieio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Billieio''s developer surface includes authentication, support, API reference, documentation, and 21 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Billieio API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 1
  slug: billieio-rules
scopes:
- name: Billieio Scopes
  scope_count: 1
  slug: billieio-scopes
  summary_line: 1 scope · password
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 67.9
    developer_ergonomics: 33.3
    discoverability: 51.8
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/billieio/refs/heads/main/screenshots/billieio-2026-10-11T102211.png
security:
- kind: authentication
  name: Billieio Authentication
  slug: billieio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Billieio Domain Security
  slug: billieio-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Billieio Vulnerability Disclosure
  slug: billieio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: billieio
tags:
- Fintech
- Payments
- B2B
- Europe
website: https://www.billie.io
---
