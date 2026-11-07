---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Betslipdoctor Ai Agentic Access
  operation_count: 6
  slug: betslipdoctor-ai-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.betslipdoctor.ai
  baseurl_source: declared
  description: The Board API from BetSlip Doctor — 1 operation(s) for board.
  name: BetSlip Doctor Board API
  slug: betslipdoctor-ai-board-api
- baseURL: https://api.betslipdoctor.ai
  baseurl_source: declared
  description: The Grade API from BetSlip Doctor — 1 operation(s) for grade.
  name: BetSlip Doctor Grade API
  slug: betslipdoctor-ai-grade-api
- baseURL: https://api.betslipdoctor.ai
  baseurl_source: declared
  description: The History API from BetSlip Doctor — 1 operation(s) for history.
  name: BetSlip Doctor History API
  slug: betslipdoctor-ai-history-api
- baseURL: https://api.betslipdoctor.ai
  baseurl_source: declared
  description: The Reports API from BetSlip Doctor — 1 operation(s) for reports.
  name: BetSlip Doctor Reports API
  slug: betslipdoctor-ai-reports-api
- baseURL: https://api.betslipdoctor.ai
  baseurl_source: declared
  description: The Slips API from BetSlip Doctor — 1 operation(s) for slips.
  name: BetSlip Doctor Slips API
  slug: betslipdoctor-ai-slips-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/vocabulary/betslipdoctor-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/betslipdoctor-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/data-model/betslipdoctor-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/betslipdoctor-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/betslipdoctor-ai/agentic-access/betslipdoctor-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/betslipdoctor-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/betslipdoctor-ai/plans/betslipdoctor-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/betslipdoctor-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/rules/betslipdoctor-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/betslipdoctor-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/betslipdoctor-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/conventions/betslipdoctor-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/betslipdoctor-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/conventions/betslipdoctor-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/betslipdoctor-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/betslipdoctor-ai/authentication/betslipdoctor-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/betslipdoctor-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/errors/betslipdoctor-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/betslipdoctor-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/betslipdoctor-ai/conformance/betslipdoctor-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/betslipdoctor-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/betslipdoctor-ai/llms/betslipdoctor-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betslipdoctor-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/betslipdoctor-ai/mcp/betslipdoctor-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/betslipdoctor-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/betslipdoctor-ai/well-known/betslipdoctor-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betslipdoctor-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/betslipdoctor-ai/hosts/betslipdoctor-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betslipdoctor-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/betslipdoctor-ai/vendors/betslipdoctor-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betslipdoctor-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://betslipdoctor.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betslipdoctor.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://betslipdoctor.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://betslipdoctor.ai/signin
- group: docs
  title: ''
  type: Documentation
  url: https://betslipdoctor.ai/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://betslipdoctor.ai/guides/nfl-2026-kickoff-setup-and-onside-declaration
- group: docs
  title: ''
  type: APIReference
  url: https://betslipdoctor.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/betslipdoctor-ai/security/betslipdoctor-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betslipdoctor-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betslipdoctor.ai/
created: '2026-11-02'
description: 'BetSlip Doctor (BSD) is the platform where cappers bring their bettors: free clubs, verified records, graded picks and Tail. Grade is the proof engine. With eligible Pro or Elite Agent Connect access, your authorized agent can run a Grade and read a saved report you own. Explore graded picks and capper records in Tail. The service offers a mobile app for iOS and a web interface, supporting sports betting analytics and community features.'
image: https://betslipdoctor.ai/opengraph-image?f3dc0247f5bf3355
json_schemas:
- name: GradeSlipRequest
  property_count: 0
  slug: betslipdoctor-ai-grade-slip-request
- name: TrackSlipRequest
  property_count: 0
  slug: betslipdoctor-ai-track-slip-request
layout: provider
mcp_servers:
- description: Remote MCP server at betslipdoctor.ai.
  name: BetSlip Doctor MCP Server
  slug: betslipdoctor-ai-mcp-yml
modified: '2026-11-02'
name: BetSlip Doctor
nav: Providers
network: true
overview: 'BetSlip Doctor publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Board API, Grade API, History API, and 2 more. Tagged areas include Company, Sports, Betting, Analytics, and Mobile.


  The BetSlip Doctor catalog on APIs.io includes 1 Spectral governance ruleset.


  BetSlip Doctor''s developer surface includes authentication, support, pricing, documentation, getting-started guide, API reference, and 19 more developer resources.'
plans:
- name: Betslipdoctor Ai Plans Pricing
  plan_count: 3
  slug: betslipdoctor-ai-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: BetSlip Doctor API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: betslipdoctor-ai-rules
scopes:
- name: Betslipdoctor Ai Scopes
  scope_count: 0
  slug: betslipdoctor-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 49.7
    developer_ergonomics: 30.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betslipdoctor Ai Authentication
  slug: betslipdoctor-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Betslipdoctor Ai Domain Security
  slug: betslipdoctor-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: grade-slip
  slug: betslipdoctor-ai-grade-slip
- name: betslipdoctor-ai-track-and-grade-slip
  slug: betslipdoctor-ai-track-and-grade-slip
- name: track-slip
  slug: betslipdoctor-ai-track-slip
slug: betslipdoctor-ai
tags:
- Company
- Sports
- Betting
- Analytics
- Mobile
website: https://betslipdoctor.ai/
---
