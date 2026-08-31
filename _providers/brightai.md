---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Brightai Agentic Access
  operation_count: 6
  slug: brightai-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: A public, read-only Model Context Protocol server (protocol 2025-06-18, serverInfo brightai-public 0.1.0) requiring no authentication. Exposes six tools over BrightAI's Global Observability Database —
  name: BrightAI Public MCP Server
  slug: public-mcp
- description: 'Two unauthenticated JSON endpoints published in BrightAI''s llms.txt: /api/public/industries returns live worldwide aggregates and per-vertical addressable annual impact from the Global Observability D'
  name: BrightAI Public Observatory Data API
  slug: public-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bright.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://public.stateful.world/start.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brightai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brightai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brightai-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brightai-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brightai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brightai-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/brightai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bright.ai/trust-and-security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bright.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://bright.ai/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://bright.ai/get-started/
created: '2026-08-08'
description: BrightAI builds Physical AI for essential services — continuous, AI-driven awareness of the real-time state of physical infrastructure for operators of water, power, energy, transportation and industrial systems. Founded in 2019 by SmartThings founder Alex Hawkinson, the company ships a four-layer Stateful platform (Data Acquisition, AI Hub, Stateful OS, Foundation Models) combining peel-and-stick sensors (Stateful Sticker), autonomous drone and quadruped inspection, a voice-interactive field Stateful Wearable, and infrastructure foundation models trained on operational outcomes across millions of industrial assets. BrightAI publishes no conventional developer portal or OpenAPI, but it does operate a public, no-authentication Model Context Protocol server at public.stateful.world/mcp exposing six read-only tools over its Global Observability Database, alongside an llms.txt index, agent-addressed markdown briefs, and two unauthenticated public JSON endpoints.
image: https://cdn.prod.website-files.com/6a4ea9e79536d28883c64986/6a4ea9e79536d28883c64b40_bright-ai-favicon-256x256.jpg
layout: provider
mcp_servers:
- description: ''
  name: BrightAI MCP Server
  slug: brightai-mcp-server
modified: '2026-08-08'
name: BrightAI
nav: Providers
network: true
overview: 'BrightAI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Physical AI, Industrial IoT, Infrastructure Monitoring, and Predictive Maintenance.


  BrightAI''s developer surface includes documentation, authentication, support, signup flow, and 13 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.6
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Brightai Authentication
  slug: brightai-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Brightai Domain Security
  slug: brightai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brightai Trust Center
  slug: brightai-trust-center
  summary_line: SOC 2
slug: brightai
tags:
- Company
- Physical AI
- Industrial IoT
- Infrastructure Monitoring
- Predictive Maintenance
- Edge AI
- Foundation Models
- MCP
- Energy and Utilities
- Water and Wastewater
website: https://www.bright.ai/
---
