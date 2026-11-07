---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: derived
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
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent Groundcrew provides a human field services MCP server and REST API that enables AI agents and swarms to submit tasks, receive quotes, handle payment checkout, and track execution of real‑world w
  name: Agent Groundcrew API
  slug: agentgroundcrew-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/agentgroundcrew-com/rate-limits/agentgroundcrew-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentgroundcrew-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentgroundcrew-com/plans/agentgroundcrew-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentgroundcrew-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentgroundcrew-com/json-ld/agentgroundcrew-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentgroundcrew-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentgroundcrew-com/vocabulary/agentgroundcrew-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentgroundcrew-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentgroundcrew-com/data-model/agentgroundcrew-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentgroundcrew-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentgroundcrew-com/conventions/agentgroundcrew-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentgroundcrew-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentgroundcrew-com/conventions/agentgroundcrew-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentgroundcrew-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentgroundcrew-com/authentication/agentgroundcrew-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentgroundcrew-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentgroundcrew-com/conformance/agentgroundcrew-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentgroundcrew-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentgroundcrew-com/llms/agentgroundcrew-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentgroundcrew-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentgroundcrew-com/mcp/agentgroundcrew-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentgroundcrew-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentgroundcrew-com/hosts/agentgroundcrew-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentgroundcrew-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentgroundcrew-com/vendors/agentgroundcrew-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentgroundcrew-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://agentgroundcrew.com/trust
- group: auth
  href: https://artifacts.apis.io/agentgroundcrew-com/security/agentgroundcrew-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentgroundcrew-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentgroundcrew.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentgroundcrew.com/agents
- group: docs
  title: ''
  type: APIReference
  url: https://agentgroundcrew.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentgroundcrew.com/agents/start
- group: commercial
  title: ''
  type: Pricing
  url: https://agentgroundcrew.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentgroundcrew.com/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentgroundcrew.com/policies
- group: operate
  title: ''
  type: Support
  url: https://agentgroundcrew.com/inbox
created: '2026-10-30'
description: Agent Groundcrew provides a human field services MCP server and REST API that enables AI agents and swarms to submit tasks, receive quotes, handle payment checkout, and track execution of real‑world work such as site photography, logistics, procurement and project management. The service offers transparent pricing, pseudonymous token‑based authentication, and a documented OpenAPI contract. It connects software‑defined intent with on‑the‑ground human execution, delivering evidence and reports back to the calling agent.
image: https://agentgroundcrew.com/social-cover.png
jsonld:
- class_count: 1
  name: Agentgroundcrew Com Context
  property_count: 11
  slug: agentgroundcrew-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentgroundcrew.com.
  name: agentgroundcrew-com MCP Server
  slug: agentgroundcrew-com-mcp-yml
modified: '2026-10-30'
name: agentgroundcrew-com
nav: Providers
network: true
overview: 'agentgroundcrew-com is listed with 1 API on the [APIs.io](https://apis.io/) network: Agent Groundcrew API. Tagged areas include Field Service Management, Human Execution, MCP, Payments, and REST API.


  The agentgroundcrew-com catalog on APIs.io includes 1 JSON-LD context.


  agentgroundcrew-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, and 17 more developer resources.'
plans:
- name: Agentgroundcrew Com Plans Pricing
  plan_count: 5
  slug: agentgroundcrew-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Agentgroundcrew Com Rate Limits
  slug: agentgroundcrew-com-rate-limits
scopes:
- name: Agentgroundcrew Com Scopes
  scope_count: 0
  slug: agentgroundcrew-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.3
    catalog_earned_first_party: 24.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 51.3
    contract_governance: 8.3
    contract_quality: 34.7
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 46.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentgroundcrew-com/agentgroundcrew-com-2026-11-03T120403.png
security:
- kind: authentication
  name: Agentgroundcrew Com Authentication
  slug: agentgroundcrew-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentgroundcrew Com Domain Security
  slug: agentgroundcrew-com-domain-security
  summary_line: TLSv1.3
slug: agentgroundcrew-com
tags:
- Field Service Management
- Human Execution
- MCP
- Payments
- REST API
website: https://agentgroundcrew.com/
---
