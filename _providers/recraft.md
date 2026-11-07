---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Recraft Agentic Access
  operation_count: 19
  slug: recraft-agentic-access
  summary_line: 19 operations · 18 acting
api_count: 1
apis:
- description: REST API for raster and vector image generation (V4 Pro / V4 / V3 / V2), inpainting, image-to-image, background replacement, style creation, vectorization, upscaling (Crisp / Creative), background rem
  name: Recraft API
  slug: platform
- baseURL: https://external.api.recraft.ai/v1
  baseurl_source: declared
  description: The Images API from Recraft — 16 operation(s) for images.
  name: Recraft Images API
  slug: recraft-images-api
- baseURL: https://external.api.recraft.ai/v1
  baseurl_source: declared
  description: The Prompts API from Recraft — 1 operation(s) for prompts.
  name: Recraft Prompts API
  slug: recraft-prompts-api
- baseURL: https://external.api.recraft.ai/v1
  baseurl_source: declared
  description: The Styles API from Recraft — 1 operation(s) for styles.
  name: Recraft Styles API
  slug: recraft-styles-api
- baseURL: https://external.api.recraft.ai/v1
  baseurl_source: declared
  description: The Users API from Recraft — 1 operation(s) for users.
  name: Recraft Users API
  slug: recraft-users-api
artifact_total: 20
collections:
- collection_type: open
  name: Recraft Images API
  slug: open-recraft-images-api
- collection_type: open
  name: Recraft Images Prompts API
  slug: open-recraft-prompts-api
- collection_type: open
  name: Recraft Images Styles API
  slug: open-recraft-styles-api
- collection_type: open
  name: Recraft Images Users API
  slug: open-recraft-users-api
- collection_type: open
  name: Recraft API
  slug: open-recraft
common:
- group: agent
  href: https://artifacts.apis.io/recraft/agentic-access/recraft-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recraft-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/recraft/security/recraft-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/recraft-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/recraft/security/recraft-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/recraft-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/recraft/security/recraft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recraft-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/recraft/authentication/recraft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recraft-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recraft-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recraftai
- group: company
  title: ''
  type: Website
  url: https://www.recraft.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.recraft.ai/docs/
- group: commercial
  href: https://artifacts.apis.io/recraft/plans/recraft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/recraft-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/recraft/rate-limits/recraft-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/recraft-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/recraft/finops/recraft-finops.yml
  title: ''
  type: FinOps
  url: finops/recraft-finops.yml
- group: other
  href: https://artifacts.apis.io/recraft/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-05-08'
description: Recraft is an AI design platform offering raster and vector image generation, image editing, inpainting, background removal/generation, vectorization, upscaling, and style creation. The Recraft API is REST-based at https://external.api.recraft.ai/v1, compatible with the OpenAI Python client, and uses prepaid API Units billed at 1,000 units = $1.
finops:
- has_sources: true
  method: generated
  name: Recraft Finops
  primary_unit: ''
  service_category: AI
  slug: recraft-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recraft.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.recraft.ai over HTTP.
  name: Recraft MCP Server
  slug: recraft
modified: '2026-05-30'
name: Recraft
nav: Providers
network: true
overview: 'Recraft publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Images API, Prompts API, and 3 more. Tagged areas include Artificial Intelligence, Image Generation, Design, Vectors, and Styles.


  The Recraft catalog on APIs.io includes 1 Spectral governance ruleset.


  Recraft''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Recraft Plans Pricing
  plan_count: 1
  slug: recraft-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Recraft Rate Limits
  slug: recraft-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Recraft API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: recraft-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 39.8
    developer_ergonomics: 21.4
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/recraft/recraft-2026-06-20T192705.png
security:
- kind: authentication
  name: Recraft Authentication
  slug: recraft-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Recraft Domain Security
  slug: recraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Recraft Vulnerability Disclosure
  slug: recraft-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Recraft Trust Center
  slug: recraft-trust-center
  summary_line: SOC 2, GDPR
slug: recraft
tags:
- Artificial Intelligence
- Image Generation
- Design
- Vectors
- Styles
website: https://www.recraft.ai/
---
