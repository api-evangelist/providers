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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DigitalAPI is an API catalog, marketplace, and management platform that unifies APIs across multiple gateways into a single searchable catalog with governance, discovery, access control, and analytics
  name: DigitalAPI
  slug: digitalapi
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/digitalapi/plans/digitalapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitalapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/digitalapi/rate-limits/digitalapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digitalapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digitalapi/finops/digitalapi-finops.yml
  title: ''
  type: FinOps
  url: finops/digitalapi-finops.yml
- group: auth
  href: https://artifacts.apis.io/digitalapi/security/digitalapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalapi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digitalapicraft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digitalapi
- group: company
  title: ''
  type: Website
  url: https://www.digitalapi.ai
- group: company
  title: ''
  type: Blog
  url: https://www.digitalapi.ai/blogs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalapi.ai/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.digitalapi.ai/llms.txt
created: '2026-03-26'
description: DigitalAPI is an API catalog, marketplace, and management platform that unifies APIs across multiple gateways into a single searchable catalog with governance, discovery, access control, and analytics.
finops:
- has_sources: false
  method: generated
  name: Digitalapi Finops
  primary_unit: request
  service_category: API
  slug: digitalapi-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digitalapi.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.digitalapi.ai over HTTP; 4 tools listed.
  name: DigitalAPI MCP Server
  slug: digitalapi
modified: '2026-08-18'
name: DigitalAPI
nav: Providers
network: true
overview: 'DigitalAPI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Aggregation, API Catalog, and API Marketplace.


  DigitalAPI''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Digitalapi Plans Pricing
  plan_count: 3
  slug: digitalapi-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Digitalapi Rate Limits
  slug: digitalapi-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.3
    operational_transparency: 10.5
  previous_composite: 9.8
  provenance:
    mcp: first-party
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/digitalapi/digitalapi-2026-06-20T180026.png
security:
- kind: domain-security
  name: Digitalapi Domain Security
  slug: digitalapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digitalapi
tags:
- API Aggregation
- API Catalog
- API Marketplace
website: https://www.digitalapi.ai
---
