---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Constructionleader Guide Agentic Access
  operation_count: 8
  slug: constructionleader-guide-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Read‑only control‑plane API for the guide registry, providing metadata about guides, books and capability spine.
  name: Guide Registry API
  slug: guide-registry-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/constructionleader-guide/agentic-access/constructionleader-guide-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/constructionleader-guide-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/constructionleader-guide/rules/constructionleader-guide-rules.yml
  title: ''
  type: Spectral
  url: rules/constructionleader-guide-rules.yml
- group: design
  href: https://artifacts.apis.io/constructionleader-guide/vocabulary/constructionleader-guide-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/constructionleader-guide-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/constructionleader-guide/errors/constructionleader-guide-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/constructionleader-guide-problem-types.yml
- group: design
  href: https://artifacts.apis.io/constructionleader-guide/conformance/constructionleader-guide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/constructionleader-guide-conformance.yml
- group: agent
  href: https://artifacts.apis.io/constructionleader-guide/llms/constructionleader-guide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/constructionleader-guide-llms.txt
- group: build
  href: https://artifacts.apis.io/constructionleader-guide/mcp/constructionleader-guide-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/constructionleader-guide-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/constructionleader-guide/mcp/constructionleader-guide-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/constructionleader-guide-mcp.yml
- group: other
  href: https://artifacts.apis.io/constructionleader-guide/hosts/constructionleader-guide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/constructionleader-guide-hosts.yml
- group: other
  href: https://artifacts.apis.io/constructionleader-guide/vendors/constructionleader-guide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/constructionleader-guide-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://constructionleader.guide/guides
- group: docs
  title: ''
  type: APIReference
  url: https://constructionleader.guide/llms.txt
- group: auth
  href: https://artifacts.apis.io/constructionleader-guide/authentication/constructionleader-guide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/constructionleader-guide-authentication.yml
- group: auth
  href: https://artifacts.apis.io/constructionleader-guide/security/constructionleader-guide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constructionleader-guide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constructionleader.guide/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://constructionleader.guide/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constructionleader.guide/terms
- group: company
  title: ''
  type: About
  url: https://constructionleader.guide/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://constructionleader.guide/help
coverage:
  detail: OpenAPI spec found at https://constructionleader.guide/openapi.json belongs to bicycle.guide, not Construction Leader Guide.
  evidence:
  - status: 200
    url: https://constructionleader.guide/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Construction Leader Guide is a Bicycle LLC brand offering a curated collection of guides and books focused on construction leadership, safety management, and extraction work. The site provides free and paid resources, including topic guides, leadership frameworks, and systematic risk management processes, aimed at professionals seeking to improve team performance and safety compliance in construction and related industries. It also features a library, help center, and contact options for user support.
image: https://constructionleader.guide/opengraph-image-1oy18k?29435694197f5727
layout: provider
mcp_servers:
- description: Remote MCP server at constructionleader.guide.
  name: Construction Leader Guide MCP Server
  slug: constructionleader-guide-mcp-yml
modified: '2026-11-04'
name: Construction Leader Guide
nav: Providers
network: true
overview: 'Construction Leader Guide is listed with 1 API on the [APIs.io](https://apis.io/) network: Guide Registry API. Tagged areas include Construction, Leadership, Safety, Guides, and Bicycle.


  The Construction Leader Guide catalog on APIs.io includes 1 Spectral governance ruleset.


  Construction Leader Guide''s developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Construction Leader Guide API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: constructionleader-guide-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 33.3
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Constructionleader Guide Authentication
  slug: constructionleader-guide-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Constructionleader Guide Domain Security
  slug: constructionleader-guide-domain-security
  summary_line: TLSv1.3 · HSTS
slug: constructionleader-guide
tags:
- Construction
- Leadership
- Safety
- Guides
- Bicycle
website: https://constructionleader.guide/
---
