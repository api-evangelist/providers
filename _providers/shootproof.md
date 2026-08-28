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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Shootproof Agentic Access
  operation_count: 67
  slug: shootproof-agentic-access
  summary_line: 67 operations · 37 acting
api_count: 7
apis:
- description: Contacts (clients) attached to a brand.
  name: ShootProof Clients API
  slug: shootproof-clients-api
- description: Client contracts, contract templates, and contract email delivery.
  name: ShootProof Contracts API
  slug: shootproof-contracts-api
- description: Client events (galleries/shoots), albums, categories, digital rules, and QR codes.
  name: ShootProof Events & Galleries API
  slug: shootproof-events-galleries-api
- description: Print/product orders, order items, lab shipments, and payments (beta).
  name: ShootProof Orders API
  slug: shootproof-orders-api
- description: Photos uploaded to an event, upload policies, originals, and zip bundles.
  name: ShootProof Photos API
  slug: shootproof-photos-api
- description: Root hypermedia entry point for the API.
  name: ShootProof Service Description API
  slug: shootproof-service-description-api
- description: Brands, brand themes, homepage settings, watermarks, and summary reports.
  name: ShootProof Studios API
  slug: shootproof-studios-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients API
  slug: open-shootproof-clients-api
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients Contracts API
  slug: open-shootproof-contracts-api
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients Events & Galleries API
  slug: open-shootproof-events-galleries-api
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients Orders API
  slug: open-shootproof-orders-api
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients Photos API
  slug: open-shootproof-photos-api
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients Service Description API
  slug: open-shootproof-service-description-api
- collection_type: open
  name: ShootProof Studio API (Curated Subset) Clients Studios API
  slug: open-shootproof-studios-api
- collection_type: open
  name: ShootProof Studio API
  slug: open-shootproof
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shootproof-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shootproof-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shootproof-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shootproof-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShootProof
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shootproof
- group: company
  title: ''
  type: Website
  url: https://www.shootproof.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shootproof.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/shootproof-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shootproof-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shootproof-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.shootproof.com/blog/feed/
created: '2026-07-04'
description: ShootProof is a SaaS platform for professional photographers that handles client galleries, proofing, digital download rules, watermarking, contracts, invoicing, and print/product e-commerce fulfilled through partner labs. The ShootProof Studio API is a RESTful, hypermedia (HAL-style links) API secured with three-legged OAuth 2.0, published with a downloadable OpenAPI 3.0 document (oas/studio.json) at developer.shootproof.com. It exposes a studio's Brands, Events (client galleries) and Albums, Photos, Contacts (clients), Contracts, Orders, Invoices, Price Sheets, and Email automation as linked resources under a single https://api.shootproof.com/studio base URL. API access is included free with a ShootProof account; a client ID is issued by ShootProof support on request. A separate legacy REST API also remains documented for older integrations.
finops:
- name: Shootproof Finops
  service_category: Photography SaaS and E-Commerce
  slug: shootproof-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shootproof.png
layout: provider
modified: '2026-07-04'
name: ShootProof
nav: Providers
network: true
overview: 'ShootProof publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Contracts API, Events & Galleries API, and 4 more. Tagged areas include Photography, Client Galleries, Proofing, Digital Downloads, and Photo Studio Management.


  ShootProof''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Shootproof Plans Pricing
  plan_count: 5
  slug: shootproof-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Shootproof Rate Limits
  slug: shootproof-rate-limits
scopes:
- name: Shootproof Scopes
  scope_count: 5
  slug: shootproof-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 39.3
  delta: 1.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.2
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Shootproof Authentication
  slug: shootproof-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Shootproof Domain Security
  slug: shootproof-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: shootproof
tags:
- Photography
- Client Galleries
- Proofing
- Digital Downloads
- Photo Studio Management
- E-Commerce
- Software-as-a-Service
website: https://www.shootproof.com
---
