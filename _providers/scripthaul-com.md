---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Find YouTube videos, deliver captions, search indexed source-language passages, and monitor uploads. Free tier, no account required.
  name: ScriptHaul API
  slug: scripthaul-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/scripthaul-com/plans/scripthaul-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scripthaul-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/scripthaul-com/conformance/scripthaul-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scripthaul-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scripthaul-com/llms/scripthaul-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scripthaul-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/scripthaul-com/well-known/scripthaul-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scripthaul-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/scripthaul-com/hosts/scripthaul-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scripthaul-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/scripthaul-com/vendors/scripthaul-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scripthaul-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scripthaul-com/security/scripthaul-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scripthaul-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scripthaul.com/
- group: docs
  title: ''
  type: Documentation
  url: https://scripthaul.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://api.scripthaul.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://api.scripthaul.com/pricing
- group: operate
  title: ''
  type: Changelog
  url: https://api.scripthaul.com/docs/changelog
- group: company
  title: ''
  type: About
  url: https://scripthaul.com/about
- group: operate
  title: ''
  type: Contact
  url: https://scripthaul.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scripthaul.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scripthaul.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://scripthaul.com/mcp
  - status: null
    url: https://api.scripthaul.com/openapi.json
  - status: 401
    url: https://api.scripthaul.com/mcp
  - status: 200
    url: https://scripthaul.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: ScriptHaul provides a free bulk YouTube transcript downloader service, allowing users to paste individual video URLs, playlists, or channel links and receive captions in multiple formats such as TXT, SRT, VTT, Markdown, and JSON. The platform operates without requiring an account, offering an always‑free tier with high throughput (over 100,000 videos per day) and a simple web interface plus browser extensions for Chrome, Edge, Brave, and Arc. It includes features like language selection, timestamp options, and bulk processing, and it openly shares its privacy policy and terms of service. The service is aimed at creators, researchers, and anyone needing accessible video transcripts.
layout: provider
modified: '2026-10-30'
name: scripthaul-com
nav: Providers
network: true
overview: 'scripthaul-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: ScriptHaul API. Tagged areas include Company, YouTube, Transcripts, Free, and Bulk.


  scripthaul-com''s developer surface includes documentation, API reference, pricing, changelog, and 12 more developer resources.'
plans:
- name: Scripthaul Com Plans Pricing
  plan_count: 6
  slug: scripthaul-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Scripthaul Com Rate Limits
  slug: scripthaul-com-rate-limits
scopes:
- name: Scripthaul Com Scopes
  scope_count: 1
  slug: scripthaul-com-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 32.2
    developer_ergonomics: 8.3
    discoverability: 71.7
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/scripthaul-com/scripthaul-com-2026-11-03T142850.png
security:
- kind: authentication
  name: Scripthaul Com Authentication
  slug: scripthaul-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Scripthaul Com Domain Security
  slug: scripthaul-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: request-auth-code
  slug: scripthaul-com-request-auth-code
slug: scripthaul-com
tags:
- Company
- YouTube
- Transcripts
- Free
- Bulk
website: https://scripthaul.com/
---
