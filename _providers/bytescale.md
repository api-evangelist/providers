---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 7
  human_in_the_loop: 0
  name: Bytescale Agentic Access
  operation_count: 9
  slug: bytescale-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- description: The Files API from Bytescale — 3 operation(s) for files.
  name: Bytescale Files API
  slug: bytescale-files-api
- description: The Folders API from Bytescale — 2 operation(s) for folders.
  name: Bytescale Folders API
  slug: bytescale-folders-api
- description: The Upload API from Bytescale — 3 operation(s) for upload.
  name: Bytescale Upload API
  slug: bytescale-upload-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bytescale Files API
  slug: open-bytescale-files-api
- collection_type: open
  name: Bytescale Files Folders API
  slug: open-bytescale-folders-api
- collection_type: open
  name: Bytescale Files Upload API
  slug: open-bytescale-upload-api
- collection_type: open
  name: Bytescale API
  slug: open-bytescale
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bytescale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bytescale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bytescale-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bytescale
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bytescale
- group: company
  title: ''
  type: Website
  url: https://www.bytescale.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bytescale.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/bytescale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bytescale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bytescale-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.bytescale.com/rss/
created: '2026-06-20'
description: Bytescale (formerly Upload.io) is a file upload, storage, image / video / audio processing, and CDN platform for developers. A simple REST API uploads files (binary, multipart form data, or from a URL), manages files and folders, and serves optimized media through real-time, URL-based transformations on a global CDN.
finops:
- name: Bytescale Finops
  service_category: Storage and Content Delivery
  slug: bytescale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bytescale.png
layout: provider
modified: '2026-06-20'
name: Bytescale
nav: Providers
network: true
overview: 'Bytescale publishes 3 APIs on the [APIs.io](https://apis.io/) network: Files API, Folders API, and Upload API. Tagged areas include File Upload, Storage, Image Processing, CDN, and Media.


  Bytescale''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Bytescale Plans Pricing
  plan_count: 6
  slug: bytescale-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Bytescale Rate Limits
  slug: bytescale-rate-limits
score:
  band: developing
  composite: 39.3
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
    contract_quality: 51.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bytescale/refs/heads/main/screenshots/bytescale-2026-06-20T173832.png
security:
- kind: authentication
  name: Bytescale Authentication
  slug: bytescale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bytescale Domain Security
  slug: bytescale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bytescale
tags:
- File Upload
- Storage
- Image Processing
- CDN
- Media
website: https://www.bytescale.com
---
