---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pixelixe Agentic Access
  operation_count: 4
  slug: pixelixe-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://studio.pixelixe.com/api
  baseurl_source: declared
  description: The Authentication API from Pixelixe — 1 operation(s) for authentication.
  name: Pixelixe Authentication API
  slug: pixelixe-authentication-api
- baseURL: https://studio.pixelixe.com/api
  baseurl_source: declared
  description: The Document API from Pixelixe — 2 operation(s) for document.
  name: Pixelixe Document API
  slug: pixelixe-document-api
- baseURL: https://studio.pixelixe.com/api
  baseurl_source: declared
  description: The Graphic API from Pixelixe — 1 operation(s) for graphic.
  name: Pixelixe Graphic API
  slug: pixelixe-graphic-api
artifact_total: 14
collections:
- collection_type: open
  name: Pixelixe Authentication API
  slug: open-pixelixe-authentication-api
- collection_type: open
  name: Pixelixe Authentication Document API
  slug: open-pixelixe-document-api
- collection_type: open
  name: Pixelixe Authentication Graphic API
  slug: open-pixelixe-graphic-api
- collection_type: open
  name: Pixelixe
  slug: open-pixelixe
common:
- group: commercial
  href: https://artifacts.apis.io/pixelixe/plans/pixelixe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pixelixe-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/pixelixe/rate-limits/pixelixe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pixelixe-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pixelixe/finops/pixelixe-finops.yml
  title: ''
  type: FinOps
  url: finops/pixelixe-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.pixelixe.com/
- group: agent
  href: https://artifacts.apis.io/pixelixe/agentic-access/pixelixe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pixelixe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/pixelixe/security/pixelixe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixelixe-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/pixelixe/authentication/pixelixe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pixelixe-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixelixe
- group: agent
  title: ''
  type: LlmsText
  url: https://pixelixe.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://pixelixe.com/blog
created: '2024-11-13'
description: Pixelixe is a comprehensive online design tool that allows users to create professional-quality graphics quickly and easily. With a user-friendly interface and a wide range of templates, images, and fonts to choose from, Pixelixe is perfect for individuals and businesses looking to enhance their online presence. Whether you need to design social media graphics, blog images, or marketing materials, Pixelixe offers the tools and resources needed to bring your vision to life.
finops:
- has_sources: false
  method: generated
  name: Pixelixe Finops
  primary_unit: request
  service_category: API
  slug: pixelixe-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixelixe.png
layout: provider
modified: '2026-05-19'
name: Pixelixe
nav: Providers
network: true
overview: 'Pixelixe publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Authentication API, Document API, and Graphic API. Tagged areas include Graphics and Image.


  The Pixelixe catalog on APIs.io includes 1 Spectral governance ruleset.


  Pixelixe''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Pixelixe Plans Pricing
  plan_count: 3
  slug: pixelixe-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Pixelixe Rate Limits
  slug: pixelixe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Pixelixe API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: pixelixe-rules
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.9
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 26.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
screenshot: https://apis.io/screenshots/pixelixe/pixelixe-2026-06-20T191739.png
security:
- kind: authentication
  name: Pixelixe Authentication
  slug: pixelixe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pixelixe Domain Security
  slug: pixelixe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pixelixe
tags:
- Graphics
- Image
website: https://www.pixelixe.com/
---
