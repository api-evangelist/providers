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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Verified human presence service API for AI agents, offering task submission, quoting, acceptance, and result retrieval.
  name: Presence API
  slug: presence-api
artifact_total: 9
asyncapis:
- description: ''
  name: Mctechnologies Presence Webhooks
  slug: mctechnologies-presence-webhooks
common:
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/rules/mctechnologies-presence-rules.yml
  title: ''
  type: Spectral
  url: rules/mctechnologies-presence-rules.yml
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/json-ld/mctechnologies-presence-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mctechnologies-presence-context.jsonld
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/vocabulary/mctechnologies-presence-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mctechnologies-presence-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/asyncapi/mctechnologies-presence-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mctechnologies-presence-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/data-model/mctechnologies-presence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mctechnologies-presence-data-model.yml
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/errors/mctechnologies-presence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mctechnologies-presence-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mctechnologies-presence/conformance/mctechnologies-presence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mctechnologies-presence-conformance.yml
- group: build
  href: https://artifacts.apis.io/mctechnologies-presence/mcp/mctechnologies-presence-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mctechnologies-presence-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/mctechnologies-presence/mcp/mctechnologies-presence-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mctechnologies-presence-mcp.yml
- group: other
  href: https://artifacts.apis.io/mctechnologies-presence/hosts/mctechnologies-presence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mctechnologies-presence-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mctechnologies-presence/security/mctechnologies-presence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mctechnologies-presence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mctechnologies.io/presence/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mctechnologies.io/presence/
- group: docs
  title: ''
  type: Documentation
  url: https://mctechnologies.io/presence/
- group: docs
  title: ''
  type: APIReference
  url: https://mctechnologies.io/presence/api/
coverage:
  checked: '2026-10-30'
  detail: API is in private beta and requires account creation; OpenAPI spec is mentioned but not publicly accessible.
  evidence:
  - status: 200
    url: https://mctechnologies.io/presence/api/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Presence API (Masterful Capital Technologies) offers verified human presence services for AI agents, providing on-demand physical verification, inspection, and witness work in South Florida. Clients can submit tasks that trigger a vetted operator to perform on-site verification with video evidence, delivering structured results, confidence scores, and signed attestations. The service supports institutions needing recurring verification such as insurers and lenders, with transparent pricing and a sandbox for evaluation. The API, currently in private beta, exposes task management endpoints and tool listings for integration into autonomous workflows.
jsonld:
- class_count: 6
  name: Mctechnologies Presence Context
  property_count: 23
  slug: mctechnologies-presence-context
layout: provider
mcp_servers:
- description: Remote MCP server at mctechnologies.io.
  name: Presence API (Masterful Capital Technologies) MCP Server
  slug: mctechnologies-presence-mcp-yml
modified: '2026-10-30'
name: Presence API (Masterful Capital Technologies)
nav: Providers
network: true
overview: 'Presence API (Masterful Capital Technologies) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Verification, Artificial Intelligence, On-Demand, and Inspection.


  The Presence API (Masterful Capital Technologies) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Presence API (Masterful Capital Technologies)''s developer surface includes documentation, API reference, and 13 more developer resources.'
plans:
- name: Mctechnologies Presence Plans Pricing
  plan_count: 0
  slug: mctechnologies-presence-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Presence API (Masterful Capital Technologies) API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mctechnologies-presence-rules
scopes:
- name: Mctechnologies Presence Scopes
  scope_count: 0
  slug: mctechnologies-presence-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.2
    developer_ergonomics: 13.1
    discoverability: 65.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mctechnologies-presence/mctechnologies-presence-2026-11-03T135412.png
security:
- kind: authentication
  name: Mctechnologies Presence Authentication
  slug: mctechnologies-presence-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mctechnologies Presence Domain Security
  slug: mctechnologies-presence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mctechnologies-presence
tags:
- Company
- Human Verification
- Artificial Intelligence
- On-Demand
- Inspection
website: https://mctechnologies.io/presence/
---
