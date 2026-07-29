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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Package Agentic Access
  operation_count: 5
  slug: microsoft-package-agentic-access
  summary_line: 5 operations
api_count: 8
apis:
- description: API for managing .NET packages through NuGet Gallery.
  name: NuGet Package API
  slug: nuget-package-api
- description: API for the Windows Package Manager client for discovering and installing applications.
  name: Windows Package Manager (WinGet) API
  slug: winget-api
- description: API for managing app submissions and accessing Microsoft Store catalog.
  name: Microsoft Store API
  slug: microsoft-store-api
- description: API for managing packages in Azure Artifacts including NuGet, npm, Maven, and Python packages.
  name: Azure Artifacts Package API
  slug: azure-artifacts-api
- description: The PackageContent API from Microsoft Package — 2 operation(s) for packagecontent.
  name: Microsoft Package PackageContent API
  slug: microsoft-package-packagecontent-api
- description: The Registration API from Microsoft Package — 1 operation(s) for registration.
  name: Microsoft Package Registration API
  slug: microsoft-package-registration-api
- description: The Search API from Microsoft Package — 1 operation(s) for search.
  name: Microsoft Package Search API
  slug: microsoft-package-search-api
- description: The ServiceIndex API from Microsoft Package — 1 operation(s) for serviceindex.
  name: Microsoft Package ServiceIndex API
  slug: microsoft-package-serviceindex-api
artifact_total: 16
collections:
- collection_type: open
  name: NuGet Server API (V3)
  slug: open-microsoft-package
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-package-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-package-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-package-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-package-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-15'
description: A collection of Microsoft package management APIs covering NuGet, Windows Package Manager (WinGet), Microsoft Store, and Azure Artifacts for managing and distributing software packages across Microsoft platforms.
finops:
- name: Microsoft Package Finops
  service_category: API
  slug: microsoft-package-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-package.png
layout: provider
modified: '2026-04-28'
name: Microsoft Package
nav: Providers
network: true
overview: 'Microsoft Package publishes 4 APIs on the [APIs.io](https://apis.io/) network, including PackageContent API, Registration API, Search API, and 1 more. Tagged areas include Azure Artifacts, Microsoft, NuGet, Package Management, and WinGet.


  Microsoft Package''s developer surface includes authentication, developer portal, support, and 5 more developer resources.'
plans:
- name: Microsoft Package Plans Pricing
  plan_count: 3
  slug: microsoft-package-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Microsoft Package Rate Limits
  slug: microsoft-package-rate-limits
score:
  band: thin
  composite: 40.7
  delta: -2.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.2
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-package/refs/heads/main/screenshots/microsoft-package-2026-06-20T185523.png
security:
- kind: authentication
  name: Microsoft Package Authentication
  slug: microsoft-package-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Package Domain Security
  slug: microsoft-package-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Package Vulnerability Disclosure
  slug: microsoft-package-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-package
tags:
- Azure Artifacts
- Microsoft
- NuGet
- Package Management
- WinGet
website: https://developer.microsoft.com/
---
