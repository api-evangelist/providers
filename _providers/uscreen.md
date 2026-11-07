---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Uscreen Webhooks
  slug: uscreen-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/uscreen/well-known/uscreen-uscreen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uscreen-uscreen-security.txt
- group: commercial
  href: https://artifacts.apis.io/uscreen/plans/uscreen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uscreen-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/uscreen/asyncapi/uscreen-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uscreen-webhooks.yml
- group: design
  href: https://artifacts.apis.io/uscreen/conformance/uscreen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uscreen-conformance.yml
- group: agent
  href: https://artifacts.apis.io/uscreen/llms/uscreen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uscreen-llms.txt
- group: auth
  href: https://artifacts.apis.io/uscreen/well-known/uscreen-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uscreen-help-security.txt
- group: agent
  href: https://artifacts.apis.io/uscreen/well-known/uscreen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uscreen-well-known.yml
- group: other
  href: https://artifacts.apis.io/uscreen/hosts/uscreen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uscreen-hosts.yml
- group: other
  href: https://artifacts.apis.io/uscreen/vendors/uscreen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uscreen-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.uscreen.tv/
- group: operate
  title: ''
  type: StatusPage
  url: https://uscreen.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uscreen.tv/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.uscreen.tv/en/articles/4315861-seo-setup-a-complete-guide
- group: auth
  href: https://artifacts.apis.io/uscreen/security/uscreen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uscreen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uscreen.tv/
- group: docs
  title: ''
  type: Documentation
  url: https://www.uscreen.tv/resources/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.uscreen.tv/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uscreen.tv/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.uscreen.tv/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.uscreen.tv/admin/registrations/new
coverage:
  checked: '2026-10-26'
  detail: Uscreen provides a video platform but does not publish any developer documentation or public API specifications.
  evidence:
  - status: 200
    url: https://www.uscreen.tv/developers
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Uscreen provides an all‑in‑one video membership platform that enables creators and businesses to launch paid subscriptions, host video‑on‑demand libraries, live‑stream events, and build community hubs. The service includes branded websites, OTT apps for iOS, Android, and web, analytics dashboards, and integrated marketing tools, helping creators scale their brands and monetize content directly.
image: https://www.uscreen.tv/og-images/video-membership-business-og.png
layout: provider
modified: '2026-10-26'
name: Uscreen
nav: Providers
network: true
overview: 'Uscreen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Membership, Platform, and Creators.


  The Uscreen catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uscreen''s developer surface includes getting-started guide, documentation, pricing, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Uscreen Plans Pricing
  plan_count: 4
  slug: uscreen-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 26.3
  previous_composite: 43.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/uscreen/uscreen-2026-11-03T145515.png
security:
- kind: domain-security
  name: Uscreen Domain Security
  slug: uscreen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uscreen
tags:
- Company
- Video
- Membership
- Platform
- Creators
website: https://www.uscreen.tv/
---
