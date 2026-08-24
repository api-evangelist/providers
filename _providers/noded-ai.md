---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'The Noded (Apollo) GraphQL API behind the Customer Context Graph. One POST endpoint serving people and accounts (both modelled as tags), the unified activity timeline (blocks: notes, emails, tasks, me'
  name: Noded GraphQL API
  slug: noded-graphql-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/noded-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getnoded.ai/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noded-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getnoded.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.getnoded.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getnoded.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getnoded.ai
- group: start
  title: ''
  type: Login
  url: https://app.getnoded.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getnoded.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getnoded.ai/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/nodedhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nodedai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getnoded.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.getnoded.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.getnoded.ai/developers#reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getnoded.ai/developers#quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.getnoded.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Notify-AI
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getnoded.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/noded-ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/noded-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/noded-ai-packages.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/noded-ai-graphql-operations.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/noded-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/noded-ai-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/noded-ai-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/noded-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/noded-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/noded-ai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/noded-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/noded-ai-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/noded-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/noded-ai-rate-limits.yml
created: '2026-07-17'
description: 'Noded AI is a customer context graph for customer success, retention, and growth teams. It consumes customer data scattered across 20+ tools — call recordings (Gong, Zoom, Meet, Fathom, Fireflies, Granola), email, notes, support tickets (Zendesk), CRM (Salesforce, HubSpot), and product/engineering signals (Linear, Jira) — and weaves every account into one living story, then surfaces a no-nonsense assessment of renewal or churn in minutes rather than months. Noded turns mentions of new teams, integrations, or initiatives across the customer ecosystem into qualified plays, and acts wherever teams already work: answering @noded questions in Slack, drafting QBR decks from the live account story, updating Salesforce fields, and filing Linear tickets. Since mid-2026 Noded also ships a developer surface: a first-party browser SDK (@bigfootai/noded-sdk on npm) over an Apollo GraphQL API at api.getnoded.ai/api/v1/graph, OIDC auth against a Noded-hosted Auth0 tenant, a provider-published
  AGENTS.md for coding agents, an llms.txt, and a single hosted MCP layer that exposes the whole customer stack to Claude, ChatGPT, and Gemini with per-agent tool scoping and one identity per agent workload. Developer credentials (issuer, client ID, API audience) and the MCP endpoint are provisioned by the Noded team on request rather than self-serve, and no OpenAPI, GraphQL SDL, or public API reference is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/noded-ai.png
layout: provider
mcp_servers:
- description: ''
  name: Noded MCP layer
  slug: noded-mcp-layer
modified: '2026-08-13'
name: Noded AI
nav: Providers
network: true
overview: 'Noded AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Customer Success, Customer Data, and Churn.


  Noded AI''s developer surface includes engineering blog, pricing, signup flow, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
plans:
- name: Noded Ai Plans Pricing
  plan_count: 4
  slug: noded-ai-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Noded Ai Rate Limits
  slug: noded-ai-rate-limits
scopes:
- name: Noded Ai Scopes
  scope_count: 4
  slug: noded-ai-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 40.6
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 40.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noded-ai/refs/heads/main/screenshots/noded-ai-2026-08-07T185418.png
security:
- kind: authentication
  name: Noded Ai Authentication
  slug: noded-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Noded Ai Domain Security
  slug: noded-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Noded Ai Trust Center
  slug: noded-ai-trust-center
  summary_line: SOC 2, GDPR
slug: noded-ai
tags:
- Company
- Ai Ml
- Customer Success
- Customer Data
- Churn
- Retention
- Revenue Operations
- Software-as-a-Service
- AI Agents
- GraphQL
- MCP
- agent-native
- Customer Context Graph
website: https://www.getnoded.ai/
---
