---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: Berkeley's centralized API management developer portal where developers browse and search published campus APIs, read interactive OpenAPI-based documentation with a "Try it out" feature, and request a
  name: API Central (Developer Portal)
  slug: api-central
- description: The single, centralized entry point for API requests across the Berkeley campus. The gateway centralizes functions common to all campus APIs, including load balancing, authentication, authorization, a
  name: UC Berkeley API Gateway
  slug: api-gateway
- description: The University of California's open-access publishing and institutional repository (which includes UC Berkeley scholarship) exposes a public, uncredentialed read API and an OAI-PMH interface for harve
  name: eScholarship Repository API (OAI-PMH)
  slug: escholarship
- description: The UC Berkeley Library runs the Ex Libris Alma/Primo platform for collection management and discovery, exposing metadata via the Alma OAI-PMH provider and Primo discovery. The library maintains publi
  name: UC Berkeley Library Alma/Primo Integrations
  slug: library-alma
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.berkeley.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.api.berkeley.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucberkeley
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-berkeley/
- group: operate
  title: ''
  type: Status
  url: https://systemstatus.berkeley.edu/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UCBerkeley
- group: auth
  title: ''
  type: Authentication
  url: https://integration-services.berkeley.edu/api-management/developer-portal-api-central
- group: commercial
  title: ''
  type: Plans
  url: plans/ucb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
description: 'The University of California, Berkeley (UC Berkeley) is a public land-grant research university and the flagship campus of the University of California system, ranked #12 in the QS World University Rankings 2025. Berkeley operates a formal, centrally governed API program through its Integration Services / Enterprise Information Services team, exposing campus data via the API Central developer portal and a shared API Gateway. Access is gated behind CalNet identity and Data Owner approval, with interactive OpenAPI-based documentation and gateway-level authentication, authorization, and rate limiting. Public, uncredentialed footprint also includes the UC-wide eScholarship repository APIs/OAI-PMH and library Alma/Primo metadata services.'
finops:
- name: Ucb Finops
  service_category: Education
  slug: ucb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucb.png
jsonld:
- class_count: 6
  name: Ucb Context
  property_count: 4
  slug: ucb-context
layout: provider
name: University of California, Berkeley
nav: Providers
network: true
overview: 'University of California, Berkeley publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of California, Berkeley catalog on APIs.io includes 1 JSON-LD context.


  University of California, Berkeley''s developer surface includes GitHub presence, status page, authentication, and 9 more developer resources.'
plans:
- name: Ucb Plans Pricing
  plan_count: 2
  slug: ucb-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Ucb Rate Limits
  slug: ucb-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucb/refs/heads/main/screenshots/ucb-2026-06-20T195937.png
security:
- kind: domain-security
  name: Ucb Domain Security
  slug: ucb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ucb
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- United States
- California
website: https://www.berkeley.edu/
---
