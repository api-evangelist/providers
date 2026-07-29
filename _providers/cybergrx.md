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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Versioned REST API for managing third-party cyber risk — search and create third parties, answer inherent-risk scoping questions, apply tags, read inherent and residual risk profiles, and bulk-export '
  name: CyberGRX Global Risk Exchange API
  slug: cybergrx-global-risk-exchange-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.cybergrx.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.cybergrx.com/v1/swagger/
- group: docs
  title: ''
  type: Documentation
  url: https://www.processunity.com/cybergrx-product-guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/CyberGRX/api-examples/blob/master/HOW-TO.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CyberGRX
- group: operate
  title: ''
  type: Support
  url: https://processunity.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.processunity.com/resources/blogs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cybergrx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cybergrx-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cybergrx-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cybergrx-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cybergrx-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cybergrx-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cybergrx-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybergrx-domain-security.yml
created: '2026-07-17'
description: CyberGRX is a third-party cyber risk management platform — the Global Risk Exchange (GRX) — that helps organizations assess, monitor, and reduce risk across their vendor and supplier ecosystem. It combines a shared library of standardized vendor risk assessments with analytics for inherent and residual risk, control gaps, and findings. CyberGRX was acquired by ProcessUnity in 2023 and is now delivered as the ProcessUnity Global Risk Exchange. It exposes a versioned REST API (v1, bulk-v1, v2) authenticated with an account API token passed in the Authorization header, including a Bulk API that returns an entire third-party ecosystem — residual risk, control scores, and findings — in a single request, plus first-party Python examples and Go/Splunk connectors.
image: https://avatars.githubusercontent.com/u/20931711?v=4
layout: provider
mcp_servers:
- description: ''
  name: cybergrx-mcp.yml
  slug: cybergrx-mcpyml
modified: '2026-07-18'
name: CyberGRX
nav: Providers
network: true
overview: 'CyberGRX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Third Party Risk, Vendor Risk Management, and Risk Management.


  CyberGRX''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, authentication, sandbox, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.0
  delta: -4.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 53.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.0
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cybergrx/refs/heads/main/screenshots/cybergrx-2026-07-25T211027.png
security:
- kind: authentication
  name: Cybergrx Authentication
  slug: cybergrx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cybergrx Domain Security
  slug: cybergrx-domain-security
  summary_line: DMARC
slug: cybergrx
tags:
- Company
- Cybersecurity
- Third Party Risk
- Vendor Risk Management
- Risk Management
- GRC
- Security Assessment
website: https://www.cybergrx.com/
---
