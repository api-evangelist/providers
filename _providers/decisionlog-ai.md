---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API generated from the GraphQL schema
  name: Decision Log API
  slug: decision-log-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/decisionlog-ai/plans/decisionlog-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decisionlog-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/decisionlog-ai/vocabulary/decisionlog-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decisionlog-ai-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/decisionlog-ai/cli/decisionlog-ai-cli.yml
  title: ''
  type: CLI
  url: cli/decisionlog-ai-cli.yml
- group: start
  href: https://artifacts.apis.io/decisionlog-ai/sandbox/decisionlog-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/decisionlog-ai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/decisionlog-ai/conformance/decisionlog-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decisionlog-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/decisionlog-ai/a2a/decisionlog-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/decisionlog-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/decisionlog-ai/mcp/decisionlog-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decisionlog-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/decisionlog-ai/well-known/decisionlog-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decisionlog-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/decisionlog-ai/hosts/decisionlog-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decisionlog-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/decisionlog-ai/vendors/decisionlog-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decisionlog-ai-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.decisionlog.ai/sandbox
- group: auth
  href: https://artifacts.apis.io/decisionlog-ai/security/decisionlog-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decisionlog-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.decisionlog.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.decisionlog.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.decisionlog.ai/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.decisionlog.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.decisionlog.ai/sign-up
created: '2026-11-05'
description: Decision Log provides a system of record for decisions made by people and AI agents, offering immutable decision storage, provenance, audit trails, and supersession history. Teams can retrieve, review, and manage decisions through a web app, REST API, GraphQL endpoint, CLI, or MCP, ensuring reliable retrieval and governance across organizational workflows. The platform supports authentication, role‑based access, rate‑limits, and sandboxed agent interactions, enabling secure and auditable decision management.
image: https://www.decisionlog.ai/og/marketing/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.decisionlog.ai requiring OAuth.
  name: Decision Log MCP Server
  slug: decisionlog-ai-mcp-yml
modified: '2026-11-05'
name: Decision Log
nav: Providers
network: true
overview: 'Decision Log is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DecisionLog, Artificial Intelligence, Knowledge Management, Audit Trail, and Collaboration.


  Decision Log''s developer surface includes CLI, sandbox, documentation, getting-started guide, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Decisionlog Ai Plans Pricing
  plan_count: 2
  slug: decisionlog-ai-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Decisionlog Ai Domain Security
  slug: decisionlog-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: decisionlog-ai
tags:
- DecisionLog
- Artificial Intelligence
- Knowledge Management
- Audit Trail
- Collaboration
website: https://www.decisionlog.ai/
---
