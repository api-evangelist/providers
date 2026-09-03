---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'REST/HTTP API for cloud image recognition: target management endpoints (/targets/, /target/<id>, /grade/detection/, /ping) and a recognition endpoint (/search), plus a token exchange service. Uses per'
  name: EasyAR CRS Web Service API
  slug: easyar-crs-web-service-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.easyar.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easyar-crs-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/easyar-crs-api-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/easyar-crs-api-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/easyar-crs-api-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/easyar-crs-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/easyar-crs-api-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/easyar-crs-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/easyar-crs-api-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/easyar-crs-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/easyar-crs-api-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/easyar-crs-api-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/easyar-crs-api-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/easyar-crs-api-data-model.yml
- group: operate
  title: ''
  type: Support
  url: https://www.easyar.com/view/support.html
- group: company
  title: ''
  type: Blog
  url: https://www.easyar.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EasyAR
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easyar.com/price.html
- group: start
  title: ''
  type: SignUp
  url: https://www.easyar.com/view/signup.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easyar.com/view/developerAgreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easyar.com/view/privacyPolicy.html
created: '2026-07-18'
description: EasyAR CRS (Cloud Recognition Service) is a cloud image-recognition solution that lets developers manage up to 100K image-targets online and recognize them from camera key-frames. It provides HTTP web-service APIs for target management and recognition, with request-signing/token authentication on per-instance regional base URLs.
image: https://www.easyar.com/static/image/logo.png
layout: provider
mcp_servers:
- description: ''
  name: EasyAR CRS API MCP Server
  slug: easyar-crs-api-mcp-server
modified: '2026-09-03'
name: EasyAR CRS API
nav: Providers
network: true
overview: 'EasyAR CRS API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Augmented Reality, ar-sdk, Cloud Recognition, Image Recognition, and Spatial Computing.


  EasyAR CRS API''s developer surface includes authentication, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Easyar Crs Api Plans Pricing
  plan_count: 3
  slug: easyar-crs-api-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Easyar Crs Api Rate Limits
  slug: easyar-crs-api-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 30.9
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 7.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/easyar-crs-api/refs/heads/main/screenshots/easyar-crs-api-2026-07-25T212712.png
security:
- kind: authentication
  name: Easyar Crs Api Authentication
  slug: easyar-crs-api-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Easyar Crs Api Domain Security
  slug: easyar-crs-api-domain-security
  summary_line: TLSv1.3
slug: easyar-crs-api
tags:
- Augmented Reality
- ar-sdk
- Cloud Recognition
- Image Recognition
- Spatial Computing
- Visual Positioning
- Computer-Vision
- Developer Tools
website: https://www.easyar.com
---
