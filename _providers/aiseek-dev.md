---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only access to AiSeek's verified changes, calendar, markets and macro figures, and your own follows and alerts.
  name: AiSeek API
  slug: aiseek-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aiseek-dev/llms/aiseek-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiseek-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/aiseek-dev/hosts/aiseek-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiseek-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiseek-dev/vendors/aiseek-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiseek-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aiseek.dev/
- group: start
  title: ''
  type: Login
  url: https://aiseek.dev/en/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YOLOW92
- group: operate
  title: ''
  type: ChangeLog
  url: https://aiseek.dev/en/changelog
- group: auth
  href: https://artifacts.apis.io/aiseek-dev/security/aiseek-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiseek-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiseek.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aiseek.dev/en/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://aiseek.dev/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiseek.dev/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiseek.dev/en/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://aiseek.dev/en/about
- group: operate
  title: ''
  type: Support
  url: https://aiseek.dev/en/contact
coverage:
  checked: '2026-11-01'
  detail: Developer portal provides HTML docs but no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://aiseek.dev/en/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AiSeek provides a platform that aggregates and visualizes economic and market data, offering real‑time dashboards, forecasts, and analytical tools for investors, analysts, and businesses to track macro‑economic indicators, financial markets, and industry trends across the globe.
image: https://aiseek.dev/brand/og.png
layout: provider
modified: '2026-11-01'
name: AiSeek
nav: Providers
network: true
overview: 'AiSeek is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Finance, Analytics, Dashboards, and Markets.


  AiSeek''s developer surface includes changelog, pricing, documentation, support, and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 24.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiseek Dev Domain Security
  slug: aiseek-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aiseek-dev
tags:
- Data
- Finance
- Analytics
- Dashboards
- Markets
website: https://aiseek.dev/
---
