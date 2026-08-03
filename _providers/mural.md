---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: The Mural Public API supports OAuth 2.0 with scopes, image and file uploads to murals, and CRUD on workspaces, rooms, murals, widgets, and members. Includes published rate limits, pagination, and erro
  name: Mural Public API
  slug: mural-public-api
- description: The Mural Enterprise API provides additional admin and management functionality for Enterprise plan customers (workspace administration, audit, identity).
  name: Mural Enterprise API
  slug: mural-enterprise-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/mural-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mural-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mural.co/
- group: start
  title: ''
  type: Portal
  url: https://developers.mural.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mural.co/pricing
- group: operate
  title: ''
  type: Community
  url: https://community.mural.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/muralco
- group: commercial
  title: ''
  type: Plans
  url: plans/mural-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mural-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mural-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.mural.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.mural.co/blog/rss.xml
created: '2026-05-08'
description: Mural is a visual collaboration platform. It exposes both a Mural API and a Mural Enterprise API with OAuth 2.0 authentication, scope-based permissions, rate limiting, pagination, and a published OpenAPI specification. Postman workspace and Zapier integration are also available.
finops:
- name: Mural Finops
  service_category: Collaboration
  slug: mural-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mural.png
layout: provider
modified: '2026-05-08'
name: Mural
nav: Providers
network: true
overview: 'Mural publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Collaboration, Whiteboard, Workshops, Enterprise, and OAuth.


  Mural''s developer surface includes developer portal, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Mural Plans Pricing
  plan_count: 1
  slug: mural-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 1
  name: Mural Rate Limits
  slug: mural-rate-limits
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mural/refs/heads/main/screenshots/mural-2026-06-20T185858.png
security:
- kind: domain-security
  name: Mural Domain Security
  slug: mural-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mural Trust Center
  slug: mural-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: mural
tags:
- Collaboration
- Whiteboard
- Workshops
- Enterprise
- OAuth
website: https://www.mural.co/
---
