---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Vigotime Com Agentic Access
  operation_count: 16
  slug: vigotime-com-agentic-access
  summary_line: 16 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.vigotime.com
  baseurl_source: declared
  description: The Account API from vigotime-com — 3 operation(s) for account.
  name: vigotime-com Account API
  slug: vigotime-com-account-api
- baseURL: https://api.vigotime.com
  baseurl_source: declared
  description: The API Tokens API from vigotime-com — 2 operation(s) for api tokens.
  name: vigotime-com API Tokens API
  slug: vigotime-com-api-tokens-api
- baseURL: https://api.vigotime.com
  baseurl_source: declared
  description: The Health API from vigotime-com — 3 operation(s) for health.
  name: vigotime-com Health API
  slug: vigotime-com-health-api
- baseURL: https://api.vigotime.com
  baseurl_source: declared
  description: The Signup API from vigotime-com — 2 operation(s) for signup.
  name: vigotime-com Signup API
  slug: vigotime-com-signup-api
- baseURL: https://api.vigotime.com
  baseurl_source: declared
  description: The Stateless Solve API from vigotime-com — 4 operation(s) for stateless solve.
  name: vigotime-com Stateless Solve API
  slug: vigotime-com-stateless-solve-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/vigotime-com/agentic-access/vigotime-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vigotime-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/vigotime-com/plans/vigotime-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vigotime-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vigotime-com/rules/vigotime-com-rules.yml
  title: ''
  type: Spectral
  url: rules/vigotime-com-rules.yml
- group: design
  href: https://artifacts.apis.io/vigotime-com/json-ld/vigotime-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vigotime-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/vigotime-com/vocabulary/vigotime-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vigotime-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vigotime-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vigotime-com/data-model/vigotime-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vigotime-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/vigotime-com/errors/vigotime-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vigotime-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vigotime-com/conformance/vigotime-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vigotime-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vigotime-com/llms/vigotime-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vigotime-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/vigotime-com/mcp/vigotime-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vigotime-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vigotime-com/well-known/vigotime-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vigotime-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/vigotime-com/hosts/vigotime-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vigotime-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vigotime.com/de/terms-condition
- group: operate
  title: ''
  type: Support
  url: https://vigotime.com/de/app/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vigotime.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vigotime.com/de/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://vigotime.com/de/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://vigotime.com/de/changelog
- group: company
  title: ''
  type: Blog
  url: https://vigotime.com/de/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vigotime.com/
- group: auth
  href: https://artifacts.apis.io/vigotime-com/security/vigotime-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vigotime-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vigotime.com/
created: '2026-10-30'
description: Vigotime provides an automated scheduling and time tracking platform for shift operations. It offers automatic planning, employee wish system, vacation management, sick leave handling, mobile apps, rule compliance, and shift swap marketplace, targeting industries such as hospitals, retail, and hospitality. The solution includes transparent pricing tiers and a demo request feature, aiming to streamline workforce management and improve operational efficiency.
image: https://vigotime.com/assets/images/metadata/og.png
json_schemas:
- name: GenerationResultSchema
  property_count: 13
  slug: vigotime-com-generation-result-schema
- name: HealthResponse
  property_count: 8
  slug: vigotime-com-health-response
- name: SolveRequest
  property_count: 38
  slug: vigotime-com-solve-request
- name: SolveStatusResponse
  property_count: 12
  slug: vigotime-com-solve-status-response
- name: SolveSubmitResponse
  property_count: 4
  slug: vigotime-com-solve-submit-response
- name: TokenListEntry
  property_count: 9
  slug: vigotime-com-token-list-entry
jsonld:
- class_count: 34
  name: Vigotime Com Context
  property_count: 144
  slug: vigotime-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.vigotime.com.
  name: vigotime-com MCP Server
  slug: vigotime-com-mcp-yml
modified: '2026-10-30'
name: vigotime-com
nav: Providers
network: true
overview: 'vigotime-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API Tokens API, Health API, and 2 more. Tagged areas include Company, Scheduling, TimeTracking, WorkforceManagement, and Automation.


  The vigotime-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  vigotime-com''s developer surface includes support, pricing, changelog, engineering blog, API reference, and 18 more developer resources.'
plans:
- name: Vigotime Com Plans Pricing
  plan_count: 3
  slug: vigotime-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: vigotime-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: vigotime-com-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 58.8
    developer_ergonomics: 16.1
    discoverability: 65.0
    operational_transparency: 31.6
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
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vigotime Com Domain Security
  slug: vigotime-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: vigotime-com-stateless-solve
  slug: vigotime-com-stateless-solve
slug: vigotime-com
tags:
- Company
- Scheduling
- TimeTracking
- WorkforceManagement
- Automation
website: https://vigotime.com/
---
