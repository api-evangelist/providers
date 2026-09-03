---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Shotstack Agentic Access
  operation_count: 20
  slug: shotstack-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.shotstack.io/edit/v1
  baseurl_source: declared
  description: Generate AI assets such as text-to-speech and text-to-image.
  name: Shotstack Create API
  slug: shotstack-create-api
- baseURL: https://api.shotstack.io/edit/v1
  baseurl_source: declared
  description: Render videos, images, and audio from a JSON edit specification.
  name: Shotstack Edit API
  slug: shotstack-edit-api
- baseURL: https://api.shotstack.io/edit/v1
  baseurl_source: declared
  description: Upload, store, and transform source assets.
  name: Shotstack Ingest API
  slug: shotstack-ingest-api
- baseURL: https://api.shotstack.io/edit/v1
  baseurl_source: declared
  description: Inspect, manage, and deliver hosted assets.
  name: Shotstack Serve API
  slug: shotstack-serve-api
- baseURL: https://api.shotstack.io/edit/v1
  baseurl_source: declared
  description: Manage and render reusable edit templates with merge fields.
  name: Shotstack Templates API
  slug: shotstack-templates-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shotstack Create API
  slug: open-shotstack-create-api
- collection_type: open
  name: Shotstack Create Edit API
  slug: open-shotstack-edit-api
- collection_type: open
  name: Shotstack Create Ingest API
  slug: open-shotstack-ingest-api
- collection_type: open
  name: Shotstack Create Serve API
  slug: open-shotstack-serve-api
- collection_type: open
  name: Shotstack Create Templates API
  slug: open-shotstack-templates-api
- collection_type: open
  name: Shotstack API
  slug: open-shotstack
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shotstack-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shotstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shotstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shotstack-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shotstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shotstack
- group: company
  title: ''
  type: Website
  url: https://shotstack.io
- group: docs
  title: ''
  type: Documentation
  url: https://shotstack.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/shotstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shotstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shotstack-finops.yml
created: '2026-06-20'
description: Shotstack is a cloud video-editing platform that turns a JSON timeline into a rendered video, image, or audio file. The Edit API renders programmatically from a JSON edit specification and templates, the Ingest API uploads and transforms source footage, the Serve API hosts and delivers generated assets, and the Create API generates AI assets such as text-to-speech, text-to-image, and image-to-video.
finops:
- name: Shotstack Finops
  service_category: Media and Content
  slug: shotstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shotstack.png
layout: provider
modified: '2026-06-20'
name: Shotstack
nav: Providers
network: true
overview: 'Shotstack publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Create API, Edit API, Ingest API, and 2 more. Tagged areas include Video, Video Editing, Media, Rendering, and Generative AI.


  Shotstack''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Shotstack Plans Pricing
  plan_count: 4
  slug: shotstack-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Shotstack Rate Limits
  slug: shotstack-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shotstack/refs/heads/main/screenshots/shotstack-2026-06-20T193841.png
security:
- kind: authentication
  name: Shotstack Authentication
  slug: shotstack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shotstack Domain Security
  slug: shotstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shotstack
tags:
- Video
- Video Editing
- Media
- Rendering
- Generative AI
website: https://shotstack.io
---
