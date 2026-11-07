---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Crisphive scheduling and dispatch platform
  name: Crisphive API
  slug: crisphive-api
- baseURL: https://api.crisphive.com
  baseurl_source: declared
  description: 'Crisphive API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Crisphive API
  slug: crisphive-com-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crisphive.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crisphive.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crisphive.com/
- group: operate
  href: https://artifacts.apis.io/crisphive-com/rate-limits/crisphive-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crisphive-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crisphive-com/plans/crisphive-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crisphive-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crisphive-com/rules/crisphive-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crisphive-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crisphive-com/json-ld/crisphive-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crisphive-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crisphive-com/vocabulary/crisphive-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crisphive-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crisphive-com/data-model/crisphive-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crisphive-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/crisphive-com/conventions/crisphive-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/crisphive-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/crisphive-com/conventions/crisphive-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crisphive-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/crisphive-com/sandbox/crisphive-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/crisphive-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/crisphive-com/authentication/crisphive-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crisphive-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/crisphive-com/conformance/crisphive-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crisphive-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crisphive-com/llms/crisphive-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crisphive-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/crisphive-com/mcp/crisphive-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crisphive-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crisphive-com/well-known/crisphive-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crisphive-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/crisphive-com/hosts/crisphive-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crisphive-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://crisphive.com/support
- group: start
  title: ''
  type: Login
  url: https://crisphive.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crisphive
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crisphive.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/crisphive-com/security/crisphive-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crisphive-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crisphive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crisphive.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://crisphive.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://crisphive.com/blog
coverage:
  checked: '2026-11-04'
  detail: Technical reference pages are rendered via Next.js and provide only HTML documentation, no OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.crisphive.com/technical-reference/authentication
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Crisphive provides AI‑powered scheduling and dispatch software for field service teams. Their platform re‑plans emergency routes in under three seconds, lets managers approve with a single click, and offers a free audit. It aims to streamline field operations with intelligent routing and real‑time updates. The solution integrates with existing ERP and GIS systems, offers a web dashboard, mobile apps for technicians, and supports multi‑language interfaces. Customers benefit from reduced travel time, higher first‑time‑fix rates, and detailed analytics for continuous improvement.
image: https://cdn.crisphive.com/web/images/marketing/home-dispatch-routes.jpg
json_schemas:
- name: GetV1JobTypesIdResponse
  property_count: 6
  slug: crisphive-com-get-v1-job-types-id-response
- name: PostV1CustomersRequest
  property_count: 9
  slug: crisphive-com-post-v1-customers-request
- name: PutV1CustomersIdRequest
  property_count: 11
  slug: crisphive-com-put-v1-customers-id-request
- name: PutV1CustomersIdResponse
  property_count: 7
  slug: crisphive-com-put-v1-customers-id-response
- name: PutV1JobTypesIdRequest
  property_count: 6
  slug: crisphive-com-put-v1-job-types-id-request
- name: PutV1VehiclesIdRequest
  property_count: 9
  slug: crisphive-com-put-v1-vehicles-id-request
jsonld:
- class_count: 20
  name: Crisphive Com Context
  property_count: 25
  slug: crisphive-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.crisphive.com requiring OAuth.
  name: Crisphive MCP Server
  slug: crisphive-com-mcp-yml
modified: '2026-11-04'
name: Crisphive
nav: Providers
network: true
overview: 'Crisphive is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Scheduling, Field Service Management, and Dispatch.


  The Crisphive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crisphive''s developer surface includes documentation, sandbox, authentication, support, API reference, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Crisphive Com Plans Pricing
  plan_count: 4
  slug: crisphive-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Crisphive Com Rate Limits
  slug: crisphive-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Crisphive API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: crisphive-com-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 52.4
    discoverability: 56.7
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crisphive Com Authentication
  slug: crisphive-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Crisphive Com Domain Security
  slug: crisphive-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crisphive-com
tags:
- Company
- Artificial Intelligence
- Scheduling
- Field Service Management
- Dispatch
website: https://crisphive.com/
---
