---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Reference documentation for the AI Developer Toolkit APIs.
  name: Developer Toolkit API
  slug: developer-toolkit-api
- description: 'developertoolkit-ai API as documented publicly: 56 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: developertoolkit-ai API
  slug: developertoolkit-ai-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/developertoolkit-ai/plans/developertoolkit-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/developertoolkit-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/developertoolkit-ai/rules/developertoolkit-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/developertoolkit-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/developertoolkit-ai/json-ld/developertoolkit-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/developertoolkit-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/developertoolkit-ai/vocabulary/developertoolkit-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/developertoolkit-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/developertoolkit-ai/data-model/developertoolkit-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/developertoolkit-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/developertoolkit-ai/changelog/developertoolkit-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/developertoolkit-ai-changelog.yml
- group: start
  href: https://artifacts.apis.io/developertoolkit-ai/sandbox/developertoolkit-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/developertoolkit-ai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/developertoolkit-ai/conformance/developertoolkit-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/developertoolkit-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/developertoolkit-ai/llms/developertoolkit-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/developertoolkit-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/developertoolkit-ai/mcp/developertoolkit-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/developertoolkit-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/developertoolkit-ai/hosts/developertoolkit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/developertoolkit-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/developertoolkit-ai/vendors/developertoolkit-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/developertoolkit-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://developertoolkit.ai/en/login/?next=%2Fen%2F
- group: other
  title: ''
  type: Leadership
  url: https://developertoolkit.ai/en/claude-code/team/claude-tag/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wondelai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developertoolkit.ai/en/start/developer/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developertoolkit.ai/en/whats-new/
- group: docs
  title: ''
  type: APIReference
  url: https://developertoolkit.ai/en/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developertoolkit.ai/en/setup-pack/
- group: auth
  href: https://artifacts.apis.io/developertoolkit-ai/security/developertoolkit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/developertoolkit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developertoolkit.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://developertoolkit.ai/en/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://developertoolkit.ai/en/roadmap/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developertoolkit.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developertoolkit.ai/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://developertoolkit.ai/en/contents/
coverage:
  checked: '2026-10-30'
  detail: Reference documentation is public but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://developertoolkit.ai/en/reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Developertoolkit.ai provides an AI‑enhanced developer toolkit that aggregates guides, recipes, and resources for Claude, Code, Codex, and Cursor. It offers a free AI Dev Score, a pricing model for individuals and teams, and a suite of services including setup packs and team collaborations. The platform supports English and Polish content, delivering over 400 guides and 100+ recipes to accelerate agentic engineering workflows.
image: https://developertoolkit.ai/favicon.svg
json_schemas:
- name: GetV1AgentsIdResponse
  property_count: 2
  slug: developertoolkit-ai-get-v1-agents-id-response
- name: GetV1AgentsIdRunsRunidResponse
  property_count: 2
  slug: developertoolkit-ai-get-v1-agents-id-runs-runid-response
- name: PostOrdersRequest
  property_count: 1
  slug: developertoolkit-ai-post-orders-request
- name: PostPaymentsPaymentidRefundsRequest
  property_count: 3
  slug: developertoolkit-ai-post-payments-paymentid-refunds-request
- name: PostV1AgentsRequest
  property_count: 4
  slug: developertoolkit-ai-post-v1-agents-request
- name: PostV1AlphaSessionsRequest
  property_count: 4
  slug: developertoolkit-ai-post-v1-alpha-sessions-request
jsonld:
- class_count: 18
  name: Developertoolkit Ai Context
  property_count: 25
  slug: developertoolkit-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at developertoolkit.ai.
  name: developertoolkit-ai MCP Server
  slug: developertoolkit-ai-mcp-yml
modified: '2026-10-30'
name: developertoolkit-ai
nav: Providers
network: true
overview: 'developertoolkit-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Developer Tools, Agentic Engineering, Guides, and Pricing.


  The developertoolkit-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  developertoolkit-ai''s developer surface includes changelog, sandbox, API reference, getting-started guide, pricing, documentation, and 20 more developer resources.'
plans:
- name: Developertoolkit Ai Plans Pricing
  plan_count: 2
  slug: developertoolkit-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Developertoolkit Ai Rate Limits
  slug: developertoolkit-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: developertoolkit-ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: developertoolkit-ai-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 26.2
    discoverability: 57.5
    operational_transparency: 13.2
  previous_composite: 40.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/developertoolkit-ai/developertoolkit-ai-2026-11-03T130605.png
security:
- kind: authentication
  name: Developertoolkit Ai Authentication
  slug: developertoolkit-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Developertoolkit Ai Domain Security
  slug: developertoolkit-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: developertoolkit-ai
tags:
- Artificial Intelligence
- Developer Tools
- Agentic Engineering
- Guides
- Pricing
website: https://developertoolkit.ai/
---
