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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: The Artifacts API from Lemma — 6 operation(s) for artifacts.
  name: Lemma Artifacts API
  slug: uselemma-artifacts-api
- description: The Issues API from Lemma — 8 operation(s) for issues.
  name: Lemma Issues API
  slug: uselemma-issues-api
- description: The Projects API from Lemma — 6 operation(s) for projects.
  name: Lemma Projects API
  slug: uselemma-projects-api
- description: The Traces API from Lemma — 17 operation(s) for traces.
  name: Lemma Traces API
  slug: uselemma-traces-api
artifact_total: 14
asyncapis:
- description: ''
  name: Uselemma Webhooks
  slug: uselemma-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lemma Platform Artifacts API
  slug: open-uselemma-artifacts-api
- collection_type: open
  name: Lemma Platform Artifacts Issues API
  slug: open-uselemma-issues-api
- collection_type: open
  name: Lemma Platform Artifacts Projects API
  slug: open-uselemma-projects-api
- collection_type: open
  name: Lemma Platform Artifacts Traces API
  slug: open-uselemma-traces-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/uselemma-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.uselemma.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uselemma.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.uselemma.ai/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.uselemma.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.uselemma.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uselemma-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uselemma
- group: start
  title: ''
  type: Login
  url: https://platform.uselemma.ai
- group: operate
  title: ''
  type: Support
  url: https://github.com/uselemma/lemma/issues
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.uselemma.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/uselemma-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uselemma-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uselemma-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/uselemma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uselemma-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uselemma-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uselemma-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/uselemma-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uselemma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uselemma-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uselemma-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uselemma-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uselemma-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uselemma-data-model.yml
created: '2026-07-17'
description: Lemma (uselemma.ai, Forge AI Labs, Inc., Y Combinator Fall 2025) is a production monitoring and observability platform for AI agents. Teams instrument agents with the Lemma tracing SDKs (TypeScript and Python) so every agent execution becomes one trace with LLM generations, tool calls, and app-logic spans as children; Lemma then surfaces silent semantic failures, groups recurring issues with root-cause analysis, sends signed incident webhooks, and exposes the whole surface — projects, traces, issues, and learn-agent artifacts — through the Lemma Platform API and an official remote MCP server so coding agents can pull the exact runs and errors they need and fix issues in place.
image: https://uselemma.ai/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: uselemma-mcp.yml
  slug: uselemma-mcpyml
modified: '2026-07-21'
name: Lemma
nav: Providers
network: true
overview: 'Lemma publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Issues API, Projects API, and 1 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Observability, and Monitoring.


  The Lemma catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lemma''s developer surface includes documentation, getting-started guide, engineering blog, changelog, support, authentication, and 20 more developer resources.'
random_paper: 112
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 68.7
    developer_ergonomics: 58.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 46.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Uselemma Authentication
  slug: uselemma-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uselemma Domain Security
  slug: uselemma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Uselemma Trust Center
  slug: uselemma-trust-center
  summary_line: trust center published
slug: uselemma
tags:
- Company
- Artificial Intelligence
- AI Agents
- Observability
- Monitoring
- Tracing
- Developer Tools
- B2B
website: https://www.uselemma.ai
---
