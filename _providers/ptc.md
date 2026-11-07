---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-11-06'
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
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/ptc/security/ptc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ptc-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ptc/security/ptc-domain-security.yml
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
  href: https://artifacts.apis.io/ptc/plans/ptc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ptc-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ptc/rate-limits/ptc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ptc-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ptc/finops/ptc-finops.yml
  title: ''
  type: FinOps
  url: finops/ptc-finops.yml
created: '2026-06-13'
description: PTC is an industrial technology company providing software platforms and APIs for Industrial IoT (ThingWorx), Product Lifecycle Management (Windchill, Arena), Augmented Reality (Vuforia), Field Service Management (ServiceMax), and industrial connectivity (Kepware) in manufacturing environments.
finops:
- has_sources: false
  method: generated
  name: Ptc Finops
  primary_unit: ''
  service_category: ''
  slug: ptc-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ptc.png
layout: provider
modified: '2026-06-13'
name: PTC
nav: Providers
network: true
overview: 'PTC is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Windchill REST Services, Arena PLM REST API, and 4 more. Tagged areas include Industrial IoT, PLM, Augmented Reality, Field Service Management, and Manufacturing.


  PTC''s developer surface includes documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Ptc Plans Pricing
  plan_count: 9
  slug: ptc-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Ptc Rate Limits
  slug: ptc-rate-limits
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 50.0
    discoverability: 62.5
    operational_transparency: 28.9
  previous_composite: 31.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ptc/ptc-2026-06-20T192239.png
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
- CAD
- Digital Transformation
- Industrial
website: https://www.ptc.com
---
