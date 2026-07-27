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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The Get Context Output API from Truth Systems — 1 operation(s) for get context output.
  name: Truth Systems Get Context Output API
  slug: truth-systems-get-context-output-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truth-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truthsystems.ai
- group: start
  title: ''
  type: Portal
  url: https://docs.truthsystems.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truthsystems.ai/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TruthSystems
- group: operate
  title: ''
  type: Support
  url: mailto:info@truthsystems.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truth-systems-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truth-systems-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/truth-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truth-systems-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truth-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truth-systems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truth-systems-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truth-systems-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/truth-systems-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Truth Systems builds AI governance and hallucination-detection infrastructure for regulated industries, with a focus on legal firms. Gateway, its core API product, fact-checks LLM-generated text against customer source documents in real time - decomposing a claim into statements, retrieving evidence, and returning SUPPORTS / REFUTES / NOT_ENOUGH_INFO verdicts with character-level evidence spans. Gateway deploys into the customer's own AWS or Azure account via Terraform, with a Python SDK. The company also offers Charter (AI governance for human users) and Alexandria (agent-focused governance), and is backed by Lightspeed Venture Partners.
image: https://www.truthsystems.ai/truthsystems-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: truth-systems-mcp.yml
  slug: truth-systems-mcpyml
modified: '2026-07-21'
name: Truth Systems
nav: Providers
network: true
overview: 'Truth Systems publishes 1 API on the [APIs.io](https://apis.io/) network: Get Context Output API. Tagged areas include Company, Artificial Intelligence, AI Governance, Hallucination Detection, and Fact Checking.


  Truth Systems'' developer surface includes developer portal, documentation, support, authentication, and 12 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 38.9
    developer_ergonomics: 54.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Truth Systems Authentication
  slug: truth-systems-authentication
  summary_line: aws-iam/apiKey · 2 schemes
- kind: domain-security
  name: Truth Systems Domain Security
  slug: truth-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truth-systems
tags:
- Company
- Artificial Intelligence
- AI Governance
- Hallucination Detection
- Fact Checking
- Compliance
- Legal
website: https://www.truthsystems.ai
---
