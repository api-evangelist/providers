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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://diagrid.io
- group: start
  title: ''
  type: Portal
  url: https://catalyst.diagrid.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.diagrid.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.diagrid.io/references
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.diagrid.io/getting-started/quickstarts/
- group: company
  title: ''
  type: Blog
  url: https://www.diagrid.io/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diagridio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.diagrid.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://catalyst.diagrid.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diagrid.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diagrid.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/pBSZ9wRFae
- group: operate
  title: ''
  type: StatusPage
  url: https://status.diagrid.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/diagrid-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/diagrid-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/diagrid-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/diagrid-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/diagrid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/diagrid-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/diagrid-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/diagrid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/diagrid-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/diagrid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diagrid-domain-security.yml
created: '2026-07-17'
description: Diagrid is the execution layer for production AI, built by the creators of the open source Dapr and KEDA projects. Its managed platform, Diagrid Catalyst, gives AI agents, workflows, and MCP servers durable execution (applications resume from the last completed step after crashes or outages) and verifiable execution (every step is cryptographically signed into a tamper-evident audit log). Catalyst exposes the Dapr APIs — service invocation, publish/subscribe, state management, workflows, and conversation/LLM calls — as a serverless, fully managed service with SPIFFE-based workload identity, mutual TLS, and declarative access policies. Diagrid Conductor is a companion product for operating and managing Dapr and KEDA across Kubernetes clusters. The platform is delivered as a free Catalyst Cloud tier and a self-hosted Catalyst Enterprise offering, is SOC 2 Type II certified, and is driven through a rich diagrid CLI, per-language SDKs, and a Terraform provider.
image: https://www.diagrid.io/favicon.ico
layout: provider
modified: '2026-07-18'
name: Diagrid
nav: Providers
network: true
overview: 'Diagrid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, AI Agents, Durable Execution, and Workflows.


  Diagrid''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 32.0
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/diagrid/refs/heads/main/screenshots/diagrid-2026-07-25T211904.png
security:
- kind: authentication
  name: Diagrid Authentication
  slug: diagrid-authentication
  summary_line: apiKey/http/oauth2/mutualTLS · 5 schemes
- kind: domain-security
  name: Diagrid Domain Security
  slug: diagrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Diagrid Trust Center
  slug: diagrid-trust-center
  summary_line: SOC 2 Type II
slug: diagrid
tags:
- Company
- Developer Tools
- AI Agents
- Durable Execution
- Workflows
- Dapr
- MCP
- Microservices
- Cloud-Native
- Distributed Systems
website: https://diagrid.io
---
