---
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Street Co Agentic Access
  operation_count: 94
  slug: street-co-agentic-access
  summary_line: 94 operations · 19 acting
api_count: 6
apis:
- description: Activity endpoints for this API.
  name: Street.co.uk Activity API
  slug: street-co-activity-api
- description: Applicants endpoints for this API.
  name: Street.co.uk Applicants API
  slug: street-co-applicants-api
- description: Area endpoints for this API.
  name: Street.co.uk Areas API
  slug: street-co-areas-api
- description: Branches endpoints for this API.
  name: Street.co.uk Branches API
  slug: street-co-branches-api
- description: Brands endpoints for this API.
  name: Street.co.uk Brands API
  slug: street-co-brands-api
- description: Companies endpoints for this API.
  name: Street.co.uk Companies API
  slug: street-co-companies-api
- description: Documents endpoints for this API.
  name: Street.co.uk Documents API
  slug: street-co-documents-api
- description: E-Sign Documents endpoints for this API.
  name: Street.co.uk E-Sign Documents API
  slug: street-co-e-sign-documents-api
- description: The Email API from Street.co.uk — 2 operation(s) for email.
  name: Street.co.uk Email API
  slug: street-co-email-api
- description: Enquiries endpoints for this API.
  name: Street.co.uk Enquiries API
  slug: street-co-enquiries-api
- description: Follow Ups endpoints for this API.
  name: Street.co.uk Follow Ups API
  slug: street-co-follow-ups-api
- description: Image endpoints for this API.
  name: Street.co.uk Images API
  slug: street-co-images-api
- description: Inspections endpoints for this API.
  name: Street.co.uk Inspections API
  slug: street-co-inspections-api
- description: Interested Applicants endpoints for this API.
  name: Street.co.uk Interested Applicants API
  slug: street-co-interested-applicants-api
- description: Invoices endpoints for this API.
  name: Street.co.uk Invoices API
  slug: street-co-invoices-api
- description: Landlords endpoints for this API.
  name: Street.co.uk Landlords API
  slug: street-co-landlords-api
- description: These are the lettings specific API Endpoints.
  name: Street.co.uk Lettings API
  slug: street-co-lettings-api
- description: Lettings Application endpoints for this API.
  name: Street.co.uk Lettings Applications API
  slug: street-co-lettings-applications-api
- description: Lettings Instruction endpoints for this API.
  name: Street.co.uk Lettings Instructions API
  slug: street-co-lettings-instructions-api
- description: Lettings Offers endpoints for this API.
  name: Street.co.uk Lettings Offers API
  slug: street-co-lettings-offers-api
- description: Maintenance Jobs endpoints for this API.
  name: Street.co.uk Maintenance Jobs API
  slug: street-co-maintenance-jobs-api
- description: Maintenance Request endpoints for this API.
  name: Street.co.uk Maintenance Requests API
  slug: street-co-maintenance-requests-api
- description: These are specific API Endpoints for retrieving meta information such as Areas or Features.
  name: Street.co.uk Meta API
  slug: street-co-meta-api
- description: Move Outs endpoints for this API.
  name: Street.co.uk Move Outs API
  slug: street-co-move-outs-api
- description: Notes endpoints for this API.
  name: Street.co.uk Notes API
  slug: street-co-notes-api
- description: People endpoints for this API.
  name: Street.co.uk People API
  slug: street-co-people-api
- description: Photo and Measure endpoints for this API.
  name: Street.co.uk Photos and Measures API
  slug: street-co-photos-and-measures-api
- description: Portal Listings endpoints for this API.
  name: Street.co.uk Portal Listings API
  slug: street-co-portal-listings-api
- description: Properties endpoints for this API.
  name: Street.co.uk Properties API
  slug: street-co-properties-api
- description: Property Key endpoints for this API.
  name: Street.co.uk Property Keys API
  slug: street-co-property-keys-api
- description: All endpoints for Spectre Property Reports
  name: Street.co.uk Property Reports API
  slug: street-co-property-reports-api
- description: Questionnaire Response endpoints for this API.
  name: Street.co.uk Questionnaire Responses API
  slug: street-co-questionnaire-responses-api
- description: Sales endpoints for this API.
  name: Street.co.uk Sales API
  slug: street-co-sales-api
- description: Sales Instructions endpoints for this API.
  name: Street.co.uk Sales Instructions API
  slug: street-co-sales-instructions-api
- description: Sales Offers endpoints for this API.
  name: Street.co.uk Sales Offers API
  slug: street-co-sales-offers-api
- description: Solicitors endpoints for this API.
  name: Street.co.uk Solicitors API
  slug: street-co-solicitors-api
- description: Tasks endpoints for this API.
  name: Street.co.uk Tasks API
  slug: street-co-tasks-api
- description: Tenancies endpoints for this API.
  name: Street.co.uk Tenancies API
  slug: street-co-tenancies-api
- description: Tenants endpoints for this API.
  name: Street.co.uk Tenants API
  slug: street-co-tenants-api
- description: Users endpoints for this API.
  name: Street.co.uk Users API
  slug: street-co-users-api
- description: Valuations endpoints for this API.
  name: Street.co.uk Valuations API
  slug: street-co-valuations-api
- description: Vendors endpoints for this API.
  name: Street.co.uk Vendors API
  slug: street-co-vendors-api
- description: Viewings endpoints for this API.
  name: Street.co.uk Viewings API
  slug: street-co-viewings-api
artifact_total: 52
asyncapis:
- description: ''
  name: Street Co Webhooks
  slug: street-co-webhooks
collections:
- collection_type: open
  name: Street Open API
  slug: open-street-co-open-api
- collection_type: open
  name: Property Feed
  slug: open-street-co-property-feed-api
- collection_type: open
  name: Spectre API
  slug: open-street-co-spectre-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/street-co-capability-edges.yml
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
overview: 'Street.co.uk publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Applicants API, Areas API, and 40 more. Tagged areas include Real-Estate, United Kingdom, PropTech, CRM, and Property Listings.


  The Street.co.uk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Street.co.uk''s developer surface includes authentication, changelog, sandbox, documentation, getting-started guide, engineering blog, pricing, and 36 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 3
  name: Street Co Rate Limits
  slug: street-co-rate-limits
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 67.3
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 55.0
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/street-co/refs/heads/main/screenshots/street-co-2026-08-17T082136.png
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
- Real-Estate
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
