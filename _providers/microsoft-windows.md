---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.7
  scored_at: '2026-09-05'
api_count: 8
apis:
- description: Modern API for building Windows applications with support for multiple programming languages.
  name: Windows Runtime (WinRT) API
  slug: windows-runtime-winrt-api
- description: Traditional Windows API for native application development with full system access.
  name: Win32 API
  slug: win32-api
- description: Infrastructure for management data and operations on Windows systems.
  name: Windows Management Instrumentation (WMI)
  slug: windows-management-instrumentation-wmi
- description: Task automation and configuration management framework from Microsoft.
  name: Windows PowerShell API
  slug: windows-powershell-api
- description: API for accessing and manipulating the Windows Registry database.
  name: Windows Registry API
  slug: windows-registry-api
- description: APIs for interacting with Windows Shell features and user interface elements.
  name: Windows Shell API
  slug: windows-shell-api
- description: Collection of APIs for handling tasks related to multimedia and game programming.
  name: DirectX Graphics API
  slug: directx-graphics-api
- description: API for creating and managing Windows notifications and toast messages.
  name: Windows Notification API
  slug: windows-notification-api
artifact_total: 13
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PowerShell/PowerShell/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/PowerShell/PowerShell/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/PowerShell/PowerShell/blob/master/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/PowerShell/PowerShell/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/PowerShell/PowerShell/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/PowerShell/PowerShell/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-windows-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-windows-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-windows
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/windows
- group: company
  title: ''
  type: Blog
  url: https://blogs.windows.com/windowsdeveloper/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/windows
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: build
  title: ''
  type: SDK Downloads
  url: https://developer.microsoft.com/windows/downloads/
created: '2024'
description: A collection of APIs and developer resources for Microsoft Windows operating system.
finops:
- name: Microsoft Windows Finops
  service_category: API
  slug: microsoft-windows-finops
image: https://www.microsoft.com/windows/windows-11-logo.png
layout: provider
modified: '2026-04-28'
name: Microsoft Windows
nav: Providers
network: true
overview: 'Microsoft Windows publishes 1 API on the [APIs.io](https://apis.io/) network: Windows Runtime (WinRT) API. Tagged areas include Desktop, Development, Microsoft, Operating System, and Windows.


  Microsoft Windows'' developer surface includes developer portal, engineering blog, support, and 13 more developer resources.'
plans:
- name: Microsoft Windows Plans Pricing
  plan_count: 3
  slug: microsoft-windows-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Microsoft Windows Rate Limits
  slug: microsoft-windows-rate-limits
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 45.2
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 65.0
  previous_composite: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-windows/refs/heads/main/screenshots/microsoft-windows-2026-06-20T185544.png
security:
- kind: domain-security
  name: Microsoft Windows Domain Security
  slug: microsoft-windows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Windows Vulnerability Disclosure
  slug: microsoft-windows-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-windows
tags:
- Desktop
- Development
- Microsoft
- Operating System
- Windows
website: https://developer.microsoft.com/windows
---
