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
    mcp_server: documented
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pay-per-call verification services for AI agents via x402 protocol.
  name: AGORA Omega API
  slug: agora-omega-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/agoraverify-com/conformance/agoraverify-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agoraverify-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agoraverify-com/llms/agoraverify-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agoraverify-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agoraverify-com/a2a/agoraverify-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agoraverify-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agoraverify-com/mcp/agoraverify-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agoraverify-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agoraverify-com/hosts/agoraverify-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agoraverify-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agoraverify-com/security/agoraverify-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agoraverify-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agoraverify.com/
- group: docs
  title: ''
  type: APIReference
  url: https://agoraverify.com/openapi.json
- group: agent
  title: ''
  type: llms
  url: https://agoraverify.com/llms.txt
- group: agent
  title: ''
  type: MCP
  url: https://agoraverify.com/mcp
created: '2026-11-01'
description: AGORA Omega provides paid services for AI agents via the x402 protocol, offering pay‑per‑call access in USDC. Its platform includes French company data, counter‑party compliance checks, AI‑agent verification, supplier due‑diligence, payment guarding, stablecoin de‑peg risk indicators, and EU AI Act compliance checks. The service operates on multiple blockchains (e.g., Base, Arbitrum) and integrates public registries, sanctions lists, and on‑chain oracles to deliver real‑time risk and compliance scores for automated workflows.
layout: provider
mcp_servers:
- description: Remote MCP server at agoraverify.com.
  name: AGORA Omega MCP Server
  slug: agoraverify-com-mcp-yml
modified: '2026-11-01'
name: AGORA Omega
nav: Providers
network: true
overview: 'AGORA Omega is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Payments, Compliance, Data, and Services.


  AGORA Omega''s developer surface includes API reference and 9 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 6.6
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agoraverify Com Domain Security
  slug: agoraverify-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agoraverify-com
tags:
- Artificial Intelligence
- Payments
- Compliance
- Data
- Services
website: https://agoraverify.com/
---
