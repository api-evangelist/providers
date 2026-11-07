---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    idempotency: verified
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
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agenthelpnetwork Com Agentic Access
  operation_count: 7
  slug: agenthelpnetwork-com-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 2
apis:
- description: The Feedback API from agenthelpnetwork-com — 1 operation(s) for feedback.
  name: agenthelpnetwork-com Feedback API
  slug: agenthelpnetwork-com-feedback-api
- description: The Health API from agenthelpnetwork-com — 1 operation(s) for health.
  name: agenthelpnetwork-com Health API
  slug: agenthelpnetwork-com-health-api
- description: The Incidents API from agenthelpnetwork-com — 3 operation(s) for incidents.
  name: agenthelpnetwork-com Incidents API
  slug: agenthelpnetwork-com-incidents-api
- description: The Observations API from agenthelpnetwork-com — 2 operation(s) for observations.
  name: agenthelpnetwork-com Observations API
  slug: agenthelpnetwork-com-observations-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/agenthelpnetwork-com/llms/agenthelpnetwork-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenthelpnetwork-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agenthelpnetwork-com/vendors/agenthelpnetwork-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenthelpnetwork-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/agenthelpnetwork-com/agentic-access/agenthelpnetwork-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenthelpnetwork-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/rules/agenthelpnetwork-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agenthelpnetwork-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/json-ld/agenthelpnetwork-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenthelpnetwork-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/vocabulary/agenthelpnetwork-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenthelpnetwork-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agenthelpnetwork-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/data-model/agenthelpnetwork-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenthelpnetwork-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/conventions/agenthelpnetwork-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agenthelpnetwork-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/conventions/agenthelpnetwork-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agenthelpnetwork-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/errors/agenthelpnetwork-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenthelpnetwork-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agenthelpnetwork-com/conformance/agenthelpnetwork-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenthelpnetwork-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenthelpnetwork-com/mcp/agenthelpnetwork-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenthelpnetwork-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agenthelpnetwork-com/well-known/agenthelpnetwork-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenthelpnetwork-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenthelpnetwork-com/hosts/agenthelpnetwork-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenthelpnetwork-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenthelpnetwork.com/en/terms
- group: operate
  title: ''
  type: Support
  url: https://agenthelpnetwork.com/en/support
- group: company
  title: ''
  type: Website
  url: https://agenthelpnetwork.com/
- group: auth
  href: https://artifacts.apis.io/agenthelpnetwork-com/security/agenthelpnetwork-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenthelpnetwork-com-domain-security.yml
coverage:
  checked: '2026-11-01'
  detail: The OpenAPI file at https://agenthelpnetwork.com/openapi.json is not owned by Agent Help Network, describing a different product.
  evidence:
  - status: 200
    url: https://agenthelpnetwork.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'agenthelpnetwork-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
jsonld:
- class_count: 54
  name: Agenthelpnetwork Com Context
  property_count: 203
  slug: agenthelpnetwork-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agenthelpnetwork.com.
  name: agenthelpnetwork-com MCP Server
  slug: agenthelpnetwork-com-mcp-yml
modified: '2026-10-31'
name: agenthelpnetwork-com
nav: Providers
network: true
overview: 'agenthelpnetwork-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Feedback API, Health API, Incidents API, and 1 more. Tagged areas include Company.


  The agenthelpnetwork-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agenthelpnetwork-com''s developer surface includes support and 18 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: agenthelpnetwork-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agenthelpnetwork-com-rules
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 31.8
    catalog_earned_first_party: 0.0
    catalog_gap: 83.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 45.3
    developer_ergonomics: 8.8
    discoverability: 28.3
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agenthelpnetwork Com Domain Security
  slug: agenthelpnetwork-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: check-incident
  slug: agenthelpnetwork-com-check-incident
- name: health
  slug: agenthelpnetwork-com-health
slug: agenthelpnetwork-com
tags:
- Company
website: https://agenthelpnetwork.com/
---
