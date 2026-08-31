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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/obot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/obot-platform/obot/security/advisories
- group: auth
  title: ''
  type: DomainSecurity
  url: security/obot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://obot.ai/
- group: start
  title: ''
  type: Portal
  url: https://docs.obot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.obot.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.obot.ai/installation/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/obot-platform
- group: company
  title: ''
  type: Blog
  url: https://obot.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://obot.ai/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://obot.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://obot.ai/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/obot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/obot-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/obot-authentication.yml
- group: build
  title: ''
  type: CLI
  url: cli/obot-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/obot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/obot-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/obot-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/obot-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/obot-changelog.yml
created: '2026-07-17'
description: Obot AI (formerly Acorn Labs) builds an open-source MCP Gateway and platform that gives organizations a central control point for Model Context Protocol (MCP) servers and AI agent Skills. Obot lets teams host local, remote, and multi-tenant MCP servers, publish an internal MCP catalog/registry, enforce OAuth-based access control and policy, and capture audit logs across every agent integration. It ships a built-in chat client with multi-model support, an enterprise edition with Okta and Microsoft Entra identity, and the companion Nanobot framework for building standalone MCP hosts. Written in Go and MIT-licensed, Obot self-hosts on Docker or Kubernetes.
image: https://obot.ai/wp-content/uploads/2026/05/obot_linkedin_01-1500x396-2.png
layout: provider
mcp_servers:
- description: ''
  name: Obot MCP Server
  slug: obot-mcp-server
modified: '2026-07-20'
name: Obot
nav: Providers
network: true
overview: 'Obot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, MCP Gateway, and Open-Source.


  Obot''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, authentication, CLI, and 14 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 28.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/obot/refs/heads/main/screenshots/obot-2026-08-07T185908.png
security:
- kind: authentication
  name: Obot Authentication
  slug: obot-authentication
  summary_line: oauth2/openIdConnect · 0 schemes
- kind: domain-security
  name: Obot Domain Security
  slug: obot-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Obot Vulnerability Disclosure
  slug: obot-vulnerability-disclosure
  summary_line: disclosure policy published
slug: obot
tags:
- Company
- MCP
- AI Agents
- MCP Gateway
- Open-Source
- Agent Governance
- Access Control
- Developer Tools
website: https://obot.ai/
---
