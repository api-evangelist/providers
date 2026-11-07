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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Radio Co Agentic Access
  operation_count: 3
  slug: radio-co-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://public.radio.co
  baseurl_source: declared
  description: Station status and metadata endpoints
  name: Radio.co Station API
  slug: radio-co-station-api
- baseURL: https://public.radio.co
  baseurl_source: declared
  description: Currently playing track information
  name: Radio.co Track API
  slug: radio-co-track-api
artifact_total: 11
collections:
- collection_type: open
  name: Radio.co Public Station API
  slug: open-radio-co-station-api
- collection_type: open
  name: Radio.co Public Station Track API
  slug: open-radio-co-track-api
- collection_type: open
  name: Radio.co Public API
  slug: open-radio-co
common:
- group: commercial
  href: https://artifacts.apis.io/radio-co/plans/radio-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/radio-co-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/radio-co/rate-limits/radio-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/radio-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/radio-co/finops/radio-co-finops.yml
  title: ''
  type: FinOps
  url: finops/radio-co-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.radio.co/
- group: agent
  href: https://artifacts.apis.io/radio-co/agentic-access/radio-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/radio-co-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/radio-co/security/radio-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/radio-co-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radiodotco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radio-co
- group: agent
  title: ''
  type: LlmsText
  url: https://www.radio.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.radio.co/blog
created: '2025-02-12'
description: Your toolset for creating bespoke players. Showcase your station to fit your website, apps, and beyond.
finops:
- has_sources: false
  method: generated
  name: Radio Co Finops
  primary_unit: request
  service_category: API
  slug: radio-co-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radio-co.png
layout: provider
modified: '2026-05-19'
name: Radio.co
nav: Providers
network: true
overview: 'Radio.co publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Station API and Track API. Tagged areas include Radio, Streaming, Audio, and Music.


  The Radio.co catalog on APIs.io includes 1 Spectral governance ruleset.


  Radio.co''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Radio Co Plans Pricing
  plan_count: 3
  slug: radio-co-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Radio Co Rate Limits
  slug: radio-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Radio.co API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: radio-co-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.5
    catalog_earned_first_party: 0.0
    catalog_gap: 77.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 43.5
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 22.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/radio-co/radio-co-2026-06-20T192532.png
security:
- kind: domain-security
  name: Radio Co Domain Security
  slug: radio-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: radio-co
tags:
- Radio
- Streaming
- Audio
- Music
website: https://www.radio.co/
---
