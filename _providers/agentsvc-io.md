---
access_model:
  confidence: high
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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pay‑per‑call web services for AI agents via x402 protocol.
  name: agentsvc.io API
  slug: agentsvc-io-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/agentsvc-io/plans/agentsvc-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentsvc-io-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/agentsvc-io/sandbox/agentsvc-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agentsvc-io-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://agentsvc.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/agentsvc-io/authentication/agentsvc-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsvc-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentsvc-io/conformance/agentsvc-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsvc-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentsvc-io/llms/agentsvc-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsvc-io-llms.txt
- group: other
  href: https://artifacts.apis.io/agentsvc-io/a2a/agentsvc-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentsvc-io-a2a.yml
- group: build
  href: https://artifacts.apis.io/agentsvc-io/mcp/agentsvc-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentsvc-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentsvc-io/mcp/agentssvc-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentssvc-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentsvc-io/well-known/agentsvc-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentsvc-io-security.txt
- group: agent
  href: https://artifacts.apis.io/agentsvc-io/well-known/agentsvc-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentsvc-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentsvc-io/hosts/agentsvc-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentsvc-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentsvc.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentsvc.io/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://agentsvc.io/docs
- group: auth
  href: https://artifacts.apis.io/agentsvc-io/security/agentsvc-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentsvc-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentsvc-io/security/agentsvc-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsvc-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsvc.io/
created: '2026-11-01'
description: Agentsvc.io is a pay‑per‑call API marketplace that enables AI agents to purchase a wide range of web services on demand. It offers over 127 endpoints covering web scraping, content summarization, data extraction, citation, document conversion, compliance checks, crypto data, and more, all billed in USDC across multiple blockchains. The platform requires no account or API key, providing instant access via the x402 payment protocol.
layout: provider
mcp_servers:
- description: Remote MCP server at agentsvc.io.
  name: Agentsvc MCP Server
  slug: agentssvc-io-mcp-yml
modified: '2026-11-01'
name: Agentsvc
nav: Providers
network: true
overview: 'Agentsvc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Payments, Web Services, and Agents.


  Agentsvc''s developer surface includes sandbox, authentication, API reference, and 15 more developer resources.'
plans:
- name: Agentsvc Io Plans Pricing
  plan_count: 1
  slug: agentsvc-io-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 61.7
    operational_transparency: 5.3
  previous_composite: 22.7
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentsvc Io Authentication
  slug: agentsvc-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentsvc Io Domain Security
  slug: agentsvc-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentsvc Io Vulnerability Disclosure
  slug: agentsvc-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentsvc-io
tags:
- Artificial Intelligence
- Marketplace
- Payments
- Web Services
- Agents
website: https://agentsvc.io/
---
