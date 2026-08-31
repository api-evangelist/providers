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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: GraphQL API for retrieving workspace and user metadata — replays/recordings, team members, and comments on a replay. POST queries to the endpoint with a Replay API key as a bearer token.
  name: Replay GraphQL API
  slug: replay-graphql-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.replay.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.replay.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.replay.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.replay.io/reference/integrations/replay-apis/replay-protocol
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.replay.io/basics/getting-started/record-your-app
- group: company
  title: ''
  type: Blog
  url: https://www.replay.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replayio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.replay.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.replay.io/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@replay.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.replay.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.replay.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replay.io
- group: agent
  title: ''
  type: MCPServer
  url: mcp/replay-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/replay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/replay-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/replay-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/replay-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/replay-www-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/replay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replay-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/replay-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.replay.io/blog/replay-achieves-soc2
- group: auth
  title: ''
  type: TrustCenter
  url: security/replay-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/replay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.replay.io/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replay-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replay-llms.txt
created: '2026-07-17'
description: Replay is an AI-native QA and time-travel debugging platform for web applications. Replay QA autonomously explores a web app, records every session in a deterministic Replay Browser, finds real bugs, and hands a coding agent the root cause and a suggested fix. The recording is a time-travel database of everything that happened in the browser — sources, console, network, DOM, React renders — inspectable after the fact without reproducing the bug locally. Replay exposes this programmatically through a GraphQL API, a WebSocket Replay Protocol, a published Model Context Protocol (MCP) server for agent debugging, a CLI (replayio), and Playwright/Cypress recording integrations. Backed by a16z and Version One Ventures.
image: https://www.replay.io/replayQA_og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Replay MCP
  slug: replay-mcp
modified: '2026-07-20'
name: Replay
nav: Providers
network: true
overview: 'Replay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Debugging, Testing, Quality Assurance, and Developer Tools.


  Replay''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 24 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 41.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/replay/refs/heads/main/screenshots/replay-2026-08-17T081521.png
security:
- kind: authentication
  name: Replay Authentication
  slug: replay-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Replay Domain Security
  slug: replay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Replay Vulnerability Disclosure
  slug: replay-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Replay Trust Center
  slug: replay-trust-center
  summary_line: SOC 2 Type 2
slug: replay
tags:
- Company
- Debugging
- Testing
- Quality Assurance
- Developer Tools
- Time Travel Debugging
- MCP
- GraphQL
- Browser Automation
- Artificial Intelligence
website: https://www.replay.io
---
