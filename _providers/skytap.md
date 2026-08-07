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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for managing Skytap environments (configurations), VMs, networks, templates, users, projects, assets and webhooks. v2 adds filtering, sorting and pagination; v1 remains for operations not yet
  name: Skytap Cloud REST API
  slug: skytap-cloud-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Skytap Webhooks
  slug: skytap-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.skytap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.skytap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.skytap.com/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://help.skytap.com/API_v2_Documentation.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.skytap.com/api-quick-start.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skytap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.skytap.com
- group: company
  title: ''
  type: Blog
  url: https://www.skytap.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.skytap.com/
- group: operate
  title: ''
  type: Support
  url: https://help.skytap.com/
- group: build
  title: ''
  type: Packages
  url: packages/skytap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/skytap-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skytap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skytap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skytap-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skytap-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skytap-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skytap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.skytap.com/blog/skytap-offers-pci-and-iso-27001-compliance-for-ibm-power-workloads-in-azure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skytap-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/skytap-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skytap-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skytap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skytap-llms.txt
created: '2026-07-17'
description: Skytap (now delivered as Kyndryl Cloud Uplift) is a cloud service for running IBM Power (AIX, IBM i) and x86 workloads natively in Microsoft Azure, enabling enterprises to lift-and-shift traditional data-center applications into self-service, on-demand virtual environments without re-architecting them. The Skytap Cloud REST API (v1 and v2, hosted at cloud.skytap.com, HTTP Basic auth with an API token) programmatically manages environments (configurations), virtual machines, networks, templates, users, projects, assets, public IPs, schedules, usage reports and webhooks. It is the engine behind Skytap's official Terraform provider, Go SDK, PowerShell module, and Ansible and Vagrant integrations. Skytap is a portfolio company of Insight Partners.
image: https://www.skytap.com/wp-content/uploads/2021/03/skytap-logo.png
layout: provider
mcp_servers:
- description: ''
  name: skytap-mcp.yml
  slug: skytap-mcpyml
modified: '2026-07-21'
name: Skytap
nav: Providers
network: true
overview: 'Skytap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, IBM Power, Infrastructure as a Service, and Application Modernization.


  The Skytap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Skytap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 103
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 43.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Skytap Authentication
  slug: skytap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Skytap Domain Security
  slug: skytap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skytap
tags:
- Company
- Cloud
- IBM Power
- Infrastructure as a Service
- Application Modernization
- Azure
- Virtual Machines
- DevOps
- REST API
website: http://www.skytap.com/
---
