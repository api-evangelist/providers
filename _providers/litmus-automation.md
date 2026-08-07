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
  score: 19.8
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: Industrial edge data platform for device connectivity, industrial DataOps, edge intelligence, and analytics. Around 871 endpoints in the 4.0.x line; most endpoints are REST while newer areas (DeviceHu
  name: Litmus Edge
  slug: litmus-edge
- description: Centralized management for distributed edge environments — fleet operations, companies, projects, licensing, RBAC, and admin console. Around 304 REST endpoints in the 2.31.x line. X-AuthToken admin AP
  name: Litmus Edge Manager
  slug: litmus-edge-manager
- description: MQTT-based Unified Namespace (UNS) operations — namespace/class config, MQTT accounts and ACL rules, clients, integrations (Kafka, connectors), and configuration. Around 46 endpoints. OAuth2 bearer to
  name: Litmus Unify
  slug: litmus-unify
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/litmus-automation-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.litmus.io/
- group: company
  title: ''
  type: Website
  url: https://litmus.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.litmus.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.litmus.io
- group: docs
  title: ''
  type: APIReference
  url: https://api.litmus.io
- group: start
  title: ''
  type: GettingStarted
  url: https://litmus.io/get-started
- group: operate
  title: ''
  type: Support
  url: https://support.litmus.io
- group: company
  title: ''
  type: Blog
  url: https://litmus.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/litmusautomation
- group: commercial
  title: ''
  type: Pricing
  url: https://litmus.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://litmus.io/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://litmus.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://litmus.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.litmus.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/litmus-automation-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/litmus-automation-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/litmus-automation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/litmus-automation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/litmus-automation-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/litmus-automation-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/litmus-automation-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/litmus-automation-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/litmus-automation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/litmus-automation-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/litmus-automation-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litmus-automation-domain-security.yml
created: '2026-07-17'
description: Litmus Automation (Litmus) is an industrial data platform company that helps manufacturers connect industrial systems, standardize operational data, and deploy analytics, AI, and automation at scale across plant locations. Its products are Litmus Edge (an industrial edge data platform for device connectivity, DataOps, edge intelligence, and analytics), Litmus Edge Manager (centralized fleet management for distributed edge deployments), and Litmus Unify (an MQTT-based Unified Namespace). Litmus exposes a large public API surface — roughly 2,004 endpoints across the three products (REST plus newer GraphQL areas), OAuth2 client-credentials authentication, a standalone litmus-cli, a Python SDK, and an open-source Model Context Protocol (MCP) server for agentic access. Backed by Insight Partners.
image: https://litmus.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: litmus-automation-mcp.yml
  slug: litmus-automation-mcpyml
modified: '2026-07-20'
name: Litmus Automation
nav: Providers
network: true
overview: 'Litmus Automation publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Industrial IoT, Edge Computing, and IIoT.


  Litmus Automation''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 109
score:
  band: developing
  composite: 42.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 42.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litmus-automation/refs/heads/main/screenshots/litmus-automation-2026-07-25T225339.png
security:
- kind: authentication
  name: Litmus Automation Authentication
  slug: litmus-automation-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Litmus Automation Domain Security
  slug: litmus-automation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Litmus Automation Trust Center
  slug: litmus-automation-trust-center
  summary_line: ISO 27001
slug: litmus-automation
tags:
- Company
- Manufacturing
- Industrial IoT
- Edge Computing
- IIoT
- Unified Namespace
- MQTT
- DataOps
- Industrial Data Platform
- Analytics
website: https://litmus.io/
---
