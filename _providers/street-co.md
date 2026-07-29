---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Street Co Agentic Access
  operation_count: 94
  slug: street-co-agentic-access
  summary_line: 94 operations · 19 acting
api_count: 3
apis:
- description: The main Street.co.uk platform API — a JSON:API-conformant REST interface over the estate agency system of record, covering properties, sales and lettings instructions, offers, applicants, viewings, v
  name: Street Open API
  slug: street-open-api
- description: A read-only property feed API for powering an agency's own website and property search — sales search, lettings search, a single property record, area lookups and a property features list. Five paths,
  name: Street Property Feed API
  slug: street-property-feed-api
- description: The public API for the Spectre products, documented on the Street.co.uk developer portal and integrated into the Street CRM. Covers Spectre Property Reports (create and retrieve property reports, retr
  name: Spectre API
  slug: spectre-api
artifact_total: 9
asyncapis:
- description: ''
  name: Street Co Webhooks
  slug: street-co-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/street-co-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/street-co-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/street-co-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/street-co-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/street-co-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/street-co-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/street-co-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.street.co.uk/docs/street-open-api/updates/open-api-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/street-co-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/street-co-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/street-co-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/street-co-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/street-co-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/street-co-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/street-co-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/street-co-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/street-co-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/street-co-sync-property-portfolio.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/street-co-capture-enquiry-and-follow-up.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/street-co-power-website-property-search.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/street-co-tenancy-and-maintenance.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/street-co-invoice-reconciliation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/street-co-spectre-property-report.md
- group: other
  title: ''
  type: Overlay
  url: overlays/street-co-open-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/street-co-property-feed-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/street-co-spectre-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/street-co-llms.txt
- group: company
  title: ''
  type: Website
  url: https://street.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.street.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.street.co.uk/docs/street-open-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.street.co.uk/docs/street-open-api
- group: company
  title: ''
  type: Blog
  url: https://street.co.uk/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://street.co.uk/pricing
- group: operate
  title: ''
  type: Support
  url: https://api-support.street.co.uk/
- group: operate
  title: ''
  type: HelpCenter
  url: https://intercom.help/streetcouk/en/
- group: start
  title: ''
  type: Login
  url: https://street.co.uk/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://street.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://street.co.uk/privacy
- group: operate
  title: ''
  type: Contact
  url: mailto:apis@street.co.uk
- group: agent
  title: ''
  type: LLMsText
  url: https://developers.street.co.uk/llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-26'
description: 'Street.co.uk (Street Systems Limited, Manchester, England) is a UK estate agency CRM and property management platform for residential sales, lettings, property management and client accounting. In the United Kingdom there is no MLS and no RESO — residential listing distribution runs from agency CRM software out to the Rightmove and Zoopla portals — which places Street.co.uk at the agency system-of-record layer of the value chain, upstream of the portal duopoly and alongside Reapit, Alto and Apex27. Its API posture is unusually open for this sector: three OpenAPI 3.1 contracts (Street Open API, Property Feed, Spectre) are published unauthenticated on a public Scalar developer portal at developers.street.co.uk and can be downloaded as JSON or YAML by anyone. Access to the data behind them is not open — production bearer tokens are generated inside a paying agency''s Street account under Settings > Account Administration > Applications, and a non-customer developer must email
  apis@street.co.uk to be issued a sandbox token on the staging environment. Nothing RESO, no OData $metadata, and no open government data is published by Street.co.uk itself; the open UK property data layer sits with HM Land Registry and Ordnance Survey, not with the CRM vendors.'
image: https://street.co.uk/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from the three OpenAPIs (Street publishes no MCP server)
  slug: candidate-mcp-tool-surface-derived-from-the-three-openapis-street-publishes-no-mcp-server
modified: '2026-07-26'
name: Street.co.uk
nav: Providers
network: true
overview: 'Street.co.uk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Street Open API, Street Property Feed API, and Spectre API. Tagged areas include Real Estate, United Kingdom, PropTech, CRM, and Property Listings.


  The Street.co.uk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Street.co.uk''s developer surface includes authentication, changelog, sandbox, documentation, getting-started guide, engineering blog, pricing, and 35 more developer resources.'
random_paper: 27
rate_limits:
- limit_count: 0
  name: Street Co Rate Limits
  slug: street-co-rate-limits
score:
  band: developing
  composite: 51.8
  delta: -0.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.0
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Street Co Authentication
  slug: street-co-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Street Co Domain Security
  slug: street-co-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: street-co
tags:
- Real Estate
- United Kingdom
- PropTech
- CRM
- Property Listings
- Property Management
- Rentals
- Lettings
- Estate Agency
- Valuation
- Conveyancing
website: https://street.co.uk/
---
