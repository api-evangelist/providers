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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Discover mock SaaS providers granted to your organization
  name: Ressl Providers API
  slug: ressl-ai-providers-api
- description: Provision short-lived hosted mock SaaS APIs
  name: Ressl Snapshots API
  slug: ressl-ai-snapshots-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ressl Platform Providers API
  slug: open-ressl-ai-providers-api
- collection_type: open
  name: Ressl Platform Providers Snapshots API
  slug: open-ressl-ai-snapshots-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ressl-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ressl-ai-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ressl-ai-platform-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ressl-ai-platform-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ressl-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ressl-ai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ressl-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ressl-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ressl-ai-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ressl-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ressl-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ressl-ai-skill.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ressl-ai-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ressl.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ressl.ai/api-reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ressl.ai/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://simulation.ressl.ai
- group: start
  title: ''
  type: SignUp
  url: https://simulation.ressl.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ressl-ai
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/resslaiaiagen-czp2639/shared_invite/zt-2vpd5vabp-D9LpsJZRiweb7_OFnvIvhA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ressl-ai/
created: '2026-07-17'
description: Ressl (ressl.ai) is a Y Combinator-backed platform that provisions hosted mock SaaS APIs for AI agents and evaluations. Its control-plane API lets you list the mock providers your organization is granted (for example jira, salesforce, slack, plus UI clones of Gmail Business and LinkedIn) and create a short-lived snapshot of one provider that returns a public HTTPS base URL your agent can call - no real customer tenant required. Snapshots carry deterministic or seeded synthetic data and expire on a TTL (default one hour, up to seven days). Control traffic runs on simulation.ressl.ai; provisioned mock traffic is served from *.mock.ressl.cc. Ressl helps teams train, benchmark, and deploy autonomous agents by giving them realistic SaaS surfaces to act against safely.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ressl-ai.png
layout: provider
mcp_servers:
- description: ''
  name: Ressl MCP Server
  slug: ressl-mcp-server
modified: '2026-07-20'
name: Ressl
nav: Providers
network: true
overview: 'Ressl publishes 2 APIs on the [APIs.io](https://apis.io/) network: Providers API and Snapshots API. Tagged areas include Mock APIs, API Testing, AI Agents, Agent Evaluation, and Sandbox.


  Ressl''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, and 15 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 28.7
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 15.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 28.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Ressl Ai Authentication
  slug: ressl-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ressl Ai Domain Security
  slug: ressl-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ressl-ai
tags:
- Mock APIs
- API Testing
- AI Agents
- Agent Evaluation
- Sandbox
- Developer Tools
- Synthetic Data
- Software-as-a-Service
website: https://simulation.ressl.ai
---
