---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Getty Agentic Access
  operation_count: 10
  slug: getty-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Downloads API from Getty Images — 1 operation(s) for downloads.
  name: Getty Images Downloads API
  slug: getty-downloads-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Images API from Getty Images — 2 operation(s) for images.
  name: Getty Images Images API
  slug: getty-images-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Reference API from Getty Images — 1 operation(s) for reference.
  name: Getty Images Reference API
  slug: getty-reference-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Search API from Getty Images — 4 operation(s) for search.
  name: Getty Images Search API
  slug: getty-search-api
- baseURL: https://api.gettyimages.com/v3
  baseurl_source: declared
  description: The Videos API from Getty Images — 2 operation(s) for videos.
  name: Getty Images Videos API
  slug: getty-videos-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Getty Images Downloads API
  slug: open-getty-downloads-api
- collection_type: open
  name: Getty Downloads Images API
  slug: open-getty-images-api
- collection_type: open
  name: Getty Images Downloads Reference API
  slug: open-getty-reference-api
- collection_type: open
  name: Getty Images Downloads Search API
  slug: open-getty-search-api
- collection_type: open
  name: Getty Images Downloads Videos API
  slug: open-getty-videos-api
- collection_type: open
  name: Getty Images API
  slug: open-getty
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getty-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/getty-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/getty-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/getty-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gettyimages
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getty-images
- group: company
  title: ''
  type: Website
  url: https://www.gettyimages.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gettyimages.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.gettyimages.com/swagger
- group: commercial
  title: ''
  type: Plans
  url: plans/getty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/getty-finops.yml
created: '2026-05-08'
description: Getty Images is a premium stock media licensor of editorial and creative photography, illustrations, video, and music. The Getty Images API exposes search, asset metadata, and download endpoints for licensing partners and enterprise customers. Authentication is via API key + OAuth 2.0 client credentials.
finops:
- name: Getty Finops
  service_category: Stock Media Licensing
  slug: getty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getty.png
layout: provider
modified: '2026-05-08'
name: Getty Images
nav: Providers
network: true
overview: 'Getty Images publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Downloads API, Images API, Reference API, and 2 more. Tagged areas include Stock Media, Image, Editorial, Video, and Music.


  Getty Images'' developer surface includes authentication and 12 more developer resources.'
plans:
- name: Getty Plans Pricing
  plan_count: 1
  slug: getty-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Getty Rate Limits
  slug: getty-rate-limits
scopes:
- name: Getty Scopes
  scope_count: 2
  slug: getty-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getty/refs/heads/main/screenshots/getty-2026-06-20T181814.png
security:
- kind: authentication
  name: Getty Authentication
  slug: getty-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Getty Domain Security
  slug: getty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getty Vulnerability Disclosure
  slug: getty-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: getty
tags:
- Stock Media
- Image
- Editorial
- Video
- Music
- Licensing
website: https://www.gettyimages.com/
---
