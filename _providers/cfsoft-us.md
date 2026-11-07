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
  dimensions:
    agent_card: conformant
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cfsoft Us Agentic Access
  operation_count: 13
  slug: cfsoft-us-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 1
apis:
- description: Pay-per-call lookup over federal enforcement actions, regulatory notices, SEC filings and court records.
  name: Enforcement Check
  slug: enforcement-check
- description: Pay-per-call abandonment checks for WordPress.org plugins, npm packages and PyPI projects.
  name: Package Check
  slug: package-check
- baseURL: https://exclusions.cfsoft.us
  baseurl_source: declared
  description: The Batch API from cfsoft-us — 1 operation(s) for batch.
  name: cfsoft-us Batch API
  slug: cfsoft-us-batch-api
- baseURL: https://exclusions.cfsoft.us
  baseurl_source: declared
  description: The Check API from cfsoft-us — 1 operation(s) for check.
  name: cfsoft-us Check API
  slug: cfsoft-us-check-api
- baseURL: https://exclusions.cfsoft.us
  baseurl_source: declared
  description: The Health API from cfsoft-us — 1 operation(s) for health.
  name: cfsoft-us Health API
  slug: cfsoft-us-health-api
- baseURL: https://exclusions.cfsoft.us
  baseurl_source: declared
  description: The Report API from cfsoft-us — 1 operation(s) for report.
  name: cfsoft-us Report API
  slug: cfsoft-us-report-api
- baseURL: https://exclusions.cfsoft.us
  baseurl_source: declared
  description: The .well Known API from cfsoft-us — 1 operation(s) for .well known.
  name: cfsoft-us .well Known API
  slug: cfsoft-us-well-known-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/cfsoft-us/agentic-access/cfsoft-us-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cfsoft-us-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cfsoft-us/plans/cfsoft-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cfsoft-us-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cfsoft-us/rules/cfsoft-us-rules.yml
  title: ''
  type: Spectral
  url: rules/cfsoft-us-rules.yml
- group: agent
  href: https://artifacts.apis.io/cfsoft-us/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cfsoft-us/errors/cfsoft-us-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cfsoft-us-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cfsoft-us/conformance/cfsoft-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cfsoft-us-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cfsoft-us/llms/cfsoft-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cfsoft-us-llms.txt
- group: other
  href: https://artifacts.apis.io/cfsoft-us/a2a/cfsoft-us-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cfsoft-us-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cfsoft-us/mcp/cfsoft-us-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cfsoft-us-mcp.yml
- group: other
  href: https://artifacts.apis.io/cfsoft-us/hosts/cfsoft-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfsoft-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/cfsoft-us/vendors/cfsoft-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cfsoft-us-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cfsoft-us/security/cfsoft-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfsoft-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cfsoft.us/
created: '2026-10-29'
description: 'CF Soft: pay-per-call x402 APIs for AI agents (exclusion screening, package abandonment risk, federal enforcement lookups), two published Chrome extensions, and the software behind CFExclusion and CourtPulse. Built by one person.'
image: https://cfsoft.us/assets/logo-768.png
layout: provider
mcp_servers:
- description: Remote MCP server at enforcement.cfsoft.us.
  name: cfsoft-us MCP Server
  slug: cfsoft-us-mcp-yml
modified: '2026-10-29'
name: cfsoft-us
nav: Providers
network: true
overview: 'cfsoft-us publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Check API, Health API, and 4 more. Tagged areas include Company, Artificial Intelligence, Finance, and Legal.


  The cfsoft-us catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Cfsoft Us Plans Pricing
  plan_count: 2
  slug: cfsoft-us-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Cfsoft Us Rate Limits
  slug: cfsoft-us-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: cfsoft-us API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: cfsoft-us-rules
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.8
    catalog_earned_first_party: 8.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 15.9
    contract_quality: 42.5
    developer_ergonomics: 6.4
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cfsoft-us/cfsoft-us-2026-11-03T123739.png
security:
- kind: domain-security
  name: Cfsoft Us Domain Security
  slug: cfsoft-us-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cfsoft-us
tags:
- Company
- Artificial Intelligence
- Finance
- Legal
website: https://cfsoft.us/
---
