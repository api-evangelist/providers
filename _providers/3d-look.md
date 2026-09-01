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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST API to create a person, upload front and side photos, and asynchronously retrieve 80+ calculated body measurements for made-to-measure apparel, uniforms, and size recommendation.
  name: SAIA Perfect Fit / Mobile Tailor (MTM) API
  slug: saia-perfect-fit-mobile-tailor-mtm-api
- description: REST API for body composition and health/fitness insights - body measurements, weight prediction, BMI/body-fat/BMR, 3D model prediction, and 2D/3D body-progress comparison, with subscription usage tra
  name: FitXpress API
  slug: fitxpress-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://3dlook.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://saia.3dlook.me/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://saia.3dlook.me/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://saia.3dlook.me/docs/perfectfit.html
- group: commercial
  title: ''
  type: Pricing
  url: https://3dlook.ai/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dlook.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dlook.ai/terms-and-policies/
- group: operate
  title: ''
  type: Support
  url: https://3dlook.ai/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/3dlook-me
- group: auth
  title: ''
  type: Authentication
  url: authentication/3d-look-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/3d-look-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/3d-look-packages.yml
- group: design
  title: ''
  type: Components
  url: components/3d-look-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/3d-look-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/3d-look-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/3d-look-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3d-look-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3d-look-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3d-look-llms.txt
created: '2026-07-17'
description: '3DLOOK is an AI-powered body measurement and mobile body-scanning company whose computer-vision technology extracts 80+ accurate body measurements and 3D body models from just two smartphone photos. It offers two developer products: SAIA Perfect Fit / Mobile Tailor (a made-to-measure and size-recommendation API for apparel, uniforms, and on-demand manufacturing) and FitXpress (a body-composition and health/fitness insights API delivering weight prediction, BMI, body-fat, BMR, and 2D/3D body-progress visualization). Both expose REST APIs with API-key authentication, a JavaScript SDK, native iOS and Android capture SDKs, and embeddable photo-capture and measurement widgets.'
image: https://3dlook.ai/wp-content/uploads/2024/12/fitxpress.jpg
layout: provider
mcp_servers:
- description: ''
  name: 3D Look MCP Server
  slug: 3d-look-mcp-server
modified: '2026-07-17'
name: 3D Look
nav: Providers
network: true
overview: '3D Look publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Body Measurement, Computer-Vision, Artificial Intelligence, and Apparel.


  3D Look''s developer surface includes documentation, API reference, pricing, support, authentication, and 14 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/3d-look/refs/heads/main/screenshots/3d-look-2026-07-25T181146.png
security:
- kind: authentication
  name: 3D Look Authentication
  slug: 3d-look-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 3D Look Domain Security
  slug: 3d-look-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3d-look
tags:
- Company
- Body Measurement
- Computer-Vision
- Artificial Intelligence
- Apparel
- Fashion Technology
- Health and Fitness
- Sizing
- 3D Body Scanning
- SDK
website: https://3dlook.ai/
---
