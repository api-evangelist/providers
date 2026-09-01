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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Plane REST API provides 180+ endpoints for managing all aspects of project management workspaces including projects, work items, cycles, modules, pages, analytics, intake, and team members. The AP
  name: Plane REST API
  slug: plane-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/plane-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plane.so/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.plane.so/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/makeplane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planepowers/
- group: company
  title: ''
  type: Blog
  url: https://plane.so/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://plane.so/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plane.so/
- group: other
  title: ''
  type: X
  url: https://twitter.com/planepowers
- group: commercial
  title: ''
  type: Plans
  url: plans/plane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/plane-finops.yml
created: '2026-06-13'
description: Plane is an open-source, AI-native project management platform that enables teams to manage issues, cycles, modules, pages, analytics, and workspace members through a comprehensive REST API. Available as a fully managed cloud service or self-hosted on your own infrastructure using Docker or Kubernetes, Plane provides 180+ REST endpoints organized around predictable resource-oriented URLs with JSON request and response bodies. The API supports OAuth 2.0 for third-party app authorization, personal access token authentication, HMAC-signed webhooks for real-time event notifications, and typed SDKs for Python and Node.js. Plane also ships an official Model Context Protocol (MCP) server to enable AI agents to interact with your workspace programmatically.
finops:
- name: Plane Finops
  service_category: ''
  slug: plane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plane.png
jsonld:
- class_count: 47
  name: Plane Context
  property_count: 1
  slug: plane-context
layout: provider
modified: '2026-06-13'
name: Plane
nav: Providers
network: true
overview: 'Plane publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Project Management, Issues, Cycles, Modules, and Pages.


  The Plane catalog on APIs.io includes 1 JSON-LD context.


  Plane''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Plane Plans Pricing
  plan_count: 4
  slug: plane-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Plane Rate Limits
  slug: plane-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 35.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plane/refs/heads/main/screenshots/plane-2026-06-20T191752.png
security:
- kind: domain-security
  name: Plane Domain Security
  slug: plane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plane Trust Center
  slug: plane-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: plane
tags:
- Project Management
- Issues
- Cycles
- Modules
- Pages
- Analytics
- Workspace
- Open-Source
- Self-Hosted
- Artificial Intelligence
website: https://plane.so/
---
