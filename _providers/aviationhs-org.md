---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aviationhs Org Agentic Access
  operation_count: 3
  slug: aviationhs-org-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.aviationhs.org
  baseurl_source: declared
  description: The Aircraft API from AviationHS — 1 operation(s) for aircraft.
  name: AviationHS Aircraft API
  slug: aviationhs-org-aircraft-api
- baseURL: https://api.aviationhs.org
  baseurl_source: declared
  description: The Airports API from AviationHS — 1 operation(s) for airports.
  name: AviationHS Airports API
  slug: aviationhs-org-airports-api
- baseURL: https://api.aviationhs.org
  baseurl_source: declared
  description: The Runway API from AviationHS — 1 operation(s) for runway.
  name: AviationHS Runway API
  slug: aviationhs-org-runway-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/aviationhs-org/vocabulary/aviationhs-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aviationhs-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aviationhs-org/data-model/aviationhs-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aviationhs-org-data-model.yml
- group: agent
  href: https://artifacts.apis.io/aviationhs-org/agentic-access/aviationhs-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aviationhs-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aviationhs-org/rules/aviationhs-org-rules.yml
  title: ''
  type: Spectral
  url: rules/aviationhs-org-rules.yml
- group: agent
  href: https://artifacts.apis.io/aviationhs-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aviationhs-org/authentication/aviationhs-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aviationhs-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/aviationhs-org/errors/aviationhs-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aviationhs-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aviationhs-org/conformance/aviationhs-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aviationhs-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aviationhs-org/llms/aviationhs-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aviationhs-org-llms.txt
- group: build
  href: https://artifacts.apis.io/aviationhs-org/mcp/aviationhs-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aviationhs-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aviationhs-org/mcp/aviationhs-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aviationhs-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/aviationhs-org/hosts/aviationhs-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aviationhs-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/aviationhs-org/vendors/aviationhs-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aviationhs-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aviationhs-org/security/aviationhs-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aviationhs-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aviationhs.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aviationhs.org/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://aviationhs.org/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://aviationhs.org/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://aviationhs.org/guides/
- group: operate
  title: ''
  type: Support
  url: https://aviationhs.org/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aviationhs.org/privacy/
created: '2026-11-02'
description: AviationHS is a US charter brokerage offering an open quote engine that displays pricing, runway limits, and aircraft suitability across 3,418 routes and 847 airports. It integrates with ChatGPT and Claude via its MCP streamable API, providing real-time charter estimates and operational data for private jet travelers.
image: https://aviationhs.org/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.aviationhs.org.
  name: AviationHS MCP Server
  slug: aviationhs-org-mcp-yml
modified: '2026-11-02'
name: AviationHS
nav: Providers
network: true
overview: 'AviationHS publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Aircraft API, Airports API, and Runway API. Tagged areas include Private-Jet, Charter, Aviation, quote-engine, and MCP.


  The AviationHS catalog on APIs.io includes 1 Spectral governance ruleset.


  AviationHS''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 16 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: AviationHS API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: aviationhs-org-rules
scopes:
- name: Aviationhs Org Scopes
  scope_count: 0
  slug: aviationhs-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 46.3
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aviationhs Org Authentication
  slug: aviationhs-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aviationhs Org Domain Security
  slug: aviationhs-org-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: main
  slug: aviationhs-org-main-skill
slug: aviationhs-org
tags:
- Private-Jet
- Charter
- Aviation
- quote-engine
- MCP
website: https://aviationhs.org/
---
