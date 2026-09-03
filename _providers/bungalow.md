---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
  score: 26.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://fieldstone.bungalow.com/api/v1/
  baseurl_source: declared
  description: The Applications API from Bungalow — 1 operation(s) for applications.
  name: Bungalow Applications API
  slug: bungalow-applications-api
- baseURL: https://fieldstone.bungalow.com/api/v1/
  baseurl_source: declared
  description: Listings endpoints allow you to get all listings in a market or a singular property. Rooms within properties can become marketable before the room is vacant, generally if there is a known move out occ
  name: Bungalow Listings API
  slug: bungalow-listings-api
- baseURL: https://fieldstone.bungalow.com/api/v1/
  baseurl_source: declared
  description: A market is a generalized geographical area that often represents a city (e.g. Seattle, Boston), but can also represent a broader metropolitan area (e.g. Bay Area).
  name: Bungalow Markets API
  slug: bungalow-markets-api
- baseURL: https://fieldstone.bungalow.com/api/v1/
  baseurl_source: declared
  description: These two endpoints will give you everything you need to get booking availability, as well as create a showing at a given property.
  name: Bungalow Showings API
  slug: bungalow-showings-api
artifact_total: 8
asyncapis:
- description: ''
  name: Bungalow Webhooks
  slug: bungalow-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bungalow-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bungalow-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://bungalow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fieldstone.bungalow.com/api/v1/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://fieldstone.bungalow.com/api/v1/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://fieldstone.bungalow.com/api/v1/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://fieldstone.bungalow.com/api/v1/docs/#section/Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://bungalow.com/faq
- group: operate
  title: ''
  type: HelpCenter
  url: https://bungalow.com/help
- group: company
  title: ''
  type: Blog
  url: https://bungalow.com/articles
- group: start
  title: ''
  type: SignUp
  url: https://bungalow.com/signup
- group: start
  title: ''
  type: Login
  url: https://bungalow.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bungalow.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bungalow.com/privacy-policy
- group: company
  title: ''
  type: About
  url: https://bungalow.com/about
- group: company
  title: ''
  type: Press
  url: https://bungalow.com/press
- group: company
  title: ''
  type: Careers
  url: https://bungalow.com/careers
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/bungalow-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bungalow-openapi-original-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bungalow-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bungalow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bungalow-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bungalow-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bungalow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bungalow-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bungalow-webhooks.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bungalow-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bungalow-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bungalow-domain-security.yml
created: '2026-08-01'
description: Bungalow is a US residential rental platform for single-family homes, operating both a co-living ("Coliving Home") product where individual rooms in a house are leased to separately screened housemates and a whole-home ("Group Home") product leased to a single group. Founded in 2017 by Andrew Collins and Justin McCarty and headquartered in Miami, FL, the company pairs a renter-facing marketplace and mobile app with a homeowner property-management portal and an SFR investment service ("Radar Powered by Bungalow") covering sourcing, underwriting, renovation and management. Bungalow publishes a small, anonymous, read-mostly public REST API — the Bungalow API at fieldstone.bungalow.com — so that third-party listing sites, rental search portals and partner platforms can syndicate its markets and property listings, retrieve showing availability, book a showing, and submit an application source. Authenticated Hotpads and Facebook Catalog XML feeds are offered to approved integration
  partners as a richer alternative, and partners are asked to post lead-capture webhooks back to Bungalow. Active in roughly 23 markets across the United States.
image: https://assets.bungalow.com/home-page/header/header-hero-min.png?h=630&w=1200&auto=format
layout: provider
mcp_servers:
- description: ''
  name: Bungalow MCP Server
  slug: bungalow-mcp-server
modified: '2026-08-01'
name: Bungalow
nav: Providers
network: true
overview: 'Bungalow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Listings API, Markets API, and 1 more. Tagged areas include Company, Real-Estate, Residential Real Estate, Rental Listings, and Property Management.


  The Bungalow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bungalow''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 39.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bungalow/refs/heads/main/screenshots/bungalow-2026-08-07T162850.png
security:
- kind: authentication
  name: Bungalow Authentication
  slug: bungalow-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Bungalow Domain Security
  slug: bungalow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bungalow
tags:
- Company
- Real-Estate
- Residential Real Estate
- Rental Listings
- Property Management
- Co-Living
- Single-Family Rental
- Listings Syndication
- Housing
- PropTech
- Marketplace
website: https://bungalow.com/
---
