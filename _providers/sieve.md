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
  - '{''url'': ''https://www.sievedata.com'', ''status'': 308, ''note'': ''declared website redirects to https://www.sieve.ai/ — a different registrable domain (sievedata.com -> sieve.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sieve Agentic Access
  operation_count: 5
  slug: sieve-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://mango.sievedata.com/v2
  baseurl_source: declared
  description: Look up metadata for public and custom functions.
  name: Sieve Functions API
  slug: sieve-functions-api
- baseURL: https://mango.sievedata.com/v2
  baseurl_source: declared
  description: Push, retrieve, list, and cancel asynchronous function jobs.
  name: Sieve Jobs API
  slug: sieve-jobs-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sieve Functions API
  slug: open-sieve-functions-api
- collection_type: open
  name: Sieve Functions Jobs API
  slug: open-sieve-jobs-api
- collection_type: open
  name: Sieve API
  slug: open-sieve
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sieve/refs/heads/main/agentic-access/sieve-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sieve-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sieve/refs/heads/main/security/sieve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sieve-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sieve/refs/heads/main/authentication/sieve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sieve-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sieve-community
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sievedata
- group: company
  title: ''
  type: Website
  url: https://www.sievedata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sievedata.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sieve/refs/heads/main/plans/sieve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sieve-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sieve/refs/heads/main/rate-limits/sieve-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sieve-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sieve/refs/heads/main/finops/sieve-finops.yml
  title: ''
  type: FinOps
  url: finops/sieve-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sieve.ai/blog
created: '2026-06-20'
description: Sieve is an AI media-processing platform that exposes prebuilt functions and apps for video, audio, and image understanding - transcription, dubbing, lip-sync, object tracking and segmentation, background removal, and more. Functions are run asynchronously as jobs via a single REST push endpoint, with results retrieved by polling or delivered via webhooks.
finops:
- has_sources: true
  method: generated
  name: Sieve Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: sieve-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sieve.png
layout: provider
modified: '2026-06-20'
name: Sieve
nav: Providers
network: true
overview: 'Sieve publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Functions API and Jobs API. Tagged areas include Artificial Intelligence, Video, Audio, Media Processing, and AsyncJobs.


  Sieve''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sieve Plans Pricing
  plan_count: 3
  slug: sieve-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Sieve Rate Limits
  slug: sieve-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 49.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Sieve Authentication
  slug: sieve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sieve Domain Security
  slug: sieve-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sieve
tags:
- Artificial Intelligence
- Video
- Audio
- Media Processing
- AsyncJobs
website: https://www.sievedata.com
---
