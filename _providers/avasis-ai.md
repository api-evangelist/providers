---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Avasis Ai Agentic Access
  operation_count: 13
  slug: avasis-ai-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Admin API from Avasis — 4 operation(s) for admin.
  name: Avasis Admin API
  slug: avasis-ai-admin-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Authors API from Avasis — 1 operation(s) for authors.
  name: Avasis Authors API
  slug: avasis-ai-authors-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Avasis Exchange API API from Avasis — 1 operation(s) for avasis exchange api.
  name: Avasis Avasis Exchange API
  slug: avasis-ai-avasis-exchange-api-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Connect API from Avasis — 1 operation(s) for connect.
  name: Avasis Connect API
  slug: avasis-ai-connect-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Fixes API from Avasis — 1 operation(s) for fixes.
  name: Avasis Fixes API
  slug: avasis-ai-fixes-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Leaderboard API from Avasis — 1 operation(s) for leaderboard.
  name: Avasis Leaderboard API
  slug: avasis-ai-leaderboard-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Problems API from Avasis — 2 operation(s) for problems.
  name: Avasis Problems API
  slug: avasis-ai-problems-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Report API from Avasis — 1 operation(s) for report.
  name: Avasis Report API
  slug: avasis-ai-report-api
- baseURL: https://api.avasis.ai/v1
  baseurl_source: declared
  description: The Stats API from Avasis — 1 operation(s) for stats.
  name: Avasis Stats API
  slug: avasis-ai-stats-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/avasis-ai/vocabulary/avasis-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avasis-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avasis-ai/data-model/avasis-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avasis-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/avasis-ai/agentic-access/avasis-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avasis-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/avasis-ai/rules/avasis-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/avasis-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/avasis-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/avasis-ai/errors/avasis-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avasis-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/avasis-ai/conformance/avasis-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avasis-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/avasis-ai/overlays/avasis-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avasis-ai-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/avasis-ai/mcp/avasis-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/avasis-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/avasis-ai/mcp/avasis-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avasis-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/avasis-ai/hosts/avasis-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avasis-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/avasis-ai/security/avasis-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avasis-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avasis.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avasis.ai/connect/
- group: docs
  title: ''
  type: Documentation
  url: https://avasis.ai/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://avasis.ai/preflight/
created: '2026-11-02'
description: 'Avasis is a small AI research lab that builds AI that runs on your own devices, reads the physical world and works within limits you set. Their products include Nearmind, a private AI for iPad that runs offline without internet, OJAS 4D for drone‑photo 3D mapping, and QuantBase for meme‑coin rule‑based trading. They emphasize privacy, edge computing, and measurable performance, publishing verified numbers on real hardware. Contact: abhay@avasis.ai.'
image: https://avasis.ai/img/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.avasis.ai.
  name: Avasis MCP Server
  slug: avasis-ai-mcp-yml
modified: '2026-11-02'
name: Avasis
nav: Providers
network: true
overview: 'Avasis publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Authors API, Avasis Exchange API, and 6 more. Tagged areas include Artificial Intelligence, Edge Computing, Privacy, Research Lab, and Device AI.


  The Avasis catalog on APIs.io includes 1 Spectral governance ruleset.


  Avasis'' developer surface includes documentation and 15 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Avasis API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: avasis-ai-rules
scopes:
- name: Avasis Ai Scopes
  scope_count: 0
  slug: avasis-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 36.4
    developer_ergonomics: 16.0
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 24.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avasis Ai Authentication
  slug: avasis-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Avasis Ai Domain Security
  slug: avasis-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: problem-search
  slug: avasis-ai-problem-search
slug: avasis-ai
tags:
- Artificial Intelligence
- Edge Computing
- Privacy
- Research Lab
- Device AI
website: https://avasis.ai/
---
