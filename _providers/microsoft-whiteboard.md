---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'First-party WhiteboardAdmin PowerShell module (PowerShell Gallery, latest 1.14.1, 2026-03-12) for tenant administration of Microsoft Whiteboard: list whiteboards for a user or tenant, get and set owne'
  name: Microsoft Whiteboard Admin PowerShell
  slug: whiteboard-admin-powershell
artifact_total: 6
common:
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: build
  href: https://artifacts.apis.io/microsoft-whiteboard/cli/microsoft-whiteboard-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-whiteboard-cli.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-whiteboard/llms/microsoft-whiteboard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-whiteboard-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-whiteboard/well-known/microsoft-whiteboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-whiteboard-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-whiteboard/well-known/microsoft-whiteboard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-whiteboard-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-whiteboard/hosts/microsoft-whiteboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-whiteboard-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-whiteboard/vendors/microsoft-whiteboard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-whiteboard-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-whiteboard/packages/microsoft-whiteboard-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-whiteboard-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-whiteboard/packages/microsoft-whiteboard-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-whiteboard-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: commercial
  href: https://artifacts.apis.io/microsoft-whiteboard/finops/microsoft-whiteboard-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-whiteboard-finops.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-whiteboard/security/microsoft-whiteboard-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-whiteboard-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-whiteboard/security/microsoft-whiteboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-whiteboard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://whiteboard.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/microsoft-whiteboard/digital-whiteboard-app
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
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/microsoft-365/whiteboard/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.microsoft.com/office/microsoft-whiteboard-help-d236aef8-fcdf-4b5e-b5d7-7f157461e920
created: '2024-01-01'
description: Microsoft Whiteboard is Microsoft's freeform digital canvas for visual collaboration, available on the web, Windows, iOS, Android, Surface Hub and inside Microsoft Teams meetings. Microsoft publishes no public Whiteboard REST API (there is no whiteboard resource in Microsoft Graph); the documented programmatic surface is the first-party WhiteboardAdmin PowerShell module, which tenant administrators use to list, transfer ownership of, delete, restore and migrate whiteboards and to manage Whiteboard settings.
finops:
- has_sources: false
  method: generated
  name: Microsoft Whiteboard Finops
  primary_unit: request
  service_category: API
  slug: microsoft-whiteboard-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-whiteboard.png
layout: provider
modified: '2026-11-04'
name: Microsoft Whiteboard
nav: Providers
network: true
overview: 'Microsoft Whiteboard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Microsoft, Microsoft 365, Visual Collaboration, and Whiteboard.


  Microsoft Whiteboard''s developer surface includes engineering blog, getting-started guide, CLI, changelog, developer portal, support, documentation, and 17 more developer resources.'
plans:
- name: Microsoft Whiteboard Plans Pricing
  plan_count: 0
  slug: microsoft-whiteboard-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Microsoft Whiteboard Rate Limits
  slug: microsoft-whiteboard-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 21.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microsoft-whiteboard/microsoft-whiteboard-2026-06-20T185544.png
security:
- kind: domain-security
  name: Microsoft Whiteboard Domain Security
  slug: microsoft-whiteboard-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Whiteboard Vulnerability Disclosure
  slug: microsoft-whiteboard-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-whiteboard
tags:
- Collaboration
- Microsoft
- Microsoft 365
- Visual Collaboration
- Whiteboard
website: https://www.microsoft.com/en-us/microsoft-365/microsoft-whiteboard/digital-whiteboard-app
---
