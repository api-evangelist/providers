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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: The ThingWorx Industrial IoT platform REST API enables developers to interact with Things, Properties, Services, Events, and Subscriptions via HTTP. Authentication uses an AppKey passed as an HTTP hea
  name: ThingWorx REST API
  slug: thingworx-rest-api
- description: Windchill PLM REST Services provide OData-compliant REST API access to product lifecycle management data including product structures, change management, documents, and configuration management. The A
  name: Windchill REST Services
  slug: windchill-rest-services
- description: Arena PLM REST API v1 provides full programmatic access to Arena's cloud-based PLM capabilities including Bill of Materials management, change management, quality, and compliance. Full OpenAPI/Swagger
  name: Arena PLM REST API
  slug: arena-plm-rest-api
- description: The Vuforia Engine Web API provides HTTPS REST access to cloud-based augmented reality capabilities including Cloud Image Recognition, Cloud Area Targets, and license management for building AR applic
  name: Vuforia Engine Web API
  slug: vuforia-engine-web-api
- description: 'ServiceMax REST API (Max REST API) enables integration with ServiceMax field service management capabilities including work orders, scheduling, service boards, and field metadata management. Built on '
  name: ServiceMax Max REST API
  slug: servicemax-max-rest-api
- description: The Kepware KEPServerEX Configuration API is a local REST API that enables programmatic configuration of the industrial connectivity server including channels, devices, tags, and IoT Gateway agents. A
  name: Kepware Configuration REST API
  slug: kepware-configuration-rest-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ptc-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ptc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ptc.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ptc.com/en/support/help/thingworx_doc_resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PTCInc
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ptc-arena
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PTC-Education
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ptc
- group: company
  title: ''
  type: Blog
  url: https://www.ptc.com/en/blogs/
- group: operate
  title: ''
  type: CommunityBlog
  url: https://community.ptc.com/t5/Blog/bg-p/BWBlog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ptc.com/en/products/vuforia/vuforia-engine/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ptc.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ptc.io/
- group: other
  title: ''
  type: X
  url: https://x.com/ptc
- group: other
  title: ''
  type: SocialMedia
  url: https://www.ptc.com/en/about/social-media
- group: commercial
  title: ''
  type: Plans
  url: plans/ptc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ptc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ptc-finops.yml
created: '2026-06-13'
description: PTC is an industrial technology company providing software platforms and APIs for Industrial IoT (ThingWorx), Product Lifecycle Management (Windchill, Arena), Augmented Reality (Vuforia), Field Service Management (ServiceMax), and industrial connectivity (Kepware) in manufacturing environments.
finops:
- name: Ptc Finops
  service_category: ''
  slug: ptc-finops
graphqls:
- description: 'PTC provides industrial IoT and digital manufacturing solutions. The ThingWorx IoT platform API covers device connectivity, thing templates and shapes, property management, services, events, streams, '
  name: PTC GraphQL API
  slug: ptc-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ptc.png
layout: provider
modified: '2026-06-13'
name: PTC
nav: Providers
network: true
overview: 'PTC publishes 2 APIs on the [APIs.io](https://apis.io/) network: Windchill REST Services and Arena PLM REST API. Tagged areas include Industrial IoT, PLM, Augmented Reality, Field Service Management, and Manufacturing.


  PTC''s developer surface includes documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Ptc Plans Pricing
  plan_count: 9
  slug: ptc-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 6
  name: Ptc Rate Limits
  slug: ptc-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ptc/refs/heads/main/screenshots/ptc-2026-06-20T192239.png
security:
- kind: domain-security
  name: Ptc Domain Security
  slug: ptc-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Ptc Trust Center
  slug: ptc-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
slug: ptc
tags:
- Industrial IoT
- PLM
- Augmented Reality
- Field Service Management
- Manufacturing
- IIoT
- CAD
- Digital Transformation
website: https://www.ptc.com
---
