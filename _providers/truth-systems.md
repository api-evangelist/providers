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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Get Context Output API from Truth Systems — 1 operation(s) for get context output.
  name: Truth Systems Get Context Output API
  slug: truth-systems-get-context-output-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gateway Get Context Output API
  slug: open-truth-systems-get-context-output-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/truth-systems-gateway-overlay.yaml
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


  Truth Systems'' developer surface includes developer portal, documentation, support, authentication, and 13 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 29.0
  delta: -0.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 40.6
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 29.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
