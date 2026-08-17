---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
api_count: 3
apis:
- description: REST APIs for the Nexus digital reality platform enabling manufacturers to build connected workflows integrating metrology, quality inspection, and production monitoring data. All endpoints are authen
  name: Hexagon Nexus API
  slug: nexus-api
- description: Enterprise Asset Management REST API providing programmatic access to asset lifecycle data including equipment management, work orders, preventive maintenance, document attachments, and service reques
  name: HxGN EAM REST API
  slug: hxgn-eam-api
- description: Smart Digital eXchange API Services enabling integration with Hexagon's engineering data management platform for plant design, document control, and digital twin workflows in process and power industr
  name: HxGN SDx API Services
  slug: hxgn-sdx-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hexagon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hexagon.com
- group: docs
  title: ''
  type: Documentation
  url: https://nexus.hexagon.com/documentationcenter/en-US/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/hexagonab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hexagon-ab
- group: company
  title: ''
  type: Blog
  url: https://blog.manufacturing.hexagon.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hexagon.com/products/product-groups/nexus
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hxdr.app/
- group: other
  title: ''
  type: X
  url: https://x.com/hexagonab
- group: commercial
  title: ''
  type: Plans
  url: plans/hexagon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hexagon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hexagon-finops.yml
created: '2026-06-13'
description: Hexagon is a global leader in digital reality solutions, combining sensor, software and autonomous technologies. Through the Nexus platform and product APIs, Hexagon delivers manufacturing intelligence capabilities spanning metrology, quality inspection, production monitoring, and digital factory solutions. The Nexus Developer Portal provides REST APIs authenticated via OAuth 2.0, enabling manufacturers and third-party developers to build connected, collaborative workflows integrating measurement data, quality processes, and industrial automation across the smart factory lifecycle.
finops:
- name: Hexagon Finops
  service_category: ''
  slug: hexagon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hexagon.png
layout: provider
modified: '2026-06-13'
name: Hexagon
nav: Providers
network: true
overview: 'Hexagon publishes 1 API on the [APIs.io](https://apis.io/) network: Nexus API. Tagged areas include Manufacturing, Metrology, Quality Inspection, Digital Factory, and Production Monitoring.


  Hexagon''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Hexagon Plans Pricing
  plan_count: 3
  slug: hexagon-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Hexagon Rate Limits
  slug: hexagon-rate-limits
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hexagon/refs/heads/main/screenshots/hexagon-2026-06-20T182709.png
security:
- kind: domain-security
  name: Hexagon Domain Security
  slug: hexagon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hexagon
tags:
- Manufacturing
- Metrology
- Quality Inspection
- Digital Factory
- Production Monitoring
- Industrial IoT
- Smart Manufacturing
website: https://hexagon.com
---
