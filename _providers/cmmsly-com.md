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
  band: agent-ready
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Cmmsly Com Agentic Access
  operation_count: 18
  slug: cmmsly-com-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://cmmsly.com
  baseurl_source: declared
  description: dataset
  name: cmmsly-com Dataset API
  slug: cmmsly-com-dataset-api
- baseURL: https://cmmsly.com
  baseurl_source: declared
  description: The mcp API from cmmsly-com — 1 operation(s) for mcp.
  name: cmmsly-com MCP API
  slug: cmmsly-com-mcp-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/cmmsly-com/agentic-access/cmmsly-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cmmsly-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cmmsly-com/rules/cmmsly-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cmmsly-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cmmsly-com/vocabulary/cmmsly-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cmmsly-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cmmsly-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://cmmsly.com/terms
- group: design
  href: https://artifacts.apis.io/cmmsly-com/errors/cmmsly-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cmmsly-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cmmsly-com/conformance/cmmsly-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cmmsly-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cmmsly-com/llms/cmmsly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cmmsly-com-llms.txt
- group: build
  href: https://artifacts.apis.io/cmmsly-com/mcp/cmmsly-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cmmsly-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cmmsly-com/mcp/cmmsly-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cmmsly-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cmmsly-com/well-known/cmmsly-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cmmsly-com-security.txt
- group: auth
  href: https://artifacts.apis.io/cmmsly-com/well-known/cmmsly-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cmmsly-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/cmmsly-com/well-known/cmmsly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cmmsly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cmmsly-com/hosts/cmmsly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cmmsly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cmmsly-com/vendors/cmmsly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cmmsly-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cmmsly-com/authentication/cmmsly-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cmmsly-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cmmsly-com/security/cmmsly-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cmmsly-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cmmsly-com/security/cmmsly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cmmsly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cmmsly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cmmsly.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cmmsly.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cmmsly.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://cmmsly.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://cmmsly.com/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://cmmsly.com/tools/
created: '2026-10-29'
description: Cmmsly provides a cloud‑based equipment maintenance management system that helps organizations track, schedule, and document maintenance activities. The platform offers free worksheets for pricing reactive work, planning schedules, and daily checks, enabling teams to estimate costs and improve asset reliability. Built around a register of equipment, Cmmsly delivers tools for maintenance logs, forklift checklists, and work order templates, all accessible via a web interface and an MCP‑style API.
image: https://cmmsly.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cmmsly.com.
  name: cmmsly-com MCP Server
  slug: cmmsly-com-mcp-yml
modified: '2026-10-29'
name: cmmsly-com
nav: Providers
network: true
overview: 'cmmsly-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Company, CMMS, Maintenance, Equipment, and Software.


  The cmmsly-com catalog on APIs.io includes 1 Spectral governance ruleset.


  cmmsly-com''s developer surface includes authentication, API reference, pricing, support, getting-started guide, and 20 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: cmmsly-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cmmsly-com-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 30.2
    discoverability: 75.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cmmsly-com/cmmsly-com-2026-11-03T124630.png
security:
- kind: authentication
  name: Cmmsly Com Authentication
  slug: cmmsly-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cmmsly Com Domain Security
  slug: cmmsly-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Cmmsly Com Vulnerability Disclosure
  slug: cmmsly-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 7
skills:
- name: cmmsly-com-dataset-columns
  slug: cmmsly-com-dataset_columns
- name: cmmsly-com-dataset-compare
  slug: cmmsly-com-dataset_compare
- name: cmmsly-com-dataset-provenance
  slug: cmmsly-com-dataset_provenance
- name: cmmsly-com-dataset-row
  slug: cmmsly-com-dataset_row
- name: cmmsly-com-dataset-search
  slug: cmmsly-com-dataset_search
- name: cmmsly-com-dataset-stats
  slug: cmmsly-com-dataset_stats
- name: cmmsly-com-dataset-top
  slug: cmmsly-com-dataset_top
slug: cmmsly-com
tags:
- Company
- CMMS
- Maintenance
- Equipment
- Software
- Tools
website: https://cmmsly.com/
---
