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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'Single GraphQL endpoint for programmatic access to WisdomAI domains, tables, users, dashboards, and analytics data. Supports queries, mutations, and real-time WebSocket subscriptions. Tenant-scoped: r'
  name: WisdomAI GraphQL API
  slug: wisdomai-graphql-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wisdom.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wisdom.ai/getting-started/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wisdom.ai/integrations/graphql-api/GraphQL-API
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wisdom.ai/getting-started/overview
- group: company
  title: ''
  type: Blog
  url: https://www.wisdom.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.wisdom.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.wisdom.ai/demo-wisdom-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wisdom.ai/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wisdom.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datawisdomai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wisdom-ai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wisdom-ai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/wisdom-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wisdom-ai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/wisdom-ai-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wisdom-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wisdom-ai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wisdom-ai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wisdom-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wisdom-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.wisdom.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.wisdom.ai/
- group: auth
  title: ''
  type: Security
  url: https://docs.wisdom.ai/manage-account/compliance-and-best-practices
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wisdom-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wisdom-ai-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wisdom-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wisdom-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wisdom-ai-well-known.yml
created: '2026-07-17'
description: WisdomAI is an enterprise agentic analytics platform built around an Adaptive Context Engine that governs business context across distributed data sources (Snowflake, BigQuery, Databricks, Redshift, SharePoint, and more). It powers conversational business intelligence, AI-powered dashboards, and analytics agents that the company reports deliver 95%+ answer accuracy in production. For developers, WisdomAI exposes a GraphQL API (queries, mutations, and WebSocket subscriptions), a React and Node embedding SDK (@wisdomai/react, @wisdomai/node), and a remote Model Context Protocol (MCP) server, all governed by row-level and column-level security, SSO, and SCIM/JIT provisioning so teams can build custom and embedded analytics experiences.
image: https://framerusercontent.com/assets/43nPV2DraEOsNMFDaMIdigVzUU.png
layout: provider
mcp_servers:
- description: ''
  name: wisdom-ai-mcp.yml
  slug: wisdom-ai-mcpyml
modified: '2026-07-21'
name: Wisdom AI
nav: Providers
network: true
overview: 'Wisdom AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Analytics, Business Intelligence, and GraphQL.


  Wisdom AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 22 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 37.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Wisdom Ai Authentication
  slug: wisdom-ai-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Wisdom Ai Domain Security
  slug: wisdom-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wisdom Ai Vulnerability Disclosure
  slug: wisdom-ai-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Wisdom Ai Trust Center
  slug: wisdom-ai-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, HIPAA-ready
slug: wisdom-ai
tags:
- Company
- AI
- Analytics
- Business Intelligence
- GraphQL
- MCP
- Embedded Analytics
- Agents
- Data
website: https://docs.wisdom.ai/
---
