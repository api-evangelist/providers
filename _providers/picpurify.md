---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Picpurify Agentic Access
  operation_count: 2
  slug: picpurify-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: Submit an image (file upload or URL) for one or more moderation/detection tasks.
  name: PicPurify Image Analysis API
  slug: picpurify-image-analysis-api
- description: Submit a video (file upload or URL) for moderation/detection tasks frame by frame.
  name: PicPurify Video Analysis API
  slug: picpurify-video-analysis-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PicPurify Image and Video Moderation Image Analysis API
  slug: open-picpurify-image-analysis-api
- collection_type: open
  name: PicPurify Image and Video Moderation Image Analysis Video Analysis API
  slug: open-picpurify-video-analysis-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/picpurify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/picpurify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.picpurify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.picpurify.com/api-services.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.picpurify.com/buying.html
- group: start
  title: ''
  type: Signup
  url: https://www.picpurify.com/inscription.html
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Picpurify
created: '2025-02-17'
description: PicPurify provides image and video moderation services including gun and knife weapon detection, nudity, drug, gore, hate sign, age, gender, and other content moderation tasks. Pictures showing someone posing with a firearm or holding a knife can offend visitors, shock young minds and displease advertisers - PicPurify detects these images so they can be filtered before publication.
finops:
- name: Picpurify Finops
  service_category: API
  slug: picpurify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/picpurify.png
layout: provider
modified: '2026-05-19'
name: PicPurify
nav: Providers
network: true
overview: 'PicPurify publishes 2 APIs on the [APIs.io](https://apis.io/) network: Image Analysis API and Video Analysis API. Tagged areas include Image Moderation, Content Moderation, Computer-Vision, and Weapon Detection.


  PicPurify''s developer surface includes documentation, pricing, signup flow, and 4 more developer resources.'
plans:
- name: Picpurify Plans Pricing
  plan_count: 3
  slug: picpurify-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Picpurify Rate Limits
  slug: picpurify-rate-limits
score:
  band: thin
  composite: 27.5
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/picpurify/refs/heads/main/screenshots/picpurify-2026-06-20T191702.png
security:
- kind: domain-security
  name: Picpurify Domain Security
  slug: picpurify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: picpurify
tags:
- Image Moderation
- Content Moderation
- Computer-Vision
- Weapon Detection
website: https://www.picpurify.com/
---
