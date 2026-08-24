---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Taalas Agentic Access
  operation_count: 6
  slug: taalas-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: 'Taalas-native REST interface for running inference against the HC1 hardcore-model silicon. Three operations: a public /health probe reporting server status, queue depth and the currently loaded LoRA a'
  name: Taalas API
  slug: taalas-api
- description: The Models API from Taalas — 1 operation(s) for models.
  name: Taalas Models API
  slug: taalas-models-api
- description: The Monitoring API from Taalas — 1 operation(s) for monitoring.
  name: Taalas Monitoring API
  slug: taalas-monitoring-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taalas API
  slug: open-taalas-inference-api
- collection_type: open
  name: Taalas API — v1
  slug: open-taalas-inference-v1-api
- collection_type: open
  name: Taalas Models API
  slug: open-taalas-models-api
- collection_type: open
  name: Taalas Monitoring API
  slug: open-taalas-monitoring-api
common:
- group: company
  title: ''
  type: Website
  url: https://taalas.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.taalas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.taalas.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.taalas.com/v1/docs
- group: start
  title: ''
  type: SignUp
  url: https://taalas.com/api-request-form/
- group: operate
  title: ''
  type: Support
  url: https://api.taalas.com/bug-report
- group: company
  title: ''
  type: Blog
  url: https://taalas.com/mission-log/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taalas.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taalas.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taalas.com/privacy-policy/
- group: other
  title: ''
  type: Products
  url: https://taalas.com/products/
- group: company
  title: ''
  type: Careers
  url: https://taalas.com/position/
- group: start
  title: ''
  type: Demo
  url: https://chatjimmy.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/taalas-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taalas-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taalas-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taalas-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taalas-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taalas-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/taalas-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taalas-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taalas-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/taalas-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taalas-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taalas-agentic-access.yml
created: '2026-08-02'
description: 'Taalas is a Toronto-based semiconductor company building "Hardcore Models" — AI models etched directly into custom silicon rather than executed as software on general-purpose GPUs, under the tagline "The Model is The Computer." Its first product, the HC1 technology demonstrator, hard-wires Meta''s Llama 3.1 8B into an 815mm2 / 53-billion-transistor die on TSMC''s 6nm process and is publicly demonstrated through the ChatJimmy chatbot. Taalas exposes that silicon to developers through a hosted inference REST API at api.taalas.com, which publishes two OpenAPI 3.1.0 contracts: a root API with health, model-info and a Taalas-native /generate operation, and an OpenAI-compatible /v1 surface with /v1/completions and /v1/chat/completions. Access is by bearer API key issued through an application form; applications are currently closed due to demand.'
image: https://taalas.com/h-content/uploads/2024/01/cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Taalas MCP Server
  slug: taalas-mcp-server
modified: '2026-08-02'
name: Taalas
nav: Providers
network: true
overview: 'Taalas publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Models API, Monitoring API, and 1 more. Tagged areas include Company, Artificial Intelligence, AI Inference, Semiconductors, and AI Accelerator.


  Taalas'' developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 44.1
    developer_ergonomics: 31.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Taalas Authentication
  slug: taalas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taalas Domain Security
  slug: taalas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taalas
tags:
- Company
- Artificial Intelligence
- AI Inference
- Semiconductors
- AI Accelerator
- Large Language Models
- Llama
- Inference API
- OpenAI-Compatible
- Hardware
- Deep Tech
website: https://taalas.com/
---
