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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Cortex Idp Agentic Access
  operation_count: 47
  slug: cortex-idp-agentic-access
  summary_line: 47 operations · 25 acting
api_count: 6
apis:
- description: Software catalog entities - services, resources, domains, and custom types.
  name: Cortex Catalog API
  slug: cortex-idp-catalog-api
- description: Arbitrary key/value metadata attached to catalog entities.
  name: Cortex Custom Data API
  slug: cortex-idp-custom-data-api
- description: Deployment events recorded per catalog entity.
  name: Cortex Deploys API
  slug: cortex-idp-deploys-api
- description: Time-boxed improvement campaigns driving entities toward a Scorecard target.
  name: Cortex Initiatives API
  slug: cortex-idp-initiatives-api
- description: Third-party integration configurations that hydrate the catalog.
  name: Cortex Integrations API
  slug: cortex-idp-integrations-api
- description: Standards that measure catalog entities, with scores and exemptions.
  name: Cortex Scorecards API
  slug: cortex-idp-scorecards-api
artifact_total: 12
collections:
- collection_type: open
  name: Cortex REST API
  slug: open-cortex-idp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cortex-idp-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cortex-idp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cortexapp
- group: company
  title: ''
  type: Website
  url: https://www.cortex.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cortex.io
- group: commercial
  title: ''
  type: Plans
  url: plans/cortex-idp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cortex-idp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cortex-idp-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cortex.io/pricing
created: '2026-07-11'
description: Cortex (cortex.io) is an internal developer portal (IDP) and software catalog platform. It gives engineering organizations a catalog of services and entities, Scorecards that measure those entities against production-readiness and reliability standards, Initiatives for driving improvement campaigns, and roughly thirty integrations (GitHub, PagerDuty, Datadog, Kubernetes, and more) that hydrate the catalog. Cortex exposes a documented REST API (base https://api.getcortexapp.com/api/v1) with Bearer/API-key authentication covering the Catalog/Entities, Scorecards, Custom Data, Initiatives, Deploys, Teams, and Integrations. NOTE - this is Cortex.io the internal developer portal / service catalog & scorecards company, NOT Cortex XSOAR (Palo Alto Networks), NOT the Cortex crypto token, and NOT Orange Logic's Cortex DAM.
finops:
- name: Cortex Idp Finops
  service_category: Developer Tools and Platform Engineering
  slug: cortex-idp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cortex-idp.png
layout: provider
modified: '2026-07-11'
name: Cortex
nav: Providers
network: true
overview: 'Cortex publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Custom Data API, Deploys API, and 3 more. Tagged areas include Software Catalog, Internal Developer Portal, Service Catalog, Developer Experience, and IDP.


  Cortex''s developer surface includes authentication, documentation, pricing, and 6 more developer resources.'
plans:
- name: Cortex Idp Plans Pricing
  plan_count: 3
  slug: cortex-idp-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Cortex Idp Rate Limits
  slug: cortex-idp-rate-limits
score:
  band: thin
  composite: 40.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cortex-idp/refs/heads/main/screenshots/cortex-idp-2026-07-25T210650.png
security:
- kind: authentication
  name: Cortex Idp Authentication
  slug: cortex-idp-authentication
  summary_line: http · 1 scheme
slug: cortex-idp
tags:
- Software Catalog
- Internal Developer Portal
- Service Catalog
- Developer Experience
- IDP
- Scorecards
- Platform Engineering
- Developer Portal
website: https://www.cortex.io
---
