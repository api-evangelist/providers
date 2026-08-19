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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The Groups API from Testerarmy — 5 operation(s) for groups.
  name: Testerarmy Groups API
  slug: testerarmy-groups-api
- description: The Projects API from Testerarmy — 13 operation(s) for projects.
  name: Testerarmy Projects API
  slug: testerarmy-projects-api
- description: The Test Runs API from Testerarmy — 5 operation(s) for test runs.
  name: Testerarmy Test Runs API
  slug: testerarmy-test-runs-api
- description: The Tests API from Testerarmy — 3 operation(s) for tests.
  name: Testerarmy Tests API
  slug: testerarmy-tests-api
- description: The Webhooks API from Testerarmy — 2 operation(s) for webhooks.
  name: Testerarmy Webhooks API
  slug: testerarmy-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Testerarmy Webhooks
  slug: testerarmy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TestArmy Groups API
  slug: open-testerarmy-groups-api
- collection_type: open
  name: TestArmy Groups Projects API
  slug: open-testerarmy-projects-api
- collection_type: open
  name: TestArmy Groups Test Runs API
  slug: open-testerarmy-test-runs-api
- collection_type: open
  name: TestArmy Groups Tests API
  slug: open-testerarmy-tests-api
- collection_type: open
  name: TestArmy Groups Webhooks API
  slug: open-testerarmy-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/testerarmy-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testerarmy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testerarmy-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/testerarmy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/testerarmy-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/testerarmy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/testerarmy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/testerarmy-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/testerarmy-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/testerarmy-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/testerarmy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/testerarmy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/testerarmy-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/testerarmy-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/testerarmy-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/testerarmy-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tester.army/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tester.army/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tester.army/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tester.army/get-started/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://tester.army/pricing
- group: company
  title: ''
  type: Blog
  url: https://tester.army/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tester-army
- group: operate
  title: ''
  type: Support
  url: https://tester.army/discord
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tester.army/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tester.army/privacy
created: '2026-07-17'
description: TesterArmy is an AI-powered QA testing platform (Y Combinator, batch P26) whose browser and mobile agents test web and mobile apps like a real user - navigating pages, filling forms, handling login, OAuth and OTP flows, and catching broken flows, rendering bugs and confusing UX. You describe tests in plain English and the agent runs them in the TesterArmy cloud (or locally), on every GitHub pull request or on a schedule, returning screenshots, recordings and actionable bug reports. It exposes a public REST API (bearer API-key auth), a first-party CLI (testerarmy / ta), inbound trigger webhooks, and mobile app upload and testing.
image: https://tester.army/logo.png
layout: provider
mcp_servers:
- description: ''
  name: testerarmy-mcp.yml
  slug: testerarmy-mcpyml
modified: '2026-07-21'
name: Testerarmy
nav: Providers
network: true
overview: 'Testerarmy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Groups API, Projects API, Test Runs API, and 2 more. Tagged areas include Company, QA, Software Testing, Browser Automation, and AI Agents.


  The Testerarmy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Testerarmy''s developer surface includes authentication, CLI, sandbox, documentation, API reference, getting-started guide, pricing, and 20 more developer resources.'
random_paper: 61
score:
  band: developing
  composite: 51.0
  delta: 0.1
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 16.7
    contract_quality: 64.1
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 50.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testerarmy/refs/heads/main/screenshots/testerarmy-2026-08-17T082329.png
security:
- kind: authentication
  name: Testerarmy Authentication
  slug: testerarmy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Testerarmy Domain Security
  slug: testerarmy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: testerarmy
tags:
- Company
- QA
- Software Testing
- Browser Automation
- AI Agents
- Developer Tools
- CI/CD
- End-to-End Testing
- Mobile Testing
website: https://docs.tester.army/
---
