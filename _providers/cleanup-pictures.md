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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cleanup Pictures Agentic Access
  operation_count: 1
  slug: cleanup-pictures-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: REST API for object/watermark/blemish removal via mask-based inpainting. POST multipart/form-data with image_file, mask_file, and optional mode (fast/quality) to https://clipdrop-api.co/cleanup/v1. De
  name: Cleanup.pictures Inpainting API
  slug: cleanup
- description: The Cleanup API from Cleanup.pictures — 1 operation(s) for cleanup.
  name: Cleanup.pictures Cleanup API
  slug: cleanup-pictures-cleanup-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: .pictures API (ClipDrop) Cleanup API
  slug: open-cleanup-pictures-cleanup-api
- collection_type: open
  name: Cleanup.pictures API (ClipDrop)
  slug: open-cleanup-pictures
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cleanup-pictures-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleanup-pictures-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cleanup-pictures-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/initml
- group: company
  title: ''
  type: Website
  url: https://cleanup.pictures/
- group: docs
  title: ''
  type: Documentation
  url: https://clipdrop.co/apis/docs/cleanup
- group: commercial
  title: ''
  type: Plans
  url: plans/cleanup-pictures-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cleanup-pictures-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cleanup-pictures-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://cleanup.pictures/llms.txt
created: '2026-05-08'
description: Cleanup.pictures provides AI-powered photo cleanup, object and watermark removal via inpainting. The public API is hosted on the ClipDrop platform (now Jasper.ai) at https://clipdrop-api.co/cleanup/v1, billed at 1 credit per successful call.
finops:
- name: Cleanup Pictures Finops
  service_category: AI
  slug: cleanup-pictures-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleanup-pictures.png
layout: provider
modified: '2026-05-08'
name: Cleanup.pictures
nav: Providers
network: true
overview: 'Cleanup.pictures publishes 1 API on the [APIs.io](https://apis.io/) network: Cleanup API. Tagged areas include Artificial Intelligence, Image Editing, Object Removal, Inpainting, and Visual.


  Cleanup.pictures'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Cleanup Pictures Plans Pricing
  plan_count: 3
  slug: cleanup-pictures-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Cleanup Pictures Rate Limits
  slug: cleanup-pictures-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cleanup-pictures/refs/heads/main/screenshots/cleanup-pictures-2026-06-20T174452.png
security:
- kind: authentication
  name: Cleanup Pictures Authentication
  slug: cleanup-pictures-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cleanup Pictures Domain Security
  slug: cleanup-pictures-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cleanup-pictures
tags:
- Artificial Intelligence
- Image Editing
- Object Removal
- Inpainting
- Visual
website: https://cleanup.pictures/
---
