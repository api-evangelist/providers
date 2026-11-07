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
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Home Assistant REST API provides endpoints under /api/ for reading states, calling services, firing events, and rendering templates.
  name: Home Assistant REST API
  slug: home-assistant-rest-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/home-assistant/well-known/home-assistant-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/home-assistant-status-security.txt
- group: auth
  href: https://artifacts.apis.io/home-assistant/authentication/home-assistant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/home-assistant-authentication.yml
- group: agent
  href: https://artifacts.apis.io/home-assistant/llms/home-assistant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/home-assistant-llms.txt
- group: auth
  href: https://artifacts.apis.io/home-assistant/well-known/home-assistant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/home-assistant-security.txt
- group: auth
  href: https://artifacts.apis.io/home-assistant/well-known/home-assistant-home-assistant-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/home-assistant-home-assistant-security.txt
- group: agent
  href: https://artifacts.apis.io/home-assistant/well-known/home-assistant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/home-assistant-well-known.yml
- group: other
  href: https://artifacts.apis.io/home-assistant/hosts/home-assistant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/home-assistant-hosts.yml
- group: other
  href: https://artifacts.apis.io/home-assistant/vendors/home-assistant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/home-assistant-vendors.yml
- group: build
  href: https://artifacts.apis.io/home-assistant/packages/home-assistant-packages.yml
  title: ''
  type: SDKs
  url: packages/home-assistant-packages.yml
- group: build
  href: https://artifacts.apis.io/home-assistant/packages/home-assistant-packages.yml
  title: ''
  type: Packages
  url: packages/home-assistant-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.home-assistant.io/tos/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.home-assistant.io
- group: auth
  title: ''
  type: Security
  url: https://www.home-assistant.io/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://contributors.home-assistant.io/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.home-assistant.io/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.home-assistant.io/developers/cla/
- group: operate
  title: ''
  type: ChangeLog
  url: https://contributors.home-assistant.io/releases/
- group: docs
  title: ''
  type: APIReference
  url: https://contributors.home-assistant.io/community/reference/events/
- group: auth
  href: https://artifacts.apis.io/home-assistant/security/home-assistant-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/home-assistant-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/home-assistant/security/home-assistant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/home-assistant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.home-assistant.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.home-assistant.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.home-assistant.io/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.home-assistant.io/help
- group: company
  title: ''
  type: Blog
  url: https://www.home-assistant.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/home-assistant
created: '2026-10-27'
description: Home Assistant is an open-source home automation platform developed by the Open Home Foundation. It enables local control and privacy‑first integration of thousands of smart devices, offering a web UI, mobile apps, voice assistants, and extensive automation capabilities. The community‑driven project provides extensive documentation, a vibrant forum, and regular releases, positioning it as a leading solution for DIY smart homes.
image: https://www.home-assistant.io/images/default-social.png
layout: provider
modified: '2026-10-27'
name: Home Assistant
nav: Providers
network: true
overview: 'Home Assistant is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Home Automation, Open Source, IoT, Community, and Non-Profit.


  Home Assistant''s developer surface includes authentication, changelog, API reference, documentation, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Home Assistant Rate Limits
  slug: home-assistant-rate-limits
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 41.7
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 32.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/home-assistant/home-assistant-2026-11-03T133426.png
security:
- kind: authentication
  name: Home Assistant Authentication
  slug: home-assistant-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Home Assistant Domain Security
  slug: home-assistant-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Home Assistant Vulnerability Disclosure
  slug: home-assistant-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: home-assistant
tags:
- Home Automation
- Open Source
- IoT
- Community
- Non-Profit
website: https://www.home-assistant.io/
---
