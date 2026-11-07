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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Ad Radar services.
  name: Ad Radar API
  slug: ad-radar-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ad-radar-dev/llms/ad-radar-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ad-radar-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/ad-radar-dev/well-known/ad-radar-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ad-radar-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/ad-radar-dev/hosts/ad-radar-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ad-radar-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ad-radar-dev/vendors/ad-radar-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ad-radar-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ad-radar-dev/security/ad-radar-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ad-radar-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ad-radar.dev/
- group: company
  title: ''
  type: Blog
  url: https://ad-radar.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ad-radar.dev/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ad-radar.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ad-radar.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://ad-radar.dev/support
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract found despite accessible documentation.
  evidence:
  - status: 200
    url: https://ad-radar.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Ad Radar provides a tool to discover winning Facebook ads quickly. It tracks Meta ads for hundreds of brands, estimates spend, flags scaling ads, and breaks down creative hooks. Users can explore ad performance, filter by niche, and integrate with Claude via an MCP server for AI‑assisted research.
image: https://ad-radar.dev/assets/og.png
layout: provider
modified: '2026-10-31'
name: Ad Radar
nav: Providers
network: true
overview: 'Ad Radar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketing, Artificial Intelligence, Competitive Intelligence, and Social Media.


  Ad Radar''s developer surface includes engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 13.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ad Radar Dev Domain Security
  slug: ad-radar-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ad-radar-dev
tags:
- Advertising
- Marketing
- Artificial Intelligence
- Competitive Intelligence
- Social Media
website: https://ad-radar.dev/
---
