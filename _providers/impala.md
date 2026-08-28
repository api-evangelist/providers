---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Making and managing bookings.
  name: Impala Bookings API
  slug: impala-bookings-api
- description: Accessing hotel content, available rooms and rates.
  name: Impala Hotels API
  slug: impala-hotels-api
- description: Getting rates for future dates.
  name: Impala Rate Calendar API
  slug: impala-rate-calendar-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Impala Hotel Booking Bookings API
  slug: open-impala-bookings-api
- collection_type: open
  name: Impala Hotel Booking Bookings Hotels API
  slug: open-impala-hotels-api
- collection_type: open
  name: Impala Hotel Booking Bookings Rate Calendar API
  slug: open-impala-rate-calendar-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/impala-hotels-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/impala-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/impala-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impala-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impala-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impala-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/impala-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impala-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impala-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impala-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impala-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/impala-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetImpala
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/getimpala/impala-hotel-booking-api/documentation/fdkbiih/impala-hotel-booking-api
created: '2026-07-17'
description: 'Impala built a single, standardized REST API for the hotel industry — one integration to search availability, read rate plans, and create, amend, and cancel bookings across many property management systems (PMS), so any app could sell hotel rooms and earn commission per booking. Founded in London in 2016 and backed by Speedinvest, Lakestar, and Kima Ventures, Impala shipped a sandbox (with a demo hotel, "The Charleston"), a Postman collection, and PHP/JavaScript wrappers. The company is now defunct: getimpala.com / impala.travel and the API and docs hosts no longer resolve, and the primary domain is held by an unrelated party. This profile preserves the historical OpenAPI (apis.guru impala.travel:hotels 1.003) and pipeline-derived artifacts for the record.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impala.png
layout: provider
mcp_servers:
- description: ''
  name: Impala MCP Server
  slug: impala-mcp-server
modified: '2026-07-19'
name: Impala
nav: Providers
network: true
overview: 'Impala publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bookings API, Hotels API, and Rate Calendar API. Tagged areas include Company, Hotels, Travel, Booking, and Hospitality.


  Impala''s developer surface includes authentication, sandbox, and 13 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 63.0
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 29.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/screenshots/impala-2026-07-25T222147.png
security:
- kind: authentication
  name: Impala Authentication
  slug: impala-authentication
  summary_line: apiKey/http · 2 schemes
slug: impala
tags:
- Company
- Hotels
- Travel
- Booking
- Hospitality
- Payments
- Defunct
---
