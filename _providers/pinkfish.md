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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 64.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pinkfish Agentic Access
  operation_count: 4
  slug: pinkfish-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- description: Poll run status and retrieve results
  name: Pinkfish Runs API
  slug: pinkfish-runs-api
- description: Execute published workflows via API and webhook triggers
  name: Pinkfish Triggers API
  slug: pinkfish-triggers-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://pinkfish.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pinkfish.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pinkfish.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pinkfish.ai/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.pinkfish.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pinkfish.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.pinkfish.ai
- group: start
  title: ''
  type: Login
  url: https://app.pinkfish.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pinkfish.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pinkfish.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.pinkfish.ai/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pinkfish-ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pinkfish-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pinkfish-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinkfish-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pinkfish-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pinkfish-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pinkfish-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pinkfish-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pinkfish-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinkfish-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinkfish-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.pinkfish.ai/api-reference/endpoint/webhook-trigger
created: '2026-07-17'
description: Pinkfish is an enterprise agentic AI and business orchestration platform that runs multi-step workflows across an organization's stack, combining AI agents with real system integrations, permissions, and auditability for critical operations. The platform pairs a natural-language "Coworker" and visual agentic workflow editor with domain-specific Agents, a Guardian monitoring and self-healing layer, and a library of 1,500+ ready-to-deploy MCP tools spanning 500+ enterprise integrations (Salesforce, Slack, Stripe, Zendesk, Jira, and more). Published workflows are exposed programmatically through the Triggers API (an API-key authenticated HTTP surface supporting synchronous and asynchronous execution, webhook triggers, and run polling) and through the embedded Pinkfish Sidekick MCP server. Pinkfish was surfaced as a portfolio company of Norwest Venture Partners and was acquired by Genesys.
image: https://www.pinkfish.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: pinkfish-mcp.yml
  slug: pinkfish-mcpyml
modified: '2026-07-20'
name: Pinkfish
nav: Providers
network: true
overview: 'Pinkfish publishes 2 APIs on the [APIs.io](https://apis.io/) network: Runs API and Triggers API. Tagged areas include Company, Artificial Intelligence, AI Agents, Agentic Workflows, and Automation.


  Pinkfish''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, changelog, authentication, and 17 more developer resources.'
random_paper: 60
score:
  band: developing
  composite: 47.3
  delta: 0.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.2
    developer_ergonomics: 47.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pinkfish Authentication
  slug: pinkfish-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pinkfish Domain Security
  slug: pinkfish-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinkfish
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agentic Workflows
- Automation
- Orchestration
- Model Context Protocol
- Integrations
- Enterprise
- No-Code
website: https://pinkfish.ai
---
