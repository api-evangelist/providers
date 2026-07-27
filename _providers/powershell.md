---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Powershell Agentic Access
  operation_count: 6
  slug: powershell-agentic-access
  summary_line: 6 operations
api_count: 7
apis:
- description: The PowerShell Gallery is the central repository for PowerShell modules, scripts, and DSC resources. It exposes a public OData v2 API for searching, retrieving, and downloading packages programmatical
  name: PowerShell Gallery API
  slug: powershell-gallery-api
- description: .NET APIs for creating, configuring, and managing PowerShell runspaces from host applications. Enables embedding PowerShell execution inside .NET programs.
  name: PowerShell Runspace API
  slug: powershell-runspace-api
- description: APIs and protocols for remote PowerShell execution over WS-Management (WinRM) and SSH. Enables one-to-one and one-to-many remote command and session management.
  name: PowerShell Remoting API
  slug: powershell-remoting-api
- description: OData service metadata.
  name: PowerShell Metadata API
  slug: powershell-metadata-api
- description: Browse and retrieve package entries from the Gallery feed.
  name: PowerShell Packages API
  slug: powershell-packages-api
- description: Search and discovery operations.
  name: PowerShell Search API
  slug: powershell-search-api
- description: Find updates for installed packages.
  name: PowerShell Updates API
  slug: powershell-updates-api
artifact_total: 16
collections:
- collection_type: open
  name: PowerShell Gallery API
  slug: open-powershell
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/powershell-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/powershell-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/powershell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powershell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/powershell-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com/powershell
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PowerShell/PowerShell
- group: docs
  title: ''
  type: Documentation
  url: https://docs.microsoft.com/en-us/powershell/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/powershell/
- group: operate
  title: ''
  type: Community
  url: https://github.com/PowerShell/PowerShell/blob/master/docs/community/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started
- group: commercial
  title: ''
  type: License
  url: https://github.com/PowerShell/PowerShell/blob/master/LICENSE.txt
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/PowerShell/PowerShell/releases
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/PowerShell/PowerShell/projects
- group: auth
  title: ''
  type: Security
  url: https://github.com/PowerShell/PowerShell/security/policy
- group: other
  title: ''
  type: Contributing
  url: https://github.com/PowerShell/PowerShell/blob/master/.github/CONTRIBUTING.md
created: '2024-01-15'
description: PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. The PowerShell ecosystem exposes APIs through the PowerShell Gallery (an OData-based package repository), the Runspace .NET hosting APIs, and PowerShell Remoting protocols (WS-Management and SSH).
finops:
- name: Powershell Finops
  service_category: API
  slug: powershell-finops
image: https://raw.githubusercontent.com/PowerShell/PowerShell/master/assets/ps_black_64.svg
layout: provider
modified: '2026-04-28'
name: PowerShell
nav: Providers
network: true
overview: 'PowerShell publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Packages API, Search API, and 1 more. Tagged areas include Automation, Command-Line, Cross-Platform, Scripting, and Shell.


  PowerShell''s developer surface includes authentication, GitHub presence, documentation, engineering blog, getting-started guide, release notes, and 10 more developer resources.'
plans:
- name: Powershell Plans Pricing
  plan_count: 3
  slug: powershell-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Powershell Rate Limits
  slug: powershell-rate-limits
score:
  band: developing
  composite: 48.2
  delta: 2.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 54.9
    developer_ergonomics: 37.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 46.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powershell/refs/heads/main/screenshots/powershell-2026-06-20T192030.png
security:
- kind: authentication
  name: Powershell Authentication
  slug: powershell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Powershell Domain Security
  slug: powershell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Powershell Vulnerability Disclosure
  slug: powershell-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Powershell Trust Center
  slug: powershell-trust-center
  summary_line: GDPR
slug: powershell
tags:
- Automation
- Command-Line
- Cross-Platform
- Scripting
- Shell
- Windows
- DevOps
website: https://microsoft.com/powershell
---
