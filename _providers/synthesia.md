---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Synthesia Agentic Access
  operation_count: 28
  slug: synthesia-agentic-access
  summary_line: 28 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Assets API from Synthesia — 3 operation(s) for assets.
  name: Synthesia Assets API
  slug: synthesia-assets-api
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Dubbing API from Synthesia — 3 operation(s) for dubbing.
  name: Synthesia Dubbing API
  slug: synthesia-dubbing-api
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Templates API from Synthesia — 3 operation(s) for templates.
  name: Synthesia Templates API
  slug: synthesia-templates-api
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Translations API from Synthesia — 4 operation(s) for translations.
  name: Synthesia Translations API
  slug: synthesia-translations-api
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Videos API from Synthesia — 5 operation(s) for videos.
  name: Synthesia Videos API
  slug: synthesia-videos-api
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Webhooks API from Synthesia — 2 operation(s) for webhooks.
  name: Synthesia Webhooks API
  slug: synthesia-webhooks-api
- baseURL: https://api.synthesia.io/v2
  baseurl_source: declared
  description: The Audit Logs API from Synthesia — 3 operation(s) for audit logs.
  name: Synthesia Audit Logs API
  slug: synthesia-audit-logs-api
artifact_total: 23
collections:
- collection_type: open
  name: Synthesia Assets API
  slug: open-synthesia-assets-api
- collection_type: open
  name: Synthesia Assets AuditLogs API
  slug: open-synthesia-auditlogs-api
- collection_type: open
  name: Synthesia Assets Dubbing API
  slug: open-synthesia-dubbing-api
- collection_type: open
  name: Synthesia Assets Templates API
  slug: open-synthesia-templates-api
- collection_type: open
  name: Synthesia Assets Translations API
  slug: open-synthesia-translations-api
- collection_type: open
  name: Synthesia Assets Videos API
  slug: open-synthesia-videos-api
- collection_type: open
  name: Synthesia Assets Webhooks API
  slug: open-synthesia-webhooks-api
- collection_type: open
  name: Synthesia API
  slug: open-synthesia
common:
- group: other
  href: https://artifacts.apis.io/synthesia/capabilities/synthesia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/synthesia-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/synthesia/plans/synthesia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synthesia-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/synthesia/rate-limits/synthesia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/synthesia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/synthesia/finops/synthesia-finops.yml
  title: ''
  type: FinOps
  url: finops/synthesia-finops.yml
- group: agent
  href: https://artifacts.apis.io/synthesia/agentic-access/synthesia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/synthesia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/synthesia/security/synthesia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synthesia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/synthesia/authentication/synthesia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/synthesia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.synthesia.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synthesia.io
- group: company
  title: ''
  type: Blog
  url: https://www.synthesia.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synthesia.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synthesia.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthesia.io/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/synthesiaIO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synthesia-technologies
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.synthesia.io/changelog
created: '2026-05-23'
description: Synthesia is the leading enterprise AI video platform for creating studio-quality videos from text using lifelike AI avatars and voices. Customers use Synthesia to produce training, learning and development, customer onboarding, marketing, and internal communications videos in 140+ languages without cameras, actors, or studios. The company sells tiered SaaS plans (Basic, Starter, Creator, Enterprise) with API access starting at the Creator tier and full programmatic capabilities for enterprise customers. The Synthesia API lets teams generate, translate, and dub videos at scale and embed video generation into their own applications.
finops:
- has_sources: false
  method: generated
  name: Synthesia Finops
  primary_unit: ''
  service_category: API
  slug: synthesia-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synthesia.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.synthesia.io over HTTP.
  name: Synthesia MCP Server
  slug: synthesia
modified: '2026-05-23'
name: Synthesia
nav: Providers
network: true
overview: 'Synthesia publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Dubbing API, Templates API, and 4 more. Tagged areas include Artificial Intelligence, Generative AI, Video, Avatars, and Video Generation.


  The Synthesia catalog on APIs.io includes 1 Spectral governance ruleset.


  Synthesia''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 11 more developer resources.'
plans:
- name: Synthesia Plans Pricing
  plan_count: 1
  slug: synthesia-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Synthesia Rate Limits
  slug: synthesia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Synthesia API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 1
  slug: synthesia-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 46.6
    developer_ergonomics: 35.7
    discoverability: 68.3
    operational_transparency: 5.3
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/synthesia/synthesia-2026-06-20T194840.png
security:
- kind: authentication
  name: Synthesia Authentication
  slug: synthesia-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Synthesia Domain Security
  slug: synthesia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synthesia
tags:
- Artificial Intelligence
- Generative AI
- Video
- Avatars
- Video Generation
- Voice
- Dubbing
- Translation
- Templates
- Enterprise
- Learning
website: https://www.synthesia.io
---
