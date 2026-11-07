---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public REST API providing access to the SkillDB skill catalog.
  name: SkillDB API
  slug: skilldb-api
- description: 'skilldb-dev API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: skilldb-dev API
  slug: skilldb-dev-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/skilldb-dev/plans/skilldb-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skilldb-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/skilldb-dev/rules/skilldb-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/skilldb-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/skilldb-dev/json-ld/skilldb-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/skilldb-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/skilldb-dev/vocabulary/skilldb-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/skilldb-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/skilldb-dev/data-model/skilldb-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skilldb-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/skilldb-dev/cli/skilldb-dev-cli.yml
  title: ''
  type: CLI
  url: cli/skilldb-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/skilldb-dev/conformance/skilldb-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skilldb-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/skilldb-dev/llms/skilldb-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skilldb-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/skilldb-dev/mcp/skilldb-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/skilldb-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/skilldb-dev/well-known/skilldb-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skilldb-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/skilldb-dev/hosts/skilldb-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skilldb-dev-hosts.yml
- group: build
  href: https://artifacts.apis.io/skilldb-dev/packages/skilldb-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/skilldb-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/skilldb-dev/packages/skilldb-dev-packages.yml
  title: ''
  type: Packages
  url: packages/skilldb-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skilldb.dev/terms
- group: start
  title: ''
  type: Sandbox
  url: https://skilldb.dev/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skilldb.dev/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://skilldb.dev/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://skilldb.dev/demo/chatgpt-pilot
- group: auth
  href: https://artifacts.apis.io/skilldb-dev/security/skilldb-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skilldb-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skilldb.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://skilldb.dev/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skilldb.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://skilldb.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://skilldb.dev/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devchad-cmd/skilldb-sdk
coverage:
  checked: '2026-10-30'
  detail: Documentation lists API endpoints but no OpenAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://skilldb.dev/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: SkillDB provides an AI‑agent‑first skills library that lets autonomous agents instantly access expert knowledge across thousands of domains. The platform hosts over 6,174 curated skills organized into 448 packs, covering areas such as programming, writing, design, finance, and more. Developers can browse, search, and integrate skills via a CLI, REST API, or SDKs for popular agents like Claude Code, Cursor, and Codex. SkillDB offers free and paid plans, detailed documentation, and open‑source SDKs, empowering agents to solve complex tasks without manual prompt engineering.
image: https://skilldb.dev/og-image.jpg
json_schemas:
- name: GetApiStatsResponse
  property_count: 5
  slug: skilldb-dev-get-api-stats-response
- name: GetApiV1ProfileResponse
  property_count: 4
  slug: skilldb-dev-get-api-v1-profile-response
- name: GetApiV1SkillsIdResponse
  property_count: 5
  slug: skilldb-dev-get-api-v1-skills-id-response
- name: PostApiCommunityRequest
  property_count: 3
  slug: skilldb-dev-post-api-community-request
- name: PostApiV1MySkillsRequest
  property_count: 4
  slug: skilldb-dev-post-api-v1-my-skills-request
- name: PutApiV1SkillsResponse
  property_count: 4
  slug: skilldb-dev-put-api-v1-skills-response
jsonld:
- class_count: 14
  name: Skilldb Dev Context
  property_count: 25
  slug: skilldb-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at skilldb.dev.
  name: skilldb-dev MCP Server
  slug: skilldb-dev-mcp-yml
modified: '2026-10-30'
name: skilldb-dev
nav: Providers
network: true
overview: 'skilldb-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Skills, Catalog, Developer Tools, and Open Source.


  The skilldb-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  skilldb-dev''s developer surface includes CLI, sandbox, changelog, getting-started guide, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Skilldb Dev Plans Pricing
  plan_count: 3
  slug: skilldb-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Skilldb Dev Rate Limits
  slug: skilldb-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: skilldb-dev API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: skilldb-dev-rules
scopes:
- name: Skilldb Dev Scopes
  scope_count: 0
  slug: skilldb-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 33.3
    contract_quality: 24.7
    developer_ergonomics: 34.5
    discoverability: 66.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.0
  provenance:
    conformance: first-party
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/skilldb-dev/skilldb-dev-2026-11-03T143302.png
security:
- kind: authentication
  name: Skilldb Dev Authentication
  slug: skilldb-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Skilldb Dev Domain Security
  slug: skilldb-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skilldb-dev
tags:
- Artificial Intelligence
- Skills
- Catalog
- Developer Tools
- Open Source
website: https://skilldb.dev/
---
