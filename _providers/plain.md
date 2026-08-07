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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Plain's Core GraphQL API — the same API the Plain product is built on. Manage customers, companies, tenants, threads, messaging, help center, labels, tiers/SLAs, snippets, tasks, events, and webhook t
  name: Plain Core GraphQL API
  slug: plain-core-graphql-api
artifact_total: 6
asyncapis:
- description: ''
  name: Plain Webhooks
  slug: plain-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plain-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.plain.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.plain.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.plain.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.plain.com/docs/graphql/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-plain
- group: company
  title: ''
  type: Blog
  url: https://www.plain.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.plain.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plain.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.plain.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plain.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plain.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plain.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.plain.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plain-changelog.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/plain-schema.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/plain-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plain-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plain-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plain-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plain-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plain-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/plain-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plain-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/plain-cli.yml
- group: design
  title: ''
  type: Components
  url: components/plain-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plain-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/plain-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plain-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/plain-trust-center.yml
created: '2026-07-17'
description: Plain is a customer support platform for B2B and technical SaaS companies, built entirely on its own public GraphQL API so there is full parity between what the product UI and the API can do. It unifies support across email, chat, Slack, and API-created threads, with customers, companies, tenants, tiers and SLAs, labels, help center articles, snippets, tasks, and events as first-class entities. Developers integrate via a Relay-style GraphQL API (bearer API keys with fine-grained permissions), typed TypeScript and Go SDKs, a CLI, customer-card UI components, HMAC-signed webhooks, a hosted MCP server, and an official agent skill. This profile was enriched from Plain's public developer surface.
image: https://framerusercontent.com/assets/8LkFDsA5X0pauVd2p3tTSJ4AF4s.png
layout: provider
mcp_servers:
- description: ''
  name: plain-mcp.yml
  slug: plain-mcpyml
modified: '2026-07-20'
name: Plain
nav: Providers
network: true
overview: 'Plain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Support, Customer Service, Help Desk, and Support.


  The Plain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plain''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, changelog, and 24 more developer resources.'
random_paper: 80
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 63.0
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 44.7
  previous_composite: 56.1
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Plain Authentication
  slug: plain-authentication
  summary_line: apiKey/oauth2/mutualTLS · 4 schemes
- kind: domain-security
  name: Plain Domain Security
  slug: plain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plain Trust Center
  slug: plain-trust-center
  summary_line: trust center published
slug: plain
tags:
- Company
- Customer Support
- Customer Service
- Help Desk
- Support
- SaaS
- GraphQL
- Webhooks
- MCP
- Developer Tools
website: https://www.plain.com/docs
---
