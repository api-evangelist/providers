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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for DigitalPipe platform to manage cloud traffic, routing, inspection, and security controls.
  name: DigitalPipe API
  slug: digitalpipe-api
- baseURL: https://app.digitalpipe.net
  baseurl_source: declared
  description: 'digitalpipe-net API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: digitalpipe-net API
  slug: digitalpipe-net-api
artifact_total: 13
common:
- group: docs
  title: ''
  type: Documentation
  url: https://digitalpipe.net/docs/pipes
- group: commercial
  href: https://artifacts.apis.io/digitalpipe-net/plans/digitalpipe-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitalpipe-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/digitalpipe-net/rules/digitalpipe-net-rules.yml
  title: ''
  type: Spectral
  url: rules/digitalpipe-net-rules.yml
- group: design
  href: https://artifacts.apis.io/digitalpipe-net/json-ld/digitalpipe-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/digitalpipe-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/digitalpipe-net/vocabulary/digitalpipe-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digitalpipe-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/digitalpipe-net/data-model/digitalpipe-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digitalpipe-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/digitalpipe-net/authentication/digitalpipe-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digitalpipe-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/digitalpipe-net/conformance/digitalpipe-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digitalpipe-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/digitalpipe-net/llms/digitalpipe-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digitalpipe-net-llms.txt
- group: other
  href: https://artifacts.apis.io/digitalpipe-net/hosts/digitalpipe-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitalpipe-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/digitalpipe-net/vendors/digitalpipe-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitalpipe-net-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.digitalpipe.net/trust
- group: operate
  title: ''
  type: Support
  url: https://app.digitalpipe.net/support
- group: start
  title: ''
  type: Login
  url: https://digitalpipe.net/login
- group: auth
  href: https://artifacts.apis.io/digitalpipe-net/security/digitalpipe-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalpipe-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://digitalpipe.net/
- group: docs
  title: ''
  type: APIReference
  url: https://digitalpipe.net/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://digitalpipe.net/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://digitalpipe.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digitalpipe.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digitalpipe.net/legal/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://digitalpipe.net/legal/security
- group: operate
  title: ''
  type: StatusPage
  url: https://digitalpipe.net/status
coverage:
  checked: '2026-10-30'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found.
  evidence:
  - status: 200
    url: https://digitalpipe.net/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: DigitalPipe provides a control layer for Managed Cloud Platform (MCP) traffic, offering a unified endpoint to route, inspect, and control tool calls across various services such as databases, payment processors, and CRM systems. Their platform enables one‑click kill switches, audit logging, and security controls, reducing operational risk and simplifying credential management for agents interacting with external APIs. The service includes both cloud‑hosted and self‑hosted deployment options, with tiered pricing plans for teams of any size.
json_schemas:
- name: GetApiAuditFlaggedResponse
  property_count: 3
  slug: digitalpipe-net-get-api-audit-flagged-response
- name: GetApiHostedMcpCatalogResponse
  property_count: 5
  slug: digitalpipe-net-get-api-hosted-mcp-catalog-response
- name: GetApiMetricsManifoldResponse
  property_count: 4
  slug: digitalpipe-net-get-api-metrics-manifold-response
- name: PostApiHostedMcpIdProxyRequest
  property_count: 1
  slug: digitalpipe-net-post-api-hosted-mcp-id-proxy-request
- name: PostApiManifoldIdToolsCallRequest
  property_count: 1
  slug: digitalpipe-net-post-api-manifold-id-tools-call-request
- name: PostApiManifoldIdToolsCallResponse
  property_count: 1
  slug: digitalpipe-net-post-api-manifold-id-tools-call-response
jsonld:
- class_count: 32
  name: Digitalpipe Net Context
  property_count: 30
  slug: digitalpipe-net-context
layout: provider
modified: '2026-10-30'
name: digitalpipe-net
nav: Providers
network: true
overview: 'digitalpipe-net is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, API Management, Security, and Cloud.


  The digitalpipe-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  digitalpipe-net''s developer surface includes documentation, authentication, support, API reference, getting-started guide, pricing, and 17 more developer resources.'
plans:
- name: Digitalpipe Net Plans Pricing
  plan_count: 4
  slug: digitalpipe-net-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: digitalpipe-net API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: digitalpipe-net-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 26.0
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digitalpipe Net Authentication
  slug: digitalpipe-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Digitalpipe Net Domain Security
  slug: digitalpipe-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digitalpipe-net
tags:
- Company
- MCP
- API Management
- Security
- Cloud
website: https://digitalpipe.net/
---
