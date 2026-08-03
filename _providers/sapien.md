---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Sapien Agentic Access
  operation_count: 22
  slug: sapien-agentic-access
  summary_line: 22 operations · 12 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Datapoints API from Sapien — 1 operation(s) for datapoints.
  name: Sapien Datapoints API
  slug: sapien-datapoints-api
- description: The Projects API from Sapien — 2 operation(s) for projects.
  name: Sapien Projects API
  slug: sapien-projects-api
- description: The System API from Sapien — 1 operation(s) for system.
  name: Sapien System API
  slug: sapien-system-api
- description: The Upload Sessions API from Sapien — 6 operation(s) for upload sessions.
  name: Sapien Upload Sessions API
  slug: sapien-upload-sessions-api
- description: The Validators API from Sapien — 9 operation(s) for validators.
  name: Sapien Validators API
  slug: sapien-validators-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapien-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sapien-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sapien-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sapien-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sapien-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/sapien-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sapien-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sapien-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sapien-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sapien-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sapien-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sapien-poq-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sapien.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sapien.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sapien.io/start/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sapien-io
- group: company
  title: ''
  type: Blog
  url: https://www.sapien.io/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.sapien.io/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://www.sapien.io/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sapien.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sapien.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.sapien.io
created: '2026-07-17'
description: Sapien is the company behind Proof of Quality (PoQ), an open protocol and consensus/attestation system for verifiable quality signals on AI data and subjective expert outputs. A panel of independent, collateral-backed validators reviews each item against a customer-defined rubric (a poq.toml spec), consensus collapses their scores into one rating per datapoint, and the result is sealed as a permanent onchain attestation (a PoQ Report) — while the underlying data never leaves the customer's systems. Use cases span training-data labeling, fine-tuning and evaluation gates, audit/compliance review, and production safety verification. Sapien ships a live Developer API (/developer/v1) and an MCP server, both authenticated with poq_live_ API keys, and runs on Base Mainnet with a $SAPIEN staking/slashing token. Backed by General Catalyst.
image: https://docs.sapien.io/favicon.jpg
layout: provider
mcp_servers:
- description: ''
  name: sapien-mcp.yml
  slug: sapien-mcpyml
modified: '2026-07-21'
name: Sapien
nav: Providers
network: true
overview: 'Sapien publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Datapoints API, Projects API, System API, and 2 more. Tagged areas include Company, AI, Data Quality, Data Labeling, and Machine Learning.


  Sapien''s developer surface includes authentication, documentation, getting-started guide, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 70
score:
  band: thin
  composite: 41.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.3
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Sapien Authentication
  slug: sapien-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sapien Domain Security
  slug: sapien-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sapien
tags:
- Company
- AI
- Data Quality
- Data Labeling
- Machine Learning
- Human in the Loop
- Attestation
- Blockchain
- Consensus
- MCP
website: https://www.sapien.io
---
