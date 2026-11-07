---
access_model:
  confidence: low
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
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/arclera-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/arclera-net/security/arclera-net-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arclera-net-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/arclera-net/llms/arclera-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arclera-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/arclera-net/mcp/arclera-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arclera-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arclera-net/well-known/arclera-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arclera-net-security.txt
- group: agent
  href: https://artifacts.apis.io/arclera-net/well-known/arclera-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arclera-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/arclera-net/hosts/arclera-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arclera-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/arclera-net/vendors/arclera-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arclera-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arclera-net/security/arclera-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arclera-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arclera-net/security/arclera-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arclera-net-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://arclera.net/llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://arclera.net/.well-known/security.txt
- group: company
  title: ''
  type: Website
  url: https://arclera.net/
coverage:
  checked: '2026-11-01'
  detail: The provider's website is publicly reachable but no OpenAPI, AsyncAPI, GraphQL, or AgentCard specifications were found at standard locations.
  evidence:
  - status: 200
    url: https://arclera.net/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Arclera Digital builds software for people and AI agents, designing, building, and supporting backend, cloud, and AI systems for business clients. Services include systems and backends, infrastructure and operations, AI integration, and architecture review consulting. The company offers MCP servers, LLM‑backed features, and open‑source model deployment.
image: https://arclera.net/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at arclera.net.
  name: Arclera Digital MCP Server
  slug: arclera-net-mcp-yml
modified: '2026-11-01'
name: Arclera Digital
nav: Providers
network: true
overview: Arclera Digital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Backend, Cloud, Artificial Intelligence, MCP, and Consulting.
plans:
- name: Arclera Net Plans Pricing
  plan_count: 0
  slug: arclera-net-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Arclera Net Rate Limits
  slug: arclera-net-rate-limits
scopes:
- name: Arclera Net Scopes
  scope_count: 0
  slug: arclera-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 9.9
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arclera Net Authentication
  slug: arclera-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arclera Net Domain Security
  slug: arclera-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arclera Net Vulnerability Disclosure
  slug: arclera-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arclera-net
tags:
- Backend
- Cloud
- Artificial Intelligence
- MCP
- Consulting
website: https://arclera.net/
---
