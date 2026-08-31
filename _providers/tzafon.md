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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Lightcone API by Tzafon provides cloud browser and desktop computers operated by AI. It spans an agent Tasks API (start, stream, pause, resume, inject messages) driven by the Northstar computer-us
  name: Lightcone API
  slug: lightcone-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tzafon-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lightcone.ai/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lightcone.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lightcone.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lightcone.ai/guides/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/tzafon-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tzafon-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tzafon.instatus.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.lightcone.ai/guides/changelog
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tzafon-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tzafon-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tzafon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tzafon-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tzafon-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/tzafon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tzafon-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tzafon-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tzafon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tzafon-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tzafon-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tzafon-data-model.yml
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/tzafon/lightcone/tree/main/examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tzafon
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.lightcone.ai/guides/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lightcone.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tzafon.ai/legal
- group: operate
  title: ''
  type: Support
  url: https://docs.lightcone.ai/guides/troubleshooting
created: '2026-07-17'
description: 'Tzafon is a machine intelligence company with offices in San Francisco, Tel Aviv, and Zurich, advancing multimodality, high performance compute, and continuous learning. Its developer platform Lightcone is the computer-use API: cloud browsers and desktops operated by Northstar, a vision-language model trained with GUI reinforcement learning to see screens and act on them. Developers describe work in plain language and Northstar operates a computer from start to finish, or they drive computers directly through a REST API, official Python and TypeScript SDKs, a CLI, and an official MCP server -- with OpenAI-compatible Responses and Chat Completions endpoints for drop-in computer-use loops.'
image: https://docs.lightcone.ai/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Tzafon MCP Server
  slug: tzafon-mcp-server
modified: '2026-07-21'
name: Tzafon
nav: Providers
network: true
overview: 'Tzafon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Use Agents, Browser Automation, and AI Agents.


  Tzafon''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, CLI, code examples, and 20 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: Tzafon Rate Limits
  slug: tzafon-rate-limits
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 35.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Tzafon Authentication
  slug: tzafon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tzafon Domain Security
  slug: tzafon-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tzafon
tags:
- Company
- Artificial Intelligence
- Computer Use Agents
- Browser Automation
- AI Agents
- Vision Language Models
- Cloud Computers
- Automation
website: https://lightcone.ai/dashboard
---
