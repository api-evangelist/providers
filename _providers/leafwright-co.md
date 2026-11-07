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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Leafwright is an HTML to PDF API. POST HTML, a public URL, or a Handlebars template plus JSON data and get a signed download URL back — no Chromium in your serverless function.
  name: Leafwright API
  slug: leafwright-api
- description: 'leafwright-co API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: leafwright-co API
  slug: leafwright-co-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/leafwright-co/plans/leafwright-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leafwright-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/leafwright-co/rules/leafwright-co-rules.yml
  title: ''
  type: Spectral
  url: rules/leafwright-co-rules.yml
- group: design
  href: https://artifacts.apis.io/leafwright-co/json-ld/leafwright-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/leafwright-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/leafwright-co/vocabulary/leafwright-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/leafwright-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/leafwright-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/leafwright-co/data-model/leafwright-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leafwright-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/leafwright-co/conformance/leafwright-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leafwright-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/leafwright-co/llms/leafwright-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leafwright-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/leafwright-co/mcp/leafwright-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leafwright-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/leafwright-co/well-known/leafwright-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leafwright-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/leafwright-co/hosts/leafwright-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leafwright-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/leafwright-co/vendors/leafwright-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leafwright-co-vendors.yml
- group: build
  href: https://artifacts.apis.io/leafwright-co/packages/leafwright-co-packages.yml
  title: ''
  type: SDKs
  url: packages/leafwright-co-packages.yml
- group: build
  href: https://artifacts.apis.io/leafwright-co/packages/leafwright-co-packages.yml
  title: ''
  type: Packages
  url: packages/leafwright-co-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://leafwright.co/docs/mcp
- group: auth
  href: https://artifacts.apis.io/leafwright-co/security/leafwright-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leafwright-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leafwright.co/
- group: docs
  title: ''
  type: Documentation
  url: https://leafwright.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://leafwright.co/docs/api
- group: company
  title: ''
  type: Blog
  url: https://leafwright.co/blog
- group: operate
  title: ''
  type: Support
  url: https://leafwright.co/support
- group: commercial
  title: ''
  type: Pricing
  url: https://leafwright.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leafwright.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leafwright.co/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation provides API details but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or gRPC spec.
  evidence:
  - status: 200
    url: https://leafwright.co/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Leafwright provides an HTML‑to‑PDF API for serverless environments. It accepts raw HTML, a public URL, or a Handlebars template with JSON data and returns a signed download URL, eliminating the need for Chromium in serverless functions. The same engine powers a document studio offering AI‑generated template drafts, brand kits, and webhook‑based logging. Leafwright targets developers building PDF generation services with minimal overhead.
image: https://leafwright.co/logo-mark.png
json_schemas:
- name: PatchApiV1DashboardBrandRequest
  property_count: 8
  slug: leafwright-co-patch-api-v1-dashboard-brand-request
- name: PostApiV1BillingCheckoutRequest
  property_count: 2
  slug: leafwright-co-post-api-v1-billing-checkout-request
- name: PostApiV1DashboardWebhooksRequest
  property_count: 3
  slug: leafwright-co-post-api-v1-dashboard-webhooks-request
- name: PostApiV1PdfsRequest
  property_count: 2
  slug: leafwright-co-post-api-v1-pdfs-request
- name: PostApiV1PdfsResponse
  property_count: 6
  slug: leafwright-co-post-api-v1-pdfs-response
jsonld:
- class_count: 5
  name: Leafwright Co Context
  property_count: 20
  slug: leafwright-co-context
layout: provider
mcp_servers:
- description: Remote MCP server at leafwright.co.
  name: leafwright-co MCP Server
  slug: leafwright-co-mcp-yml
modified: '2026-10-30'
name: leafwright-co
nav: Providers
network: true
overview: 'leafwright-co is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HTML to PDF, Serverless, Artificial Intelligence, and PDF.


  The leafwright-co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  leafwright-co''s developer surface includes getting-started guide, documentation, API reference, engineering blog, support, pricing, and 18 more developer resources.'
plans:
- name: Leafwright Co Plans Pricing
  plan_count: 2
  slug: leafwright-co-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: leafwright-co API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: leafwright-co-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 36.8
    contract_governance: 19.7
    contract_quality: 24.7
    developer_ergonomics: 31.4
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 35.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/leafwright-co/leafwright-co-2026-11-03T134746.png
security:
- kind: domain-security
  name: Leafwright Co Domain Security
  slug: leafwright-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: leafwright-co
tags:
- Company
- HTML to PDF
- Serverless
- Artificial Intelligence
- PDF
website: https://leafwright.co/
---
