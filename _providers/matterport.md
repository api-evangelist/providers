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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Matterport's public GraphQL API family. The Model API reads and manages 3D models (spaces, meshes, assets, labels/tags, sweeps); the Account API manages account, folders and users; the Import API inge
  name: Matterport Model API (GraphQL)
  slug: matterport-model-api-graphql
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/matterport-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matterport-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://matterport.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://matterport.github.io/showcase-sdk/
- group: docs
  title: ''
  type: APIReference
  url: https://api.matterport.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://matterport.github.io/showcase-sdk/sdk_home.html
- group: operate
  title: ''
  type: Support
  url: https://support.matterport.com
- group: company
  title: ''
  type: Blog
  url: https://matterport.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matterport
- group: commercial
  title: ''
  type: Pricing
  url: https://matterport.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://buy.matterport.com/free-account-register
- group: start
  title: ''
  type: Login
  url: https://authn.matterport.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://matterport.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.costar.com/about/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.matterport.com
- group: auth
  title: ''
  type: Compliance
  url: https://matterport.com/trust
- group: operate
  title: ''
  type: ChangeLog
  url: https://matterport.github.io/showcase-sdk/sdk_changelog.html
- group: build
  title: ''
  type: Packages
  url: packages/matterport-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/matterport-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matterport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matterport-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/matterport-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matterport-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/matterport-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matterport-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matterport-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matterport-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matterport-llms.txt
created: '2026-07-17'
description: Matterport is a spatial data company (now a CoStar Group company) whose platform captures physical spaces and turns them into immersive, dimensionally-accurate 3D models known as digital twins. Used across residential and commercial real estate, architecture/engineering/construction, facilities management, insurance, retail and travel, the platform pairs a capture pipeline (Pro cameras, 360 cameras, LiDAR and smartphone apps) with a hosted Showcase 3D player and a developer surface. Developers build on Matterport through a GraphQL API family (Model API, Account API, Import API), the Property Intelligence API, the Custom Roles API, and a family of JavaScript SDKs (SDK for Embeds, SDK Bundle, and a WebComponent) that let applications embed and script the 3D Showcase player, read space geometry and metadata, and manage models.
image: https://matterport.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: MatterPort
nav: Providers
network: true
overview: 'MatterPort publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D, Digital Twin, Spatial Data, and Real-Estate.


  MatterPort''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 37.4
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matterport/refs/heads/main/screenshots/matterport-2026-07-25T230424.png
security:
- kind: authentication
  name: Matterport Authentication
  slug: matterport-authentication
  summary_line: http-basic/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Matterport Domain Security
  slug: matterport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Matterport Trust Center
  slug: matterport-trust-center
  summary_line: SOC 2, GDPR
slug: matterport
tags:
- Company
- 3D
- Digital Twin
- Spatial Data
- Real-Estate
- Construction
- GraphQL
- SDK
- Computer-Vision
- Property Intelligence
website: https://matterport.com/developers
---
