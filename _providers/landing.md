---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Landing Agentic Access
  operation_count: 9
  slug: landing-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The Public API from Landing — 9 operation(s) for public.
  name: Landing Public API
  slug: landing-public-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Landing API (HTTP GET) Public API
  slug: open-landing-public-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/landing-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.hellolanding.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hellolanding.com/api/public
- group: docs
  title: ''
  type: Documentation
  url: https://www.hellolanding.com/api/public
- group: docs
  title: ''
  type: APIReference
  url: https://www.hellolanding.com/api/public/tools
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hellolanding.com/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/landing-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/landing-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landing-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/landing-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.hellolanding.com/.well-known/api-catalog
- group: auth
  title: ''
  type: Authentication
  url: authentication/landing-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/landing-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landing-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/landing-public-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/landing-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/landing-public-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/landing-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landing-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landing-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hellolanding
- group: operate
  title: ''
  type: Support
  url: https://www.hellolanding.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.hellolanding.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.hellolanding.com/blog/feed
- group: start
  title: ''
  type: SignUp
  url: https://www.hellolanding.com/users/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellolanding.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellolanding.com/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://www.hellolanding.com/faq
created: '2026-07-17'
description: 'Landing rents fully-furnished apartments for flexible monthly, short-term, and open-ended (LandingFlex) stays across 250+ US markets, booked entirely online with no security deposit and 24/7 local support. Landing operates one of the more complete agent-native API surfaces in proptech: a public, unauthenticated, read-only REST API and a public MCP server that expose the same nine capabilities — market discovery, filter vocabularies, apartment search, home detail with full availability calendars, LandingFlex commitment tiers, real anonymous quotes from the pricing engine that powers checkout, market statistics, and grounded policy answers. Discovery is wired end to end: an RFC 9727 api-catalog, an llms.txt agent guide, an OpenAPI 3.1 document and tool catalog generated from the live tool set, an agentskills.io index, schema.org JSON-LD, and a robots.txt that steers agents to the API instead of scraping. Reservations are not exposed — read tools return checkout links and a person
  completes payment on the website.'
image: https://files.hellolanding.com/home.png
layout: provider
mcp_servers:
- description: 'Read-only public access to Landing''s furnished apartment catalog: search by market and dates, fetch a home, check availability, get an anonymous quote. No authentication is required to call any tool.'
  name: Landing MCP Server
  slug: landing-mcp-server
modified: '2026-07-19'
name: Landing
nav: Providers
network: true
overview: 'Landing publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, PropTech, Real-Estate, Rentals, and Furnished Apartments.


  Landing''s developer surface includes documentation, API reference, getting-started guide, authentication, code examples, support, engineering blog, and 22 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/landing/refs/heads/main/screenshots/landing-2026-08-17T123950.png
security:
- kind: authentication
  name: Landing Authentication
  slug: landing-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Landing Domain Security
  slug: landing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: landing
tags:
- Company
- PropTech
- Real-Estate
- Rentals
- Furnished Apartments
- Corporate Housing
- Travel
- Agent Native
- MCP
- Search
website: https://www.hellolanding.com
---
