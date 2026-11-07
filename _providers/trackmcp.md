---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'TrackMCP API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: TrackMCP API
  slug: trackmcp-api
artifact_total: 11
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://trackmcp.com/mcp-server-analytics/quickstart
- group: commercial
  href: https://artifacts.apis.io/trackmcp/plans/trackmcp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trackmcp-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trackmcp/rules/trackmcp-rules.yml
  title: ''
  type: Spectral
  url: rules/trackmcp-rules.yml
- group: design
  href: https://artifacts.apis.io/trackmcp/json-ld/trackmcp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trackmcp-context.jsonld
- group: design
  href: https://artifacts.apis.io/trackmcp/vocabulary/trackmcp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trackmcp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trackmcp/data-model/trackmcp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trackmcp-data-model.yml
- group: design
  href: https://artifacts.apis.io/trackmcp/conformance/trackmcp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trackmcp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trackmcp/llms/trackmcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trackmcp-llms.txt
- group: other
  href: https://artifacts.apis.io/trackmcp/hosts/trackmcp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trackmcp-hosts.yml
- group: other
  href: https://artifacts.apis.io/trackmcp/vendors/trackmcp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trackmcp-vendors.yml
- group: build
  href: https://artifacts.apis.io/trackmcp/packages/trackmcp-packages.yml
  title: ''
  type: SDKs
  url: packages/trackmcp-packages.yml
- group: build
  href: https://artifacts.apis.io/trackmcp/packages/trackmcp-packages.yml
  title: ''
  type: Packages
  url: packages/trackmcp-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://trackmcp.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trackmcp
- group: operate
  title: ''
  type: ChangeLog
  url: https://trackmcp.com/blog/releases
- group: auth
  href: https://artifacts.apis.io/trackmcp/security/trackmcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trackmcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trackmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://trackmcp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://trackmcp.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://trackmcp.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://trackmcp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://trackmcp.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trackmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trackmcp.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.trackmcp.com/signup?content_path=%2F&content_cta=Get+started&content_surface=marketing
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found despite probing common spec endpoints.
  evidence:
  - status: 403
    url: https://trackmcp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: TrackMCP provides a platform to monitor and analyze usage of your MCP (Model‑Control‑Program) servers. It offers real‑time dashboards, workflow analytics, and tool‑level insights, helping developers understand client behavior, detect failures, and improve performance. Users can get started with a single CLI command, integrate SDKs for TypeScript and Python, and explore detailed documentation, pricing, and blog resources.
image: https://trackmcp.com/opengraph-image
json_schemas:
- name: GetApiV1AnalyticsResponse
  property_count: 9
  slug: trackmcp-get-api-v1-analytics-response
- name: PostApiV1AlertDestinationsRequest
  property_count: 2
  slug: trackmcp-post-api-v1-alert-destinations-request
- name: PostApiV1AnalyticsRequest
  property_count: 1
  slug: trackmcp-post-api-v1-analytics-request
- name: PostApiV1IngestRequest
  property_count: 14
  slug: trackmcp-post-api-v1-ingest-request
- name: PostApiV1OtelV1TracesRequest
  property_count: 8
  slug: trackmcp-post-api-v1-otel-v1-traces-request
- name: PostApiV1OtelV1TracesResponse
  property_count: 2
  slug: trackmcp-post-api-v1-otel-v1-traces-response
jsonld:
- class_count: 8
  name: Trackmcp Context
  property_count: 40
  slug: trackmcp-context
layout: provider
modified: '2026-10-19'
name: TrackMCP
nav: Providers
network: true
overview: 'TrackMCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Analytics, MCP, and Dashboards.


  The TrackMCP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TrackMCP''s developer surface includes getting-started guide, changelog, documentation, API reference, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Trackmcp Plans Pricing
  plan_count: 3
  slug: trackmcp-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: TrackMCP API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: trackmcp-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 25.0
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trackmcp/trackmcp-2026-11-03T144950.png
security:
- kind: domain-security
  name: Trackmcp Domain Security
  slug: trackmcp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trackmcp
tags:
- Company
- Monitoring
- Analytics
- MCP
- Dashboards
website: https://trackmcp.com/
---
