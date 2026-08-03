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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Verdaccio Agentic Access
  operation_count: 24
  slug: verdaccio-agentic-access
  summary_line: 24 operations · 11 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: 'The Verdaccio npm Registry REST API implements the CommonJS Compliant Package Registry specification, providing endpoints to publish, retrieve, search, and delete npm packages. It supports JWT tokens '
  name: Verdaccio npm Registry API
  slug: verdaccio-npm-registry-api
- description: Manage dist-tags for packages
  name: Verdaccio dist-tags API
  slug: verdaccio-dist-tags-api
- description: Retrieve package metadata and tarballs
  name: Verdaccio packages API
  slug: verdaccio-packages-api
- description: User profile management
  name: Verdaccio profile API
  slug: verdaccio-profile-api
- description: Publish, update, and unpublish packages
  name: Verdaccio publish API
  slug: verdaccio-publish-api
- description: Search the registry
  name: Verdaccio search API
  slug: verdaccio-search-api
- description: API token management
  name: Verdaccio tokens API
  slug: verdaccio-tokens-api
- description: User authentication and management
  name: Verdaccio user API
  slug: verdaccio-user-api
- description: Utility endpoints
  name: Verdaccio utility API
  slug: verdaccio-utility-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verdaccio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verdaccio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verdaccio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.verdaccio.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.verdaccio.org/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/verdaccio
- group: company
  title: ''
  type: Blog
  url: https://www.verdaccio.org/blog/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/7qWJxBf
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/verdaccio.org
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/verdaccio/verdaccio
- group: other
  title: ''
  type: Sponsorship
  url: https://opencollective.com/verdaccio
- group: commercial
  title: ''
  type: Plans
  url: plans/verdaccio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/verdaccio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/verdaccio-finops.yml
created: 2026-06-13
description: Verdaccio is an open-source, lightweight private npm proxy registry built in Node.js that enables organizations to host, cache, and manage packages privately. It implements the CommonJS Compliant Package Registry specification and provides a REST API for publishing, searching, and managing npm packages in self-hosted or cloud-deployed environments. Verdaccio supports JWT and Basic Auth token authentication, rate limiting, pluggable storage backends, and seamless proxying of upstream registries such as npmjs.org.
examples:
- key_count: 6
  name: Verdaccio Login Request Example
  slug: verdaccio-login-request-example
- key_count: 6
  name: Verdaccio Publish Package Example
  slug: verdaccio-publish-package-example
- key_count: 3
  name: Verdaccio Search Results Example
  slug: verdaccio-search-results-example
- key_count: 3
  name: Verdaccio Token Create Example
  slug: verdaccio-token-create-example
finops:
- name: Verdaccio Finops
  service_category: ''
  slug: verdaccio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verdaccio.png
json_schemas:
- name: Verdaccio Package Manifest
  property_count: 8
  slug: verdaccio-package-manifest
- name: Verdaccio Publish Request
  property_count: 6
  slug: verdaccio-publish-request
- name: Verdaccio Search Results
  property_count: 3
  slug: verdaccio-search-results
jsonld:
- class_count: 35
  name: Verdaccio Context
  property_count: 9
  slug: verdaccio-context
layout: provider
modified: 2026-06-13
name: Verdaccio
nav: Providers
network: true
overview: 'Verdaccio publishes 8 APIs on the [APIs.io](https://apis.io/) network, including dist-tags API, packages API, profile API, and 5 more. Tagged areas include npm, registry, package-manager, private-registry, and proxy.


  The Verdaccio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Verdaccio''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Verdaccio Plans Pricing
  plan_count: 2
  slug: verdaccio-plans-pricing
random_paper: 89
rules:
- name: Verdaccio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: verdaccio-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verdaccio/refs/heads/main/screenshots/verdaccio-2026-06-20T200918.png
security:
- kind: authentication
  name: Verdaccio Authentication
  slug: verdaccio-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Verdaccio Domain Security
  slug: verdaccio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: verdaccio
tags:
- npm
- registry
- package-manager
- private-registry
- proxy
- nodejs
- open-source
- self-hosted
- yarn
- pnpm
- docker
- kubernetes
website: https://www.verdaccio.org/
---
