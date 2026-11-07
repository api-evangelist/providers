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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-11-06'
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
- group: auth
  href: https://artifacts.apis.io/powershell/well-known/powershell-microsoft-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/powershell-microsoft-security.txt
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: design
  href: https://artifacts.apis.io/powershell/rules/powershell-rules.yml
  title: ''
  type: Spectral
  url: rules/powershell-rules.yml
- group: design
  href: https://artifacts.apis.io/powershell/vocabulary/powershell-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/powershell-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/powershell/errors/powershell-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/powershell-problem-types.yml
- group: design
  href: https://artifacts.apis.io/powershell/conformance/powershell-conformance.yml
  title: ''
  type: Conformance
  url: conformance/powershell-conformance.yml
- group: agent
  href: https://artifacts.apis.io/powershell/llms/powershell-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/powershell-llms.txt
- group: auth
  href: https://artifacts.apis.io/powershell/well-known/powershell-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/powershell-security.txt
- group: agent
  href: https://artifacts.apis.io/powershell/well-known/powershell-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/powershell-well-known.yml
- group: other
  href: https://artifacts.apis.io/powershell/hosts/powershell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/powershell-hosts.yml
- group: other
  href: https://artifacts.apis.io/powershell/vendors/powershell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/powershell-vendors.yml
- group: build
  href: https://artifacts.apis.io/powershell/packages/powershell-packages.yml
  title: ''
  type: Packages
  url: packages/powershell-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/MicrosoftDocs/PowerShell-Docs/blob/main/reference/docs-conceptual/developer/windows-powershell.md
- group: commercial
  href: https://artifacts.apis.io/powershell/plans/powershell-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/powershell-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/powershell/rate-limits/powershell-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/powershell-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/powershell/finops/powershell-finops.yml
  title: ''
  type: FinOps
  url: finops/powershell-finops.yml
- group: agent
  href: https://artifacts.apis.io/powershell/agentic-access/powershell-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/powershell-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/powershell/security/powershell-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/powershell-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/powershell/security/powershell-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/powershell-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/powershell/security/powershell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powershell-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/powershell/authentication/powershell-authentication.yml
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
- has_sources: false
  method: generated
  name: Powershell Finops
  primary_unit: request
  service_category: API
  slug: powershell-finops
  template: true
image: https://raw.githubusercontent.com/PowerShell/PowerShell/master/assets/ps_black_64.svg
layout: provider
modified: '2026-04-28'
name: PowerShell
nav: Providers
network: true
overview: 'PowerShell publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Metadata API, Packages API, Search API, and 4 more. Tagged areas include Automation, Command Line, Cross-Platform, Scripting, and Shell.


  The PowerShell catalog on APIs.io includes 1 Spectral governance ruleset.


  PowerShell''s developer surface includes support, API reference, authentication, GitHub presence, documentation, engineering blog, getting-started guide, and 27 more developer resources.'
plans:
- name: Powershell Plans Pricing
  plan_count: 3
  slug: powershell-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Powershell Rate Limits
  slug: powershell-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: PowerShell API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: powershell-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.0
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 50.5
    developer_ergonomics: 61.9
    discoverability: 57.1
    operational_transparency: 44.7
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/powershell/powershell-2026-06-20T192030.png
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
