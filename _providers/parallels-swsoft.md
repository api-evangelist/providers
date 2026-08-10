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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for automating Parallels Remote Application Server (RAS) — infrastructure, sites, secure gateways, RD session hosts, cloud providers, publishing, policies and licensing. Served by the self-ho
  name: Parallels RAS REST API
  slug: parallels-ras-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: http://www.parallels.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.parallels.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parallels.com/landing/ras-rest-api-guide
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parallels.com/landing/ras-rest-api-guide/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.parallels.com/landing/ras-rest-api-guide
- group: operate
  title: ''
  type: Support
  url: https://www.parallels.com/products/ras/support/
- group: company
  title: ''
  type: Blog
  url: https://www.parallels.com/blogs/ras/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Parallels
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parallels.com/products/ras/buy/
- group: start
  title: ''
  type: SignUp
  url: https://www.parallels.com/products/ras/trial/
- group: start
  title: ''
  type: Login
  url: https://my.parallels.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parallels.com/about/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parallels.com/about/legal/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/parallels-swsoft-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parallels-swsoft-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parallels-swsoft-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/parallels-swsoft-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parallels-swsoft-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parallels-swsoft-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parallels-swsoft-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parallels-swsoft-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parallels-swsoft-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parallels-swsoft-domain-security.yml
created: '2026-07-17'
description: Parallels is a virtualization and remote-access software company, originally founded as SWSoft in 1999 and renamed Parallels in 2008 (now part of Alludo/Corel). Its flagship enterprise product, Parallels Remote Application Server (RAS), delivers virtual apps and desktops and exposes a public REST API plus a PowerShell SDK (RASAdmin) for automating farm administration — sites, secure gateways, RD session hosts, cloud providers (Azure/AVD, AWS EC2, Hyper-V, VMware, Nutanix), publishing, policies and licensing. The RAS REST API is served by the customer's self-hosted RAS server (default TCP port 20443) and authenticated with a session token obtained via api/session/logon.
image: https://www.parallels.com/fileadmin/images/logo/parallels-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: parallels-swsoft-mcp.yml
  slug: parallels-swsoft-mcpyml
modified: '2026-07-20'
name: Parallels (SWSoft)
nav: Providers
network: true
overview: 'Parallels (SWSoft) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtualization, Remote Desktop, Application Delivery, and Cloud Infrastructure.


  Parallels (SWSoft)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 59
score:
  band: thin
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 29.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parallels-swsoft/refs/heads/main/screenshots/parallels-swsoft-2026-08-07T191426.png
security:
- kind: authentication
  name: Parallels Swsoft Authentication
  slug: parallels-swsoft-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Parallels Swsoft Domain Security
  slug: parallels-swsoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parallels-swsoft
tags:
- Company
- Virtualization
- Remote Desktop
- Application Delivery
- Cloud Infrastructure
- VDI
- Automation
- REST API
website: http://www.parallels.com/
---
