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
  band: agent-aware
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
    error_semantics: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Audito Lat Agentic Access
  operation_count: 6
  slug: audito-lat-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://agent.audito.lat
  baseurl_source: declared
  description: The Audit API from audito-lat — 1 operation(s) for audit.
  name: audito-lat Audit API
  slug: audito-lat-audit-api
- baseURL: https://agent.audito.lat
  baseurl_source: declared
  description: The Deep API from audito-lat — 1 operation(s) for deep.
  name: audito-lat Deep API
  slug: audito-lat-deep-api
- baseURL: https://agent.audito.lat
  baseurl_source: declared
  description: The Report API from audito-lat — 1 operation(s) for report.
  name: audito-lat Report API
  slug: audito-lat-report-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/audito-lat/agentic-access/audito-lat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audito-lat-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/audito-lat/rules/audito-lat-rules.yml
  title: ''
  type: Spectral
  url: rules/audito-lat-rules.yml
- group: agent
  href: https://artifacts.apis.io/audito-lat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://agent.audito.lat/llms.txt
- group: design
  href: https://artifacts.apis.io/audito-lat/errors/audito-lat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audito-lat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/audito-lat/conformance/audito-lat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audito-lat-conformance.yml
- group: agent
  href: https://artifacts.apis.io/audito-lat/llms/audito-lat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audito-lat-llms.txt
- group: build
  href: https://artifacts.apis.io/audito-lat/mcp/audito-lat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/audito-lat-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/audito-lat/mcp/audito-lat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audito-lat-mcp.yml
- group: auth
  href: https://artifacts.apis.io/audito-lat/well-known/audito-lat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audito-lat-security.txt
- group: auth
  href: https://artifacts.apis.io/audito-lat/well-known/audito-lat-agent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audito-lat-agent-security.txt
- group: agent
  href: https://artifacts.apis.io/audito-lat/well-known/audito-lat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audito-lat-well-known.yml
- group: other
  href: https://artifacts.apis.io/audito-lat/hosts/audito-lat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audito-lat-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.audito.lat/status
- group: auth
  href: https://artifacts.apis.io/audito-lat/security/audito-lat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/audito-lat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/audito-lat/security/audito-lat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audito-lat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audito.lat/
created: '2026-11-02'
description: 'audito-lat is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://agent.audito.lat/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at audito.lat.
  name: audito-lat MCP Server
  slug: audito-lat-mcp-yml
modified: '2026-11-02'
name: audito-lat
nav: Providers
network: true
overview: 'audito-lat publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Audit API, Deep API, and Report API. Tagged areas include Company.


  The audito-lat catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Audito Lat Plans Pricing
  plan_count: 0
  slug: audito-lat-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Audito Lat Rate Limits
  slug: audito-lat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: audito-lat API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: audito-lat-rules
scopes:
- name: Audito Lat Scopes
  scope_count: 0
  slug: audito-lat-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 45.9
    developer_ergonomics: 6.4
    discoverability: 48.3
    operational_transparency: 13.2
  previous_composite: 24.9
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Audito Lat Authentication
  slug: audito-lat-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Audito Lat Domain Security
  slug: audito-lat-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Audito Lat Vulnerability Disclosure
  slug: audito-lat-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: audit-site
  slug: audito-lat-audit-site
- name: deep-audit
  slug: audito-lat-deep-audit
slug: audito-lat
tags:
- Company
website: https://audito.lat/
---
