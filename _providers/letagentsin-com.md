---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Letagentsin Com Agentic Access
  operation_count: 9
  slug: letagentsin-com-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 1
apis:
- description: Scan a domain via the Let Agents In API, returning a scorecard and detailed check results.
  name: Let Agents In API
  slug: letagentsin-com-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The C API from letagentsin-com — 1 operation(s) for c.
  name: letagentsin-com C API
  slug: letagentsin-com-c-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The Corpus.csv API from letagentsin-com — 1 operation(s) for corpus.csv.
  name: letagentsin-com Corpus.csv API
  slug: letagentsin-com-corpus-csv-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The Corpus.json API from letagentsin-com — 1 operation(s) for corpus.json.
  name: letagentsin-com Corpus.json API
  slug: letagentsin-com-corpus-json-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The Mcp API from letagentsin-com — 1 operation(s) for mcp.
  name: letagentsin-com MCP API
  slug: letagentsin-com-mcp-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The Scan API from letagentsin-com — 2 operation(s) for scan.
  name: letagentsin-com Scan API
  slug: letagentsin-com-scan-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The Visibility API from letagentsin-com — 1 operation(s) for visibility.
  name: letagentsin-com Visibility API
  slug: letagentsin-com-visibility-api
- baseURL: https://letagentsin.com
  baseurl_source: declared
  description: The Watch API from letagentsin-com — 1 operation(s) for watch.
  name: letagentsin-com Watch API
  slug: letagentsin-com-watch-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/letagentsin-com/agentic-access/letagentsin-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/letagentsin-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/letagentsin-com/rate-limits/letagentsin-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/letagentsin-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/letagentsin-com/plans/letagentsin-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/letagentsin-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/letagentsin-com/rules/letagentsin-com-rules.yml
  title: ''
  type: Spectral
  url: rules/letagentsin-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/letagentsin-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/letagentsin-com/errors/letagentsin-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/letagentsin-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/letagentsin-com/conformance/letagentsin-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/letagentsin-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/letagentsin-com/llms/letagentsin-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/letagentsin-com-llms.txt
- group: build
  href: https://artifacts.apis.io/letagentsin-com/mcp/letagentsin-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/letagentsin-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/letagentsin-com/mcp/letagentsin-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/letagentsin-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/letagentsin-com/well-known/letagentsin-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/letagentsin-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/letagentsin-com/hosts/letagentsin-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/letagentsin-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://letagentsin.com/privacy
- group: auth
  href: https://artifacts.apis.io/letagentsin-com/security/letagentsin-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/letagentsin-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://letagentsin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://letagentsin.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://letagentsin.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://letagentsin.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://letagentsin.com/#scan
- group: other
  title: ''
  type: Image
  url: https://letagentsin.com/icon.svg?icon.1nofz5_2t64-q.svg
created: '2026-10-30'
description: Let Agents In provides a platform that audits how coding agents interact with APIs and developer tools. It offers free site scans, detailed integration reports, and research findings. Users can run audits, view categories, pricing, and access API documentation for integration. The service is founded by Krystian Gwizdała and aims to improve agent integration reliability across the ecosystem.
layout: provider
mcp_servers:
- description: Remote MCP server at letagentsin.com.
  name: letagentsin-com MCP Server
  slug: letagentsin-com-mcp-yml
modified: '2026-10-30'
name: letagentsin-com
nav: Providers
network: true
overview: 'letagentsin-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including C API, Corpus.csv API, Corpus.json API, and 5 more. Tagged areas include Artificial Intelligence, Agent Audits, Developer Tools, API Testing, and Integration.


  The letagentsin-com catalog on APIs.io includes 1 Spectral governance ruleset.


  letagentsin-com''s developer surface includes documentation, API reference, pricing, getting-started guide, and 16 more developer resources.'
plans:
- name: Letagentsin Com Plans Pricing
  plan_count: 2
  slug: letagentsin-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Letagentsin Com Rate Limits
  slug: letagentsin-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: letagentsin-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: letagentsin-com-rules
scopes:
- name: Letagentsin Com Scopes
  scope_count: 0
  slug: letagentsin-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 50.5
    catalog_earned_first_party: 16.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 20.7
    discoverability: 53.3
    operational_transparency: 21.1
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/letagentsin-com/letagentsin-com-2026-11-03T134813.png
security:
- kind: authentication
  name: Letagentsin Com Authentication
  slug: letagentsin-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Letagentsin Com Domain Security
  slug: letagentsin-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: scan-domain
  slug: letagentsin-com-scan_domain
slug: letagentsin-com
tags:
- Artificial Intelligence
- Agent Audits
- Developer Tools
- API Testing
- Integration
website: https://letagentsin.com/
---
