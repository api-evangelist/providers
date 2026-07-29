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
- acting_count: 2
  human_in_the_loop: 0
  name: Microsoft Nuget Agentic Access
  operation_count: 10
  slug: microsoft-nuget-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 6
apis:
- description: The Autocomplete API from Microsoft NuGet — 1 operation(s) for autocomplete.
  name: Microsoft NuGet Autocomplete API
  slug: microsoft-nuget-autocomplete-api
- description: The Flatcontainer API from Microsoft NuGet — 3 operation(s) for flatcontainer.
  name: Microsoft NuGet Flatcontainer API
  slug: microsoft-nuget-flatcontainer-api
- description: The Index.json API from Microsoft NuGet — 1 operation(s) for index.json.
  name: Microsoft NuGet Index.json API
  slug: microsoft-nuget-index-json-api
- description: The Package API from Microsoft NuGet — 2 operation(s) for package.
  name: Microsoft NuGet Package API
  slug: microsoft-nuget-package-api
- description: The Query API from Microsoft NuGet — 1 operation(s) for query.
  name: Microsoft NuGet Query API
  slug: microsoft-nuget-query-api
- description: The Registration5 Gz Semver2 API from Microsoft NuGet — 2 operation(s) for registration5 gz semver2.
  name: Microsoft NuGet Registration5 Gz Semver2 API
  slug: microsoft-nuget-registration5-gz-semver2-api
artifact_total: 13
collections:
- collection_type: open
  name: NuGet Server API (V3)
  slug: open-microsoft-nuget
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-nuget-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-nuget-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-nuget-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.nuget.org/
- group: company
  title: ''
  type: Website
  url: https://www.nuget.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NuGet
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/nuget/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-in-visual-studio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuget.org/policies/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuget.org/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/dotnet/category/nuget/feed/
created: '2024-01-01'
description: NuGet is the package manager for .NET, hosted by Microsoft. It provides APIs for searching, downloading, publishing, and managing .NET packages through the NuGet Gallery and private feeds.
finops:
- name: Microsoft Nuget Finops
  service_category: API
  slug: microsoft-nuget-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-nuget.png
layout: provider
modified: '2026-05-19'
name: Microsoft NuGet
nav: Providers
network: true
overview: 'Microsoft NuGet publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Flatcontainer API, Index.json API, and 3 more. Tagged areas include .NET, Microsoft, NuGet, and Package Management.


  Microsoft NuGet''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Nuget Plans Pricing
  plan_count: 3
  slug: microsoft-nuget-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Microsoft Nuget Rate Limits
  slug: microsoft-nuget-rate-limits
score:
  band: developing
  composite: 45.6
  delta: -1.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 47.9
    developer_ergonomics: 45.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-nuget/refs/heads/main/screenshots/microsoft-nuget-2026-06-20T185508.png
security:
- kind: authentication
  name: Microsoft Nuget Authentication
  slug: microsoft-nuget-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Nuget Domain Security
  slug: microsoft-nuget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-nuget
tags:
- .NET
- Microsoft
- NuGet
- Package Management
website: https://www.nuget.org/
---
