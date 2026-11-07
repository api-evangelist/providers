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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Agent Reputation runs the Complaint Bureau: a registry of complaints about paid agent transactions.'
  name: Agent Reputation
  slug: agent-reputation
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agentreputation-dev/llms/agentreputation-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentreputation-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentreputation-dev/a2a/agentreputation-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentreputation-dev-a2a.yml
- group: other
  href: https://artifacts.apis.io/agentreputation-dev/hosts/agentreputation-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentreputation-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentreputation-dev/vendors/agentreputation-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentreputation-dev-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://agentreputation.dev/register
- group: auth
  href: https://artifacts.apis.io/agentreputation-dev/security/agentreputation-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentreputation-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentreputation.dev/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known endpoints.
  evidence:
  - status: 404
    url: https://agentreputation.dev/api/openapi.json
  - status: 200
    url: https://agentreputation.dev/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agent Reputation provides a platform for independent, cross-registry evidence before purchasing AI agents. It operates a Complaint Bureau for payment‑verified complaints, offers a paid pre‑purchase evidence brief, and supplies tools via MCP for checking complaints and filing them. The service emphasizes transparency, manual analysis, and does not provide universal ratings or endorsements.
layout: provider
modified: '2026-11-01'
name: Agent Reputation
nav: Providers
network: true
overview: 'Agent Reputation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Evidence, Complaint, Marketplace, and Platform.


  Agent Reputation''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 6.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentreputation Dev Domain Security
  slug: agentreputation-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentreputation-dev
tags:
- Artificial Intelligence
- Evidence
- Complaint
- Marketplace
- Platform
- Company
website: https://agentreputation.dev/
---
