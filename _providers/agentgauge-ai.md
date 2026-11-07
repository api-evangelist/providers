---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgentGauge provides an AI‑readiness scanner that grades websites on AI agent discoverability, trustworthiness, and usability.
  name: AgentGauge API
  slug: agentgauge-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/agentgauge-ai/plans/agentgauge-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentgauge-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentgauge-ai/conformance/agentgauge-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentgauge-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentgauge-ai/llms/agentgauge-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentgauge-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentgauge-ai/mcp/agentgauge-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentgauge-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentgauge-ai/well-known/agentgauge-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentgauge-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentgauge-ai/hosts/agentgauge-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentgauge-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentgauge-ai/vendors/agentgauge-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentgauge-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.agentgauge.ai/directory/news
- group: auth
  href: https://artifacts.apis.io/agentgauge-ai/security/agentgauge-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentgauge-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentgauge.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentgauge.ai/guides
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentgauge.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentgauge.ai/privacy
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found after probing common spec endpoints.
  evidence:
  - status: 404
    url: https://www.agentgauge.ai/openapi.json
  - status: 404
    url: https://www.agentgauge.ai/openapi.yaml
  - status: 404
    url: https://www.agentgauge.ai/swagger.json
  - status: 404
    url: https://www.agentgauge.ai/api-docs
  - status: 404
    url: https://www.agentgauge.ai/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AgentGauge provides an AI-readiness scanner that grades websites on how discoverable, trustworthy, and usable they are for AI agents and answer engines. It offers llms.txt listings, schema extraction, agent tools signals, and a watch service that re‑scans sites weekly, delivering actionable fixes. Users can paste any URL to see if AI can find and act on the site.
image: https://www.agentgauge.ai/agentgauge-wordmark.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.agentgauge.ai.
  name: AgentGauge MCP Server
  slug: agentgauge-ai-mcp-yml
modified: '2026-10-31'
name: AgentGauge
nav: Providers
network: true
overview: 'AgentGauge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agent Readiness, WebScanning, SEO, and Llms.txt.


  AgentGauge''s developer surface includes documentation and 12 more developer resources.'
plans:
- name: Agentgauge Ai Plans Pricing
  plan_count: 1
  slug: agentgauge-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Agentgauge Ai Rate Limits
  slug: agentgauge-ai-rate-limits
scopes:
- name: Agentgauge Ai Scopes
  scope_count: 0
  slug: agentgauge-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.5
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentgauge Ai Authentication
  slug: agentgauge-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentgauge Ai Domain Security
  slug: agentgauge-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentgauge-ai
tags:
- Artificial Intelligence
- Agent Readiness
- WebScanning
- SEO
- Llms.txt
website: https://www.agentgauge.ai/
---
