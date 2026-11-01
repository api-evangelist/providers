---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gumballtools Com Agentic Access
  operation_count: 4
  slug: gumballtools-com-agentic-access
  summary_line: 4 operations
api_count: 4
apis:
- description: A directory of the Gumball tools, a live view of who is calling them, and a single MCP server that exposes every tool in the portfolio.
  name: Project Gumball
  slug: project-gumball
- description: Builds a full period-by-period amortization schedule — principal, interest, PMI, extra-principal, running balance — for monthly or daily-accrual loans.
  name: Amortization Schedule
  slug: amortization-schedule
- description: Convert height and weight in any common unit, then compute BMI, resting and total energy expenditure, and protein targets.
  name: Body Metrics
  slug: body-metrics
- description: Validates IBAN, ISBN, EAN/UPC and card numbers, and suggests corrections for invalid inputs.
  name: Check Digit Validator
  slug: check-digit-validator
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/gumballtools-com/agentic-access/gumballtools-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gumballtools-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/gumballtools-com/rate-limits/gumballtools-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gumballtools-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gumballtools-com/plans/gumballtools-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gumballtools-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gumballtools-com/rules/gumballtools-com-rules.yml
  title: ''
  type: Spectral
  url: rules/gumballtools-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/gumballtools-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/gumballtools-com/changelog/gumballtools-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gumballtools-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/gumballtools-com/lifecycle/gumballtools-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gumballtools-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gumballtools-com/errors/gumballtools-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gumballtools-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gumballtools-com/conformance/gumballtools-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gumballtools-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gumballtools-com/llms/gumballtools-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gumballtools-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/gumballtools-com/mcp/gumballtools-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gumballtools-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/gumballtools-com/hosts/gumballtools-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gumballtools-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gumballtools-com/vendors/gumballtools-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gumballtools-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gumballtools-com/security/gumballtools-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gumballtools-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gumballtools.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gumballtools.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://gumballtools.com/.well-known/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://gumballtools.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gumballtools.com/docs
created: '2026-10-29'
description: Project Gumball is an open‑source experiment that aggregates a collection of small utility tools into a single MCP (Multi‑Capability Provider) endpoint. The platform offers a directory of fifteen tools, each accessible via a web page, a JSON API, and an MCP server, allowing agents to discover, call, and pay for capabilities in a unified way. It showcases how agents can find each other, agree on value, and record usage metrics, providing transparent insight into tool usage and integration patterns across the ecosystem.
image: https://via.placeholder.com/300
layout: provider
mcp_servers:
- description: Remote MCP server at gumballtools.com.
  name: gumballtools-com MCP Server
  slug: gumballtools-com-mcp-yml
modified: '2026-10-29'
name: gumballtools-com
nav: Providers
network: true
overview: 'gumballtools-com is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Project Gumball, and 3 more. Tagged areas include Company, API, MCP, Tools, and OpenSource.


  The gumballtools-com catalog on APIs.io includes 1 Spectral governance ruleset.


  gumballtools-com''s developer surface includes changelog, documentation, API reference, getting-started guide, and 15 more developer resources.'
plans:
- name: Gumballtools Com Plans Pricing
  plan_count: 1
  slug: gumballtools-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Gumballtools Com Rate Limits
  slug: gumballtools-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: gumballtools-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: gumballtools-com-rules
scopes:
- name: Gumballtools Com Scopes
  scope_count: 0
  slug: gumballtools-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 44.5
    discoverability: 70.0
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gumballtools Com Authentication
  slug: gumballtools-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gumballtools Com Domain Security
  slug: gumballtools-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-tools
  slug: gumballtools-com-list-tools
slug: gumballtools-com
tags:
- Company
- API
- MCP
- Tools
- OpenSource
website: https://gumballtools.com/
---
