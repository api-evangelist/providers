---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    agentic_commerce: self
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for free key minting and registry access.
  name: Agent Nexus API
  slug: agent-nexus-api
artifact_total: 5
common:
- group: docs
  title: ''
  type: Documentation
  url: https://agentnexus.app/guides/api-fallbacks
- group: commercial
  href: https://artifacts.apis.io/agentnexus-app/plans/agentnexus-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentnexus-app-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/agentnexus-app/sandbox/agentnexus-app-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agentnexus-app-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://agentnexus.app/privacy
- group: design
  href: https://artifacts.apis.io/agentnexus-app/conformance/agentnexus-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentnexus-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentnexus-app/llms/agentnexus-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentnexus-app-llms.txt
- group: other
  href: https://artifacts.apis.io/agentnexus-app/a2a/agentnexus-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentnexus-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentnexus-app/mcp/agentnexus-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentnexus-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentnexus-app/well-known/agentnexus-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentnexus-app-security.txt
- group: auth
  href: https://artifacts.apis.io/agentnexus-app/well-known/agentnexus-app-nothumansearch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentnexus-app-nothumansearch-security.txt
- group: agent
  href: https://artifacts.apis.io/agentnexus-app/well-known/agentnexus-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentnexus-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentnexus-app/hosts/agentnexus-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentnexus-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentnexus-app/vendors/agentnexus-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentnexus-app-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://agentnexus.app/status
- group: docs
  title: ''
  type: APIReference
  url: https://agentnexus.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/agentnexus-app/security/agentnexus-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentnexus-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentnexus-app/security/agentnexus-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentnexus-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentnexus.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentnexus.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentnexus.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentnexus.app/privacy
created: '2026-11-01'
description: Agent Nexus provides an infrastructure platform for AI agents, offering a public registry of APIs, MCP servers, and CLI tools that agents can discover and call without authentication. It supports free and paid tiers, with rate limits and monitoring, enabling developers to integrate and monetize agentic services. The service includes a searchable catalog, automated health checks, and drift alerts, aiming to simplify the creation and operation of AI-driven applications.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_6azj38tkaw81pa6ecj0qapfbj2/df95917af844da4d059273e7804179d8_1793429071564.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentnexus.app.
  name: Agent Nexus MCP Server
  slug: agentnexus-app-mcp-yml
modified: '2026-11-01'
name: Agent Nexus
nav: Providers
network: true
overview: 'Agent Nexus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Infrastructure, Registry, and Agents.


  Agent Nexus'' developer surface includes documentation, sandbox, API reference, pricing, and 17 more developer resources.'
plans:
- name: Agentnexus App Plans Pricing
  plan_count: 3
  slug: agentnexus-app-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 29.8
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentnexus App Domain Security
  slug: agentnexus-app-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agentnexus App Vulnerability Disclosure
  slug: agentnexus-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentnexus-app
tags:
- Company
- Artificial Intelligence
- Infrastructure
- Registry
- Agents
- Platform
website: https://agentnexus.app/
---
