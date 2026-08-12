---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Apod Agentic Access
  operation_count: 1
  slug: nasa-apod-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Astronomy Picture of the Day endpoints
  name: NASA APOD APOD API
  slug: nasa-apod-apod-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-apod-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-apod-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasa-apod-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://api.nasa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/nasa/apod-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nasa
- group: company
  title: ''
  type: Blog
  url: https://apod.nasa.gov/apod/
- group: commercial
  title: ''
  type: Pricing
  url: https://api.nasa.gov/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.nasa.gov/
- group: other
  title: ''
  type: X
  url: https://x.com/apod
- group: commercial
  title: ''
  type: Plans
  url: plans/nasa-apod-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasa-apod-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nasa-apod-finops.yml
created: '2026-06-13'
description: NASA Astronomy Picture of the Day (APOD) REST API providing daily astronomy images and explanations curated by NASA scientists. Supports retrieval by specific date, date ranges, and random selection, with high-definition image URLs, media type detection, and optional concept tags derived from image metadata. Data is available from 1995-06-16 onward.
examples:
- key_count: 9
  name: Apod Single Date
  slug: apod-single-date
finops:
- name: Nasa Apod Finops
  service_category: ''
  slug: nasa-apod-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-apod.png
json_schemas:
- name: APOD Entry
  property_count: 12
  slug: apod-entry
- name: APOD Request Parameters
  property_count: 8
  slug: apod-request
jsonld:
- class_count: 0
  name: Nasa Apod Context
  property_count: 13
  slug: nasa-apod-context
layout: provider
modified: '2026-06-13'
name: NASA APOD
nav: Providers
network: true
overview: 'NASA APOD publishes 1 API on the [APIs.io](https://apis.io/) network: APOD API. Tagged areas include NASA, Astronomy, Space, Images, and Science.


  The NASA APOD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NASA APOD''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Nasa Apod Plans Pricing
  plan_count: 3
  slug: nasa-apod-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 3
  name: Nasa Apod Rate Limits
  slug: nasa-apod-rate-limits
rules:
- name: NASA APOD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nasa-apod-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  delta: -0.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa-apod/refs/heads/main/screenshots/nasa-apod-2026-06-20T185946.png
security:
- kind: authentication
  name: Nasa Apod Authentication
  slug: nasa-apod-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nasa Apod Domain Security
  slug: nasa-apod-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nasa-apod
tags:
- NASA
- Astronomy
- Space
- Images
- Science
- Education
- Open Data
website: https://api.nasa.gov/
---
