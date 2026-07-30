---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Self-hosted administration REST API for Parallels RAS (Remote Application Server). Applications authenticate with administrator credentials to obtain an authToken, then manage infrastructure (agents, '
  name: Parallels RAS REST API
  slug: parallels-ras-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.parallels.com/
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
  url: https://www.parallels.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.parallels.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Parallels
- group: start
  title: ''
  type: SignUp
  url: https://my.parallels.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parallels.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/parallels-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parallels-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parallels-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/parallels-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://kb.parallels.com/en/122073
- group: build
  title: ''
  type: CLI
  url: cli/parallels-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/parallels-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parallels-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parallels-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parallels-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parallels-domain-security.yml
created: '2026-07-17'
description: Parallels is a virtualization and remote-access software company (part of Alludo, with the Parallels virtualization division held by KKR) best known for Parallels Desktop for Mac, which runs Windows, Linux and other operating systems on Apple hardware for over 7 million users. Its enterprise line, Parallels RAS (Remote Application Server), delivers virtual apps and desktops (VDI/DaaS) across on-premises and hybrid-cloud deployments. For developers and IT admins, Parallels exposes a self-hosted Parallels RAS REST API (token-authenticated, port 20443) plus a RAS PowerShell administration module and the prlctl/prlsrvctl command-line tools, and publishes official Terraform, Packer, Vagrant, and Docker Machine integrations for Parallels Desktop from its GitHub organization.
image: https://www.parallels.com/static/pl/fileadmin/res/img/general/default-og-logo.png
layout: provider
modified: '2026-07-20'
name: Parallels
nav: Providers
network: true
overview: 'Parallels publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtualization, Remote Desktop, VDI, and DaaS.


  Parallels'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 14 more developer resources.'
random_paper: 58
score:
  band: thin
  composite: 30.2
  delta: -0.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 30.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Parallels Authentication
  slug: parallels-authentication
  summary_line: token · 2 schemes
- kind: domain-security
  name: Parallels Domain Security
  slug: parallels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parallels
tags:
- Company
- Virtualization
- Remote Desktop
- VDI
- DaaS
- Mac
- Infrastructure
- IT Management
website: https://www.parallels.com/
---
