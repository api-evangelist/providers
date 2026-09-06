---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Osmosis Agentic Access
  operation_count: 5
  slug: osmosis-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.osmosis.ai
  baseurl_source: declared
  description: Operations for enhancing agent interactions and decisions
  name: Osmosis agent API
  slug: osmosis-agent-api
- baseURL: https://api.osmosis.ai
  baseurl_source: declared
  description: Operations for managing the knowledge base
  name: Osmosis knowledge API
  slug: osmosis-knowledge-api
- baseURL: https://api.osmosis.ai
  baseurl_source: declared
  description: The Osmosis Agent Improvement API API from Osmosis — 1 operation(s) for osmosis agent improvement api.
  name: Osmosis Osmosis Agent Improvement API API
  slug: osmosis-osmosis-agent-improvement-api-api
artifact_total: 12
asyncapis:
- description: ''
  name: Osmosis Webhooks
  slug: osmosis-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Osmosis Improvement agent API
  slug: open-osmosis-agent-api
- collection_type: open
  name: Osmosis Improvement agent knowledge API
  slug: open-osmosis-knowledge-api
- collection_type: open
  name: Osmosis Improvement agent Osmosis Agent Improvement API API
  slug: open-osmosis-osmosis-agent-improvement-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/osmosis-agent-improvement-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://osmosis.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.osmosis.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.osmosis.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.osmosis.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.osmosis.ai/platform/quickstart
- group: company
  title: ''
  type: Blog
  url: https://osmosis.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://osmosis.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Osmosis-AI
- group: start
  title: ''
  type: SignUp
  url: https://platform.osmosis.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://osmosis.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://osmosis.ai/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.osmosis.ai
- group: build
  title: ''
  type: Packages
  url: packages/osmosis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/osmosis-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/osmosis-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/osmosis-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osmosis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/osmosis-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/osmosis-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osmosis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osmosis-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/osmosis-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osmosis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osmosis-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/osmosis-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osmosis-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/osmosis-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osmosis-authentication.yml
created: '2026-07-17'
description: Osmosis (Gulp AI Inc.) is a forward-deployed reinforcement-learning platform for post-training large language models. Teams implement an AgentWorkflow and a Grader in Python, then use the Osmosis CLI and web platform to submit evaluation and training runs (GRPO/DAPO, multi-turn tool training) that produce task-specific LoRA models which beat foundation models at a fraction of the cost. Osmosis also ships an Agent Improvement REST API for storing agent interaction knowledge and enhancing agent tasks from past interactions, an open-source Python SDK/CLI (osmosis-ai), a TypeScript logging SDK, an open-source MCP server (Osmosis-Apply), webhooks, and hosted documentation. Backed by CRV, Felicis, and Paradigm.
image: https://raw.githubusercontent.com/Osmosis-AI/osmosis-sdk-python/main/.github/osmosis-logo-light.svg
layout: provider
mcp_servers:
- description: 'An open-source Model Context Protocol server that uses the Osmosis-Apply-1.7B model (served locally via Ollama) to merge code edits into files. Integrates into AI IDE / MCP-client workflows. Requires '
  name: Osmosis MCP Server
  slug: osmosis-mcp-server
modified: '2026-07-20'
name: Osmosis
nav: Providers
network: true
overview: 'Osmosis publishes 3 APIs on the [APIs.io](https://apis.io/) network: agent API, knowledge API, and Osmosis Agent Improvement API API. Tagged areas include Company, Artificial Intelligence, Reinforcement Learning, LLM, and Post-Training.


  The Osmosis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Osmosis'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 23 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 62.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/osmosis/refs/heads/main/screenshots/osmosis-2026-08-07T191013.png
security:
- kind: authentication
  name: Osmosis Authentication
  slug: osmosis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Osmosis Domain Security
  slug: osmosis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: osmosis
tags:
- Company
- Artificial Intelligence
- Reinforcement Learning
- LLM
- Post-Training
- Model Training
- Agents
- Machine-Learning
- Developer Tools
website: https://osmosis.ai/
---
