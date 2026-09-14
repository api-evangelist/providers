---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''http://www.skytap.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.kyndryl.com/us/en/services/cloud-uplift — a different registrable domain (skytap.com -> kyndryl.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: REST API for managing Skytap environments (configurations), VMs, networks, templates, users, projects, assets and webhooks. v2 adds filtering, sorting and pagination; v1 remains for operations not yet
  name: Skytap Cloud REST API
  slug: skytap-cloud-rest-api
artifact_total: 4
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
  type: X-MCPServerCandidate
  url: mcp/skytap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skytap-llms.txt
created: '2026-07-17'
description: Skytap (now delivered as Kyndryl Cloud Uplift) is a cloud service for running IBM Power (AIX, IBM i) and x86 workloads natively in Microsoft Azure, enabling enterprises to lift-and-shift traditional data-center applications into self-service, on-demand virtual environments without re-architecting them. The Skytap Cloud REST API (v1 and v2, hosted at cloud.skytap.com, HTTP Basic auth with an API token) programmatically manages environments (configurations), virtual machines, networks, templates, users, projects, assets, public IPs, schedules, usage reports and webhooks. It is the engine behind Skytap's official Terraform provider, Go SDK, PowerShell module, and Ansible and Vagrant integrations. Skytap is a portfolio company of Insight Partners.
image: https://www.skytap.com/wp-content/uploads/2021/03/skytap-logo.png
layout: provider
modified: '2026-07-21'
name: Skytap
nav: Providers
network: true
overview: 'Skytap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, IBM Power, Infrastructure-as-a-Service, and Application Modernization.


  The Skytap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Skytap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/skytap/refs/heads/main/screenshots/skytap-2026-09-02T155821.png
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
- Infrastructure-as-a-Service
- Application Modernization
- Azure
- Virtual Machines
- DevOps
- REST API
website: http://www.skytap.com/
---
