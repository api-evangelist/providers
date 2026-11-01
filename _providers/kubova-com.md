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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Kubova public REST API for container and pallet loading calculations.
  name: Kubova REST API
  slug: kubova-rest-api
- description: 'kubova-com API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: kubova-com API
  slug: kubova-com-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/kubova-com/rate-limits/kubova-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kubova-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kubova-com/plans/kubova-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kubova-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kubova-com/rules/kubova-com-rules.yml
  title: ''
  type: Spectral
  url: rules/kubova-com-rules.yml
- group: design
  href: https://artifacts.apis.io/kubova-com/json-ld/kubova-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kubova-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/kubova-com/vocabulary/kubova-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kubova-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kubova-com/data-model/kubova-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kubova-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/kubova-com/authentication/kubova-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kubova-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/kubova-com/errors/kubova-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kubova-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kubova-com/conformance/kubova-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kubova-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kubova-com/llms/kubova-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kubova-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/kubova-com/mcp/kubova-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kubova-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/kubova-com/hosts/kubova-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kubova-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kubova-com/vendors/kubova-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kubova-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/kubova-com/packages/kubova-com-packages.yml
  title: ''
  type: SDKs
  url: packages/kubova-com-packages.yml
- group: build
  href: https://artifacts.apis.io/kubova-com/packages/kubova-com-packages.yml
  title: ''
  type: Packages
  url: packages/kubova-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://kubova.com/en/login
- group: start
  title: ''
  type: GettingStarted
  url: https://kubova.com/en/docs/mcp
- group: auth
  href: https://artifacts.apis.io/kubova-com/security/kubova-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kubova-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kubova.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kubova.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://kubova.com/en/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://kubova.com/en/docs/api
- group: operate
  title: ''
  type: Support
  url: https://kubova.com/en/contact
- group: company
  title: ''
  type: Blog
  url: https://kubova.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kubova.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kubova.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kubova.com/en/privacy
coverage:
  checked: '2026-10-31'
  detail: Public HTML docs exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or gRPC spec is provided.
  evidence:
  - status: 200
    url: https://kubova.com/en/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Kubova provides a 3‑D container and pallet loading calculator with a public REST API and MCP (Machine‑Control Protocol). Users can plan container and pallet loads in three dimensions, fit more cartons on mixed‑SKU shipments, export load plans as PDFs or JSON, and integrate the service into AI agents, workflow tools, or custom applications. The platform supports metric and imperial units, offers a modern 3‑D viewer, and includes pricing tiers, documentation, and a blog.
image: https://kubova.com/og-image.jpg
json_schemas:
- name: PostApiV1MeRequest
  property_count: 3
  slug: kubova-com-post-api-v1-me-request
- name: PostApiV1PackRequest
  property_count: 3
  slug: kubova-com-post-api-v1-pack-request
- name: PostApiV1PackResponse
  property_count: 4
  slug: kubova-com-post-api-v1-pack-response
- name: PostApiV1ReportRequest
  property_count: 3
  slug: kubova-com-post-api-v1-report-request
jsonld:
- class_count: 4
  name: Kubova Com Context
  property_count: 8
  slug: kubova-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at kubova.com requiring OAuth.
  name: kubova-com MCP Server
  slug: kubova-com-mcp-yml
modified: '2026-10-30'
name: kubova-com
nav: Providers
network: true
overview: 'kubova-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, 3D-Loading, API, and Container-Optimization.


  The kubova-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kubova-com''s developer surface includes authentication, getting-started guide, documentation, API reference, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Kubova Com Plans Pricing
  plan_count: 4
  slug: kubova-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Kubova Com Rate Limits
  slug: kubova-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: kubova-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: kubova-com-rules
scopes:
- name: Kubova Com Scopes
  scope_count: 0
  slug: kubova-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 84.7
    catalog_earned_first_party: 0.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 47.5
    developer_ergonomics: 64.3
    discoverability: 56.7
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kubova Com Authentication
  slug: kubova-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kubova Com Domain Security
  slug: kubova-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kubova-com
tags:
- Company
- Logistics
- 3D-Loading
- API
- Container-Optimization
website: https://kubova.com/
---
