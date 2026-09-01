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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Snappr Agentic Access
  operation_count: 14
  slug: snappr-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
apis:
- description: Check available shoot start times.
  name: Snappr Availability API
  slug: snappr-availability-api
- description: Create and retrieve photoshoot bookings.
  name: Snappr Bookings API
  slug: snappr-bookings-api
- description: Check Snappr coverage for a location and shoot type.
  name: Snappr Coverage API
  slug: snappr-coverage-api
- description: Available Snappr editing job types.
  name: Snappr Editing Job Types API
  slug: snappr-editing-job-types-api
- description: Create and retrieve photo editing jobs (beta).
  name: Snappr Editing Jobs API
  slug: snappr-editing-jobs-api
- description: Retrieve images for bookings and editing jobs.
  name: Snappr Images API
  slug: snappr-images-api
- description: Editing presets defined in the Photography Portal.
  name: Snappr Presets API
  slug: snappr-presets-api
- description: Available Snappr shoot types.
  name: Snappr Shoot Types API
  slug: snappr-shoot-types-api
- description: Retrieve videos for bookings.
  name: Snappr Videos API
  slug: snappr-videos-api
artifact_total: 24
asyncapis:
- description: ''
  name: Snappr Webhooks
  slug: snappr-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snappr Availability API
  slug: open-snappr-availability-api
- collection_type: open
  name: Snappr Availability Bookings API
  slug: open-snappr-bookings-api
- collection_type: open
  name: Snappr Availability Coverage API
  slug: open-snappr-coverage-api
- collection_type: open
  name: Snappr Availability Editing Job Types API
  slug: open-snappr-editing-job-types-api
- collection_type: open
  name: Snappr Availability Editing Jobs API
  slug: open-snappr-editing-jobs-api
- collection_type: open
  name: Snappr Availability Images API
  slug: open-snappr-images-api
- collection_type: open
  name: Snappr Availability Presets API
  slug: open-snappr-presets-api
- collection_type: open
  name: Snappr Availability Shoot Types API
  slug: open-snappr-shoot-types-api
- collection_type: open
  name: Snappr Availability Videos API
  slug: open-snappr-videos-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/snappr-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snappr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snappr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snappr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.snappr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snappr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.snappr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snappr.com/#introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/snappr-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/snappr-sandbox.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://snappr.statuspage.io
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/snappr-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snappr-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snappr-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snappr-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snappr
- group: operate
  title: ''
  type: Support
  url: https://www.snappr.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.snappr.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.snappr.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.snappr.com/enterprise
- group: start
  title: ''
  type: Login
  url: https://app.snappr.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.snappr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.snappr.com/privacy
created: '2026-07-17'
description: Snappr is an on-demand visual content marketplace that connects businesses with a global network of professional photographers and videographers, plus automated and human-augmented photo editing services. The Snappr API (the "API for visual content", available to Snappr for Enterprise customers) lets developers programmatically check coverage and availability, book photoshoots, submit photo editing jobs against presets, and retrieve the resulting images and videos. Authentication is a bearer API key; a sandbox environment mirrors production for testing, and custom webhooks notify on booking changes. Backed by Foundry Group and surfaced into the API Evangelist network for enrichment.
image: https://cdn.prod.website-files.com/5ca95f7a3be192f65a7b4e4f/6993a952a20874ef53a0524e_snappr-og-photography-and-videography.jpg
layout: provider
mcp_servers:
- description: ''
  name: Snappr MCP Server
  slug: snappr-mcp-server
modified: '2026-07-21'
name: Snappr
nav: Providers
network: true
overview: 'Snappr publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Coverage API, and 6 more. Tagged areas include Company, Marketplace, Photography, Videography, and Visual Content.


  The Snappr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Snappr''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 17 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 22.5
    developer_ergonomics: 60.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snappr/refs/heads/main/screenshots/snappr-2026-08-17T081939.png
security:
- kind: authentication
  name: Snappr Authentication
  slug: snappr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Snappr Domain Security
  slug: snappr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: snappr
tags:
- Company
- Marketplace
- Photography
- Videography
- Visual Content
- Photo Editing
- On-Demand
- Enterprise
website: https://snappr.com
---
