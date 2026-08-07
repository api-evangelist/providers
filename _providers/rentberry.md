---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Versioned REST API behind the Rentberry rental marketplace, described by an OpenAPI 3.0.0 document published in the Swagger UI at https://api.rentberry.com/docs. 188 paths / 220 operations across 44 t
  name: Rentberry API
  slug: rentberry-api
- description: 'Open-source gRPC geocoding and timezone-lookup service Rentberry built and runs for its own property search, with published proto3 definitions and PHP client bindings on Packagist. Two services: Geoco'
  name: Rentberry Geocoder (gRPC)
  slug: rentberry-geocoder-grpc
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://rentberry.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.rentberry.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.rentberry.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.rentberry.com/docs
- group: operate
  title: ''
  type: Support
  url: https://help.rentberry.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.rentberry.com/en/
- group: company
  title: ''
  type: Blog
  url: https://rentberry.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://rentberry.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rentberry
- group: commercial
  title: ''
  type: Pricing
  url: https://rentberry.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://rentberry.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rentberry.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rentberry.com/privacy
- group: company
  title: ''
  type: About
  url: https://rentberry.com/about
- group: company
  title: ''
  type: Investors
  url: https://rentberry.com/investors
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/rentberry-openapi.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/rentberry-geocoder.proto
- group: auth
  title: ''
  type: Authentication
  url: authentication/rentberry-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rentberry-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rentberry-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rentberry-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rentberry-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rentberry-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rentberry-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/rentberry-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rentberry-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rentberry-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentberry-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rentberry-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Rentberry, Inc. is an international long-term home rental marketplace founded in 2015 and headquartered in San Francisco, California. The platform runs the whole rental lifecycle in one closed loop for both tenants and landlords: property listing and syndication, search across residential rental cities worldwide, virtual tours and open-house scheduling, custom rent offers and negotiation, rental applications with proof-of-income attachments, US credit and background screening, e-signed rental contracts and contract templates, online rent collection and rental subscriptions via Stripe, in-platform messaging, maintenance and complaint handling, and a flexible-living concept aimed at digital nomads. Rentberry operates a versioned REST API at api.rentberry.com whose Swagger UI at /docs publishes an OpenAPI 3.0.0 description covering applications, auth and social OAuth login, listings, search, contracts, screening, payments, rentals, messaging, user verification and localization.'
image: https://cdn.rentberry.com/files/seo/main.jpg
layout: provider
modified: '2026-08-02'
name: Rentberry
nav: Providers
network: true
overview: 'Rentberry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include real-estate, proptech, rentals, rental-marketplace, and property-management.


  Rentberry''s developer surface includes API reference, documentation, support, engineering blog, pricing, signup flow, authentication, and 23 more developer resources.'
random_paper: 85
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 47.9
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 41.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Rentberry Authentication
  slug: rentberry-authentication
  summary_line: token · 1 scheme
- kind: domain-security
  name: Rentberry Domain Security
  slug: rentberry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rentberry
tags:
- real-estate
- proptech
- rentals
- rental-marketplace
- property-management
- tenant-screening
- e-signature
- payments
- listings
- search
- geocoding
- marketplace
website: https://rentberry.com/
---
