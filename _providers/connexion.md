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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Connexion is a contract-first Python web framework that loads an OpenAPI specification and routes requests to Python handlers based on operationId. It performs request validation, parameter parsing, a
  name: Connexion Python Framework
  slug: framework
- description: Connexion 3 introduces a stack of pluggable ASGI middlewares that handle exceptions, server errors, lifespan, security, routing, request validation, response validation, Swagger UI, and context propag
  name: Connexion Middleware Stack
  slug: middleware
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connexion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connexion.readthedocs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://connexion.readthedocs.io/en/latest/quickstart.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/spec-first/connexion
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spec-first
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/spec-first/connexion/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/spec-first/connexion/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/spec-first/connexion/blob/main/LICENSE
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/connexion/
- group: company
  title: ''
  type: Blog
  url: https://github.com/spec-first/connexion/releases.atom
created: '2026-03-25'
description: 'Connexion is an open source Python framework that automatically handles HTTP requests based on OpenAPI specifications. Connexion 3 provides AsyncApp, FlaskApp, and ConnexionMiddleware as primary entry points, with built-in routing, request and response validation, parameter parsing, security enforcement, content negotiation, error handling, lifespan, and Swagger UI integration. Connexion takes a contract-first, design-first approach: the OpenAPI specification is the source of truth and Python handlers are resolved from operationId or via configurable resolvers.'
finops:
- name: Connexion Finops
  service_category: API
  slug: connexion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/connexion.png
layout: provider
modified: '2026-04-28'
name: Connexion
nav: Providers
network: true
overview: 'Connexion publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, ASGI, Design-First, Flask, and OpenAPI.


  Connexion''s developer surface includes documentation, changelog, engineering blog, and 7 more developer resources.'
plans:
- name: Connexion Plans Pricing
  plan_count: 3
  slug: connexion-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Connexion Rate Limits
  slug: connexion-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connexion/refs/heads/main/screenshots/connexion-2026-06-20T174905.png
security:
- kind: domain-security
  name: Connexion Domain Security
  slug: connexion-domain-security
  summary_line: TLSv1.3 · HSTS
slug: connexion
tags:
- API Design
- ASGI
- Design-First
- Flask
- OpenAPI
- Python
- Validation
- WSGI
website: https://connexion.readthedocs.io/
---
