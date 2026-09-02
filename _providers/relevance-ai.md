---
access_model:
  confidence: high
  label: Freemium with self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST API for the Relevance AI agent platform — 521 paths and 566 operations covering agents, tools (called "studios" in the API), multi-agent workforces, knowledge tables, conversations, triggers, eva
  name: Relevance AI API
  slug: relevance-ai
- description: First-party hosted MCP server exposing a Relevance AI project's agents, tools, workforces, knowledge tables, evals, analytics, folders and triggers to any MCP-compatible client (Claude, ChatGPT, Curso
  name: Relevance AI MCP Server
  slug: relevance-ai-mcp
artifact_total: 11
asyncapis:
- description: ''
  name: Relevance Ai Events
  slug: relevance-ai-events
common:
- group: company
  title: ''
  type: Website
  url: https://relevanceai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://relevanceai.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://relevanceai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api-f1db6c.stack.tryrelevance.com/latest/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://relevanceai.com/docs/get-started/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://relevanceai.com/docs/get-started/support
- group: company
  title: ''
  type: Blog
  url: https://relevanceai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RelevanceAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/relevanceai
- group: commercial
  title: ''
  type: Pricing
  url: https://relevanceai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://relevanceai.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.relevanceai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relevanceai.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relevanceai.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.relevanceai.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.relevanceai.com/
- group: auth
  title: ''
  type: Compliance
  url: security/relevance-ai-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/relevance-ai-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/relevance-ai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/relevance-ai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/relevance-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/relevance-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/relevance-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/relevance-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/relevance-ai-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/relevance-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/relevance-ai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/relevance-ai-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/relevance-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/relevance-ai-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/relevance-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/relevance-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/relevance-ai-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/relevance-ai-events.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/relevance-ai-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/relevance-ai-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/relevance-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/relevance-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/relevance-ai-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relevance-ai-domain-security.yml
created: '2026-03-27'
description: 'Relevance AI is an agent platform for building, testing and running specialist AI agents and multi-agent "workforces" — teams of agents that coordinate on a shared goal. Domain experts build agents in a no-code visual builder, hold them to pass/fail quality bars with a built-in evals system, and connect them to 1,000+ integrations across sales, marketing, customer success, operations and HR. Developers reach the same platform three ways: a 566-operation REST API served from regional hosts in the US, EU and Australia; a first-party JavaScript/TypeScript SDK on npm and JSR; and a hosted, OAuth-protected MCP server at mcp.relevanceai.com that exposes agents, tools, workforces, knowledge tables, evals and analytics to any MCP client. Enterprise governance covers RBAC, human-in-the-loop approvals, SSO/SAML, PII masking, version control with rollback, multi-region data residency, and OpenTelemetry audit-log and trace streaming to the customer''s own S3 bucket. Operated by OnSearch
  Pty Ltd T/A Relevance AI; SOC 2 Type II and GDPR compliant.'
finops:
- name: Relevance Ai Finops
  service_category: API
  slug: relevance-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relevance-ai.png
layout: provider
mcp_servers:
- description: 'Relevance AI runs a first-party remote MCP server that exposes a project''s agents, tools, workforces, knowledge tables, evals, analytics and triggers to any MCP-compatible client. It is a hosted HTTP '
  name: Relevance AI MCP Server
  slug: relevance-ai-mcp-server
modified: '2026-08-29'
name: Relevance AI
nav: Providers
network: true
overview: 'Relevance AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, AI Automation, Multi-Agent Systems, Agent Platform, and MCP.


  The Relevance AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Relevance AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Relevance Ai Plans Pricing
  plan_count: 4
  slug: relevance-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 10
  name: Relevance Ai Rate Limits
  slug: relevance-ai-rate-limits
scopes:
- name: Relevance Ai Scopes
  scope_count: 0
  slug: relevance-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 7.6
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 54.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/relevance-ai/refs/heads/main/screenshots/relevance-ai-2026-06-20T192832.png
security:
- kind: authentication
  name: Relevance Ai Authentication
  slug: relevance-ai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Relevance Ai Domain Security
  slug: relevance-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Relevance Ai Trust Center
  slug: relevance-ai-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: relevance-ai
tags:
- AI Agents
- AI Automation
- Multi-Agent Systems
- Agent Platform
- MCP
- agent-native
- Workflow-Automation
- LLM Orchestration
- Knowledge-Management
- Observability
- Sales Automation
- GTM Engineering
website: https://relevanceai.com
---
