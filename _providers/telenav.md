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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Location-based semantic search for the connected car - onebox search with category, brand, corridor, polygon, and bounding-box filters, reverse geocoding, EV charge-station search, auto-suggest and wo
  name: Telenav Entity Service REST API
  slug: telenav-entity-service-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Telenav Webhooks
  slug: telenav-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.telenav.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.telenav.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telenav.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.telenav.com/api-references/sdk/entity/current/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telenav.com/entity-android/install-sdk.html
- group: company
  title: ''
  type: Blog
  url: https://www.telenav.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.telenav.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telenav.com/legal/policies-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telenav.com/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Telenav
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telenav-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telenav-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telenav-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telenav-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telenav-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/telenav-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telenav-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/telenav-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/telenav-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telenav-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telenav-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telenav-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/telenav-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telenav-llms.txt
created: '2026-07-17'
description: Telenav is a connected-car and location-based services company that powers in-vehicle navigation (VIVID NAV), infotainment (VIVID IVI), and in-car commerce (VIVID COMMERCE) for automotive partners including Daimler, Ford, GM, Toyota, and Xpeng. Its developer surface centers on the Entity Service REST API for location-aware semantic search, auto-suggest predictions, entity detail lookup, and discovery including EV charge-station search, alongside partner-distributed navigation and driver-intelligence SDKs documented at docs.telenav.com and open-source Java tooling on Maven Central.
image: https://avatars.githubusercontent.com/u/3743554?v=4
layout: provider
mcp_servers:
- description: ''
  name: telenav-mcp.yml
  slug: telenav-mcpyml
modified: '2026-07-21'
name: Telenav
nav: Providers
network: true
overview: 'Telenav publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mapping, Navigation, Location, Search, and Automotive.


  The Telenav catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telenav''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 17 more developer resources.'
random_paper: 86
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 77.8
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 41.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Telenav Authentication
  slug: telenav-authentication
  summary_line: apiKey/requestSignature · 3 schemes
- kind: domain-security
  name: Telenav Domain Security
  slug: telenav-domain-security
  summary_line: HSTS · DMARC
slug: telenav
tags:
- Mapping
- Navigation
- Location
- Search
- Automotive
- Connected Cars
- EV Charging
- Points of Interest
website: https://www.telenav.com
---
