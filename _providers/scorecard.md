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
    agent_skills: true
    agentic_access: true
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
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Scorecard Agentic Access
  operation_count: 35
  slug: scorecard-agentic-access
  summary_line: 35 operations · 20 acting
api_count: 7
apis:
- description: The Metrics API from Scorecard — 1 operation(s) for metrics.
  name: Scorecard Metrics API
  slug: scorecard-metrics-api
- description: The Projects API from Scorecard — 5 operation(s) for projects.
  name: Scorecard Projects API
  slug: scorecard-projects-api
- description: The Records API from Scorecard — 5 operation(s) for records.
  name: Scorecard Records API
  slug: scorecard-records-api
- description: The Runs API from Scorecard — 2 operation(s) for runs.
  name: Scorecard Runs API
  slug: scorecard-runs-api
- description: The Systems API from Scorecard — 3 operation(s) for systems.
  name: Scorecard Systems API
  slug: scorecard-systems-api
- description: The Testcases API from Scorecard — 2 operation(s) for testcases.
  name: Scorecard Testcases API
  slug: scorecard-testcases-api
- description: The Testsets API from Scorecard — 2 operation(s) for testsets.
  name: Scorecard Testsets API
  slug: scorecard-testsets-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/scorecard-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scorecard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scorecard.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scorecard.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scorecard.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scorecard.io/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scorecard.io/intro/sdk-quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.scorecard.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scorecard.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getscorecard.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scorecard.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scorecard.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scorecard-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scorecard.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.scorecard.io/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://trust.scorecard.io/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scorecard-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/scorecard-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scorecard-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scorecard-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/scorecard-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scorecard-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scorecard-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scorecard-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scorecard-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scorecard-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scorecard-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Scorecard is a simulation and evaluation platform for building, testing, and deploying frontier AI agents. Teams run their agents through thousands of realistic scenarios, judge outputs with configurable AI, human, and heuristic metrics, and ship new capabilities with confidence. The platform organizes work into Projects, Testsets, Testcases, Metrics, Runs, Records, Scores, and Systems, and exposes a REST API (bearer API keys prefixed ak_) plus official Python, TypeScript/Node, and Go SDKs, a hosted MCP server, tracing integrations for LangChain, the Vercel AI SDK, and the Claude Agent SDK, and a GitHub Actions integration for evals in CI. Scorecard was founded to solve AI agent evaluation at scale and is backed by Kindred Ventures.
image: https://cdn.prod.website-files.com/68012f5eeeda4ace0fca1c46/680be2472e0c42225eb5c6fb_bb737b32df1d17f3492808c99d78bb0b_scorecard-open-graph.jpg
layout: provider
mcp_servers:
- description: ''
  name: scorecard-mcp.yml
  slug: scorecard-mcpyml
modified: '2026-07-21'
name: Scorecard
nav: Providers
network: true
overview: 'Scorecard publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Metrics API, Projects API, Records API, and 4 more. Tagged areas include Company, AI, Agents, Evaluation, and Testing.


  Scorecard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 21 more developer resources.'
random_paper: 32
score:
  band: developing
  composite: 55.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.8
    developer_ergonomics: 69.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 55.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Scorecard Authentication
  slug: scorecard-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scorecard Domain Security
  slug: scorecard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scorecard Trust Center
  slug: scorecard-trust-center
  summary_line: SOC 2
slug: scorecard
tags:
- Company
- AI
- Agents
- Evaluation
- Testing
- LLM
- Observability
- Simulation
- Developer Tools
- MCP
website: https://www.scorecard.io/
---
