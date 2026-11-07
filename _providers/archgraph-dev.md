---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
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
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.archgraph.dev
  baseurl_source: declared
  description: 'ArchGraph API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: ArchGraph API
  slug: archgraph-dev-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/archgraph-dev/plans/archgraph-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/archgraph-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/archgraph-dev/rules/archgraph-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/archgraph-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/archgraph-dev/json-ld/archgraph-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/archgraph-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/archgraph-dev/vocabulary/archgraph-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/archgraph-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/archgraph-dev/data-model/archgraph-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/archgraph-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/archgraph-dev/authentication/archgraph-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/archgraph-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/archgraph-dev/errors/archgraph-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/archgraph-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/archgraph-dev/conformance/archgraph-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archgraph-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/archgraph-dev/llms/archgraph-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archgraph-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/archgraph-dev/hosts/archgraph-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archgraph-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/archgraph-dev/vendors/archgraph-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/archgraph-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/archgraph-dev/security/archgraph-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archgraph-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archgraph.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archgraph.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archgraph.dev/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archgraph.dev/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://archgraph.dev/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://archgraph.dev/pricing
created: '2026-11-01'
description: ArchGraph provides code intelligence for AI agents by parsing repositories and exposing a Model Context Protocol (MCP) endpoint. Users can connect their codebase, obtain an instant MCP endpoint, and enable AI agents to understand code with compiler-backed precision across 16 languages. The platform offers a free tier, quick setup, and integrates with tools like Claude, Cursor, Windsurf, and Cline.
image: https://archgraph.dev/favicon.svg
json_schemas:
- name: PostApiReposIdExtractRequest
  property_count: 6
  slug: archgraph-dev-post-api-repos-id-extract-request
- name: PostApiReposIdExtractResponse
  property_count: 5
  slug: archgraph-dev-post-api-repos-id-extract-response
jsonld:
- class_count: 2
  name: Archgraph Dev Context
  property_count: 11
  slug: archgraph-dev-context
layout: provider
modified: '2026-11-01'
name: ArchGraph
nav: Providers
network: true
overview: 'ArchGraph is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Code Intelligence, MCP, Developer Tools, and Platform.


  The ArchGraph catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ArchGraph''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, and 12 more developer resources.'
plans:
- name: Archgraph Dev Plans Pricing
  plan_count: 3
  slug: archgraph-dev-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: ArchGraph API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 4
  slug: archgraph-dev-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 24.5
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 34.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Archgraph Dev Authentication
  slug: archgraph-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Archgraph Dev Domain Security
  slug: archgraph-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: archgraph-dev
tags:
- Artificial Intelligence
- Code Intelligence
- MCP
- Developer Tools
- Platform
website: https://archgraph.dev/
---
