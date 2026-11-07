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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Longwatch Dev Agentic Access
  operation_count: 22
  slug: longwatch-dev-agentic-access
  summary_line: 22 operations · 18 acting
api_count: 1
apis:
- description: Monitoring API for intermittent AI agents, offering managed change detection for public web pages, RSS feeds, crypto price thresholds, and SEC filings.
  name: Longwatch Monitoring API
  slug: longwatch-monitoring-api
- baseURL: https://longwatch.dev
  baseurl_source: declared
  description: The mcp API from longwatch-dev — 1 operation(s) for mcp.
  name: longwatch-dev MCP API
  slug: longwatch-dev-mcp-api
- baseURL: https://longwatch.dev
  baseurl_source: declared
  description: The website monitoring API from longwatch-dev — 20 operation(s) for website monitoring.
  name: longwatch-dev website monitoring API
  slug: longwatch-dev-website-monitoring-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/longwatch-dev/agentic-access/longwatch-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/longwatch-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/longwatch-dev/plans/longwatch-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/longwatch-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/longwatch-dev/rules/longwatch-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/longwatch-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/longwatch-dev/vocabulary/longwatch-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/longwatch-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/longwatch-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/longwatch-dev/conventions/longwatch-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/longwatch-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/longwatch-dev/conventions/longwatch-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/longwatch-dev-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://longwatch.dev/
- group: design
  href: https://artifacts.apis.io/longwatch-dev/errors/longwatch-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/longwatch-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/longwatch-dev/conformance/longwatch-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/longwatch-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/longwatch-dev/llms/longwatch-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/longwatch-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/longwatch-dev/a2a/longwatch-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/longwatch-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/longwatch-dev/mcp/longwatch-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/longwatch-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/longwatch-dev/well-known/longwatch-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/longwatch-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/longwatch-dev/well-known/longwatch-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/longwatch-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/longwatch-dev/hosts/longwatch-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/longwatch-dev-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://longwatch.dev/privacy
- group: auth
  href: https://artifacts.apis.io/longwatch-dev/security/longwatch-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/longwatch-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/longwatch-dev/security/longwatch-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/longwatch-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://longwatch.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://longwatch.dev/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://longwatch.dev/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://longwatch.dev/pricing.md
created: '2026-10-30'
description: Longwatch provides a monitoring API for intermittent AI agents, offering managed change detection for public web pages, RSS feeds, crypto price thresholds, and SEC filings. Users can retrieve unseen alerts via cursor through MCP or REST, with a paid watch including seven days of polling. The service operates without requiring an API key or account, enabling seamless integration for AI-driven monitoring tasks.
image: https://longwatch.dev/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at longwatch.dev.
  name: longwatch-dev MCP Server
  slug: longwatch-dev-mcp-yml
modified: '2026-10-30'
name: longwatch-dev
nav: Providers
network: true
overview: 'longwatch-dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including MCP API, website monitoring API, and 1 more. Tagged areas include Company, Monitoring, Artificial Intelligence, Web, and Finance.


  The longwatch-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  longwatch-dev''s developer surface includes documentation, pricing, and 21 more developer resources.'
plans:
- name: Longwatch Dev Plans Pricing
  plan_count: 35
  slug: longwatch-dev-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: longwatch-dev API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: longwatch-dev-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 49.4
    developer_ergonomics: 11.3
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/longwatch-dev/longwatch-dev-2026-11-03T135039.png
security:
- kind: domain-security
  name: Longwatch Dev Domain Security
  slug: longwatch-dev-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Longwatch Dev Vulnerability Disclosure
  slug: longwatch-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: longwatch-dev-website-monitoring
  slug: longwatch-dev-website-monitoring
slug: longwatch-dev
tags:
- Company
- Monitoring
- Artificial Intelligence
- Web
- Finance
website: https://longwatch.dev/
---
