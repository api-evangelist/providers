---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Powershell Agentic Access
  operation_count: 6
  slug: powershell-agentic-access
  summary_line: 6 operations
api_count: 1
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
- baseURL: https://www.powershellgallery.com/api/v2
  baseurl_source: declared
  description: OData service metadata.
  name: PowerShell Metadata API
  slug: powershell-metadata-api
- baseURL: https://www.powershellgallery.com/api/v2
  baseurl_source: declared
  description: Browse and retrieve package entries from the Gallery feed.
  name: PowerShell Packages API
  slug: powershell-packages-api
- baseURL: https://www.powershellgallery.com/api/v2
  baseurl_source: declared
  description: Search and discovery operations.
  name: PowerShell Search API
  slug: powershell-search-api
- baseURL: https://www.powershellgallery.com/api/v2
  baseurl_source: declared
  description: Find updates for installed packages.
  name: PowerShell Updates API
  slug: powershell-updates-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PowerShell Gallery Metadata API
  slug: open-powershell-metadata-api
- collection_type: open
  name: PowerShell Gallery Metadata Packages API
  slug: open-powershell-packages-api
- collection_type: open
  name: PowerShell Gallery Metadata Search API
  slug: open-powershell-search-api
- collection_type: open
  name: PowerShell Gallery Metadata Updates API
  slug: open-powershell-updates-api
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
overview: 'PowerShell publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Packages API, Search API, and 1 more. Tagged areas include Automation, Command Line, Cross-Platform, Scripting, and Shell.


  PowerShell''s developer surface includes authentication, GitHub presence, documentation, engineering blog, getting-started guide, release notes, and 10 more developer resources.'
plans:
- name: Powershell Plans Pricing
  plan_count: 3
  slug: powershell-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Powershell Rate Limits
  slug: powershell-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Command Line
- Cross-Platform
- Scripting
- Shell
- Windows
- DevOps
website: https://microsoft.com/powershell
---
