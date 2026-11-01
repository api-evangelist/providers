---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/storycut-com/plans/storycut-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/storycut-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/storycut-com/llms/storycut-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/storycut-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/storycut-com/well-known/storycut-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/storycut-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/storycut-com/hosts/storycut-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/storycut-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/storycut-com/vendors/storycut-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/storycut-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storycut.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storycut.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.storycut.com/blog
- group: auth
  href: https://artifacts.apis.io/storycut-com/security/storycut-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/storycut-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.storycut.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.storycut.com/features
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storycut.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.storycut.com
- group: start
  title: ''
  type: SignUp
  url: https://app.storycut.com/register
coverage:
  checked: '2026-10-29'
  detail: No machine‑readable API specification (OpenAPI, GraphQL SDL, AsyncAPI, etc.) is publicly available; attempts to fetch common spec URLs on the API host returned no content.
  evidence:
  - status: 0
    url: https://api.storycut.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: StoryCut provides an AI-powered platform that automatically creates short, viral‑ready videos for TikTok, Reels, Shorts and other social channels. Users upload long‑form video content and the service extracts key moments, adds dynamic captions, auto‑reframes, and applies transitions, all within seconds. The platform offers multiple caption styles, AI‑generated B‑Roll, and tools for branding, targeting creators, businesses and marketers looking to boost engagement across short‑form video platforms.
image: https://www.storycut.com/assets/og-image.png
layout: provider
modified: '2026-10-28'
name: StoryCut
nav: Providers
network: true
overview: 'StoryCut is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Video, SocialMedia, and Automation.


  StoryCut''s developer surface includes engineering blog, documentation, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Storycut Com Plans Pricing
  plan_count: 4
  slug: storycut-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Storycut Com Domain Security
  slug: storycut-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storycut-com
tags:
- Company
- AI
- Video
- SocialMedia
- Automation
website: https://www.storycut.com
---
