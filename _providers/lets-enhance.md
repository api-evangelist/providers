---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Lets Enhance Agentic Access
  operation_count: 20
  slug: lets-enhance-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.claid.ai/v1/
  baseurl_source: declared
  description: Encompasses operations with images.
  name: Let's Enhance Image API
  slug: lets-enhance-image-api
- baseURL: https://api.claid.ai/v1/
  baseurl_source: declared
  description: 'Perform operations with storage: check supported storage types, safely connect your cloud buckets and more.'
  name: Let's Enhance Storage API
  slug: lets-enhance-storage-api
- baseURL: https://api.claid.ai/v1/
  baseurl_source: declared
  description: Encompasses operations with videos.
  name: Let's Enhance Video API
  slug: lets-enhance-video-api
artifact_total: 13
asyncapis:
- description: ''
  name: Lets Enhance Claid Webhooks
  slug: lets-enhance-claid-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Claid REST Image API
  slug: open-lets-enhance-image-api
- collection_type: open
  name: Claid REST Image Storage API
  slug: open-lets-enhance-storage-api
- collection_type: open
  name: Claid REST Image Video API
  slug: open-lets-enhance-video-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lets-enhance-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lets-enhance-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lets-enhance-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lets-enhance-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://letsenhance.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://claid.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.claid.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.claid.ai/image-editing-api/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.claid.ai/quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.letsenhance.io/
- group: company
  title: ''
  type: Blog
  url: https://claid.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/letsenhance
- group: commercial
  title: ''
  type: Pricing
  url: https://letsenhance.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://letsenhance.io/signup
- group: start
  title: ''
  type: Login
  url: https://letsenhance.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://letsenhance.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://letsenhance.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.letsenhance.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lets-enhance-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/lets-enhance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lets-enhance-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/lets-enhance-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lets-enhance-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lets-enhance-claid-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lets-enhance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lets-enhance-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lets-enhance-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lets-enhance-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lets-enhance-claid-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Let's Enhance is an AI image enhancement company whose consumer product at letsenhance.io upscales, sharpens, denoises and restores photographs up to 512MP, and whose developer platform is shipped as Claid.ai — a REST API for AI image editing, generation and image-to-video. The Claid API exposes synchronous and asynchronous image editing pipelines, batch processing, direct upload, natural-language AI edit, AI fashion models, AI background scene generation, image generation, image-to-video, and cloud storage connectors for AWS S3, Google Cloud Storage and web folders. It is used by ecommerce, marketplace, real-estate and print-on-demand teams to automate product and listing imagery at scale. Authentication is a bearer API key with per-key permission scopes; long-running jobs are polled or delivered by HMAC-signed webhooks. Let's Enhance is a Techstars-backed company.
image: https://letsenhance.io/favicon.ico
layout: provider
modified: '2026-07-19'
name: Let's Enhance
nav: Providers
network: true
overview: 'Let''s Enhance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Image API, Storage API, and Video API. Tagged areas include Company, Artificial Intelligence, Image Processing, Image Enhancement, and Image-Generation.


  The Let''s Enhance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Let''s Enhance''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 2
  name: Lets Enhance Rate Limits
  slug: lets-enhance-rate-limits
scopes:
- name: Lets Enhance Scopes
  scope_count: 4
  slug: lets-enhance-scopes
  summary_line: 4 scopes · password
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 59.4
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lets-enhance/refs/heads/main/screenshots/lets-enhance-2026-07-25T224934.png
security:
- kind: authentication
  name: Lets Enhance Authentication
  slug: lets-enhance-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Lets Enhance Domain Security
  slug: lets-enhance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lets-enhance
tags:
- Company
- Artificial Intelligence
- Image Processing
- Image Enhancement
- Image-Generation
- Computer-Vision
- E-Commerce
- Media
- Photography
- Video Generation
website: https://letsenhance.io/
---
