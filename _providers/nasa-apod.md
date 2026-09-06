---
access_model:
  confidence: medium
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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Apod Agentic Access
  operation_count: 1
  slug: nasa-apod-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.nasa.gov
  baseurl_source: declared
  description: Astronomy Picture of the Day endpoints
  name: NASA APOD APOD API
  slug: nasa-apod-apod-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NASA Astronomy Picture of the Day () APOD API
  slug: open-nasa-apod-apod-api
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
overview: 'NASA APOD publishes 1 API on the [APIs.io](https://apis.io/) network: APOD API. Tagged areas include NASA, Astronomy, Space, Image, and Science.


  The NASA APOD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NASA APOD''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Nasa Apod Plans Pricing
  plan_count: 3
  slug: nasa-apod-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Nasa Apod Rate Limits
  slug: nasa-apod-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: NASA APOD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nasa-apod-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 75.3
    catalog_earned_first_party: 0.0
    catalog_gap: 39.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 44.7
  previous_composite: 44.7
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
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Image
- Science
- Education
- Open Data
website: https://api.nasa.gov/
---
