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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Alpic Agentic Access
  operation_count: 24
  slug: alpic-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 8
apis:
- description: The analytics API from Alpic — 1 operation(s) for analytics.
  name: Alpic analytics API
  slug: alpic-analytics-api
- description: The beacon API from Alpic — 2 operation(s) for beacon.
  name: Alpic beacon API
  slug: alpic-beacon-api
- description: The deployments API from Alpic — 1 operation(s) for deployments.
  name: Alpic deployments API
  slug: alpic-deployments-api
- description: The distribution API from Alpic — 2 operation(s) for distribution.
  name: Alpic distribution API
  slug: alpic-distribution-api
- description: The environments API from Alpic — 8 operation(s) for environments.
  name: Alpic environments API
  slug: alpic-environments-api
- description: The projects API from Alpic — 2 operation(s) for projects.
  name: Alpic projects API
  slug: alpic-projects-api
- description: The teams API from Alpic — 1 operation(s) for teams.
  name: Alpic teams API
  slug: alpic-teams-api
- description: The tunnels API from Alpic — 1 operation(s) for tunnels.
  name: Alpic tunnels API
  slug: alpic-tunnels-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.alpic.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alpic.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alpic.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alpic.ai/quickstart
- group: build
  title: ''
  type: CLI
  url: cli/alpic-cli.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alpic-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/alpic-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alpic-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alpic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alpic-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alpic-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.alpic.ai/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alpic-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alpic-ai
- group: company
  title: ''
  type: Blog
  url: https://alpic.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://alpic.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.alpic.ai
- group: operate
  title: ''
  type: Support
  url: https://alpic.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alpic.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alpic.ai/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://alpic.ai/
created: '2026-07-17'
description: Alpic is the MCP-native cloud platform for building, deploying, monitoring, and distributing Model Context Protocol (MCP) servers and ChatGPT Apps. Its stack spans the open-source Skybridge TypeScript framework, the `alpic` CLI, Alpic Cloud (one-click deploy, multi-environment support, runtime and build logs, analytics, DCR proxy, Node.js/Python runtimes), Beacon compliance audits, and one-click distribution to the MCP registry. The Alpic REST API (https://api.alpic.ai, v1) programmatically manages teams, projects, environments, environment variables, deployments, analytics, playgrounds, tunnels, distribution, and Beacon audits, with an agentic self-registration path so AI agents can obtain an API key and ship MCP servers autonomously. Founded by the repeat team behind Streamroot; backed by Partech.
image: https://framerusercontent.com/images/WZiXUn1MVLa0eLUmTzKrnFH9tUs.png
layout: provider
modified: '2026-07-17'
name: Alpic
nav: Providers
network: true
overview: 'Alpic publishes 8 APIs on the [APIs.io](https://apis.io/) network, including analytics API, beacon API, deployments API, and 5 more. Tagged areas include Company, Ai/Ml, MCP, Model Context Protocol, and Cloud Platform.


  Alpic''s developer surface includes documentation, API reference, getting-started guide, CLI, authentication, engineering blog, pricing, and 15 more developer resources.'
random_paper: 69
scopes:
- name: Alpic Scopes
  scope_count: 3
  slug: alpic-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.1
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alpic/refs/heads/main/screenshots/alpic-2026-07-25T195808.png
security:
- kind: authentication
  name: Alpic Authentication
  slug: alpic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alpic Domain Security
  slug: alpic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Alpic Trust Center
  slug: alpic-trust-center
  summary_line: trust center published
slug: alpic
tags:
- Company
- Ai/Ml
- MCP
- Model Context Protocol
- Cloud Platform
- Developer Tools
- Deployment
- ChatGPT Apps
- Agentic
website: https://alpic.ai/
---
