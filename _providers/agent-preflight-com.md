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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Preflight decision service API providing allow/block/etc responses.
  name: Agent Preflight API
  slug: agent-preflight-api
- baseURL: https://api.agent-preflight.com
  baseurl_source: declared
  description: 'V0.3: V0.1 validates a proposed HTTP body against JSON Schema. POST /v0.2/preflight/tool-call returns allow|block|reuse|defer|advise for a budgeted tool call without executing it. Production charges $'
  name: Agent Preflight Api API
  slug: agent-preflight-api-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/agent-preflight-com/rules/agent-preflight-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-preflight-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-preflight-com/conformance/agent-preflight-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-preflight-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/agent-preflight-com/errors/agent-preflight-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-preflight-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agent-preflight-com/llms/agent-preflight-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-preflight-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agent-preflight-com/well-known/agent-preflight-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-preflight-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-preflight-com/hosts/agent-preflight-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-preflight-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-preflight-com/vendors/agent-preflight-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-preflight-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agent-preflight-com/security/agent-preflight-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-preflight-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-preflight.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-preflight.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.agent-preflight.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agent-preflight.com/docs
created: '2026-10-31'
description: Agent Preflight provides a pre‑execution decision service for autonomous agents, allowing them to check planned tool calls before spending resources. It returns one of allow, block, reuse, defer, or advise, and never executes the destination tool itself. The platform aims to improve safety and cost‑efficiency for AI‑driven workflows, offering clear guidance on whether a tool call should proceed.
layout: provider
modified: '2026-10-31'
name: Agent Preflight
nav: Providers
network: true
overview: 'Agent Preflight publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api API, and 1 more. Tagged areas include Agents, Preflight, Tool, and Decisions.


  The Agent Preflight catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Preflight''s developer surface includes documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Agent Preflight API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: agent-preflight-com-rules
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 36.3
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 22.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agent Preflight Com Domain Security
  slug: agent-preflight-com-domain-security
  summary_line: TLSv1.3
slug: agent-preflight-com
tags:
- Agents
- Preflight
- Tool
- Decisions
website: https://agent-preflight.com/
---
