---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: The core open-source, git-native desktop API client (a lightweight Postman/Insomnia alternative). Compose and send HTTP, REST, GraphQL, and gRPC requests, organize them into collections, manage enviro
  name: Bruno API Client
  slug: bruno-api-client
- description: Bru is Bruno's plain-text domain-specific markup language. Each request is stored as a .bru file capturing the HTTP method, URL, query params, headers, body, authentication, scripts, tests, assertions
  name: Bru Markup Language (.bru)
  slug: bruno-bru-language
- description: 'OpenCollection is the open, YAML-based collection format Bruno now recommends for new collections as an alternative representation to .bru. Like .bru it stores requests, folders, auth, and scripts as '
  name: OpenCollection Format
  slug: bruno-opencollection
- description: The @usebruno/cli command-line runner (invoked as bru, installed via npm install -g @usebruno/cli) executes individual requests or entire collections headlessly for CI/CD, with JSON, JUnit, and HTML t
  name: Bruno CLI (bru)
  slug: bruno-cli
- description: Paid Bruno (Pro and Ultimate) adds native in-app Git integration and OpenAPI sync (5 syncs/month on Pro, unlimited on Ultimate) plus SSO, SCIM, audit logs, and license/admin controls. Collaboration ha
  name: Bruno Git Integration and Sync
  slug: bruno-git-collaboration
artifact_total: 8
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usebruno
- group: company
  title: ''
  type: Website
  url: https://www.usebruno.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usebruno.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usebruno
- group: commercial
  title: ''
  type: Plans
  url: plans/bruno-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bruno-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bruno-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.usebruno.com/
created: '2026-07-11'
description: Bruno is an open-source (MIT), git-native API client - a lightweight, offline-first alternative to Postman and Insomnia for exploring and testing APIs. It is a developer TOOL, not a hosted HTTP API provider. Collections are stored on the local filesystem as folders of plain-text files (the .bru "Bru" markup language, with OpenCollection YAML now recommended for new collections), so API requests are version-controlled in Git alongside code. Bruno sends HTTP, REST, GraphQL, and gRPC requests, manages environments and variables, and runs pre-request/post-response scripts, tests, and assertions. The @usebruno/cli command-line runner (bru) executes collections headlessly in CI/CD with JSON, JUnit, and HTML reporters. Bruno is offline-only and does not sync request data to a Bruno-hosted cloud; paid Pro/Ultimate tiers add native in-app Git integration, OpenAPI sync, and enterprise admin controls that run through your own Git provider and identity systems. Bruno does not expose a documented
  public REST HTTP API.
finops:
- name: Bruno Api Finops
  service_category: Developer Tools
  slug: bruno-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bruno-api.png
layout: provider
modified: '2026-07-11'
name: Bruno
nav: Providers
network: true
overview: 'Bruno publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, API Testing, Developer Tools, Open-Source, and Git-Native.


  Bruno''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Bruno Api Plans Pricing
  plan_count: 4
  slug: bruno-api-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Bruno Api Rate Limits
  slug: bruno-api-rate-limits
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 23.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bruno-api/refs/heads/main/screenshots/bruno-api-2026-07-25T204007.png
slug: bruno-api
tags:
- API Client
- API Testing
- Developer Tools
- Open-Source
- Git-Native
- CLI
- Postman Alternative
website: https://www.usebruno.com/
---
