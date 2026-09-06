---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 20.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Zartico operates a public, anonymously readable GeoServer instance at geoserver.zartico.com serving OGC Web Services over its destination geospatial estate. The WMS 1.3.0 capabilities document adverti
  name: Zartico GeoServer OGC Web Services
  slug: zartico-geoserver
- description: Zartico fronts its platform with Okta-hosted identity, and two of its hosts publish complete, anonymously readable discovery documents - login.zartico.com and platform.zartico.com. Each serves both Op
  name: Zartico Identity (OpenID Connect / OAuth 2.0)
  slug: zartico-identity
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.zartico.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.zartico.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zartico.com/kb-tickets/new
- group: company
  title: ''
  type: Blog
  url: https://www.zartico.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zartico.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zartico
- group: start
  title: ''
  type: SignUp
  url: https://www.zartico.com/see-a-live-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zartico.com/privacy-promise
- group: company
  title: ''
  type: Careers
  url: https://www.zartico.com/careers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zartico-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zartico-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zartico-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zartico-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zartico-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/zartico-packages.yml
- group: design
  title: ''
  type: Components
  url: components/zartico-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zartico-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zartico-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zartico-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zartico-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zartico-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zartico-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zartico-problem-types.yml
created: '2026-09-05'
description: Zartico is a Salt Lake City based destination-intelligence software company, founded in 2019, that operates the Zartico Destination Operating System (ZDOS) for destination marketing and management organizations, states, airports, attractions and ski resorts. The platform fuses daily geolocation observations, credit-card spending data, lodging and short-term-rental data, event demand and DMO digital analytics into a single integrated data model, and surfaces it through the Z5 visualization suite, Event Pulse and visitor-journey modules. Zartico publishes no general-purpose developer portal or REST API reference; its public machine-readable surface is an anonymously readable OGC GeoServer estate (WMS 1.3.0, WFS 2.0.0, WCS 2.0.1) at geoserver.zartico.com and two Okta-hosted OpenID Connect / OAuth 2.0 authorization servers at login.zartico.com and platform.zartico.com. Customer-facing integration is inbound rather than outbound - Zartico is granted read access to a destination's
  Google Analytics, ad server and CRM, and deploys a per-client geolocation attribution pixel.
image: https://go.zartico.com/hubfs/zartico-logo-final_rgb-white-horizontal.png
layout: provider
mcp_servers:
- description: ''
  name: Zartico MCP Server
  slug: zartico-mcp-server
modified: '2026-09-05'
name: Zartico
nav: Providers
network: true
overview: 'Zartico publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Tourism, Destination Marketing, and Location Intelligence.


  Zartico''s developer surface includes support, engineering blog, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Zartico Plans Pricing
  plan_count: 0
  slug: zartico-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Zartico Rate Limits
  slug: zartico-rate-limits
scopes:
- name: Zartico Scopes
  scope_count: 0
  slug: zartico-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Zartico Authentication
  slug: zartico-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Zartico Domain Security
  slug: zartico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zartico
tags:
- Company
- Travel
- Tourism
- Destination Marketing
- Location Intelligence
- Geospatial
- Analytics
- Data
- Business Intelligence
- OGC
website: https://www.zartico.com/
---
