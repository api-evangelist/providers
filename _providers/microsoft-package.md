---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
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
- baseURL: https://api.nuget.org/v3/index.json
  baseurl_source: declared
  description: The PackageContent API from Microsoft Package — 2 operation(s) for packagecontent.
  name: Microsoft Package PackageContent API
  slug: microsoft-package-packagecontent-api
- baseURL: https://api.nuget.org/v3/index.json
  baseurl_source: declared
  description: The Registration API from Microsoft Package — 1 operation(s) for registration.
  name: Microsoft Package Registration API
  slug: microsoft-package-registration-api
- baseURL: https://api.nuget.org/v3/index.json
  baseurl_source: declared
  description: The Search API from Microsoft Package — 1 operation(s) for search.
  name: Microsoft Package Search API
  slug: microsoft-package-search-api
- baseURL: https://api.nuget.org/v3/index.json
  baseurl_source: declared
  description: The Service Index API from Microsoft Package — 1 operation(s) for service index.
  name: Microsoft Package Service Index API
  slug: microsoft-package-service-index-api
artifact_total: 21
collections:
- collection_type: open
  name: NuGet Server API (V3) PackageContent API
  slug: open-microsoft-package-packagecontent-api
- collection_type: open
  name: NuGet Server API (V3) PackageContent Registration API
  slug: open-microsoft-package-registration-api
- collection_type: open
  name: NuGet Server API (V3) PackageContent Search API
  slug: open-microsoft-package-search-api
- collection_type: open
  name: NuGet Server API (V3) PackageContent ServiceIndex API
  slug: open-microsoft-package-serviceindex-api
- collection_type: open
  name: NuGet Server API (V3)
  slug: open-microsoft-package
common:
- group: commercial
  href: https://artifacts.apis.io/microsoft-package/plans/microsoft-package-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-package-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-package/rate-limits/microsoft-package-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-package-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-package/finops/microsoft-package-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-package-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-package/agentic-access/microsoft-package-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-package-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-package/security/microsoft-package-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-package-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-package/security/microsoft-package-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-package-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-package/authentication/microsoft-package-authentication.yml
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
- has_sources: false
  method: generated
  name: Microsoft Package Finops
  primary_unit: request
  service_category: API
  slug: microsoft-package-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-package.png
layout: provider
modified: '2026-04-28'
name: Microsoft Package
nav: Providers
network: true
overview: 'Microsoft Package is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including PackageContent API, Registration API, Search API, and 5 more. Tagged areas include Azure Artifacts, Developer Tools, Microsoft, NuGet, and Package Management.


  The Microsoft Package catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Package''s developer surface includes authentication, developer portal, support, and 9 more developer resources.'
plans:
- name: Microsoft Package Plans Pricing
  plan_count: 3
  slug: microsoft-package-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Microsoft Package Rate Limits
  slug: microsoft-package-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Microsoft Package API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 1
  slug: microsoft-package-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 42.2
    developer_ergonomics: 23.8
    discoverability: 78.6
    operational_transparency: 21.1
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/microsoft-package/microsoft-package-2026-06-20T185523.png
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
- Developer Tools
- Microsoft
- NuGet
- Package Management
- WinGet
website: https://www.microsoft.com/
---
