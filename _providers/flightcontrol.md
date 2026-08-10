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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Flightcontrol Agentic Access
  operation_count: 10
  slug: flightcontrol-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 7
apis:
- description: 'Version-controlled flightcontrol.json (or flightcontrol.cue) declaring environments, services, regions, sources, and environment variables that drive AWS provisioning; a published JSON Schema enables '
  name: Flightcontrol Config-as-Code
  slug: flightcontrol-config-as-code
- description: The CloudFront API from Flightcontrol — 2 operation(s) for cloudfront.
  name: Flightcontrol CloudFront API
  slug: flightcontrol-cloudfront-api
- description: The Deploy Hooks API from Flightcontrol — 2 operation(s) for deploy hooks.
  name: Flightcontrol Deploy Hooks API
  slug: flightcontrol-deploy-hooks-api
- description: The Deployments API from Flightcontrol — 1 operation(s) for deployments.
  name: Flightcontrol Deployments API
  slug: flightcontrol-deployments-api
- description: The Environment Variables API from Flightcontrol — 1 operation(s) for environment variables.
  name: Flightcontrol Environment Variables API
  slug: flightcontrol-environment-variables-api
- description: The Environments API from Flightcontrol — 1 operation(s) for environments.
  name: Flightcontrol Environments API
  slug: flightcontrol-environments-api
- description: The Services API from Flightcontrol — 2 operation(s) for services.
  name: Flightcontrol Services API
  slug: flightcontrol-services-api
artifact_total: 14
collections:
- collection_type: open
  name: Flightcontrol Management API
  slug: open-flightcontrol
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flightcontrol-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flightcontrol-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flightcontrol-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flightcontrol
- group: company
  title: ''
  type: Website
  url: https://www.flightcontrol.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.flightcontrol.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/flightcontrol-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flightcontrol-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flightcontrol-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.flightcontrol.dev/blog
created: '2026-06-20'
description: Flightcontrol deploys applications to your own AWS account with a Heroku-like developer experience. It provisions and manages AWS infrastructure from a flightcontrol.json config-as-code file and exposes an HTTP management API for triggering deployments, managing environments, services, environment variables, scaling, jobs, domains, and CloudFront cache invalidation.
finops:
- name: Flightcontrol Finops
  service_category: Developer Tools and Deployment
  slug: flightcontrol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flightcontrol.png
layout: provider
modified: '2026-06-20'
name: Flightcontrol
nav: Providers
network: true
overview: 'Flightcontrol publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CloudFront API, Deploy Hooks API, Deployments API, and 3 more. Tagged areas include Deployment, PaaS, Infrastructure, and DevOps.


  Flightcontrol''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Flightcontrol Plans Pricing
  plan_count: 4
  slug: flightcontrol-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Flightcontrol Rate Limits
  slug: flightcontrol-rate-limits
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.7
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flightcontrol/refs/heads/main/screenshots/flightcontrol-2026-06-20T181311.png
security:
- kind: authentication
  name: Flightcontrol Authentication
  slug: flightcontrol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flightcontrol Domain Security
  slug: flightcontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flightcontrol
tags:
- Deployment
- PaaS
- Infrastructure
- DevOps
website: https://www.flightcontrol.dev
---
