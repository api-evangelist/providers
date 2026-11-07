---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for generating app store screenshots and mockups via the AppScreenshots service. Documentation is available at the provider's docs site.
  name: AppScreenshots API
  slug: appscreenshots-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/appscreenshots-net/plans/appscreenshots-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appscreenshots-net-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/appscreenshots-net/changelog/appscreenshots-net-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appscreenshots-net-changelog.yml
- group: agent
  href: https://artifacts.apis.io/appscreenshots-net/llms/appscreenshots-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appscreenshots-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/appscreenshots-net/mcp/appscreenshots-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/appscreenshots-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/appscreenshots-net/well-known/appscreenshots-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appscreenshots-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/appscreenshots-net/hosts/appscreenshots-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appscreenshots-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/appscreenshots-net/vendors/appscreenshots-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appscreenshots-net-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://appscreenshots.net/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://appscreenshots.net/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/appscreenshots-net/security/appscreenshots-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appscreenshots-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appscreenshots.net/
- group: docs
  title: ''
  type: Documentation
  url: https://appscreenshots.net/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://appscreenshots.net/pricing
- group: company
  title: ''
  type: Blog
  url: https://appscreenshots.net/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appscreenshots.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appscreenshots.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://appscreenshots.net/contact
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are served as a JavaScript‑rendered Next.js application, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://appscreenshots.net/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AppScreenshots provides a free, easy‑to‑use online editor for creating app store screenshots and mockups. Users can upload app captures, apply device frames, backgrounds, multi‑language support and AI‑assisted layouts, then export PNGs or ZIPs. The service supports iOS App Store, Google Play, Huawei AppGallery and Chrome Web Store, offering free core editing with paid plans for batch translation, AI workflows and premium templates. It targets developers and designers needing quick, professional‑looking store listings.
image: https://appscreenshots.net/og-v2.png
layout: provider
mcp_servers:
- description: Remote MCP server at appscreenshots.net.
  name: AppScreenshots MCP Server
  slug: appscreenshots-net-mcp-yml
modified: '2026-11-01'
name: AppScreenshots
nav: Providers
network: true
overview: 'AppScreenshots is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Screenshots, Design, Developer Tools, and Free.


  AppScreenshots'' developer surface includes changelog, getting-started guide, documentation, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Appscreenshots Net Plans Pricing
  plan_count: 2
  slug: appscreenshots-net-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 23.8
  provenance:
    mcp: first-party
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
  name: Appscreenshots Net Domain Security
  slug: appscreenshots-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appscreenshots-net
tags:
- Company
- Screenshots
- Design
- Developer Tools
- Free
website: https://appscreenshots.net/
---
