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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pika Labs Agentic Access
  operation_count: 5
  slug: pika-labs-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: Pika's video generation models are exposed through the fal.ai inference platform. Use fal.ai's standard REST submission + polling API to access Pika models.
  name: Pika via fal.ai
  slug: fal
- baseURL: https://queue.fal.run
  baseurl_source: declared
  description: Cancel an in-flight request.
  name: Pika Labs Cancel API
  slug: pika-labs-cancel-api
- baseURL: https://queue.fal.run
  baseurl_source: declared
  description: Retrieve the result of a completed request.
  name: Pika Labs Result API
  slug: pika-labs-result-api
- baseURL: https://queue.fal.run
  baseurl_source: declared
  description: Inspect request status.
  name: Pika Labs Status API
  slug: pika-labs-status-api
- baseURL: https://queue.fal.run
  baseurl_source: declared
  description: Submit inference requests.
  name: Pika Labs Submission API
  slug: pika-labs-submission-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel API
  slug: open-pika-labs-cancel-api
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel Result API
  slug: open-pika-labs-result-api
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel Status API
  slug: open-pika-labs-status-api
- collection_type: open
  name: Pika Labs via fal.ai Queue Cancel Submission API
  slug: open-pika-labs-submission-api
- collection_type: open
  name: Pika Labs via fal.ai Queue API
  slug: open-pika-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pika-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pika-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pika-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pika-Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pika-labs
- group: company
  title: ''
  type: Website
  url: https://pika.art/
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/models?keywords=pika
- group: commercial
  title: ''
  type: Plans
  url: plans/pika-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pika-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pika-labs-finops.yml
created: '2026-05-08'
description: Pika Labs is an AI video generation platform offering text-to-video, image-to-video, and video editing capabilities. As of May 2026 Pika does not publish a first-party REST API on its main domain; production API access is provided through partner aggregators (notably fal.ai) which host hosted endpoints for Pika models.
finops:
- name: Pika Labs Finops
  service_category: AI
  slug: pika-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pika-labs.png
layout: provider
modified: '2026-05-08'
name: Pika Labs
nav: Providers
network: true
overview: 'Pika Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cancel API, Result API, Status API, and 1 more. Tagged areas include Artificial Intelligence, Video Generation, Text-to-Video, Multi-Modal, and Generative.


  Pika Labs'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Pika Labs Plans Pricing
  plan_count: 2
  slug: pika-labs-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Pika Labs Rate Limits
  slug: pika-labs-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 53.4
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pika-labs/refs/heads/main/screenshots/pika-labs-2026-06-20T191707.png
security:
- kind: authentication
  name: Pika Labs Authentication
  slug: pika-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pika Labs Domain Security
  slug: pika-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pika-labs
tags:
- Artificial Intelligence
- Video Generation
- Text-to-Video
- Multi-Modal
- Generative
website: https://pika.art/
---
