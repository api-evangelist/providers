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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Get decisions from your knowledge maps. **Start** a session, **inject** any available facts, run a **query**, provide a **response** to any questions asked and **undo** your answers to give a differen
  name: Rainbird Technologies Decisions API
  slug: rainbird-technologies-decisions-api
- description: Access the facts, information and the chain of reasoning that led to a decision
  name: Rainbird Technologies Evidence API
  slug: rainbird-technologies-evidence-api
- description: Retrieve information about the Rainbird Platform itself.
  name: Rainbird Technologies Platform API
  slug: rainbird-technologies-platform-api
arazzos:
- description: Start a session against a Knowledge Map, run a query, then retrieve the evidence chain behind the result.
  name: Rainbird — run a decision and fetch its evidence
  slug: rainbird-technologies-run-and-explain
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rainbird API Documentation Decisions API
  slug: open-rainbird-technologies-decisions-api
- collection_type: open
  name: Rainbird API Documentation Decisions Evidence API
  slug: open-rainbird-technologies-evidence-api
- collection_type: open
  name: Rainbird API Documentation Decisions Platform API
  slug: open-rainbird-technologies-platform-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rainbird.ai/rainbird/developer-docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rainbird.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://rainbird.redoc.ly/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rainbird.ai/rainbird/getting-started/quickstart-guide
- group: company
  title: ''
  type: Blog
  url: https://rainbird.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RainBirdAi
- group: start
  title: ''
  type: SignUp
  url: https://app.rainbird.ai/
- group: operate
  title: ''
  type: Support
  url: https://forum.rainbird.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rainbird.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rainbird.ai/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.rainbird.ai/rainbird/whats-new/change-log
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/rainbird-technologies-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/rainbird-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rainbird-technologies-packages.yml
- group: design
  title: ''
  type: Components
  url: components/rainbird-technologies-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rainbird-technologies-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rainbird-technologies-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rainbird-technologies-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rainbird-technologies-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rainbird-technologies-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/rainbird-technologies-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rainbird-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rainbird-technologies-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rainbird-technologies-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rainbird-technologies-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rainbird-technologies-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rainbird-technologies-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rainbird-technologies-run-and-explain.yml
- group: company
  title: ''
  type: Website
  url: https://rainbird.ai/
created: '2026-07-17'
description: Rainbird Technologies is an AI decision automation platform for regulated industries (banking and finance, insurance, tax and audit, healthcare, and law). It turns regulations, policies, and expert knowledge into deterministic, fully auditable decision systems using symbolic reasoning over knowledge graphs (Knowledge Maps), promising zero hallucinations and explainable, evidence-backed outcomes. The Rainbird API lets developers query a published Knowledge Map by starting a session, injecting known facts, running queries, answering the questions the engine asks, and retrieving the evidence chain behind every decision. Community and Enterprise hosting environments are offered, with first-party JavaScript/React and Go SDKs.
image: https://rainbird.ai/wp-content/uploads/2023/01/rainbird-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Rainbird Technologies MCP Server
  slug: rainbird-technologies-mcp-server
modified: '2026-07-20'
name: Rainbird Technologies
nav: Providers
network: true
overview: 'Rainbird Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Decisions API, Evidence API, and Platform API. Tagged areas include Company, Artificial Intelligence, Decision Automation, Knowledge Graph, and Symbolic Reasoning.


  Rainbird Technologies'' developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, changelog, and 23 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rainbird-technologies/refs/heads/main/screenshots/rainbird-technologies-2026-08-17T081442.png
security:
- kind: authentication
  name: Rainbird Technologies Authentication
  slug: rainbird-technologies-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Rainbird Technologies Domain Security
  slug: rainbird-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rainbird-technologies
tags:
- Company
- Artificial Intelligence
- Decision Automation
- Knowledge Graph
- Symbolic Reasoning
- Explainable AI
- Governance
- RegTech
website: https://rainbird.ai/
---
