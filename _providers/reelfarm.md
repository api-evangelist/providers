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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/reelfarm/hosts/reelfarm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reelfarm-hosts.yml
- group: other
  href: https://artifacts.apis.io/reelfarm/vendors/reelfarm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reelfarm-vendors.yml
- group: auth
  href: https://artifacts.apis.io/reelfarm/security/reelfarm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reelfarm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reel.farm/
- group: docs
  title: ''
  type: Documentation
  url: https://reel.farm/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://reel.farm/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://reel.farm/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://reel.farm/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reel.farm/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reel.farm/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation is a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://reel.farm/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: ReelFarm provides AI‑powered TikTok automation and video marketing services. It lets users generate faceless TikTok slideshows automatically, schedule posts, and manage content at scale. The platform offers a dashboard, API access for creating slideshows, managing automations, and retrieving analytics, targeting creators and marketers who want hands‑free video production.
image: https://reel.farm/og_image_3.png
layout: provider
modified: '2026-10-26'
name: ReelFarm
nav: Providers
network: true
overview: 'ReelFarm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, TikTok, Automation, and Video Marketing.


  ReelFarm''s developer surface includes documentation, API reference, getting-started guide, pricing, and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reelfarm/reelfarm-2026-11-03T142108.png
security:
- kind: domain-security
  name: Reelfarm Domain Security
  slug: reelfarm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reelfarm
tags:
- Company
- Artificial Intelligence
- TikTok
- Automation
- Video Marketing
website: https://reel.farm/
---
