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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Cinegenta provides a Machine Control Protocol (MCP) JSON-RPC API for managing AI film projects. Documentation is available at the developer portal.
  name: Cinegenta MCP
  slug: cinegenta-mcp
- description: 'Cinegenta API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Cinegenta API
  slug: cinegenta-com-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/cinegenta-com/plans/cinegenta-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cinegenta-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cinegenta-com/rules/cinegenta-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cinegenta-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cinegenta-com/vocabulary/cinegenta-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cinegenta-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/cinegenta-com/changelog/cinegenta-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cinegenta-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/cinegenta-com/conformance/cinegenta-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cinegenta-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cinegenta-com/llms/cinegenta-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cinegenta-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cinegenta-com/mcp/cinegenta-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cinegenta-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cinegenta-com/well-known/cinegenta-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cinegenta-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cinegenta-com/hosts/cinegenta-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cinegenta-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cinegenta-com/vendors/cinegenta-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cinegenta-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cinegenta.com/mcp/security
- group: commercial
  title: ''
  type: Pricing
  url: https://cinegenta.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://cinegenta.com/guides/continuity-in-ai-filmmaking
- group: operate
  title: ''
  type: ChangeLog
  url: https://cinegenta.com/mcp/changelog
- group: auth
  href: https://artifacts.apis.io/cinegenta-com/security/cinegenta-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cinegenta-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cinegenta.com/
coverage:
  checked: '2026-11-04'
  detail: Only MCP JSON-RPC endpoint is available; no OpenAPI/GraphQL/AsyncAPI spec found despite documentation pages.
  evidence:
  - status: 405
    url: https://cinegenta.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Cinegenta is an AI director agent that transforms screenplays into complete, editable feature-length films. It handles casting, coverage, production, and final cut, offering a co-director experience powered by artificial intelligence. Users can generate movies from scripts, manage creative decisions, and receive editable video outputs, positioning Cinegenta as a SaaS platform for filmmakers and storytellers.
layout: provider
mcp_servers:
- description: Remote MCP server at cinegenta.com.
  name: Cinegenta MCP Server
  slug: cinegenta-com-mcp-yml
modified: '2026-11-03'
name: Cinegenta
nav: Providers
network: true
overview: 'Cinegenta is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Film Production, Video Generation, Editing, and Microdrama.


  The Cinegenta catalog on APIs.io includes 1 Spectral governance ruleset.


  Cinegenta''s developer surface includes changelog, pricing, documentation, and 13 more developer resources.'
plans:
- name: Cinegenta Com Plans Pricing
  plan_count: 4
  slug: cinegenta-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Cinegenta API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: cinegenta-com-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.8
    catalog_earned_first_party: 12.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 4.8
    discoverability: 53.3
    operational_transparency: 13.2
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cinegenta Com Domain Security
  slug: cinegenta-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cinegenta-com
tags:
- Artificial Intelligence
- Film Production
- Video Generation
- Editing
- Microdrama
- Personal Cinema
website: https://cinegenta.com/
---
