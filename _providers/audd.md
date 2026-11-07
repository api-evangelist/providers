---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Audd Agentic Access
  operation_count: 11
  slug: audd-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.audd.io
  baseurl_source: declared
  description: Music recognition from a short clip, file or URL (api.audd.io), and the enterprise endpoint for audio and video files of any length (enterprise.audd.io).
  name: AudD Recognition API
  slug: audd-recognition-api
- baseURL: https://api.audd.io
  baseurl_source: declared
  description: Add your own tracks to a custom recognition catalog (special access).
  name: AudD Custom Catalog API
  slug: audd-custom-catalog-api
- baseURL: https://api.audd.io
  baseurl_source: declared
  description: Live audio stream monitoring - add and manage streams, with recognition results delivered by callback URL or longpoll.
  name: AudD Streams API
  slug: audd-streams-api
- baseURL: https://api.audd.io
  baseurl_source: declared
  description: The Agent payments API from AudD — 3 operation(s) for agent payments.
  name: AudD Agent payments API
  slug: audd-agent-payments-api
artifact_total: 15
collections:
- collection_type: open
  name: AudD Music Recognition Custom catalog API
  slug: open-audd-custom-catalog-api
- collection_type: open
  name: AudD Music Recognition API
  slug: open-audd-recognition-api
- collection_type: open
  name: AudD Music Recognition Streams API
  slug: open-audd-streams-api
common:
- group: other
  href: https://artifacts.apis.io/audd/capabilities/audd-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/audd-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/audd/agentic-access/audd-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audd-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/audd/security/audd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audd-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/audd/authentication/audd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audd-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AudDMusic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audd-io
- group: company
  title: ''
  type: Website
  url: https://audd.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.audd.io/
- group: agent
  href: https://artifacts.apis.io/audd/well-known/audd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audd-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://audd.io/.well-known/api-catalog
- group: commercial
  href: https://artifacts.apis.io/audd/plans/audd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/audd-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/audd/rate-limits/audd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/audd-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/audd/finops/audd-finops.yml
  title: ''
  type: FinOps
  url: finops/audd-finops.yml
created: '2026-06-21'
description: AudD is a music recognition service. Its REST API identifies songs from short audio clips, uploaded files or URLs on api.audd.io, scans audio and video files of any length on the enterprise endpoint (enterprise.audd.io), monitors live audio streams with results delivered by callback or longpoll, and adds an account's own tracks to a custom catalog (special access). Matches return track metadata (artist, title, album, ISRC) with optional Apple Music, Spotify, Deezer and MusicBrainz data.
finops:
- has_sources: true
  method: generated
  name: Audd Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: audd-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/audd.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.audd.io over HTTP.
  name: AudD MCP Server
  slug: audd
modified: '2026-10-08'
name: AudD
nav: Providers
network: true
overview: 'AudD publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Recognition API, Custom Catalog API, Streams API, and 1 more. Tagged areas include Music, Music Recognition, Audio, and Fingerprinting.


  The AudD catalog on APIs.io includes 1 Spectral governance ruleset.


  AudD''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Audd Plans Pricing
  plan_count: 4
  slug: audd-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Audd Rate Limits
  slug: audd-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: AudD API Rules
  rule_count: 60
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 3
  slug: audd-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 53.0
    developer_ergonomics: 26.2
    discoverability: 70.0
    operational_transparency: 10.5
  previous_composite: 28.2
  provenance:
    agentic_access: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/audd/audd-2026-07-25T201708.png
security:
- kind: authentication
  name: Audd Authentication
  slug: audd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Audd Domain Security
  slug: audd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: audd
tags:
- Music
- Music Recognition
- Audio
- Fingerprinting
website: https://audd.io/
---
