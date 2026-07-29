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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 137
  human_in_the_loop: 0
  name: Arthur Online Agentic Access
  operation_count: 317
  slug: arthur-online-agentic-access
  summary_line: 317 operations · 137 acting
api_count: 16
apis:
- description: Property records and everything hung off a property in Arthur - assets, certificates, conversations, general information, notes, units, tenancies, tasks, work orders, utilities, transactions and tags.
  name: Arthur Properties API
  slug: arthur-properties-api
- description: Individual lettable units beneath a property, plus the unit-level assets, certificates, conversations, notes, viewings, tenancies, tasks, work orders, utilities, transactions and tags. 22 documented p
  name: Arthur Units API
  slug: arthur-units-api
- description: 'Tenancy agreements over a unit, including tenants on the tenancy, deposit registration, recurring charges, certificates, tasks, work orders, conversations, transactions, notes and tags. 21 documented '
  name: Arthur Tenancies API
  slug: arthur-tenancies-api
- description: Tenant people records - list, view, create and update tenants, and invite a tenant into the Arthur tenant portal. 3 documented paths.
  name: Arthur Tenants API
  slug: arthur-tenants-api
- description: Prospective renters moving through the lettings funnel, including applicant status, credit checks, managers, assets, conversations, notes, tasks and tags. 15 documented paths.
  name: Arthur Applicants API
  slug: arthur-applicants-api
- description: Property and unit viewing appointments, the applicants attached to each viewing, assigned managers, conversations, notes and tags. 15 documented paths.
  name: Arthur Viewings API
  slug: arthur-viewings-api
- description: The largest surface in the API - tasks, subtasks, work orders, quotes and the contractor workflow around them. 45 documented paths.
  name: Arthur Maintenance API
  slug: arthur-maintenance-api
- description: Rental financials - invoices, transactions, transaction payoff and recurring charges. Read and update only; no create operations are documented. 6 documented paths.
  name: Arthur Financials API
  slug: arthur-financials-api
- description: Files and documents stored in Arthur and shared with owners, tenants and contractors. 2 documented paths.
  name: Arthur Assets API
  slug: arthur-assets-api
- description: Utility accounts attached to properties and units, and the meter readings recorded against them. 4 documented paths.
  name: Arthur Utilities API
  slug: arthur-utilities-api
- description: Compliance certificates - gas safety, electrical, EPC and similar - with expiry tracking that also drives webhook events at 30 days, 7 days and on the day. 2 documented paths.
  name: Arthur Certificates API
  slug: arthur-certificates-api
- description: Arthur entities - the account boundary that every API call must name in the mandatory X-EntityID request header. 2 documented paths.
  name: Arthur Entities API
  slug: arthur-entities-api
- description: Threaded conversations and messages between managers, tenants, owners and contractors, with attached assets. 4 documented paths.
  name: Arthur Conversations API
  slug: arthur-conversations-api
- description: Cross-cutting tags applied to properties, units, tenancies, applicants, viewings and notes, with tag and untag operations on each resource. 2 documented paths.
  name: Arthur Tags API
  slug: arthur-tags-api
- description: Free-text notes recorded against any Arthur resource, with their own tagging operations. 5 documented paths.
  name: Arthur Notes API
  slug: arthur-notes-api
- description: Read-only reference vocabularies backing every enumerated field in Arthur - access detail types, applicant statuses and types, area types, asset types, certificate types, citizen types, contract types
  name: Arthur Types API
  slug: arthur-types-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: 'The UK lettings funnel in Arthur Online: confirm the entity, create an applicant, book a viewing on a unit, record the offer, convert the viewing into a tenancy, add the tenant and register the deposi'
  name: Arthur Online - applicant to tenancy
  slug: arthur-online-applicant-to-tenancy
- description: Raise a maintenance task against a property, break it into subtasks, dispatch it to a contractor as a work order, open the conversation and read back quotes and invoices. Approval steps (manager appro
  name: Arthur Online - maintenance dispatch
  slug: arthur-online-maintenance-dispatch
- description: 'Bring a new building into Arthur Online: create the property, add a lettable unit, file the compliance certificate, publish the information shared with occupants and attach the document. Every operati'
  name: Arthur Online - onboard a property
  slug: arthur-online-onboard-property
artifact_total: 44
asyncapis:
- description: The Arthur Online webhook event surface. A property manager subscribes a webhook URL to one or more of the 125 published triggers on the Arthur webhook page; Arthur then POSTs a form-encoded payload t
  name: Arthur Online Webhooks
  slug: arthur-online-webhooks-asyncapi
- description: ''
  name: Arthur Online Webhooks
  slug: arthur-online-webhooks
collections:
- collection_type: postman
  name: Arthur Applicants API
  slug: postman-arthur-online-applicants
- collection_type: postman
  name: Arthur Assets API
  slug: postman-arthur-online-assets
- collection_type: postman
  name: Arthur Certificates API
  slug: postman-arthur-online-certificates
- collection_type: postman
  name: Arthur Conversations API
  slug: postman-arthur-online-conversations
- collection_type: postman
  name: Arthur Entities API
  slug: postman-arthur-online-entities
- collection_type: postman
  name: Arthur Financials API
  slug: postman-arthur-online-financials
- collection_type: postman
  name: Arthur Maintenance API
  slug: postman-arthur-online-maintenance
- collection_type: postman
  name: Arthur Notes API
  slug: postman-arthur-online-notes
- collection_type: postman
  name: Arthur Properties API
  slug: postman-arthur-online-properties
- collection_type: postman
  name: Arthur Tags API
  slug: postman-arthur-online-tags
- collection_type: postman
  name: Arthur Tenancies API
  slug: postman-arthur-online-tenancies
- collection_type: postman
  name: Arthur Tenants API
  slug: postman-arthur-online-tenants
- collection_type: postman
  name: Arthur Types API
  slug: postman-arthur-online-types
- collection_type: postman
  name: Arthur Units API
  slug: postman-arthur-online-units
- collection_type: postman
  name: Arthur Utilities API
  slug: postman-arthur-online-utilities
- collection_type: postman
  name: Arthur Viewings API
  slug: postman-arthur-online-viewings
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/arthur-online/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arthur-online-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arthur-online-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arthur-online-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.arthuronline.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://developer.arthuronline.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.arthuronline.co.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.arthuronline.co.uk/
- group: build
  title: ''
  type: PostmanCollection
  url: collections/arthur-online.postman_collection.json
- group: start
  title: ''
  type: Signup
  url: https://www.arthuronline.co.uk/connect/arthur-api
- group: operate
  title: ''
  type: Support
  url: https://support.arthuronline.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.arthuronline.co.uk/arthur-insight/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arthuronline.co.uk/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arthuronline.co.uk/legal/terms-and-conditions
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.arthuronline.co.uk/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.arthuronline.co.uk/connect/arthur-api
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/22554870/2s93sZ5YeM
- group: start
  title: ''
  type: SignUp
  url: https://www.arthuronline.co.uk/connect/arthur-api
- group: start
  title: ''
  type: Login
  url: https://login.arthuronline.co.uk/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.arthuronline.co.uk/support/solutions
- group: commercial
  title: ''
  type: Pricing
  url: https://www.arthuronline.co.uk/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arthur-crm
- group: design
  title: ''
  type: Conventions
  url: conventions/arthur-online-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arthur-online-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arthur-online-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arthur-online-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arthur-online-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/arthur-online-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/arthur-online-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arthur-online-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/arthur-online-vocabulary.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arthur-online-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arthur-online-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/arthur-online-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/arthur-online-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/arthur-online-webhooks-asyncapi.yml
created: '2026-07-26'
description: 'Arthur Online is a London-headquartered UK property management software platform, founded in 2008 and acquired by Aareon in January 2021, that gives letting agents, self-managing landlords, block and social housing managers, and student accommodation operators a cloud system of record for properties, units, tenancies, tenants, applicants, viewings, maintenance work orders, certificates, utilities and rental financials, with companion mobile apps for managers, tenants, contractors and owners. It sits in the middle of the UK residential lettings value chain: it is the agency-side operational system that pushes stock out to the Rightmove and Zoopla portals and pulls accounting into Xero and QuickBooks, rather than a listings marketplace or a data cooperative. Its API posture is unusually open for the sector but is not open data: the full Arthur API v2 reference is published without a login as a public Postman collection at developer.arthuronline.co.uk covering 324 documented requests
  across 16 resource areas, yet every call is tenant-scoped OAuth 2.0 Authorization Code plus an X-EntityID header, credentials are issued only from inside a paying Arthur account after contacting Arthur support, and no data is readable anonymously. There is no RESO posture at all — the United Kingdom has no MLS, no NAR, and no RESO Data Dictionary or Web API certification regime, so listings interoperability here is portal-to-CRM feeds rather than a certified machine-readable standard.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arthur-online.png
layout: provider
mcp_servers:
- description: ''
  name: arthur-online-mcp.yml
  slug: arthur-online-mcpyml
modified: '2026-07-26'
name: Arthur Online
nav: Providers
network: true
overview: 'Arthur Online publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Arthur Properties API, Arthur Units API, Arthur Tenancies API, and 13 more. Tagged areas include Real Estate, United Kingdom, Property Management, PropTech, and Rentals.


  The Arthur Online catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Arthur Online''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, support, engineering blog, and 32 more developer resources.'
plans:
- name: Arthur Online Plans
  plan_count: 3
  slug: arthur-online-plans
random_paper: 72
rate_limits:
- limit_count: 1
  name: Arthur Online Rate Limits
  slug: arthur-online-rate-limits
score:
  band: strong
  composite: 58.4
  delta: -5.2
  facets:
    commercial_clarity: 76.3
    contract_quality: 58.9
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 21.9
    operational_transparency: 34.2
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Arthur Online Authentication
  slug: arthur-online-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Arthur Online Domain Security
  slug: arthur-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arthur-online
tags:
- Real Estate
- United Kingdom
- Property Management
- PropTech
- Rentals
- Lettings
- Tenancy
- Maintenance
- Property Listings
- Social Housing
- Student Housing
- Block Management
website: https://www.arthuronline.co.uk/
---
