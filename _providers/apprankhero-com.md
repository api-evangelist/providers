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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 25.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AppRankHero provides a macOS application that tracks App Store and Google Play keyword rankings daily.
  name: AppRankHero API
  slug: apprankhero-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/apprankhero-com/plans/apprankhero-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apprankhero-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/apprankhero-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apprankhero-com/lifecycle/apprankhero-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apprankhero-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/apprankhero-com/llms/apprankhero-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apprankhero-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/apprankhero-com/well-known/apprankhero-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apprankhero-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apprankhero-com/hosts/apprankhero-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apprankhero-com-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://apprankhero.com/changelog
- group: auth
  href: https://artifacts.apis.io/apprankhero-com/security/apprankhero-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apprankhero-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apprankhero.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://apprankhero.com/pricing
- group: operate
  title: ''
  type: Help
  url: https://apprankhero.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://apprankhero.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apprankhero.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apprankhero.com/terms
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://apprankhero.com/help
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AppRankHero provides a macOS application that tracks App Store and Google Play keyword rankings daily. It offers both free and paid plans, allowing users to monitor keyword positions, competitor movements, and market intelligence across multiple countries. The service includes AI integration via MCP, enabling natural‑language queries of ranking data. Features include daily scans of top‑200 App Store results and top‑30 Google Play results, customizable alerts, and exportable reports. The platform aims to help app developers and marketers optimize ASO strategies with real‑time insights.
image: https://apprankhero.com/og.png
layout: provider
modified: '2026-11-01'
name: AppRankHero
nav: Providers
network: true
overview: 'AppRankHero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ASO, macOS, KeywordTracking, AI Integration, and Analytics.


  AppRankHero''s developer surface includes changelog, pricing, and 12 more developer resources.'
plans:
- name: Apprankhero Com Plans Pricing
  plan_count: 3
  slug: apprankhero-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 24.4
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apprankhero Com Domain Security
  slug: apprankhero-com-domain-security
  summary_line: TLSv1.3
slug: apprankhero-com
tags:
- ASO
- macOS
- KeywordTracking
- AI Integration
- Analytics
website: https://apprankhero.com/
---
