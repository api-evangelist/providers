---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documented at the Guides page, providing access to guide resources.
  name: Church Leader Guide API
  slug: church-leader-guide-api
- description: 'Church Leader Guide API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Church Leader Guide API
  slug: churchleader-guide-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/churchleader-guide/plans/churchleader-guide-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/churchleader-guide-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/churchleader-guide/rules/churchleader-guide-rules.yml
  title: ''
  type: Spectral
  url: rules/churchleader-guide-rules.yml
- group: design
  href: https://artifacts.apis.io/churchleader-guide/json-ld/churchleader-guide-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/churchleader-guide-context.jsonld
- group: design
  href: https://artifacts.apis.io/churchleader-guide/vocabulary/churchleader-guide-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/churchleader-guide-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/churchleader-guide/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/churchleader-guide/data-model/churchleader-guide-data-model.yml
  title: ''
  type: DataModel
  url: data-model/churchleader-guide-data-model.yml
- group: design
  href: https://artifacts.apis.io/churchleader-guide/conformance/churchleader-guide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/churchleader-guide-conformance.yml
- group: agent
  href: https://artifacts.apis.io/churchleader-guide/llms/churchleader-guide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/churchleader-guide-llms.txt
- group: build
  href: https://artifacts.apis.io/churchleader-guide/mcp/churchleader-guide-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/churchleader-guide-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/churchleader-guide/mcp/churchleader-guide-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/churchleader-guide-mcp.yml
- group: other
  href: https://artifacts.apis.io/churchleader-guide/hosts/churchleader-guide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/churchleader-guide-hosts.yml
- group: other
  href: https://artifacts.apis.io/churchleader-guide/vendors/churchleader-guide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/churchleader-guide-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://churchleader.guide/terms
- group: operate
  title: ''
  type: Support
  url: https://churchleader.guide/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://churchleader.guide/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://churchleader.guide/guides
- group: docs
  title: ''
  type: APIReference
  url: https://churchleader.guide/llms.txt
- group: auth
  href: https://artifacts.apis.io/churchleader-guide/security/churchleader-guide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/churchleader-guide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://churchleader.guide/
coverage:
  checked: '2026-11-04'
  detail: OpenAPI document at https://churchleader.guide/openapi.json describes a different product (bicycle.guide) and does not belong to Church Leader Guide.
  evidence:
  - status: 200
    url: https://churchleader.guide/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Church Leader Guide provides ministry training resources that cover leading an organization, including volunteers, money, staff, growth, and the weight of a congregation's trust. It offers guides, books, and tools to help church leaders develop effective strategies and deepen their impact within their communities.
image: https://churchleader.guide/opengraph-image-1oy18k?29435694197f5727
json_schemas:
- name: GetApiV1GuidesResponse
  property_count: 3
  slug: churchleader-guide-get-api-v1-guides-response
jsonld:
- class_count: 1
  name: Churchleader Guide Context
  property_count: 0
  slug: churchleader-guide-context
layout: provider
mcp_servers:
- description: Remote MCP server at churchleader.guide.
  name: Church Leader Guide MCP Server
  slug: churchleader-guide-mcp-yml
modified: '2026-11-03'
name: Church Leader Guide
nav: Providers
network: true
overview: 'Church Leader Guide is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Church, Leadership, Ministry, Training, and Community.


  The Church Leader Guide catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Church Leader Guide''s developer surface includes support, documentation, API reference, and 16 more developer resources.'
plans:
- name: Churchleader Guide Plans Pricing
  plan_count: 3
  slug: churchleader-guide-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Church Leader Guide API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: churchleader-guide-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 17.1
    discoverability: 56.7
    operational_transparency: 0.0
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Churchleader Guide Domain Security
  slug: churchleader-guide-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-guides
  slug: churchleader-guide-list-guides
slug: churchleader-guide
tags:
- Church
- Leadership
- Ministry
- Training
- Community
website: https://churchleader.guide/
---
