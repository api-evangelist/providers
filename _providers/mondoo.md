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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Mondoo Platform API is a GraphQL API for programmatically querying assets, configuring integrations, and fetching vulnerability, policy, and compliance reports. Authentication is token-based via s
  name: Mondoo Platform GraphQL API
  slug: mondoo-platform-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mondoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/mondoohq/.github/blob/main/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mondoo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mondoo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mondoo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://mondoo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://mondoo.com/docs/platform/maintain/access/service_accounts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mondoohq
- group: company
  title: ''
  type: Blog
  url: https://mondoo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://mondoo.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://mondoo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.mondoo.com
- group: start
  title: ''
  type: Login
  url: https://console.mondoo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mondoo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mondoo.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mondoo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/mondoo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mondoo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mondoo-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mondoo-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mondoo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mondoo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mondoo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mondoo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mondoo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mondoo.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mondoo-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mondoo-data-model.yml
created: '2026-07-17'
description: Mondoo is a cloud-native security and vulnerability risk management platform built around "Agentic Vulnerability Management" — AI agents that discover, prioritize by business impact, and automatically remediate vulnerabilities and misconfigurations across cloud accounts, containers, Kubernetes, servers, endpoints, SaaS products, network devices, and infrastructure-as-code. The platform is built on the open-source cnquery infrastructure query tool and the cnspec policy-as-code security scanner, both driven by MQL (the Mondoo Query Language), and exposes a GraphQL Platform API for programmatic access to assets, integrations, and vulnerability, policy, and compliance reports. Mondoo ships official SDKs, a Terraform provider, cnquery/cnspec CLIs with an MCP server interface, and packaged Agent Skills for MQL and secure coding.
image: https://github.com/mondoohq.png
layout: provider
mcp_servers:
- description: ''
  name: mondoo-mcp.yml
  slug: mondoo-mcpyml
modified: '2026-07-20'
name: Mondoo
nav: Providers
network: true
overview: 'Mondoo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Vulnerability Management, and Compliance.


  Mondoo''s developer surface includes documentation, getting-started guide, engineering blog, support, pricing, signup flow, CLI, and 22 more developer resources.'
random_paper: 72
score:
  band: thin
  composite: 41.1
  delta: 1.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 40.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mondoo/refs/heads/main/screenshots/mondoo-2026-08-07T184145.png
security:
- kind: authentication
  name: Mondoo Authentication
  slug: mondoo-authentication
  summary_line: bearer-token/oidc · 2 schemes
- kind: domain-security
  name: Mondoo Domain Security
  slug: mondoo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mondoo Vulnerability Disclosure
  slug: mondoo-vulnerability-disclosure
  summary_line: contact published
slug: mondoo
tags:
- Company
- Cybersecurity
- Security
- Vulnerability Management
- Compliance
- Cloud Security
- Policy as Code
- DevSecOps
- GraphQL
- SAST
website: https://mondoo.com
---
