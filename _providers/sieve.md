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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-05'
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
  title: ''
  type: AgenticAccess
  url: agentic-access/sieve-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sieve-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/sieve-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sieve-rate-limits.yml
- group: commercial
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
- name: Sieve Finops
  service_category: AI and Machine Learning
  slug: sieve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sieve.png
layout: provider
modified: '2026-06-20'
name: Sieve
nav: Providers
network: true
overview: 'Sieve publishes 2 APIs on the [APIs.io](https://apis.io/) network: Functions API and Jobs API. Tagged areas include Artificial Intelligence, Video, Audio, Media Processing, and AsyncJobs.


  Sieve''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sieve Plans Pricing
  plan_count: 3
  slug: sieve-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Sieve Rate Limits
  slug: sieve-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
